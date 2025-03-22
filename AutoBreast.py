from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('Plan design')
root.geometry('400x550')

def show_error():
    messagebox.showerror("ERROR", "Sorry, please check execution details")

#For select CT calibration curve
lbCT = Label(root, text= 'Select CT Curve')
lbCT.grid(column=0 , row=0)
lbCT.config(width=27, height =2)
CT_Curve=examination.EquipmentInfo.ImagingSystemReference
try:
    if CT_Curve.ImagingSystemName == "CTAWP100076":
        lbCT3 = Label(root, text= 'Used CT3_Siemens')
        lbCT3.grid(column=1 , row=0)
        lbCT3.config(width=27, height =2)
    elif CT_Curve.ImagingSystemName == "HOST-768005":
        lbCT3 = Label(root, text= 'Used CT1_PhilipsBigBore')
        lbCT3.grid(column=1 , row=0)
        lbCT3.config(width=27, height =2)
    else:
        combo_variableCT = StringVar()
        combo_CT = ['Siemens 120kVp', 'Philips RT Big Bore 120kV']
        comboMac = ttk.Combobox(root, values = combo_CT, textvariable= combo_variableCT)
        comboMac.grid(column=1,row=0)
        comboMac.config(width=27, height =2)
except:
    combo_variableCT = StringVar()
    combo_CT = ['Siemens 120kVp', 'Philips RT Big Bore 120kV']
    comboMac = ttk.Combobox(root, values = combo_CT, textvariable= combo_variableCT)
    comboMac.grid(column=1,row=0)
    comboMac.config(width=27, height =2)
def get_CT_Curve():
    print("Getting CT cureve")
    CT_Curve=examination.EquipmentInfo.ImagingSystemReference
    if CT_Curve.ImagingSystemName == "CTAWP100076":
    	print('Use CT3')
    elif CT_Curve.ImagingSystemName == "HOST-768005":
    	print('Use CT1')
    else:
    	print("get selected CT")
    	Select_CT = combo_variableCT.get()
    	print(f"Selected CT = {Select_CT}")
    	if Select_CT == "Siemens 120kVp":
    		CT_Curve.ImagingSystemName = "Siemens 120kVp"
    		print('Use Siemens 120kVp')
    	elif Select_CT == "Philips RT Big Bore 120kV":
    		CT_Curve.ImagingSystemName = "Philips RT Big Bore 120kV"
    		print('Use Philips RT Big Bore 120kV')


#Combobox for select treatment machine
lbMac = Label(root, text= 'Select Machine')
lbMac.grid(column=0 , row=1)
lbMac.config(width=27, height =2)
combo_variableMac = StringVar()
combo_machine = ['N3_VersaHD', 'N4_VersaHD','TrueBeam_L6', 'TrueBeam_L7', 'TrueBeam_N5']
comboMac = ttk.Combobox(root, values = combo_machine, textvariable= combo_variableMac)
comboMac.grid(column=1,row=1)
comboMac.config(width=27, height =2)

#textbox for insert number of fraction
lbFac = Label(root, text= 'Fill No. of Fraction')
lbFac.grid(column=0 ,row=2)
lbFac.config(width=27, height =2)
NumF = StringVar()
textNumF = Entry(root, textvariable = NumF)
textNumF.grid(column=1,row=2)
textNumF.config(width=27)

#textbox for insert Dose prescription
lbTotalDose = Label(root, text= 'Fill Total dose (Gy)')
lbTotalDose.grid(column=0 ,row=3)
lbTotalDose.config(width=27, height =2)
TotalDose_Gy = StringVar()
textTotalDose = Entry(root, textvariable = TotalDose_Gy)
textTotalDose.grid(column=1,row=3)
textTotalDose.config(width=27)

#Test open patient
try:
    patient = get_current('Patient')
except:
    messagebox.showinfo('No patient selected. \nScript terminated')
    exit()
 
#Combobox for select Roi for dose prescription
lbRoiPre = Label(root, text = 'Prescription to')
lbRoiPre.grid(column=0,row=4)
lbRoiPre.config(width=27, height =2)
combo_variableRoiPre = StringVar()
combo_valuesRoiPre = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
comboRoiPre = ttk.Combobox(root, values= combo_valuesRoiPre, textvariable=combo_variableRoiPre)
comboRoiPre.grid(column=1,row=4)
comboRoiPre.config(width=27, height =20)

