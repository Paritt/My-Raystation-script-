from connect import *

case = get_current('Case')
examination = get_current('Examination')
plan = get_current('Plan')
beam_set = get_current('BeamSet')
patient = get_current('Patient')

#Function for create Field Name of VMAT
def Arc_Direction():
    ArcDirect = beam_set.Beams[i].ArcRotationDirection
    if ArcDirect == 'Clockwise':
    	return 'CW'
    elif ArcDirect == 'CounterClockwise':
    	return 'CCW'

#Function for create setup field
def SetupField():
	Pt_position = beam_set.PatientPosition
	if Pt_position == 'HeadFirstSupine':
		try:
			beam_set.PatientSetup.SetupBeams['SB1_1'].Name = "I1"
			beam_set.PatientSetup.SetupBeams['I1'].Description = "kV AP"
			beam_set.PatientSetup.SetupBeams['SB1_2'].Name = "I2"
			beam_set.PatientSetup.SetupBeams['I2'].Description = "kV Lt Lat"
			beam_set.PatientSetup.SetupBeams['SB1_3'].Name = "I3"
			beam_set.PatientSetup.SetupBeams['I3'].Description = "CBCT"
			beam_set.PatientSetup.SetupBeams['I3'].GantryAngle = 0
		except:
			print('Setup field already set')
	elif Pt_position == 'HeadFirstProne':
		try:
			beam_set.PatientSetup.SetupBeams['SB1_1'].Name = "I1"
			beam_set.PatientSetup.SetupBeams['I1'].Description = "kV PA"
			beam_set.PatientSetup.SetupBeams['SB1_2'].Name = "I2"
			beam_set.PatientSetup.SetupBeams['I2'].Description = "kV Rt Lat"
			beam_set.PatientSetup.SetupBeams['SB1_3'].Name = "I3"
			beam_set.PatientSetup.SetupBeams['I3'].Description = "CBCT"
			beam_set.PatientSetup.SetupBeams['I3'].GantryAngle = 0
		except:
			print('Setup field already set')
	elif Pt_position == 'HeadFirstProne':
		try:
			beam_set.PatientSetup.SetupBeams['SB1_1'].Name = "I1"
			beam_set.PatientSetup.SetupBeams['I1'].Description = "kV AP"
			beam_set.PatientSetup.SetupBeams['SB1_2'].Name = "I2"
			beam_set.PatientSetup.SetupBeams['I2'].Description = "kV Rt Lat"
			beam_set.PatientSetup.SetupBeams['SB1_3'].Name = "I3"
			beam_set.PatientSetup.SetupBeams['I3'].Description = "CBCT"
			beam_set.PatientSetup.SetupBeams['I3'].GantryAngle = 0
		except:
			print('Setup field already set')



Technique = beam_set.GetTreatmentTechniqueType()
print(Technique)
i = 0

#Create field name includ gantry angle parameter, setup filed and creat QA plan for VMAT
if Technique == 'Conformal':
    while True:
        try:
            ConformAngleInt = int(beam_set.Beams[i].GantryAngle)
            beam_set.Beams[i].Description = str(i+1) + str('G') + str(ConformAngleInt)
            i=i+1
        except:
            print('Error')
            break
elif Technique == 'VMAT':
	List_Roi_Unknow =[e.Name for e in patient.Cases[0].PatientModel.RegionsOfInterest if e.OrganData.OrganType == "Unknown"]
	print(List_Roi_Unknow)
	case.PatientModel.ToggleExcludeFromExport(ExcludeFromExport=True, RegionOfInterests=List_Roi_Unknow, PointsOfInterests=[])
	while True:
		try:
			StartAngle = int(beam_set.Beams[i].GantryAngle)
			StopAngle = int(beam_set.Beams[i].ArcStopGantryAngle)
			beam_set.Beams[i].Description = str(i+1) + Arc_Direction() + str(StartAngle)+ str(' - ') + str(StopAngle)
			i=i+1
		except:
			print('Error')
			break            
	try:
		beam_set.CreateQAPlan(PhantomName="PTW OctaviusFull_3", PhantomId="12102015", 
						QAPlanName="QA2", IsoCenter={ 'x': 0, 'y': 0, 'z': 0 }, 
						DoseGrid={ 'x': 0.25, 'y': 0.25, 'z': 0.25 }, 
						GantryAngle=None, CollimatorAngle=None, CouchRotationAngle=None, 
						ComputeDoseWhenPlanIsCreated=True)
	except:
		print('Error create QA plan')
SetupField()

