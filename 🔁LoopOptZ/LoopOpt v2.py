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
root.geometry('1750x210')
#############################
# ROW 1
#############################
# Show Pt Name, HN, Plan Name
name = patient.Name
lbName = Label(root, text= f"Name: {name}")
lbName.grid(column=1,row=1)
lbName.config(width=27, height =2)

hn = patient.PatientID
lbHN = Label(root, text= f"HN: {hn}")
lbHN.grid(column=2 ,row=1)
lbHN.config(width=27, height =2)

plan_name = plan.Name
lbHN = Label(root, text= f"Plan name: {plan_name}")
lbHN.grid(column=3 ,row=1)
lbHN.config(width=27, height =2)

# No. of Loop
lbLoop = Label(root, text= 'No. of Loop')
lbLoop.grid(column=4 ,row=1)
lbLoop.config(width=27, height =2)
NumL = StringVar()
textNumL = Entry(root, textvariable = NumL)
textNumL.grid(column=5,row=1)
textNumL.config(width=27)
textNumL.insert(0, "2")

# No. of Oprimize/Loop
lbOptL = Label(root, text= 'No. of Oprimize/Loop')
lbOptL.grid(column=6 ,row=1)
lbOptL.config(width=27, height =2)
NumOL = StringVar()
textNumOL = Entry(root, textvariable = NumOL)
textNumOL.grid(column=7,row=1)
textNumOL.config(width=27)
textNumOL.insert(0, "2")

#############################
# ROW 2
#############################
lbROI = Label(root, text= 'ROI')
lbROI.config(width=27, height =2)
lbROI.grid(column=0 ,row=2)

lbcdose = Label(root, text= 'Convert Plus Dose (Gy)')
lbcdose.config(width=27, height =2)
lbcdose.grid(column=1 ,row=2)

lbdose = Label(root, text= 'Plus Dose (Gy)')
lbdose.config(width=27, height =2)
lbdose.grid(column=2 ,row=2)

lbcrop = Label(root, text= 'Boarder crop (cm)')
lbcrop.config(width=27, height =2)
lbcrop.grid(column=3 ,row=2)

lbPriority = Label(root, text= 'Priority')
lbPriority.config(width=27, height =2)
lbPriority.grid(column=4 ,row=2)

lbcdose = Label(root, text= 'Convert Minus Dose (Gy)')
lbcdose.config(width=27, height =2)
lbcdose.grid(column=5 ,row=2)

lbdose = Label(root, text= 'Minus Dose (Gy)')
lbdose.config(width=27, height =2)
lbdose.grid(column=6 ,row=2)

lbcrop = Label(root, text= 'Boarder crop (cm)')
lbcrop.config(width=27, height =2)
lbcrop.grid(column=7 ,row=2)

lbPriority = Label(root, text= 'Priority')
lbPriority.config(width=27, height =2)
lbPriority.grid(column=8 ,row=2)

#############################
# ROW 3+
#############################
# ROI 1
## Get Name
ROI1 = StringVar()
ROI1_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
comboROI1 = ttk.Combobox(root, values= ROI1_combo, textvariable=ROI1)
comboROI1.grid(column=0, row=3)
comboROI1.config(width=27)

## Get Convert Plus Dose
ROI1_convertp = StringVar()
textROI1_convertp = Entry(root, textvariable = ROI1_convertp)
textROI1_convertp.grid(column=1, row=3)
textROI1_convertp.config(width=27)

## Get Plus Dose
ROI1_pdose = StringVar()
textROI1_pdose = Entry(root, textvariable = ROI1_pdose)
textROI1_pdose.grid(column=2, row=3)
textROI1_pdose.config(width=27)

## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI1_pcrop = StringVar()
textROI1_pcrop = Entry(root, textvariable = ROI1_pcrop)
textROI1_pcrop.grid(column=3, row=3)
textROI1_pcrop.config(width=27)

## Get Priority for Plus
ROI1_pprio = StringVar()
textROI1_pprio = Entry(root, textvariable = ROI1_pprio)
textROI1_pprio.grid(column=4, row=3)
textROI1_pprio.config(width=27)