#Combobox for select isocenter to center of Roi or poi
lbIso = Label(root, text= 'Isocenter placment')
lbIso.grid(column=0 , row=5)
lbIso.config(width=27, height =2)
combo_variableIso = StringVar()
combo_Iso = [i.Name for i in patient.Cases[0].PatientModel.PointsOfInterest]
comboIso = ttk.Combobox(root, values = combo_Iso, textvariable= combo_variableIso)
comboIso.grid(column=1,row=5)
comboIso.config(width=27, height =5)

#Combobox for select photon energy
lbPhotonE = Label(root, text= 'Select photon energy')
lbPhotonE.grid(column=0 , row=6)
lbPhotonE.config(width=27, height =2)
combo_variablePhotonE = StringVar()
combo_PhotonE = ['6', '10', '6 FFF']
comboPhotonE = ttk.Combobox(root, values = combo_PhotonE, textvariable= combo_variablePhotonE)
comboPhotonE.grid(column=1,row=6)
comboPhotonE.config(width=27, height =5)

#textbox for insert Start Gantry angle
lbStartGantry = Label(root, text= 'Star Gantry angle')
lbStartGantry.grid(column=0 ,row=7)
lbStartGantry.config(width=27, height =2)
StartGantry = StringVar()
textStartGantry = Entry(root, textvariable = StartGantry)
textStartGantry.grid(column=1,row=7)
textStartGantry.config(width=27)

#textbox for insert Start Gantry angle
lbMidGantry = Label(root, text= 'Mid Gantry angle')
lbMidGantry.grid(column=0 ,row=8)
lbMidGantry.config(width=27, height =2)
MidGantry = StringVar()
textMidGantry = Entry(root, textvariable = MidGantry)
textMidGantry.grid(column=1,row=8)
textMidGantry.config(width=27)

#textbox for insert Start Gantry angle
lbStopGantry = Label(root, text= 'Stop Gantry angle')
lbStopGantry.grid(column=0 ,row=9)
lbStopGantry.config(width=27, height =2)
StopGantry = StringVar()
textStopGantry = Entry(root, textvariable = StopGantry)
textStopGantry.grid(column=1,row=9)
textStopGantry.config(width=27)

#textbox for insert Med collimator angle
lbMedColli = Label(root, text= 'Medial collimator angle')
lbMedColli.grid(column=0 ,row=10)
lbMedColli.config(width=27, height =2)
MedColli = StringVar()
textMedColli = Entry(root, textvariable = MedColli)
textMedColli.grid(column=1,row=10)
textMedColli.config(width=27)

#textbox for insert Lat collimator angle
lbLatColli = Label(root, text= 'Lateral collimator angle')
lbLatColli.grid(column=0 ,row=11)
lbLatColli.config(width=27, height =2)
LatColli = StringVar()
textLatColli = Entry(root, textvariable = LatColli)
textLatColli.grid(column=1,row=11)
textLatColli.config(width=27)


#For match ROI to optimization
ptv = "PTV"
ctv = "CTV"
lt_lung = "Lung Lt"
rt_lung = "Lung Rt"
rt_breast = "Breast Rt"
heart = "Heart"
thyroid = "Thyroid Gland"
eso = "Esophagus"
body = "BODY"
arm = "zArm"

