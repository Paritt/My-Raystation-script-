from connect import *

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")
plan = get_current("Plan")

def report_max(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Max")
    print(f"{ReportName} = {round(float(value/100),2)} Gy")
    return ReportName, round(float(value/100),2)
def report_mean(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Average")
    print(f"{ReportName} = {round(float(value/100),2)} Gy")
    return ReportName, round(float(value/100),2)
def report_min(plan, RoiName, ReportName):
    value = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = RoiName, DoseType = "Min")
    print(f"{ReportName} = {float(round(value/100),2)} Gy")
    return ReportName, round(float(value/100),2)
def report_DoseAtVolume(plan, RoiName, ReportName, Volume):
    value = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName= RoiName, RelativeVolumes=[Volume/100])
    print(f"{ReportName} = {round(float(value/100),2)} Gy")
    return ReportName, round(float(value/100),2)
def report_VolumeAtDose(plan, RoiName, ReportName, Dose):
    value = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= RoiName, DoseValues=[Dose*100])
    print(f"{ReportName} = {round(float(value*100),2)}%")
    return ReportName, round(float(value*100),2)
def GetAbsoluteVolumeAtDose(plan,roi,dose):
	Vd = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= roi, DoseValues=[dose*100])
	roi = case.PatientModel.StructureSets[0].RoiGeometries[roi]
	Vdcc = Vd*roi.GetRoiVolume()
	return Vdcc

report_list = []
[rn, v] = report_max(plan = plan, RoiName = "BODY", ReportName = "Hot max")
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzCTV", ReportName = "CTV D90%", Volume=90)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzCTV", ReportName = "CTV D95%", Volume=95)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzCTV", ReportName = "CTV D98%", Volume=98)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D90%", Volume=90)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D95%", Volume=95)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D98%", Volume=98)
report_list.append([rn, v])
[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "zzPTV", ReportName = "PTV D2%", Volume=2)
report_list.append([rn, v])
[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "zzPTV", ReportName = "PTV V105%", Dose=1.05*50)
report_list.append([rn, v])
[rn, v] = report_mean(plan = plan, RoiName = "Heart", ReportName = "Heart Mean")
report_list.append([rn, v])
[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Heart", ReportName = "Heart V20Gy", Dose=20)
report_list.append([rn, v])
[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Lung Lt", ReportName = "Ipsilateral Lung V5Gy", Dose=5)
report_list.append([rn, v])
[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Lung Lt", ReportName = "Ipsilateral Lung V20Gy", Dose=20)
report_list.append([rn, v])
[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Lung Rt", ReportName = "Contralateral Lung V5Gy", Dose=5)
report_list.append([rn, v])
try: 
	[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast V5Gy", Dose=5)
	report_list.append([rn, v])
	[rn, v] = report_mean(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast Mean")
	report_list.append([rn, v])
	[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "Breast Rt", ReportName = "Contralateral Breast D2%", Volume=2)
	report_list.append([rn, v])
except:
	[rn, v] = report_VolumeAtDose(plan = plan, RoiName = "Contralat breast", ReportName = "Contralateral Breast V5Gy", Dose=5)
	report_list.append([rn, v])
	[rn, v] = report_mean(plan = plan, RoiName = "Contralat breast", ReportName = "Contralateral Breast Mean")
	report_list.append([rn, v])
	[rn, v] = report_DoseAtVolume(plan = plan, RoiName = "Contralat breast", ReportName = "Contralateral Breast D2%", Volume=2)
	report_list.append([rn, v])
try: 
	[rn, v] = report_mean(plan = plan, RoiName = "Thyroid Gland", ReportName = "Thyroid Mean")
	report_list.append([rn, v])
except:
	print("No Thyroid")

for i in range(len(report_list)):
    print(f"{report_list[i][0]} = {report_list[i][1]}")