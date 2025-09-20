from connect import *
from tkinter import *
from tkinter import ttk

case = get_current("Case")
examination = get_current("Examination")
patient = get_current("Patient")
plan = get_current("Plan")
db = get_current("PatientDB")

root = Tk()
root.title('Loop Optimize')
root.geometry('1360x210')
#############################
# ROW 1
#############################
# Show Pt Name, HN, Plan Name
name = patient.Name
lbName = Label(root, text= f"Name: {name}")
lbName.grid(column=0 ,row=1)
lbName.config(width=27, height =2)

hn = patient.PatientID
lbHN = Label(root, text= f"HN: {hn}")
lbHN.grid(column=1 ,row=1)
lbHN.config(width=27, height =2)

plan_name = "Plan_X"
lbHN = Label(root, text= f"Plan name: {plan_name}")
lbHN.grid(column=2 ,row=1)
lbHN.config(width=27, height =2)

# No. of Loop
lbLoop = Label(root, text= 'No. of Loop')
lbLoop.grid(column=3 ,row=1)
lbLoop.config(width=27, height =2)
NumL = StringVar()
textNumL = Entry(root, textvariable = NumL)
textNumL.grid(column=4,row=1)
textNumL.config(width=27)

# No. of Oprimize/Loop
lbOptL = Label(root, text= 'No. of Oprimize/Loop')
lbOptL.grid(column=5 ,row=1)
lbOptL.config(width=27, height =2)
NumOL = StringVar()
textNumOL = Entry(root, textvariable = NumOL)
textNumOL.grid(column=6,row=1)
textNumOL.config(width=27)

#############################
# ROW 2
#############################
lbROI = Label(root, text= 'ROI')
lbROI.config(width=27, height =2)
lbROI.grid(column=0 ,row=2)

lbdose = Label(root, text= 'Plus Dose (Gy)')
lbdose.config(width=27, height =2)
lbdose.grid(column=1 ,row=2)

lbcrop = Label(root, text= 'Boarder crop (cm)')
lbcrop.config(width=27, height =2)
lbcrop.grid(column=2 ,row=2)

lbPriority = Label(root, text= 'Priority')
lbPriority.config(width=27, height =2)
lbPriority.grid(column=3 ,row=2)

lbdose = Label(root, text= 'Minus Dose (Gy)')
lbdose.config(width=27, height =2)
lbdose.grid(column=4 ,row=2)

lbcrop = Label(root, text= 'Boarder crop (cm)')
lbcrop.config(width=27, height =2)
lbcrop.grid(column=5 ,row=2)

lbPriority = Label(root, text= 'Priority')
lbPriority.config(width=27, height =2)
lbPriority.grid(column=6 ,row=2)

#############################
# ROW 3+
#############################
# ROI 1
## Get Name
ROI1 = StringVar()
ROI1_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI1_combo.insert(0,"--None--")
comboROI1 = ttk.Combobox(root, values= ROI1_combo, textvariable=ROI1)
comboROI1.grid(column=0, row=3)
comboROI1.config(width=27)
## Get Plus Dose
ROI1_pdose = StringVar()
textROI1_pdose = Entry(root, textvariable = ROI1_pdose)
textROI1_pdose.grid(column=1, row=3)
textROI1_pdose.config(width=27)

## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI1_pcrop = StringVar()
textROI1_pcrop = Entry(root, textvariable = ROI1_pcrop)
textROI1_pcrop.grid(column=2, row=3)
textROI1_pcrop.config(width=27)

## Get Priority for Plus
ROI1_pprio = StringVar()
textROI1_pprio = Entry(root, textvariable = ROI1_pprio)
textROI1_pprio.grid(column=3, row=3)
textROI1_pprio.config(width=27)

## Get Minus dose (eg. 105%, 103%)
ROI1_mdose = StringVar()
textROI1_mdose = Entry(root, textvariable = ROI1_mdose)
textROI1_mdose.grid(column=4, row=3)
textROI1_mdose.config(width=27)
## Get crop from boarder for Minus (eg. 0.3 cm)
ROI1_mcrop = StringVar()
textROI1_mcrop = Entry(root, textvariable = ROI1_mcrop)
textROI1_mcrop.grid(column=5, row=3)
textROI1_mcrop.config(width=27)
## Get Priority for Minus 
ROI1_mprio = StringVar()
textROI1_mprio = Entry(root, textvariable = ROI1_mprio)
textROI1_mprio.grid(column=6, row=3)
textROI1_mprio.config(width=27)