## Get Convert Minus Dose
ROI1_convertm = StringVar()
textROI1_convertm = Entry(root, textvariable = ROI1_convertm)
textROI1_convertm.grid(column=5, row=3)
textROI1_convertm.config(width=27)

## Get Minus dose (eg. 105%, 103%)
ROI1_mdose = StringVar()
textROI1_mdose = Entry(root, textvariable = ROI1_mdose)
textROI1_mdose.grid(column=6, row=3)
textROI1_mdose.config(width=27)
## Get crop from boarder for Minus (eg. 0.3 cm)
ROI1_mcrop = StringVar()
textROI1_mcrop = Entry(root, textvariable = ROI1_mcrop)
textROI1_mcrop.grid(column=7, row=3)
textROI1_mcrop.config(width=27)
## Get Priority for Minus 
ROI1_mprio = StringVar()
textROI1_mprio = Entry(root, textvariable = ROI1_mprio)
textROI1_mprio.grid(column=8, row=3)
textROI1_mprio.config(width=27)

# ROI2
## Get Name
ROI2 = StringVar()
ROI2_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI2_combo.insert(0,"--None--")
comboROI2 = ttk.Combobox(root, values= ROI2_combo, textvariable=ROI2)
comboROI2.grid(column=0, row=4)
comboROI2.config(width=27)
comboROI2.set("--None--")
## Get Convert Plus Dose
ROI2_convertp = StringVar()
textROI2_convertp = Entry(root, textvariable = ROI2_convertp)
textROI2_convertp.grid(column=1, row=4)
textROI2_convertp.config(width=27)
textROI2_convertp.insert(0, "-")
## Get Plus Dose
ROI2_pdose = StringVar()
textROI2_pdose = Entry(root, textvariable = ROI2_pdose)
textROI2_pdose.grid(column=2, row=4)
textROI2_pdose.config(width=27)
textROI2_pdose.insert(0, "-")
## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI2_pcrop = StringVar()
textROI2_pcrop = Entry(root, textvariable = ROI2_pcrop)
textROI2_pcrop.grid(column=3, row=4)
textROI2_pcrop.config(width=27)
textROI2_pcrop.insert(0, "-")
## Get Priority for Plus
ROI2_pprio = StringVar()
textROI2_pprio = Entry(root, textvariable = ROI2_pprio)
textROI2_pprio.grid(column=4, row=4)
textROI2_pprio.config(width=27)
textROI2_pprio.insert(0, "-")
## Get Convert Minus Dose
ROI2_convertm = StringVar()
textROI2_convertm = Entry(root, textvariable = ROI2_convertm)
textROI2_convertm.grid(column=5, row=4)
textROI2_convertm.config(width=27)
textROI2_convertm.insert(0, "-")
## Get Minus dose (eg. 105%, 103%)
ROI2_mdose = StringVar()
textROI2_mdose = Entry(root, textvariable = ROI2_mdose)
textROI2_mdose.grid(column=6, row=4)
textROI2_mdose.config(width=27)
textROI2_mdose.insert(0, "-")
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI2_mcrop = StringVar()
textROI2_mcrop = Entry(root, textvariable = ROI2_mcrop)
textROI2_mcrop.grid(column=7, row=4)
textROI2_mcrop.config(width=27)
textROI2_mcrop.insert(0, "-")
## Get Priority for Minus 
ROI2_mprio = StringVar()
textROI2_mprio = Entry(root, textvariable = ROI2_mprio)
textROI2_mprio.grid(column=8, row=4)
textROI2_mprio.config(width=27)
textROI2_mprio.insert(0, "-")

