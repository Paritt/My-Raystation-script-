from connect import *
from tkinter import *
from tkinter import ttk, messagebox

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

plan = get_current("Plan")
Po = plan.PlanOptimizations[0]

def max_dvh(po, roi_name, dose_level, percent_volume, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.PercentVolume = percent_volume
    o.DoseFunctionParameters.Weight = weigth

def max_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth

def max_eud(po, roi_name, dose_level, eud_parameter, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.EudParameterA =  eud_parameter
    o.DoseFunctionParameters.Weight = weigth

def min_dvh(po, roi_name, dose_level, percent_volume, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinDvh", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.PercentVolume = percent_volume
    o.DoseFunctionParameters.Weight = weigth

def min_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth

def min_eud(po, roi_name, dose_level, eud_parameter, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinEud", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.EudParameterA = eud_parameter
    o.DoseFunctionParameters.Weight = weigth

def fall_off(po, roi_name, high_dose_level, low_dose_level, distance, weigth, adapt=False, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName = roi_name)
    o.DoseFunctionParameters.AdaptToTargetDoseLevels = adapt
    o.DoseFunctionParameters.HighDoseLevel = high_dose_level
    o.DoseFunctionParameters.LowDoseLevel = low_dose_level
    o.DoseFunctionParameters.LowDoseDistance = distance
    o.DoseFunctionParameters.Weight = weigth

def uniform_constraint(po, roi_name, stdv, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="UniformityConstraint", RoiName = roi_name, IsConstraint=True)
    o.DoseFunctionParameters.PercentStdDeviation = stdv
    
############################################################
#Loop optimize algorithum
############################################################
DosePrescription = float(50*100)
for i in range(1,6):
    print(f"Star Optimization loop {i}")
    ## 1.Reduce 100% outside target
    if i <= 2:
        MaxBodyNoPTV = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="zzBodynoPTV", RelativeVolumes=[0])
        print("Check 100 outside PTV")
    if MaxBodyNoPTV[0] > int(DosePrescription*0.99):
        print("Add objective for reduce 100 out PTV")
        max_eud(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), eud_parameter=10,weigth=60*i)
        max_dose(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), weigth=60*i)
        print(f"Optimizing reduce 100% outside target {i}")
        Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
    else:
        print("No 100 percent prescirption outside target")
    ## 2.Reduce 110%
    if i > 2 and i <= 4:
        MaxBodyNoPTV = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="zzBodynoPTV", RelativeVolumes=[0])
        MaxBody = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=body, RelativeVolumes=[0])
        MaxPtv = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="zzPTV", RelativeVolumes=[0])
        opt = False
        print("Check 110% condition")
        if MaxBodyNoPTV[0] > int(DosePrescription*0.99):
            print("Add objective for Reduce 110% in PTV")
            max_eud(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), eud_parameter=10,weigth=60*i)
            max_dose(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), weigth=60*i)
            opt = True
        if MaxBody[0] > int(DosePrescription*1.1):
            print("Add objective for Reduce 110% in body")
            create_contour_from_dose(plan.TreatmentCourse.TotalDose, 110, f"zzDose_110%_{i-2}")
            max_dose(Po, f"zzDose_110%_{i-2}", dose_level=int(DosePrescription*1.09), weigth=30*i)
            max_dose(Po, body, dose_level=int(DosePrescription*1.09), weigth=30*i)
            opt = True
        if opt:
            print(f"Optimizing Reduce 110% {i}")
            Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
        else:
            print("not opt yet")
    ## 3.Increase coverage
    if i > 4:
        MinDvhPtv = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="zzPTV", RelativeVolumes=[0.95])
        MinCtv = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="zzCTV", DoseValues=[int(DosePrescription)])
        opt = False
        print("Check cold condition")
        if MinDvhPtv[0] < int(DosePrescription):
            print("Add objective for increase cold")
            create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, f"zz100%_{i-4}")
            zicCover = case.PatientModel.CreateRoi(Name=f"zz+100%_{i-4}", Color="Yellow", Type="Control",
                                                    TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            zicCover.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV"], 
                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 } }, 
                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%_{i-4}"], 
                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 } }, 
                    ResultOperation="Subtraction", 
                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0.1,'Inferior': 0.1, 
                                            'Anterior': 0.1, 'Posterior': 0.1, 
                                            'Right': 0.1, 'Left': 0.1 })
            min_dvh(Po, f"zz+100%_{i-4}", dose_level=int(DosePrescription+100), percent_volume=100, weigth=110)
            opt = True
        if MinCtv[0] < int(DosePrescription):
            print("Add objective for increase cold")
            create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, f"zz100%_{i-4}")
            zicCoverC = case.PatientModel.CreateRoi(Name=f"zz+100%C_{i-4}", Color="Yellow", Type="Control",
                                                    TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            zicCoverC.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzCTV"], 
                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 } }, 
                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%_{i-4}"], 
                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 } }, 
                    ResultOperation="Subtraction", 
                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0.1,'Inferior': 0.1, 
                                            'Anterior': 0.1, 'Posterior': 0.1, 
                                            'Right': 0.1, 'Left': 0.1 })
            min_dvh(Po, f"zz+100%C_{i-4}", dose_level=int(DosePrescription+100), percent_volume=100, weigth=200)
            opt = True
            if opt:
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            else:
                print("not opt yet")