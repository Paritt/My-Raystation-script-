from connect import *
import time
from tkinter import *
from tkinter import ttk

case = get_current("Case")
plan = get_current("Plan")
beamset = get_current("BeamSet")
examination = get_current("Examination")
db = get_current("PatientDB")

#===============================================================================#
#===========================   FUNCTION DEFINE   ===============================#
#===============================================================================#

def create_contour_from_dose(dose, dose_level, case, beamset, n=0):
	roi = case.PatientModel.CreateRoi(Name=f"z Dose_{dose_level}%_{n}", Color="Yellow", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current("BeamSet")
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print(f"Create z Dose_{dose_level}%_{n}")

def FiF(case, plan, beamset, subMedTang="3",subLatTang="4",initial_MU = 10,step_MU=2, accept_hot=1.05, PTV_name="PTV", n=0):
	for beam in beamset.Beams:
		if beam.Name == subMedTang:
			beamset.DeleteBeam(BeamName=subMedTang)
	for beam in beamset.Beams:
		if beam.Name == subLatTang:
			beamset.DeleteBeam(BeamName=subLatTang)
			
	beamset.SetMUAndComputeDose(ForceRecompute=True)
		
	for roi in case.PatientModel.StructureSets[0].RoiGeometries:
		if roi.OfRoi.Name == f'z PTV_{n}':
			case.PatientModel.RegionsOfInterest[f'z PTV_{n}'].DeleteRoi()
	for roi in case.PatientModel.StructureSets[0].RoiGeometries:
		if roi.OfRoi.Name == f'z Dose_100%_{n}':
			case.PatientModel.RegionsOfInterest[f'z Dose_100%_{n}'].DeleteRoi()
		
	beamset.CopyBeam(BeamName=str(int(subMedTang)-2))
	beamset.CopyBeam(BeamName=str(int(subLatTang)-2))
	print("Copy Beam sucess")
	
	create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, case, beamset, n=n)
	
	retval_0 = case.PatientModel.CreateRoi(Name=f"z PTV_{n}", Color="Green", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	
	retval_0.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': ["BODY", f"{PTV_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"z Dose_100%_{n}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	#beamset.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = 'z PTV_1')
	#beamset.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = 'z Dose_100%')
	
	
	beamset.Beams[subMedTang].SetTreatOrProtectRoi(RoiName = f'z PTV_{n}')
	beamset.Beams[subMedTang].SetTreatOrProtectRoi(RoiName = f'z Dose_100%_{n}')
	beamset.Beams[subMedTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z PTV_{n}")
	beamset.Beams[subMedTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z Dose_100%_{n}")
	
	beamset.Beams[subLatTang].SetTreatOrProtectRoi(RoiName = f'z PTV_{n}')
	beamset.Beams[subLatTang].SetTreatOrProtectRoi(RoiName = f'z Dose_100%_{n}')
	beamset.Beams[subLatTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z PTV_{n}")
	beamset.Beams[subLatTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z Dose_100%_{n}")
	
	beamset.Beams[subMedTang].ConformMlc()
	beamset.Beams[subLatTang].ConformMlc()
	
	beamset.Beams[subMedTang].BeamMU = initial_MU
	beamset.Beams[subLatTang].BeamMU = initial_MU
	beamset.SetMUAndComputeDose(ForceRecompute=True)
	
	max_dose = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="BODY", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
	
	while max_dose>accept_hot:
		initial_MU -= step_MU
		beamset.Beams[subMedTang].BeamMU = initial_MU
		beamset.Beams[subLatTang].BeamMU = initial_MU
		max_dose = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="BODY", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue

	beamset.SetMUAndComputeDose(ForceRecompute=False)
	
def Start():
	PTV_name = str(combo_PTV.get())
	N = int(N_input.get())
	accept_hot = (float(Hot_input.get())/100.0)
	initial_MU = int(Initial_MU_input.get())
	step_MU = int(Step_MU_input.get())
	total_iterations = (N*N)+N+N
	progress_bar["maximum"] = total_iterations
	progress_bar["value"] = N
	root.update_idletasks()
	for n in range(3,N+3):
		FiF(case, plan, beamset, subMedTang=str(n),subLatTang=str(n+1),initial_MU = initial_MU,step_MU=step_MU, accept_hot=accept_hot, PTV_name=PTV_name, n=n)
		progress_bar["value"] += N
		root.update_idletasks()
	for n in range(3,N+3):
		case.PatientModel.RegionsOfInterest[f'z Dose_100%_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f'z PTV_{n}'].DeleteRoi()
		progress_bar["value"] += 1
		root.update_idletasks()
	root.destroy()

#===============================================================================#
#===========================   CODE START HERE   ===============================#
#===============================================================================#

root = Tk()
root.title('Plan design')
root.geometry('400x240')

lbN = Label(root, text= 'Number of sub field (N)')
lbN.grid(column=0 ,row=3)
lbN.config(width=27, height =2)
N_input = StringVar()
textN = Entry(root, textvariable = N_input)
textN.grid(column=1,row=3)
textN.config(width=27)

lbHot = Label(root, text= 'Accept hot (%)')
lbHot.grid(column=0 ,row=4)
lbHot.config(width=27, height =2)
Hot_input = StringVar()
textHot = Entry(root, textvariable = Hot_input)
textHot.grid(column=1,row=4)
textHot.config(width=27)

lbInitial_MU = Label(root, text= 'Initial MU for sub field')
lbInitial_MU.grid(column=0 ,row=5)
lbInitial_MU.config(width=27, height =2)
Initial_MU_input = StringVar()
textInitial_MU_input = Entry(root, textvariable = Initial_MU_input)
textInitial_MU_input.grid(column=1,row=5)
textInitial_MU_input.config(width=27)

lbStep_MU = Label(root, text= 'Step MU')
lbStep_MU.grid(column=0 ,row=6)
lbStep_MU.config(width=27, height =2)
Step_MU_input = StringVar()
textStep_MU_input = Entry(root, textvariable = Step_MU_input)
textStep_MU_input.grid(column=1,row=6)
textStep_MU_input.config(width=27)

ListRoi = [r.Name for r in case.PatientModel.RegionsOfInterest]
lbMatchRoi1 = Label(root, text= 'PTV')
lbMatchRoi1.grid(column=0 , row=7)
lbMatchRoi1.config(width=27)
combo_PTV = StringVar()
comboPTV = ttk.Combobox(root, values = ListRoi, textvariable= combo_PTV)
comboPTV.grid(column=1,row=7)
comboPTV.config(width=27)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate")
progress_bar.grid(column=0,row=8)

buttStart = Button(root, text = 'Start', command = Start)
buttStart.grid(column=1,row=8,padx=10,pady=25)
buttStart.config(width=15)


root.mainloop()
	
#===============================================================================#
#============================   CODE END HERE   ================================#
#===============================================================================#