# ROI3
## Get Name
ROI3 = StringVar()
ROI3_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI3_combo.insert(0,"--None--")
comboROI3 = ttk.Combobox(root, values= ROI3_combo, textvariable=ROI3)
comboROI3.grid(column=0, row=5)
comboROI3.config(width=27)
comboROI3.set("--None--")
## Get Convert Plus Dose
ROI3_convertp = StringVar()
textROI3_convertp = Entry(root, textvariable = ROI3_convertp)
textROI3_convertp.grid(column=1, row=5)
textROI3_convertp.config(width=27)
textROI3_convertp.insert(0, "-")
## Get Plus Dose
ROI3_pdose = StringVar()
textROI3_pdose = Entry(root, textvariable = ROI3_pdose)
textROI3_pdose.grid(column=2, row=5)
textROI3_pdose.config(width=27)
textROI3_pdose.insert(0, "-")
## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI3_pcrop = StringVar()
textROI3_pcrop = Entry(root, textvariable = ROI3_pcrop)
textROI3_pcrop.grid(column=3, row=5)
textROI3_pcrop.config(width=27)
textROI3_pcrop.insert(0, "-")
## Get Priority for Plus
ROI3_pprio = StringVar()
textROI3_pprio = Entry(root, textvariable = ROI3_pprio)
textROI3_pprio.grid(column=4, row=5)
textROI3_pprio.config(width=27)
textROI3_pprio.insert(0, "-")
## Get Convert Minus Dose
ROI3_convertm = StringVar()
textROI3_convertm = Entry(root, textvariable = ROI3_convertm)
textROI3_convertm.grid(column=5, row=5)
textROI3_convertm.config(width=27)
textROI3_convertm.insert(0, "-")
## Get Minus dose (eg. 105%, 103%)
ROI3_mdose = StringVar()
textROI3_mdose = Entry(root, textvariable = ROI3_mdose)
textROI3_mdose.grid(column=6, row=5)
textROI3_mdose.config(width=27)
textROI3_mdose.insert(0, "-")
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI3_mcrop = StringVar()
textROI3_mcrop = Entry(root, textvariable = ROI3_mcrop)
textROI3_mcrop.grid(column=7, row=5)
textROI3_mcrop.config(width=27)
textROI3_mcrop.insert(0, "-")
## Get Priority for Minus 
ROI3_mprio = StringVar()
textROI3_mprio = Entry(root, textvariable = ROI3_mprio)
textROI3_mprio.grid(column=8, row=5)
textROI3_mprio.config(width=27)
textROI3_mprio.insert(0, "-")

# ROI4
## Get Name
ROI4 = StringVar()
ROI4_combo = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ROI4_combo.insert(0,"--None--")
comboROI4 = ttk.Combobox(root, values= ROI4_combo, textvariable=ROI4)
comboROI4.grid(column=0, row=6)
comboROI4.config(width=27)
comboROI4.set("--None--")
## Get Convert Plus Dose
ROI4_convertp = StringVar()
textROI4_convertp = Entry(root, textvariable = ROI4_convertp)
textROI4_convertp.grid(column=1, row=6)
textROI4_convertp.config(width=27)
textROI4_convertp.insert(0, "-")
## Get Plus Dose
ROI4_pdose = StringVar()
textROI4_pdose = Entry(root, textvariable = ROI4_pdose)
textROI4_pdose.grid(column=2, row=6)
textROI4_pdose.config(width=27)
textROI4_pdose.insert(0, "-")
## Get crop from boarder for Pluse (eg. 0.3 cm)
ROI4_pcrop = StringVar()
textROI4_pcrop = Entry(root, textvariable = ROI4_pcrop)
textROI4_pcrop.grid(column=3, row=6)
textROI4_pcrop.config(width=27)
textROI4_pcrop.insert(0, "-")
## Get Priority for Plus
ROI4_pprio = StringVar()
textROI4_pprio = Entry(root, textvariable = ROI4_pprio)
textROI4_pprio.grid(column=4, row=6)
textROI4_pprio.config(width=27)
textROI4_pprio.insert(0, "-")
## Get Convert Minus Dose
ROI4_convertm = StringVar()
textROI4_convertm = Entry(root, textvariable = ROI4_convertm)
textROI4_convertm.grid(column=5, row=6)
textROI4_convertm.config(width=27)
textROI4_convertm.insert(0, "-")
## Get Minus dose (eg. 105%, 103%)
ROI4_mdose = StringVar()
textROI4_mdose = Entry(root, textvariable = ROI4_mdose)
textROI4_mdose.grid(column=6, row=6)
textROI4_mdose.config(width=27)
textROI4_mdose.insert(0, "-")
## Get crop from boarder for Minus (eg. 0.4 cm)
ROI4_mcrop = StringVar()
textROI4_mcrop = Entry(root, textvariable = ROI4_mcrop)
textROI4_mcrop.grid(column=7, row=6)
textROI4_mcrop.config(width=27)
textROI4_mcrop.insert(0, "-")
## Get Priority for Minus 
ROI4_mprio = StringVar()
textROI4_mprio = Entry(root, textvariable = ROI4_mprio)
textROI4_mprio.grid(column=8, row=6)
textROI4_mprio.config(width=27)
textROI4_mprio.insert(0, "-")