# ROI2
## Get Name
ROI2 = StringVar()
ROI2_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI2_combo.insert(0,"--None--")
comboROI2 = ttk.Combobox(root, values= ROI2_combo, textvariable=ROI2)
comboROI2.grid(column=0, row=4)
comboROI2.config(width=27)
## Get Plus Dose
ROI2_pdose = StringVar()
textROI2_pdose = Entry(root, textvariable = ROI2_pdose)
textROI2_pdose.grid(column=1, row=4)
textROI2_pdose.config(width=27)

## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI2_pcrop = StringVar()
textROI2_pcrop = Entry(root, textvariable = ROI2_pcrop)
textROI2_pcrop.grid(column=2, row=4)
textROI2_pcrop.config(width=27)

## Get Priority for Plus
ROI2_pprio = StringVar()
textROI2_pprio = Entry(root, textvariable = ROI2_pprio)
textROI2_pprio.grid(column=3, row=4)
textROI2_pprio.config(width=27)

## Get Minus dose (eg. 105%, 103%)
ROI2_mdose = StringVar()
textROI2_mdose = Entry(root, textvariable = ROI2_mdose)
textROI2_mdose.grid(column=4, row=4)
textROI2_mdose.config(width=27)
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI2_mcrop = StringVar()
textROI2_mcrop = Entry(root, textvariable = ROI2_mcrop)
textROI2_mcrop.grid(column=5, row=4)
textROI2_mcrop.config(width=27)
## Get Priority for Minus 
ROI2_mprio = StringVar()
textROI2_mprio = Entry(root, textvariable = ROI2_mprio)
textROI2_mprio.grid(column=6, row=4)
textROI2_mprio.config(width=27)

# ROI3
## Get Name
ROI3 = StringVar()
ROI3_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI3_combo.insert(0,"--None--")
comboROI3 = ttk.Combobox(root, values= ROI3_combo, textvariable=ROI3)
comboROI3.grid(column=0, row=5)
comboROI3.config(width=27)
## Get Plus Dose
ROI3_pdose = StringVar()
textROI3_pdose = Entry(root, textvariable = ROI3_pdose)
textROI3_pdose.grid(column=1, row=5)
textROI3_pdose.config(width=27)

## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI3_pcrop = StringVar()
textROI3_pcrop = Entry(root, textvariable = ROI3_pcrop)
textROI3_pcrop.grid(column=2, row=5)
textROI3_pcrop.config(width=27)

## Get Priority for Plus
ROI3_pprio = StringVar()
textROI3_pprio = Entry(root, textvariable = ROI3_pprio)
textROI3_pprio.grid(column=3, row=5)
textROI3_pprio.config(width=27)

## Get Minus dose (eg. 105%, 103%)
ROI3_mdose = StringVar()
textROI3_mdose = Entry(root, textvariable = ROI3_mdose)
textROI3_mdose.grid(column=4, row=5)
textROI3_mdose.config(width=27)
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI3_mcrop = StringVar()
textROI3_mcrop = Entry(root, textvariable = ROI3_mcrop)
textROI3_mcrop.grid(column=5, row=5)
textROI3_mcrop.config(width=27)
## Get Priority for Minus 
ROI3_mprio = StringVar()
textROI3_mprio = Entry(root, textvariable = ROI3_mprio)
textROI3_mprio.grid(column=6, row=5)
textROI3_mprio.config(width=27)

# ROI4
## Get Name
ROI4 = StringVar()
ROI4_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI4_combo.insert(0,"--None--")
comboROI4 = ttk.Combobox(root, values= ROI4_combo, textvariable=ROI4)
comboROI4.grid(column=0, row=6)
comboROI4.config(width=27)
## Get Plus Dose
ROI4_pdose = StringVar()
textROI4_pdose = Entry(root, textvariable = ROI4_pdose)
textROI4_pdose.grid(column=1, row=6)
textROI4_pdose.config(width=27)

## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI4_pcrop = StringVar()
textROI4_pcrop = Entry(root, textvariable = ROI4_pcrop)
textROI4_pcrop.grid(column=2, row=6)
textROI4_pcrop.config(width=27)