def Button_MatchRoi():
    Sub_root1 = Toplevel()
    Sub_root1.title('Match Roi')
    Sub_root1.geometry('320x420')
    ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]

    def lbMatch(root_frame=Sub_root1,  List = ListRoi, roi = 'ROI', row_n = 0):
        lbMatchROI = Label(root_frame, text= roi)
        lbMatchROI.grid(column=0 , row=row_n)
        lbMatchROI.config(width=15, height =2)
        if roi in ListRoi:
            lbMatchROI = Label(root_frame, text= 'Matched')
            lbMatchROI.grid(column=1 , row=row_n)
            lbMatchROI.config(width=27, height =2)
            return None
        else:
            combo_ROI = StringVar()
            comboROI = ttk.Combobox(root_frame, values = ListRoi, textvariable= combo_ROI)
            comboROI.grid(column=1,row=row_n)
            comboROI.config(width=27, height =20)
            return combo_ROI

    combo_PTV = lbMatch(Sub_root1, ListRoi, roi = "PTV", row_n = 0)
    combo_CTV = lbMatch(Sub_root1, ListRoi, roi = "CTV", row_n = 1)
    combo_LtLung = lbMatch(Sub_root1, ListRoi, roi = "Lt Lung", row_n = 2)
    combo_RtLung = lbMatch(Sub_root1, ListRoi, roi = "Rt Lung", row_n = 3)
    combo_RtBreast = lbMatch(Sub_root1, ListRoi, roi = "Rt Breast", row_n = 4)
    combo_heart = lbMatch(Sub_root1, ListRoi, roi = "Heart", row_n = 5)
    combo_thyroid = lbMatch(Sub_root1, ListRoi, roi = "Thyroid Gland", row_n = 6)
    combo_eso = lbMatch(Sub_root1, ListRoi, roi = "Esophagus", row_n = 7)
    combo_body = lbMatch(Sub_root1, ListRoi, roi = "BODY", row_n = 8)
    combo_arm = lbMatch(Sub_root1, ListRoi, roi = "zArm", row_n = 9)

    #Cancel Button in Sub_root1
    def Button_Cancel_sub1():
        Sub_root1.destroy()

    buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
    buttCancelSub1.grid(column=0,row=10,pady=15)
    buttCancelSub1.config(width=10)

    #Apply Button in Sub_root1
    def Button_Apply_sub1():
        global ptv
        global ctv
        global lt_lung
        global rt_breast
        global rt_lung
        global heart
        global thyroid
        global eso
        global body
        global arm
        if "PTV" in ListRoi:
            ptv = "PTV"
        else:
            ptv = combo_PTV.get()
        if "CTV" in ListRoi:
            ctv = "CTV"
        else:
            ctv = combo_CTV.get()
        if "Lung Lt" in ListRoi:
            lt_lung = "Lung Lt"
        else:
            lt_lung = combo_LtLung.get()
        if "Lung Rt" in ListRoi:
            rt_lung = "Lung Rt"
        else:
            rt_lung = combo_RtLung.get()
        if "Breast Rt" in ListRoi:
            rt_breast = "Breast Rt"
        else:
            rt_breast = combo_RtBreast.get()
        if "Heart" in ListRoi:
            heart = "Heart"
        else:
            heart = combo_heart.get()
        if "Thyroid Gland" in ListRoi:
            thyroid = "Thyroid Gland"
        else:
            thyroid = combo_thyroid.get()
        if "Esophagus" in ListRoi:
            eso = "Esophagus"
        else:
            eso = combo_eso.get()
        if "BODY" in ListRoi:
            body = "BODY"
        else:
            body = combo_body.get()
        if "zArm" in ListRoi:
            arm = "zArm"
        else:
            arm = combo_arm.get()
        Sub_root1.destroy()

    buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
    buttApplySub1.grid(column=1,row=10,pady=15)
    buttApplySub1.config(width=10)
 
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=12)
lbMatchRoi.config(width=27, height =2)
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = ["PTV","CTV","Lung Lt","Lung Rt","Breast Rt","Heart","Esophagus","Thyroid Gland","BODY","zArm"]
print(ListRoi)

for roi in ListRoiOpt:
	if roi in ListRoi:
	    lbMatchRoi2 = Label(root, text= 'Already match roi')
	    lbMatchRoi2.grid(column=1 , row=12)
	    lbMatchRoi2.config(width=27, height =2)
	    continue
	else:
	    buttMatch = Button(root, text = 'Match ROI', command = Button_MatchRoi)
	    buttMatch.grid(column=1,row=12,padx=10,pady=5)
	    buttMatch.config(width=15)
	    break

#Cancel Button
def Button_Cancel(): 
    root.destroy()

buttCancel = Button(root, text = 'Cancel', command = Button_Cancel)
buttCancel.grid(column=0,row=13,padx=10,pady=25)
buttCancel.config(width=15)  
def AddCostFuncn():
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    DosePrescription = float(TotalDose_Gy.get()) * 100
    