# # Progress Bar
# progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate")
# progress_bar.grid(column=7,row=7)



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
def create_contour_and_constrain(roi, cplus, plus,plus_prio,pcon, cminus, minus,minus_prio,mcon,i,dose,plan,po):
    name_plus = f"z{roi}_+{plus}_{i}"
    name_minus = f"z{roi}_-{minus}_{i}"
    print(f"Minus: {minus*100} cGy")
    print(f"Minus: {plus*100} cGy")
    minus_vol = GetAbsoluteVolumeAtDose(plan,roi,dose=minus*100)
    plus_d98 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=roi, RelativeVolumes=[0.98])
    print(minus_vol)
    print(plus_d98)
    if float(minus_vol) > float(2.0):
        create_minus_dose(dose,cminus,name_minus,roi,mcon)
        max_dose(po, name_minus, dose_level=minus*100, weigth=minus_prio)
    if float(plus_d98) < float(plus*100):
        create_plus_dose(dose,cplus,name_plus,roi,pcon)
        min_dose(po, name_plus, dose_level=plus*100, weigth=plus_prio)




# RUN
def run():
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    dose = plan.TreatmentCourse.TotalDose
    roi2 = ROI2.get()
    roi3 = ROI3.get()
    roi4 = ROI4.get()
    for i in range(0,int(NumL.get())):
        print(f'Num Loop = {int(NumL.get())}')
        print(f'Loop: {i}')
        create_contour_and_constrain(ROI1.get(), float(ROI1_convertp.get()), float(ROI1_pdose.get()),float(ROI1_pprio.get()),float(ROI1_pcrop.get())
                                    , float(ROI1_convertm.get()), float(ROI1_mdose.get()),float(ROI1_mprio.get()),float(ROI1_mcrop.get()),int(i),dose,plan,Po)
        if roi2 != "--None--":
             create_contour_and_constrain(ROI2.get(), float(ROI2_convertp.get()), float(ROI2_pdose.get()),float(ROI2_pprio.get()),float(ROI2_pcrop.get())
                                    , float(ROI2_convertm.get()), float(ROI2_mdose.get()),float(ROI2_mprio.get()),float(ROI2_mcrop.get()),int(i),dose,plan,Po)
        if roi3 != "--None--":
             create_contour_and_constrain(ROI3.get(), float(ROI3_convertp.get()), float(ROI3_pdose.get()),float(ROI3_pprio.get()),float(ROI3_pcrop.get())
                                    , float(ROI3_convertm.get()), float(ROI3_mdose.get()),float(ROI3_mprio.get()),float(ROI3_mcrop.get()),int(i),dose,plan,Po) 
        if roi4 != "--None--":
             create_contour_and_constrain(ROI4.get(), float(ROI4_convertp.get()), float(ROI4_pdose.get()),float(ROI4_pprio.get()),float(ROI4_pcrop.get())
                                    , float(ROI4_convertm.get()), float(ROI4_mdose.get()),float(ROI4_mprio.get()),float(ROI4_mcrop.get()),int(i),dose,plan,Po)            
        multiple_optz(optz_number= int(NumOL.get()))
    root.destroy()

# Button Loop Optimize
buttOpt = Button(root , text = 'RUN', command = run)
buttOpt.grid(column=8,row=7,pady=15)
buttOpt.config(width=10)

root.mainloop()