## Get Priority for Plus
ROI4_pprio = StringVar()
textROI4_pprio = Entry(root, textvariable = ROI4_pprio)
textROI4_pprio.grid(column=3, row=6)
textROI4_pprio.config(width=27)

## Get Minus dose (eg. 105%, 103%)
ROI4_mdose = StringVar()
textROI4_mdose = Entry(root, textvariable = ROI4_mdose)
textROI4_mdose.grid(column=4, row=6)
textROI4_mdose.config(width=27)
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI4_mcrop = StringVar()
textROI4_mcrop = Entry(root, textvariable = ROI4_mcrop)
textROI4_mcrop.grid(column=5, row=6)
textROI4_mcrop.config(width=27)
## Get Priority for Minus 
ROI4_mprio = StringVar()
textROI4_mprio = Entry(root, textvariable = ROI4_mprio)
textROI4_mprio.grid(column=6, row=6)
textROI4_mprio.config(width=27)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate")
progress_bar.grid(column=5,row=7)



# Create PluseDose Contour Function
def create_plus_dose(dose, dose_level, name, roi_x, con):
        roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
        beamset = get_current('BeamSet')
        threshold_level = dose_level*100
        roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
        roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [roi_x], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"{name}"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
        roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"{name}"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [roi_x], 
                                                'MarginSettings': { 'Type': "Contract", 'Superior': con, 'Inferior': con, 
                                                                    'Anterior': con, 'Posterior': con, 
                                                                    'Right': con, 'Left': con } }, 
                                    ResultOperation="Intersection", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })                                                    
# Create MinusDose Contour Function
def create_minus_dose(dose, dose_level, name, roi_x, con):
        roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Blue", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
        beamset = get_current('BeamSet')
        threshold_level = dose_level*100
        roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
        roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"{name}"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [roi_x], 
                                                'MarginSettings': { 'Type': "Contract", 'Superior': con, 'Inferior': con, 
                                                                    'Anterior': con, 'Posterior': con, 
                                                                    'Right': con, 'Left': con } }, 
                                    ResultOperation="Intersection", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })                                                                      

def max_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth

def min_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth

def multiple_optz(optz_number=1):
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    for i in range(0, optz_number):
        print(f"Optimize {i}")
        Po.RunOptimization(ScalingOfSoftMachineConstraints=None)   

def GetAbsoluteVolumeAtDose(plan,roi,dose):
	Vd = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= roi, DoseValues=[dose])
	roi = case.PatientModel.StructureSets[0].RoiGeometries[roi]
	Vdcc = Vd*roi.GetRoiVolume()
	return Vdcc
# Loop Optimize Function
def create_contour_and_constrain(roi,plus,plus_prio,pcon,minus,minus_prio,mcon,i,dose,plan,po):
    name_plus = f"z{roi}_+{plus}_{i}"
    name_minus = f"z{roi}_-{minus}_{i}"
    print(f"Minus: {minus*100} cGy")
    print(f"Minus: {plus*100} cGy")
    minus_vol = GetAbsoluteVolumeAtDose(plan,roi,dose=minus*100)
    plus_d98 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=roi, RelativeVolumes=[0.98])
    print(minus_vol)
    print(plus_d98)
    if float(minus_vol) > float(2.0):
        create_minus_dose(dose,minus,name_minus,roi,mcon)
        max_dose(po, name_minus, dose_level=minus*100, weigth=minus_prio)
    if float(plus_d98) < float(plus*100):
        create_plus_dose(dose,plus,name_plus,roi,pcon)
        min_dose(po, name_plus, dose_level=plus*100, weigth=plus_prio)




# RUN
def run():
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    dose = plan.TreatmentCourse.TotalDose
    for i in range(0,int(NumL.get())):
        print(f'Num Loop = {int(NumL.get())}')
        print(f'Loop: {i+1}')
        create_contour_and_constrain(ROI1.get(),float(ROI1_pdose.get()),float(ROI1_pprio.get()),float(ROI1_pcrop.get())
                                    ,float(ROI1_mdose.get()),float(ROI1_mprio.get()),float(ROI1_mcrop.get()),int(i),dose,plan,Po)
        multiple_optz(optz_number= int(NumOL.get()))
    root.destroy()

# Button Loop Optimize
buttOpt = Button(root , text = 'RUN', command = run)
buttOpt.grid(column=6,row=7,pady=15)
buttOpt.config(width=10)

root.mainloop()