def create_contour_from_dose(dose, dose_level, name):
	roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print("Create D105%")
 
def create_virtual():
    # zPTV
    zPTV = case.PatientModel.CreateRoi(Name="zzPTV", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                        'MarginSettings': { 'Type': "Contract", 'Superior': 0.3, 'Inferior': 0.3, 
                                                            'Anterior': 0.3, 'Posterior': 0.3, 
                                                            'Right': 0.3, 'Left': 0.3 } }, 
                            ResultOperation="Intersection", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    # zCTV
    zCTV = case.PatientModel.CreateRoi(Name="zzCTV", Color="Red", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zCTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ctv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                'Anterior': 0.3, 'Posterior': 0.3, 
                                                                'Right': 0.3, 'Left': 0.3 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zRing
    zRing = case.PatientModel.CreateRoi(Name="zzRing", Color="White", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 1, 'Posterior': 1, 
                                                                'Right': 1, 'Left': 1 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0.3, 'Posterior': 0.3, 
                                                                'Right': 0.3, 'Left': 0.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzRing"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                'Anterior': 0.3, 'Posterior': 0.3, 
                                                                'Right': 0.3, 'Left': 0.3 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zSkinFlash
    zSkinFlash = case.PatientModel.CreateRoi(Name="zzSkinFlash", Color="Pink", Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zSkinFlash.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 1 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="None", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zLtLung
    zLtLung = case.PatientModel.CreateRoi(Name="zzLtLung", Color="Blue", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zLtLung.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [lt_lung], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                'Anterior': 1.3, 'Posterior': 1.3, 
                                                                'Right': 1.3, 'Left': 1.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zHeart
    zHeart = case.PatientModel.CreateRoi(Name="zzHeart", Color="Red", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zHeart.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [heart], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                'Anterior': 1.3, 'Posterior': 1.3, 
                                                                'Right': 1.3, 'Left': 1.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zLiver_Stomach
    zLiver_Stomach = case.PatientModel.CreateRoi(Name="zzLiver_Stomach", Color="Green", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zLiver_Stomach.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [lt_lung,rt_lung,heart], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 10, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                    'Anterior': 1.3, 'Posterior': 1.3, 
                                                                    'Right': 1.3, 'Left': 1.3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
    zLiver_Stomach.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzLiver_Stomach"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [lt_lung,rt_lung,heart], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })

    case.PatientModel.StructureSets['CT Plan'].SimplifyContours(RoiNames=["zzLiver_Stomach"], RemoveHoles3D=False, RemoveSmallContours=True, AreaThreshold=50, ReduceMaxNumberOfPointsInContours=False, MaxNumberOfPoints=None, CreateCopyOfRoi=False, ResolveOverlappingContours=False)
    
    # zLiver_Stomach
    zGV = case.PatientModel.CreateRoi(Name="zzGV", Color="Aqua", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zGV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [heart], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 5, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                    'Anterior': 2, 'Posterior': 2, 
                                                                    'Right': 2, 'Left': 2 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
    zGV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzGV"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [heart], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })

    case.PatientModel.StructureSets['CT Plan'].SimplifyContours(RoiNames=["zzGV"], RemoveHoles3D=False, RemoveSmallContours=True, AreaThreshold=20, ReduceMaxNumberOfPointsInContours=False, MaxNumberOfPoints=None, CreateCopyOfRoi=False, ResolveOverlappingContours=False)

    # zThyroid
    zThyroid = case.PatientModel.CreateRoi(Name="zzThyroid", Color="Purple", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zThyroid.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [thyroid], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                'Anterior': 1.3, 'Posterior': 1.3, 
                                                                'Right': 1.3, 'Left': 1.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    #zBody
    zBody = case.PatientModel.CreateRoi(Name="zzBodynoPTV", Color="Black", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zBody.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                'Anterior': 1.3, 'Posterior': 1.3, 
                                                                'Right': 1.3, 'Left': 1.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })

def addPlan():
    print("Creaste Plan")
    plan = case.AddNewPlan(PlanName = "AutoBreast VMAT", ExaminationName = 'CT Plan') 
    beam_set = plan.AddNewBeamSet(Name='AutoBreast VMAT', ExaminationName = 'CT Plan', 
                                MachineName = comboMac.get(), Modality = 'Photons', 
                                PatientPosition = 'HeadFirstSupine', TreatmentTechnique = 'VMAT', 
                                NumberOfFractions = NumF.get(), CreateSetupBeams=True, 
                                UseLocalizationPointAsSetupIsocenter=False, 
                                UseUserSelectedIsocenterSetupIsocenter=False)
    patient.Save()
    plan.SetCurrent()
    beam_set.SetCurrent()
    #Add prescription
    print("Add presciption")
    TotalDose = float(TotalDose_Gy.get()) * 100
    beam_set.AddRoiPrescriptionDoseReference(RoiName= comboRoiPre.get(),
                                            PrescriptionType= "DoseAtVolume",
                                            DoseValue= TotalDose,
                                            DoseVolume= 95,
                                            RelativePrescriptionLevel= 1)
    beam_set.SetDefaultDoseGrid(VoxelSize={'x': 0.2, 'y': 0.2, 'z': 0.2})
    #Isocenter placment
    print("Isocenter placment")
    Iso_StructureSet =  case.PatientModel.StructureSets['CT Plan']
    isocenter = Iso_StructureSet.PoiGeometries[comboIso.get()].Point
    iso_data = beam_set.CreateDefaultIsocenterData(Position={'x': isocenter.x, 
                    'y': isocenter.y, 
                    'z': isocenter.z})
    patient.Save()
    plan.SetCurrent()
    beam_set.SetCurrent()

    #Add Beam
    print("Add Beam")
    PhotonE = comboPhotonE.get()
    start = int(StartGantry.get())
    mid = int(MidGantry.get())
    stop = int(StopGantry.get())
    medC = int(MedColli.get())
    latC = int(LatColli.get())
    print(f"arm: {arm}")
    Add_Beam1 = beam_set.CreateArcBeam(ArcStopGantryAngle=mid, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="1", Description=f"1.CW{start}-{mid}", GantryAngle=start, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=medC)
    beam_set.Beams[0].SetFluenceProtectRoi(EntranceOnly=True,RoiName=arm)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[0].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=30, BurstGantrySpacing=None, MaxArcMU=None)
    #if comboMac.get() == 'TrueBeam_L6' or comboMac.get() == 'TrueBeam_L7' or comboMac.get() == 'TrueBeam_N5':
        #plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[0].EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt", "SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="UseLimitsAsMax", LeftJaw=-2, RightJaw=20, TopJaw=-20, BottomJaw=20)
    print("Add Beam 1 compleate")
    Add_Beam2 = beam_set.CreateArcBeam(ArcStopGantryAngle=stop, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="2", Description=f"2.CW{mid}-{stop}", GantryAngle=mid, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=latC)
    beam_set.Beams[1].SetFluenceProtectRoi(EntranceOnly=True,RoiName=arm)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[1].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=30, BurstGantrySpacing=None, MaxArcMU=None)
    #if comboMac.get() == 'TrueBeam_L6' or comboMac.get() == 'TrueBeam_L7' or comboMac.get() == 'TrueBeam_N5':
        #plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[1].EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt", "SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="UseLimitsAsMax", LeftJaw=-20, RightJaw=2, TopJaw=-20, BottomJaw=20)
    print("Add Beam 2 compleate")
    Add_Beam3 = beam_set.CreateArcBeam(ArcStopGantryAngle=mid, ArcRotationDirection="CounterClockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="3", Description=f"3.CW{stop}-{mid}", GantryAngle=stop, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)
    beam_set.Beams[2].SetFluenceProtectRoi(EntranceOnly=True,RoiName=arm)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[2].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=30, BurstGantrySpacing=None, MaxArcMU=None)
    if comboMac.get() == 'TrueBeam_L6' or comboMac.get() == 'TrueBeam_L7' or comboMac.get() == 'TrueBeam_N5':
        plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[2].EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt", "SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="UseLimitsAsMax", LeftJaw=-20, RightJaw=2, TopJaw=-20, BottomJaw=20)
    print("Add Beam 3 compleate")
    Add_Beam4 = beam_set.CreateArcBeam(ArcStopGantryAngle=start, ArcRotationDirection="CounterClockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="4", Description=f"4.CW{mid}-{start}", GantryAngle=mid, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)
    beam_set.Beams[3].SetFluenceProtectRoi(EntranceOnly=True,RoiName=arm)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[3].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=30, BurstGantrySpacing=None, MaxArcMU=None)
    if comboMac.get() == 'TrueBeam_L6' or comboMac.get() == 'TrueBeam_L7' or comboMac.get() == 'TrueBeam_N5':
        plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[3].EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt", "SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="UseLimitsAsMax", LeftJaw=-2, RightJaw=20, TopJaw=-20, BottomJaw=20)
    print("Add Beam 4 compleate")
    #Edit name description and gantry angle of setup field
    print("Edit setup beam name")
    beam_set.PatientSetup.SetupBeams['SB1_1'].Name = "I1"
    beam_set.PatientSetup.SetupBeams['I1'].Description = "kV AP"
    beam_set.PatientSetup.SetupBeams['SB1_2'].Name = "I2"
    beam_set.PatientSetup.SetupBeams['I2'].Description = "kV Lt Lat"
    beam_set.PatientSetup.SetupBeams['SB1_3'].Name = "I3"
    beam_set.PatientSetup.SetupBeams['I3'].Description = "CBCT"
    beam_set.PatientSetup.SetupBeams['I3'].GantryAngle = 0   
    return plan, beam_set

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

def AddCostFunction():
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    DosePrescription = float(TotalDose_Gy.get()) * 100
    print("Start add cost function")
    min_dvh(Po,"zzPTV", dose_level=int(DosePrescription*0.95), percent_volume=100, weigth=110)
    min_dvh(Po,"zzPTV", dose_level=int(DosePrescription+100), percent_volume=99.5, weigth=100)
    max_dvh(Po, "zzPTV", dose_level=int(DosePrescription+200), percent_volume=5,weigth=90)
    min_eud(Po, "zzPTV", dose_level=int(DosePrescription+100), eud_parameter=-5, weigth=100)
    uniform_constraint(Po, "zzCTV", stdv=1)
    min_dvh(Po, "zzCTV", dose_level=int(DosePrescription+100), percent_volume=100, weigth=110)
    min_dvh(Po, "zzSkinFlash",dose_level=int(DosePrescription), percent_volume=100, weigth=0)
    max_dvh(Po, "zzHeart", dose_level=1500, percent_volume=0, weigth=1)
    max_dvh(Po, "zzHeart", dose_level=1000, percent_volume=2, weigth=1)
    max_dvh(Po, "zzHeart", dose_level=450, percent_volume=4, weigth=1)
    max_dvh(Po, "zzLtLung", dose_level=3000, percent_volume=0, weigth=1)
    max_dvh(Po, "zzLtLung", dose_level=2000, percent_volume=5, weigth=1)
    max_dvh(Po, "zzLtLung", dose_level=1000, percent_volume=15, weigth=1)
    max_dvh(Po, "zzLtLung", dose_level=500, percent_volume=20, weigth=1)
    max_eud(Po, "zzLtLung", dose_level=2000, eud_parameter=7, weigth=1)
    max_dvh(Po, lt_lung, dose_level=2000, percent_volume=25, weigth=1)
    max_dvh(Po, lt_lung, dose_level=500, percent_volume=35, weigth=1)
    max_eud(Po, heart, dose_level=250, eud_parameter=1, weigth=1)
    max_dvh(Po, heart, dose_level=2300, percent_volume=0, weigth=1)
    max_dvh(Po, "zzGV", dose_level=500, percent_volume=10, weigth=1)
    max_dvh(Po, rt_breast, dose_level=450, percent_volume=0, weigth=10)
    max_eud(Po, rt_breast, dose_level=500, eud_parameter=5, weigth=10)
    max_dvh(Po, rt_lung, dose_level=450, percent_volume=0, weigth=10)
    max_eud(Po, rt_lung, dose_level=500, eud_parameter=5, weigth=10)
    max_dvh(Po, "zzRing", dose_level=int(DosePrescription*0.92), percent_volume=0, weigth=70)
    fall_off(Po, body, high_dose_level=int(DosePrescription+100), low_dose_level=int(DosePrescription*0.94), distance=2, weigth=1, adapt=True)
    max_dvh(Po, thyroid, dose_level=int(DosePrescription*1.05), percent_volume=0,weigth=1)
    max_eud(Po, thyroid, dose_level=2500, eud_parameter=1, weigth=1)
    max_dvh(Po, "zzThyroid", dose_level=3000, percent_volume=0, weigth=1)
    max_dvh(Po, eso, dose_level=int(DosePrescription*1.05), percent_volume=0,weigth=1)
    max_dvh(Po, "zzLiver_Stomach", dose_level=500, percent_volume=0.3, weigth=1)
    max_dvh(Po, arm, dose_level=500,percent_volume=5,weigth=1)
    print("Add cost function finish")

def GetAbsoluteVolumeAtDose(plan,roi,dose):
	Vd = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= roi, DoseValues=[dose])
	roi = case.PatientModel.StructureSets[0].RoiGeometries[roi]
	Vdcc = Vd*roi.GetRoiVolume()
	return Vdcc

#Next Button
def Button_Next():
	
    try:
        current = float(NumF.get())
        try:
            current = float(TotalDose_Gy.get())
            start_time = time.time()
            if examination.Name == 'CT Plan':
                print('CT name is CT Plan already')
            else:
                examination.Name = 'CT Plan'
            get_CT_Curve()
            print("Creating virtual contour")
            create_virtual()
            print("Finish creating virtual contour")
            plan, beam_set = addPlan()
            AddCostFunction()
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            plan = get_current("Plan")
            Po = plan.PlanOptimizations[0]
            print("Start Optimization")
            for i in range(0,2):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            DosePrescription = float(TotalDose_Gy.get()) * 100
            ############################################################
            #Loop optimize algorithum
            ############################################################
            for i in range(1,6):
                print(f"Star Optimization loop {i}")
                ## 1.Reduce 100% outside target
                if i <= 1:
                    MaxBodyNoPTV = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName = "zzBodynoPTV", DoseType = "Max")
                    print("Check 100 outside PTV")
                    if float(MaxBodyNoPTV) > float(DosePrescription*0.99):
                        print("Add objective for reduce 100 out PTV")
                        max_eud(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), eud_parameter=10,weigth=60*i)
                        max_dose(Po, "zzBodynoPTV", dose_level=int(DosePrescription*0.99), weigth=60*i)

                        create_contour_from_dose(plan.TreatmentCourse.TotalDose, 95, f"zzDose_95%_{i}")
                        zOutside = case.PatientModel.CreateRoi(Name=f"zzDose_95%_outside_{i}", Color="Yellow", Type="Control",
                                                                    TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
                        zOutside.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                                        ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"zzDose_95%_{i}"], 
                                                                    'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                                        'Anterior': 0, 'Posterior': 0, 
                                                                                        'Right': 0, 'Left': 0 } }, 
                                                        ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                                                    'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                                                        'Anterior': 1, 'Posterior': 1, 
                                                                                        'Right': 1, 'Left': 1 } }, 
                                                        ResultOperation="Subtraction", 
                                                        ResultMarginSettings={ 'Type': "Expand", 'Superior': 0.1,'Inferior': 0.1, 
                                                                                'Anterior': 0.1, 'Posterior': 0.1, 
                                                                                'Right': 0.1, 'Left': 0.1 })
                        max_dvh(Po, f"zzDose_95%_outside_{i}", dose_level=int(DosePrescription*0.95), percent_volume=0, weigth=80*i)
                        print(f"Optimizing reduce 100% outside target {i}")
                        Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
                    else:
                        print("No 100 percent prescirption outside target")
                ## 2.Reduce 110%
                if i > 1 and i <= 3:
                    Body_V110cc = GetAbsoluteVolumeAtDose(plan,roi=body,dose=DosePrescription*1.1)
                    opt = False
                    print("Check 110% condition")
                    if float(Body_V110cc) > float(2.0):
                        print("Add objective for Reduce 110% in body")
                        create_contour_from_dose(plan.TreatmentCourse.TotalDose, 110, f"zzDose_110%_{i-2}")
                        case.PatientModel.RegionsOfInterest[f"zzDose_110%_{i-2}"].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                                                                                        ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"zzDose_110%_{i-2}"], 
                                                                                                                    'MarginSettings': { 'Type': "Expand", 'Superior': 0.1, 'Inferior': 0.1, 
                                                                                                                                        'Anterior': 0.1, 'Posterior': 0.1, 
                                                                                                                                        'Right': 0.1, 'Left': 0 } }, 
                                                                                                        ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                                                                                                    'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                                                                                        'Anterior': 0, 'Posterior': 0, 
                                                                                                                                        'Right': 0, 'Left': 0 } }, 
                                                                                                        ResultOperation="None", 
                                                                                                        ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                                                                                                'Anterior': 0, 'Posterior': 0, 
                                                                                                                                'Right': 0, 'Left': 0 })
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
                    MinDvhCtv = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="zzCTV", RelativeVolumes=[0.95])
                    CTV_V50Gy = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="zzCTV", DoseValues=[int(DosePrescription)])
                    opt = False
                    print("Check cold condition")
                    if float(MinDvhPtv) < float(DosePrescription*0.98):
                        print("Add objective for increase cold")
                        create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, f"zz100%p_{i-4}")
                        zicCover = case.PatientModel.CreateRoi(Name=f"zz+100%p_{i-4}", Color="Yellow", Type="Control",
                                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
                        zicCover.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV"], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.2, 'Inferior': 0.2, 
                                                                'Anterior': 0.2, 'Posterior': 0.2, 
                                                                'Right': 0.2, 'Left': 0.2 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%p_{i-4}"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0.1,'Inferior': 0.1, 
                                                        'Anterior': 0.1, 'Posterior': 0.1, 
                                                        'Right': 0.1, 'Left': 0.1 })
                        zicCover.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%p_{i-4}"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.4, 'Inferior': 0.4, 
                                                                'Anterior': 0.4, 'Posterior': 0.4, 
                                                                'Right': 0.4, 'Left': 0.4 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
                        min_dvh(Po, f"zz+100%p_{i-4}", dose_level=int(DosePrescription+100), percent_volume=100, weigth=110)
                        opt = True
                    if float(MinDvhCtv) < float(DosePrescription):
                        print("Add objective for increase cold")
                        create_contour_from_dose(plan.TreatmentCourse.TotalDose, 100, f"zz100%c_{i-4}")
                        zicCoverC = case.PatientModel.CreateRoi(Name=f"zz+100%c_{i-4}", Color="Yellow", Type="Control",
                                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
                        zicCoverC.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzCTV"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%c_{i-4}"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.1, 'Inferior': 0.1, 
                                                                'Anterior': 0.1, 'Posterior': 0.1, 
                                                                'Right': 0.1, 'Left': 0.1 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0})
                        zicCoverC.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [f"zz100%c_{i-4}"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.4, 'Inferior': 0.4, 
                                                                'Anterior': 0.4, 'Posterior': 0.4, 
                                                                'Right': 0.4, 'Left': 0.4 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
                        min_dvh(Po, f"zz+100%c_{i-4}", dose_level=int(DosePrescription+100), percent_volume=100, weigth=200)
                        opt = True
                    if float(CTV_V50Gy) < 0.6:
                        print("Delete Uniformity Constrain")
                        try:
                            plan.PlanOptimizations[0].Constraints[-1].DeleteFunction()
                            opt = True
                        except:
                            print("Uniformity Constrain already delete")
                    if opt:
                        Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
                    else:
                        print("not opt yet")
            ############################################################
            end_time = time.time()
            elaps = end_time - start_time
            hours = elaps // 3600
            minutes = (elaps % 3600)//60
            seconds = elaps % 60
            print(f"Running time = {int(hours)}:{int(minutes)}:{int(seconds)}")
            root.destroy()
        except:
            show_error()
    except:
        show_error()
    

buttNext = Button(root, text = 'Next', command = Button_Next)
buttNext.grid(column=1,row=13,padx=10,pady=25)
buttNext.config(width=15)
root.mainloop()