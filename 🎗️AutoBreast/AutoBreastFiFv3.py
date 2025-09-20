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

def FiF(case, plan, beamset, subMedTang="3",subLatTang="4",initial_MU = 10,step_MU=2, accept_hot=1.05, PTV_name="PTV", Body_name="BODY", n=0, symmetry = True):
	for beam in beamset.Beams:
		if beam.Name == subMedTang:
			beamset.DeleteBeam(BeamName=subMedTang)
		elif beam.Name == subLatTang:
			beamset.DeleteBeam(BeamName=subLatTang)
			
	beamset.SetMUAndComputeDose(ForceRecompute=True)
		
	for roi in case.PatientModel.StructureSets[0].RoiGeometries:
		if roi.OfRoi.Name == f'z PTV_{n}':
			case.PatientModel.RegionsOfInterest[f'z PTV_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z Dose_100%_{n}':
			case.PatientModel.RegionsOfInterest[f'z Dose_100%_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z medDose_100%_{n}':
			case.PatientModel.RegionsOfInterest[f'z medDose_100%_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z latDose_100%_{n}':
			case.PatientModel.RegionsOfInterest[f'z latDose_100%_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z medPTV_{n}':
			case.PatientModel.RegionsOfInterest[f'z medPTV_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z latPTV_{n}':
			case.PatientModel.RegionsOfInterest[f'z latPTV_{n}'].DeleteRoi()
		elif roi.OfRoi.Name == f'z latPTV_{n}':
			case.PatientModel.RegionsOfInterest[f'z maxEval_{n}'].DeleteRoi()
		
	beamset.CopyBeam(BeamName=str(int(subMedTang)-2))
	beamset.CopyBeam(BeamName=str(int(subLatTang)-2))
	print("Copy Beam sucess")
	
	create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, case, beamset, n=n)
	
	retval_0 = case.PatientModel.CreateRoi(Name=f"z PTV_{n}", Color="Green", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	retval_0.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': ["BODY", f"{PTV_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"z Dose_100%_{n}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	
	medPTV = case.PatientModel.CreateRoi(Name=f"z medPTV_{n}", Color="Green", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	medPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"{PTV_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"z Dose_100%_{n}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	medPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"z medPTV_{n}", "zMedHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	medDose100 = case.PatientModel.CreateRoi(Name=f"z medDose_100%_{n}", Color="Green", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	medDose100.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"z Dose_100%_{n}", "zMedHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	latPTV = case.PatientModel.CreateRoi(Name=f"z latPTV_{n}", Color="Green", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	latPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"{PTV_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"z Dose_100%_{n}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	latPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"z latPTV_{n}", "zLatHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	latDose100 = case.PatientModel.CreateRoi(Name=f"z latDose_100%_{n}", Color="Green", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	latDose100.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"z Dose_100%_{n}", "zMedHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	
	if symmetry == True:
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
	else:	
		beamset.Beams[subMedTang].SetTreatOrProtectRoi(RoiName = f'z medPTV_{n}')
		beamset.Beams[subMedTang].SetTreatOrProtectRoi(RoiName = f'z medDose_100%_{n}')
		beamset.Beams[subMedTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z medPTV_{n}")
		beamset.Beams[subMedTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z medDose_100%_{n}")
		
		beamset.Beams[subLatTang].SetTreatOrProtectRoi(RoiName = f'z latPTV_{n}')
		beamset.Beams[subLatTang].SetTreatOrProtectRoi(RoiName = f'z latDose_100%_{n}')
		beamset.Beams[subLatTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z latPTV_{n}")
		beamset.Beams[subLatTang].SetTreatAndProtectMarginsForBeam(TopMargin=0.0,BottomMargin=0.0,LeftMargin=0.0,RightMargin=0.0,Roi= f"z latDose_100%_{n}")
		
		beamset.Beams[subMedTang].ConformMlc()
		beamset.Beams[subLatTang].ConformMlc()
		
		beamset.Beams[subMedTang].BeamMU = initial_MU
		beamset.Beams[subLatTang].BeamMU = initial_MU
		beamset.SetMUAndComputeDose(ForceRecompute=True)
	
	no100 = case.PatientModel.CreateRoi(Name=f"z no100_{n}", Color="White", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	no100.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"{Body_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"z Dose_100%_{n}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	max_out100 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"z no100_{n}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
	max_dose_med = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"z medDose_100%_{n}", RelativeVolumes=[0.1])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
	max_dose_lat = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"z latDose_100%_{n}", RelativeVolumes=[0.1])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
	global_max = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"{Body_name}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
	med_MU = 0
	lat_MU = 0
	state = 1
	ln=0
	
	while max_out100<accept_hot*1.01:
		print(f"......................................loop={ln}....................................................")
		print(f"......................................loop={ln}....................................................")
		print(f"......................................loop={ln}....................................................")
		print(f"......................................loop={ln}....................................................")
		ln += 1
		if  state%2 != 0:
			if med_MU == 0:
				med_MU = initial_MU + step_MU
			else:
				med_MU += step_MU
			beamset.Beams[subMedTang].BeamMU = med_MU
			beamset.SetMUAndComputeDose(ForceRecompute=True)
			max_out100 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"z no100_{n}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
			global_max = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"{Body_name}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
			state += 1
			print(f"......................................State={state}....................................................")
			print(f"......................................State={state}....................................................")
		elif state%2 ==0:
			if lat_MU == 0:
				lat_MU = initial_MU + step_MU
			else:
				lat_MU += step_MU
			beamset.Beams[subLatTang].BeamMU = lat_MU
			beamset.SetMUAndComputeDose(ForceRecompute=True)
			max_out100 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"z no100_{n}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
			global_max = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=f"{Body_name}", RelativeVolumes=[0])/beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
			state += 1
			print(f"......................................State={state}....................................................")
			print(f"......................................State={state}....................................................")

	#beamset.SetMUAndComputeDose(ForceRecompute=False)

def Halving_breast(beam_set=beamset, PTV = "PTV", Body_name= "Body"):
	beam_set.CopyBeam(BeamName="2")
	beam_set.Beams['3'].GantryAngle = beam_set.Beams['2'].GantryAngle + 90
	beam_set.Beams['3'].SetInitialJawPositions(X1=-20, X2=0, Y1=-20, Y2=20)
	beam_set.Beams['3'].ConformMlc()
	beam_set.Beams['3'].BeamMU = 100
	Medtang_MU = beam_set.Beams['1'].BeamMU
	Lattang_MU = beam_set.Beams['2'].BeamMU
	beam_set.Beams['1'].BeamMU = 1
	beam_set.Beams['2'].BeamMU = 1
	beam_set.SetMUAndComputeDose(ForceRecompute=False)
	roi = case.PatientModel.CreateRoi(Name=f"zLatHalf", Color="Yellow", Type="Undefined", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	roi.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = 1000)
	roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"{PTV}", "zLatHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	roi2 = case.PatientModel.CreateRoi(Name=f"zMedHalf", Color="Blue", Type="Undefined", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	roi2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [f"{PTV}",f"{Body_name}"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zLatHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	beam_set.DeleteBeam(BeamName="3")
	beam_set.Beams['1'].BeamMU = Medtang_MU
	beam_set.Beams['2'].BeamMU = Lattang_MU
	beam_set.SetMUAndComputeDose(ForceRecompute=False)
	
def Start():
	PTV_name = str(combo_PTV.get())
	Body_name = str(combo_Body.get())
	N = int(N_input.get())
	accept_hot = (float(Hot_input.get())/100.0)
	initial_MU = int(Initial_MU_input.get())
	step_MU = int(Step_MU_input.get())
	total_iterations = (N*N)+N+N
	progress_bar["maximum"] = total_iterations
	progress_bar["value"] = N
	root.update_idletasks()
	Halving_breast(beam_set=beamset, PTV =PTV_name, Body_name= Body_name)
	for n in range(3,N+3):
		if n<3:
			FiF(case, plan, beamset, subMedTang=str(n),subLatTang=str(n+1),initial_MU = initial_MU,step_MU=step_MU, accept_hot=accept_hot, PTV_name=PTV_name, Body_name=Body_name, n=n, symmetry = True)
			progress_bar["value"] += N
			root.update_idletasks()
		else:
			FiF(case, plan, beamset, subMedTang=str(n),subLatTang=str(n+1),initial_MU = initial_MU,step_MU=step_MU, accept_hot=accept_hot, PTV_name=PTV_name, Body_name=Body_name, n=n, symmetry = False)
			progress_bar["value"] += N
			root.update_idletasks()
	case.PatientModel.RegionsOfInterest[f'zLatHalf'].DeleteRoi()
	case.PatientModel.RegionsOfInterest[f'zMedHalf'].DeleteRoi()
	for n in range(3,N+3):
		case.PatientModel.RegionsOfInterest[f'z Dose_100%_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f'z medDose_100%_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f'z medPTV_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f'z latDose_100%_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f'z latPTV_{n}'].DeleteRoi()
		case.PatientModel.RegionsOfInterest[f"z no100_{n}"].DeleteRoi()
		progress_bar["value"] += 1
		root.update_idletasks()
	root.destroy()

#===============================================================================#
#============================   GUI START HERE   ===============================#
#===============================================================================#

root = Tk()
root.title('Plan design')
root.geometry('400x260')

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

lbInitial_MU = Label(root, text= 'Minimum MU for sub field')
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
lbMatchRoi1.config(width=27, height =2)
combo_PTV = StringVar()
comboPTV = ttk.Combobox(root, values = ListRoi, textvariable= combo_PTV)
comboPTV.grid(column=1,row=7)
comboPTV.config(width=27)

ListRoi = [r.Name for r in case.PatientModel.RegionsOfInterest]
lbMatchRoi2 = Label(root, text= 'BODY')
lbMatchRoi2.grid(column=0 , row=8)
lbMatchRoi2.config(width=27, height =2)
combo_Body = StringVar()
comboBody = ttk.Combobox(root, values = ListRoi, textvariable= combo_Body)
comboBody.grid(column=1,row=8)
comboBody.config(width=27)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate")
progress_bar.grid(column=0,row=9)

buttStart = Button(root, text = 'Start', command = Start)
buttStart.grid(column=1,row=9)
buttStart.config(width=15, height =1)


root.mainloop()
	
#===============================================================================#
#============================   CODE END HERE   ================================#
#===============================================================================#