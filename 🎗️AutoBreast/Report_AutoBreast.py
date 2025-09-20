from connect import *

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")
plan = get_current("Plan")

def report_max(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Max")
    print(f"{ReportName} = {round(value/100,2)} Gy")
    return ReportName, round(value/100,2)
def report_mean(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Average")
    print(f"{ReportName} = {round(value/100,2)} Gy")
    return ReportName, round(value/100,2)
def report_min(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Min")
    print(f"{ReportName} = {round(value/100,2)} Gy")
    return ReportName, round(value/100,2)
def report_DoseAtVolume(plan, RoiName, ReportName, Volume):
    value = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName= RoiName, RelativeVolumes=[Volume/100])
    print(f"{ReportName} = {round(float(value/100),2)} Gy")
    return ReportName, round(float(value/100),2)
def report_VolumeAtDose(plan, RoiName, ReportName, Dose):
    value = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= RoiName, DoseValues=[Dose*100])
    print(f"{ReportName} = {round(float(value*100),2)}%")
    return ReportName, round(float(value*100),2)


report_max(plan = plan, RoiName = "BODY", ReportName = "Hot max")
report_DoseAtVolume(plan = plan, RoiName = "zzCTV", ReportName = "CTV D90%", Volume=90)
report_DoseAtVolume(plan = plan, RoiName = "zzCTV", ReportName = "CTV D95%", Volume=95)
report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D90%", Volume=90)
report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D95%", Volume=95)
report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D2%", Volume=2)
report_VolumeAtDose(plan = plan, RoiName = "zzPTV", ReportName = "PTV V105%", Dose=105)
report_mean(plan = plan, RoiName = "Heart", ReportName = "Heart Mean")
report_VolumeAtDose(plan = plan, RoiName = "Heart", ReportName = "Heart V20Gy", Dose=20)
report_VolumeAtDose(plan = plan, RoiName = "Lung Lt", ReportName = "Ipsilateral Lung V5Gy", Dose=5)
report_VolumeAtDose(plan = plan, RoiName = "Lung Lt", ReportName = "Ipsilateral Lung V20Gy", Dose=20)
report_VolumeAtDose(plan = plan, RoiName = "Lung Rt", ReportName = "Contralateral Lung V5Gy", Dose=5)
report_VolumeAtDose(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast V5Gy", Dose=5)
report_mean(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast Mean")
report_DoseAtVolume(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast D2%", Volume=2)
try: 
	report_mean(plan = plan, RoiName = "Thyroid Gland", ReportName = "Thyroid Mean")
except:
	print("No thyroid")