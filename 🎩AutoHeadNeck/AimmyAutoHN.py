from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time
case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")
root = Tk()
root.title('Plan design')
root.geometry('400x450')
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
#textbox for insert collimator angle Arc 1 (DualArc)
lbMedColli = Label(root, text= 'collimator angleArc 1 (DualArc)')
lbMedColli.grid(column=0 ,row=10)
lbMedColli.config(width=27, height =2)
MedColli = StringVar()
textMedColli = Entry(root, textvariable = MedColli)
textMedColli.grid(column=1,row=10)
textMedColli.config(width=27)
#textbox for insert Lat collimator angle
lbLatColli = Label(root, text= 'collimator angle Arc 2')
lbLatColli.grid(column=0 ,row=11)
lbLatColli.config(width=27, height =2)
LatColli = StringVar()
textLatColli = Entry(root, textvariable = LatColli)
textLatColli.grid(column=1,row=11)
textLatColli.config(width=27)
#For match ROI to optimization
ptv54 = "PTV 54"
ptv57 = "PTV 57"
ptv60 = "PTV 60"
ptv66 = "PTV 66"
ptv70 = "PTV 70"
lips = "Lips"
brain = "Brain"
cord = "Spinal Cord"
bstem = "Brainstem"
thyroid = "Thyroid Gland"
trachea = "Trachea"
larynx = "Larynx"
lens_lt = "Lens Lt"
lens_rt = "Lens Rt"
lacrimal_lt = "Lacrimal Gland Lt"
lacrimal_rt = "Lacrimal Gland Rt"
parotid_lt = "Parotid Lt"
parotid_rt = "Parotid Rt"
opticn_lt = "Optic Nerve Lt"
opticn_rt = "Optic Nerve Rt"
eye_lt = "Eye Lt"
eye_rt = "Eye Rt"
optic_chiasm ="Optic Chiasm"
eso = "Esophagus"
body = "BODY"
constrict_mus = "Constrict Muscle"
cricoid = "Cricoid"
cochlea_lt= "Cochlea Lt"
cochlea_rt  = "Cochlea Rt"
IAC_lt = "IAC Lt"
IAC_rt = "IAC Rt"
inner_ear_lt = "Inner ear Lt"
inner_ear_rt = "Inner ear Rt"
oral = "Oral Cavity"
def Button_MatchRoi():
    Sub_root1 = Toplevel()
    Sub_root1.title('Match Roi')
    Sub_root1.geometry('620x670')
    ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]

    def lbMatch(root_frame=Sub_root1,  List = ListRoi, roi = 'ROI', row_n = 0,column_n = 0):
        lbMatchROI = Label(root_frame, text= roi)
        lbMatchROI.grid(column=column_n , row=row_n)
        lbMatchROI.config(width=15, height =2)
        if roi in ListRoi:
            lbMatchROI = Label(root_frame, text= 'Matched')
            lbMatchROI.grid(column=column_n+1, row=row_n)
            lbMatchROI.config(width=27, height =2)
            return roi
        else:
            combo_ROI = StringVar()
            comboROI = ttk.Combobox(root_frame, values = ListRoi, textvariable= combo_ROI)
            comboROI.grid(column=column_n+1,row=row_n)
            comboROI.config(width=27, height =20)
            return comboROI

    combo_ptv54 = lbMatch(Sub_root1, ListRoi, roi = ptv54, row_n = 0,column_n = 0)
    combo_ptv57 = lbMatch(Sub_root1, ListRoi, roi = ptv57, row_n = 1,column_n = 0)
    combo_ptv60 = lbMatch(Sub_root1, ListRoi, roi = ptv60, row_n = 2,column_n = 0)
    combo_ptv66 = lbMatch(Sub_root1, ListRoi, roi = ptv66, row_n = 3,column_n = 0)
    combo_ptv70 = lbMatch(Sub_root1, ListRoi, roi = ptv70, row_n = 4,column_n = 0)
    combo_body = lbMatch(Sub_root1, ListRoi, roi = body, row_n = 5,column_n = 0)
    combo_thyroid = lbMatch(Sub_root1, ListRoi, roi = thyroid, row_n = 6,column_n = 0)
    combo_eso = lbMatch(Sub_root1, ListRoi, roi = eso, row_n = 7,column_n = 0)
    combo_lips = lbMatch(Sub_root1, ListRoi, roi = lips, row_n = 8,column_n = 0)
    combo_brain = lbMatch(Sub_root1, ListRoi, roi = brain, row_n = 9,column_n = 0)
    combo_bstem = lbMatch(Sub_root1, ListRoi, roi = bstem, row_n = 10,column_n = 0)
    combo_cord = lbMatch(Sub_root1, ListRoi, roi = cord, row_n = 11,column_n = 0)
    combo_trachea = lbMatch(Sub_root1, ListRoi, roi = trachea, row_n = 12,column_n = 0)
    combo_larynx = lbMatch(Sub_root1, ListRoi, roi = larynx, row_n = 13,column_n = 0)
    combo_lens_lt = lbMatch(Sub_root1, ListRoi, roi = lens_lt, row_n = 14,column_n = 0)
    combo_lens_rt = lbMatch(Sub_root1, ListRoi, roi = lens_rt, row_n = 15,column_n = 0)
    combo_lacrimal_lt = lbMatch(Sub_root1, ListRoi, roi = lacrimal_lt, row_n = 16,column_n = 0)
    combo_lacrimal_rt = lbMatch(Sub_root1, ListRoi, roi = lacrimal_rt, row_n = 0,column_n = 2)
    combo_parotid_lt = lbMatch(Sub_root1, ListRoi, roi = parotid_lt, row_n = 1,column_n = 2)
    combo_parotid_rt = lbMatch(Sub_root1, ListRoi, roi = parotid_rt, row_n = 2,column_n = 2)
    combo_opticn_lt = lbMatch(Sub_root1, ListRoi, roi = opticn_lt, row_n = 3,column_n = 2)
    combo_opticn_rt = lbMatch(Sub_root1, ListRoi, roi = opticn_rt, row_n = 4,column_n = 2)
    combo_optic_chiasm = lbMatch(Sub_root1, ListRoi, roi = optic_chiasm, row_n = 5,column_n = 2)
    combo_eye_lt = lbMatch(Sub_root1, ListRoi, roi = eye_lt, row_n = 6,column_n = 2)
    combo_eye_rt = lbMatch(Sub_root1, ListRoi, roi = eye_rt, row_n = 7,column_n = 2)
    combo_constrict_mus = lbMatch(Sub_root1, ListRoi, roi = constrict_mus, row_n = 8,column_n = 2)
    combo_cricoid = lbMatch(Sub_root1, ListRoi, roi = cricoid, row_n = 9,column_n = 2)
    combo_cochlea_lt = lbMatch(Sub_root1, ListRoi, roi = cochlea_lt, row_n = 10,column_n = 2)
    combo_cochlea_rt = lbMatch(Sub_root1, ListRoi, roi = cochlea_rt, row_n = 11,column_n = 2)
    combo_IAC_lt = lbMatch(Sub_root1, ListRoi, roi = IAC_lt, row_n = 12,column_n = 2)
    combo_IAC_rt = lbMatch(Sub_root1, ListRoi, roi = IAC_rt, row_n = 13,column_n = 2)
    combo_inner_ear_lt = lbMatch(Sub_root1, ListRoi, roi = inner_ear_lt, row_n = 14,column_n = 2)
    combo_inner_ear_rt = lbMatch(Sub_root1, ListRoi, roi = inner_ear_rt, row_n = 15,column_n = 2)
    combo_oral = lbMatch(Sub_root1, ListRoi, roi = oral, row_n = 16,column_n = 2)
    #Cancel Button in Sub_root1
    def Button_Cancel_sub1():
        Sub_root1.destroy()
    buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
    buttCancelSub1.grid(column=0,row=17,pady=15)
    buttCancelSub1.config(width=10)
    #Apply Button in Sub_root1
    def Button_Apply_sub1():
        global ptv54
        global ptv57
        global ptv60
        global ptv66
        global ptv70
        global lips
        global brain
        global cord
        global bstem
        global thyroid
        global trachea
        global larynx
        global lens_lt
        global lens_rt
        global parotid_lt
        global parotid_rt
        global opticn_lt
        global opticn_rt
        global eye_lt
        global eye_rt
        global optic_chiasm
        global eso 
        global body
        global constrict_mus 
        global cricoid
        global cochlea_lt
        global cochlea_rt 
        global oral
        
        def apply(roi, combo_roi):
            try:
                roi = combo_roi.get()
                return roi
            except:
                roi = combo_roi
                return roi

        ptv54 = apply(ptv54, combo_ptv54)
        ptv57 = apply(ptv57, combo_ptv57) 
        ptv60 = apply(ptv60, combo_ptv60)
        ptv66 = apply(ptv66, combo_ptv66)
        ptv70 = apply(ptv70, combo_ptv70)
        lips = apply(lips, combo_lips)
        brain = apply(brain, combo_brain)
        cord = apply(cord, combo_cord)
        bstem = apply(bstem, combo_bstem)
        thyroid = apply(thyroid, combo_thyroid)
        trachea = apply(trachea, combo_trachea)
        larynx = apply(larynx, combo_larynx)  
        print(larynx)  
        lens_lt = apply(lens_lt, combo_lens_lt)
        lens_rt = apply(lens_rt, combo_lens_rt)
        parotid_lt = apply(parotid_lt, combo_parotid_lt)
        parotid_rt = apply(parotid_rt, combo_parotid_rt)
        opticn_lt = apply(opticn_lt, combo_opticn_lt)
        opticn_rt = apply(opticn_rt, combo_opticn_rt)
        eye_lt = apply(eye_lt, combo_eye_lt)
        eye_rt = apply(eye_rt, combo_eye_rt)
        optic_chiasm = apply(optic_chiasm, combo_optic_chiasm)
        eso  = apply(eso , combo_eso)
        body = apply(body, combo_body)
        constrict_mus  = apply(constrict_mus, combo_constrict_mus) 
        cricoid = apply(cricoid, combo_cricoid)
        cochlea_lt = apply(cochlea_lt, combo_cochlea_lt)
        cochlea_rt  = apply(cochlea_rt , combo_cochlea_rt)
        oral = apply(oral, combo_oral)
        Sub_root1.destroy()
    
    buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
    buttApplySub1.grid(column=1,row=17,pady=15)
    buttApplySub1.config(width=10)
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=12)
lbMatchRoi.config(width=27, height =2)
#For check is ROI are match
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = [ptv54,ptv57,ptv60,ptv66,ptv70,lips,brain,cord,bstem,thyroid,trachea,larynx,lens_lt,lens_rt,lacrimal_lt ,lacrimal_rt ,parotid_lt,parotid_rt,opticn_lt,opticn_rt,eye_lt,eye_rt,optic_chiasm,eso ,body,constrict_mus ,cricoid,cochlea_lt,cochlea_rt ,IAC_lt,IAC_rt ,inner_ear_lt,inner_ear_rt,oral
]
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
	print(f"Create {name}")
def create_virtual():
    # zOptic
    zOptic = case.PatientModel.CreateRoi(Name="zzOptic", Color="Blue", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zOptic.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [eye_lt,eye_rt,lens_lt,lens_rt], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="None", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zBrainstem
    zBrainstem = case.PatientModel.CreateRoi(Name="zzBrainstem", Color="Red", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zBrainstem.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [bstem,opticn_lt,opticn_rt,optic_chiasm], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="None", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zPTV54
    zPTV54 = case.PatientModel.CreateRoi(Name="zzPTV54", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv54], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv60,ptv66], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                            'Anterior': 0.5, 'Posterior': 0.5, 
                                                            'Right': 0.5, 'Left': 0.5 } }, 
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    zPTV54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV54"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv70], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.7, 'Inferior': 0.7, 
                                                            'Anterior': 0.7, 'Posterior': 0.7, 
                                                            'Right': 0.7, 'Left': 0.7 } }, 
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    zPTV54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV54"], 
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
    zPTV54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV54"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzBrainstem"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 
                                                            'Anterior': 0.2, 'Posterior': 0.2, 
                                                            'Right': 0.2, 'Left': 0.2 } },
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })                                                    
     # zPTV60
    print("1")
    zPTV60 = case.PatientModel.CreateRoi(Name="zzPTV60", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    print("2")
    zPTV60.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv60], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv66,ptv70,"zzBrainstem"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                            'Anterior': 0.5, 'Posterior': 0.5, 
                                                            'Right': 0.5, 'Left': 0.5 } }, 
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })                   
    print("3")
    zPTV60.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV60"], 
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
 # zPTV66
    zPTV66 = case.PatientModel.CreateRoi(Name="zzPTV66", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV66.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv66], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv70], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                            'Anterior': 0.3, 'Posterior': 0.3, 
                                                            'Right': 0.3, 'Left': 0.3 } }, 
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    zPTV66.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV66"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzBrainstem"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                            'Anterior': 0.5, 'Posterior': 0.5, 
                                                            'Right': 0.5, 'Left': 0.5 } },
                            ResultOperation="subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    zPTV66.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto",
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV66"], 
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
# zPTV70
    zPTV70 = case.PatientModel.CreateRoi(Name="zzPTV70", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV70.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv70],
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
    zPTV70.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV70"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzBrainstem"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                            'Anterior': 0.5, 'Posterior': 0.5, 
                                                            'Right': 0.5, 'Left': 0.5 } })
    # zParotid_Lt
    zParotid_Lt = case.PatientModel.CreateRoi(Name="zzParotid_Lt", Color="Red", Type="Control",
                                         TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zParotid_Lt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [parotid_lt], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv66,ptv60,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                'Anterior': 0.5, 'Posterior': 0.5, 
                                                                'Right': 0.5, 'Left': 0.5 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
   # zParotid_Rt
    zParotid_Rt = case.PatientModel.CreateRoi(Name="zzParotid_Rt", Color="Red", Type="Control",
                                         TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zParotid_Rt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [parotid_rt], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                'Anterior': 0.5, 'Posterior': 0.5, 
                                                                'Right': 0.5, 'Left': 0.5 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zLips
    zLips = case.PatientModel.CreateRoi(Name="zzLips", Color="Red", Type="Control",
                                         TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zLips.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [lips], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                'Anterior': 0.3, 'Posterior': 0.3, 
                                                                'Right': 0.3, 'Left': 0.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zEars
    zEars = case.PatientModel.CreateRoi(Name="zzEars", Color="Green", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zEars.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [cochlea_lt,cochlea_rt], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 1, 'Posterior': 2, 
                                                                    'Right': 2, 'Left': 1 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                    'Anterior': 0.5, 'Posterior': 0.5, 
                                                                    'Right': 0.5, 'Left': 0.5 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
    # zCord
    zCord = case.PatientModel.CreateRoi(Name="zzCord", Color="Aqua", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zCord.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [cord], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                    'Anterior': 0.3, 'Posterior': 0.3, 
                                                                    'Right': 0.3, 'Left': 0.3 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ResultOperation="None", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
    # zOral
    zOral = case.PatientModel.CreateRoi(Name="zzOral", Color="Aqua", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zOral.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [oral], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                    'Anterior': 2, 'Posterior': 2, 
                                                                    'Right': 2, 'Left': 2 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })                                           
    # zOral2
    zOral2 = case.PatientModel.CreateRoi(Name="zzOral2", Color="Aqua", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zOral2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [oral], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 3, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 3, 'Inferior': 3, 
                                                                    'Anterior': 3, 'Posterior': 3, 
                                                                    'Right': 3, 'Left': 3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })   
    # zbrain
    zbrain = case.PatientModel.CreateRoi(Name="zzBrain", Color="Aqua", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zbrain.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [brain], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                    'Anterior': 2, 'Posterior': 2, 
                                                                    'Right': 2, 'Left': 2 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })   
    #virtual structure
    # zPost
    zPost = case.PatientModel.CreateRoi(Name="zzPost", Color="Purple", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [cord], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 10, 'Posterior': 10, 
                                                                'Right': 3, 'Left': 3 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                'Anterior': 2, 'Posterior': 2, 
                                                                'Right': 2, 'Left': 2 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zPost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPost"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } },
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                                    
    zPost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPost"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } },
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 15, 'Posterior': 15, 
                                                                'Right': 15, 'Left': 15 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    print(larynx)                                                    
    zPost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPost"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } },
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [constrict_mus,cricoid,larynx], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 15, 'Inferior': 15, 
                                                                'Anterior': 15, 'Posterior': 0, 
                                                                'Right': 15, 'Left': 15 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                                           
    #zMid
    zMid = case.PatientModel.CreateRoi(Name="zzMid", Color="Black", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zMid.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [cord], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 15, 'Posterior': 15, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zMid.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzMid"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv66,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                'Anterior': 0.5, 'Posterior': 0.5, 
                                                                'Right': 0.5, 'Left': 0.5 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zMid.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzMid"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                 ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 15, 'Posterior': 15, 
                                                                'Right': 15, 'Left': 15 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    #zMid2
    zMid2 = case.PatientModel.CreateRoi(Name="zzMid2", Color="Black", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zMid2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzMid"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.8, 'Inferior': 0.8, 
                                                                'Anterior': 0.8, 'Posterior': 0.8, 
                                                                'Right': 0.8, 'Left': 0.8 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                                                                                             
    #zMid3
    zMid3 = case.PatientModel.CreateRoi(Name="zzMid3", Color="Black", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zMid3.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzMid"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54,ptv60,ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.2, 'Inferior': 1.2, 
                                                                'Anterior': 1.2, 'Posterior': 1.2, 
                                                                'Right': 1.2, 'Left': 1.2 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 }) 
    zMid3.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzMid3"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzOral"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0} }, 
                                ResultOperation="Union", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 }) 
    # zeyes
    zEyes = case.PatientModel.CreateRoi(Name="zzEyes", Color="Red", Type="Control",
                                         TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zEyes.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [eye_lt,eye_rt], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 10, 'Left': 10 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zEyes.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzEyes"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv60], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                'Anterior': 0.5, 'Posterior': 0.5, 
                                                                'Right': 0.5, 'Left': 0.5 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })    
    zEyes.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzEyes"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv70], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                                'Anterior': 1, 'Posterior': 1, 
                                                                'Right': 1, 'Left': 1 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })    
def addPlan():
    print("Creaste Plan")
    plan = case.AddNewPlan(PlanName = "AutoHN VMAT", ExaminationName = 'CT Plan') 
    beam_set = plan.AddNewBeamSet(Name='AutoHN VMAT', ExaminationName = 'CT Plan', 
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
    #start = int(StartGantry.get())
    #stop = int(StopGantry.get())
    #medC = int(MedColli.get())
    #latC = int(LatColli.get())
    Add_Beam1 = beam_set.CreateArcBeam(ArcStopGantryAngle=179, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="1", Description=f"1.CW{181}-{179}", GantryAngle=181, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=355)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[0].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=True, FinalGantrySpacing=2, MaxArcDeliveryTime=80, BurstGantrySpacing=None, MaxArcMU=None)

    print("Add Beam 1 compleate")
    Add_Beam2 = beam_set.CreateArcBeam(ArcStopGantryAngle=179, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="2", Description=f"2.CCW{181}-{179}", GantryAngle=181, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=5)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[1].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=80, BurstGantrySpacing=None, MaxArcMU=None)
    print("Add Beam 2 compleate")
    #Add_Beam3 = beam_set.CreateArcBeam(ArcStopGantryAngle=stop, ArcRotationDirection="Clockwise", 
                            #BeamQualityId=PhotonE, IsocenterData= iso_data,
                            #Name="3", Description=f"3.CW{start}-{stop}", GantryAngle=stop, CouchRotationAngle=0, 
                            #CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)
    #beam_set.Beams[2].SetFluenceProtectRoi(EntranceOnly=True,RoiName=arm)
    #plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[2].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=30, BurstGantrySpacing=None, MaxArcMU=None)
    print("Add Beam 3 compleate")
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
    return o
def max_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth
    return o
def max_eud(po, roi_name, dose_level, eud_parameter, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.EudParameterA =  eud_parameter
    o.DoseFunctionParameters.Weight = weigth
    return o
def min_dvh(po, roi_name, dose_level, percent_volume, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinDvh", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.PercentVolume = percent_volume
    o.DoseFunctionParameters.Weight = weigth
    return o
def min_dose(po, roi_name, dose_level, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinDose", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.Weight = weigth
    return o
def min_eud(po, roi_name, dose_level, eud_parameter, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MinEud", RoiName = roi_name)
    o.DoseFunctionParameters.DoseLevel = dose_level
    o.DoseFunctionParameters.EudParameterA = eud_parameter
    o.DoseFunctionParameters.Weight = weigth
    return o
def fall_off(po, roi_name, high_dose_level, low_dose_level, distance, weigth, adapt=False, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName = roi_name)
    o.DoseFunctionParameters.AdaptToTargetDoseLevels = adapt
    o.DoseFunctionParameters.HighDoseLevel = high_dose_level
    o.DoseFunctionParameters.LowDoseLevel = low_dose_level
    o.DoseFunctionParameters.LowDoseDistance = distance
    o.DoseFunctionParameters.Weight = weigth
    return o
def uniform_constraint(po, roi_name, stdv, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="UniformityConstraint", RoiName = roi_name, IsConstraint=True)
    o.DoseFunctionParameters.PercentStdDeviation = stdv
    return o
def AddCostFunction():
    plan = get_current("Plan")
    Po = plan.PlanOptimizations[0]
    DosePrescription = float(TotalDose_Gy.get()) * 100
    print("Star add cost function")
    global o_min_dose_zzPTV54
    global o_max_dose_zzPTV54
    global o_min_dose_zzPTV60
    global o_max_dose_zzPTV60
    global o_min_dose_zzPTV66
    global o_max_dose_zzPTV66
    global o_min_dose_zzPTV70
    global o_max_dose_zzPTV70
    global o_max_dose_zzBrainstem
    global o_fall_off_body
    global o_fall_off_zzOral
    global o_fall_off_zzPost
    global o_fall_off_zzParotid_Lt
    global o_fall_off_zzParotid_Rt
    global o_fall_off_zzEars
    global o_fall_off_zzBrain
    global o_fall_off_zzBrainstem
    global o_fall_off_zzEyes
    global o_max_eud_zzOptic
    global o_max_eud_zzParotid_Lt
    global o_max_eud_zzParot_Rt
    global o_max_eud_zzEars
    global o_max_eud_zzPost
    global o_max_dvh_zzLips
    global o_max_dvh_zzMid
    global o_max_dvh_zzCord
    global o_max_dvh_lens_lt
    global o_max_dvh_lens_rt

    o_min_dose_zzPTV54 = min_dose(Po,"zzPTV54", dose_level=5500, weigth=100)
    o_max_dose_zzPTV54 = max_dose(Po, "zzPTV54", dose_level=5600, weigth=80)
    o_min_dose_zzPTV60 = min_dose(Po,"zzPTV60", dose_level=6100, weigth=100)
    o_max_dose_zzPTV60 = max_dose(Po, "zzPTV60", dose_level=6200, weigth=80)
    o_min_dose_zzPTV66 = min_dose(Po,"zzPTV66", dose_level=6700, weigth=100)
    o_max_dose_zzPTV66 = max_dose(Po, "zzPTV66", dose_level=6800, weigth=80)
    o_min_dose_zzPTV70= min_dose(Po,"zzPTV70", dose_level=7100, weigth=100)
    o_max_dose_zzPTV70 = max_dose(Po, "zzPTV70", dose_level=7200, weigth=80)
    o_max_dose_zzBrainstem = max_dose(Po, "zzBrainstem", dose_level=5300, weigth=10)
    o_fall_off_body = fall_off(Po, body, high_dose_level=7000, low_dose_level=2700, distance=4, weigth=5, adapt=True)
    o_fall_off_zzOral = fall_off(Po, "zzOral", high_dose_level=7000, low_dose_level=2700, distance=3, weigth=5, adapt=True)
    o_fall_off_zzPost = fall_off(Po, "zzPost", high_dose_level=7000, low_dose_level=2700, distance=3, weigth=5, adapt=True)
    o_fall_off_zzParotid_Lt = fall_off(Po, "zzParotid_Lt", high_dose_level=7000, low_dose_level=2700, distance=3, weigth=5, adapt=True)
    o_fall_off_zzParotid_Rt = fall_off(Po, "zzParotid_Rt", high_dose_level=7000, low_dose_level=2700, distance=3, weigth=5, adapt=True)
    o_fall_off_zzEars = fall_off(Po, "zzEars", high_dose_level=6000, low_dose_level=3000, distance=2, weigth=5, adapt=False)
    o_fall_off_zzBrain = fall_off(Po, "zzBrain", high_dose_level=7000, low_dose_level=2700, distance=3, weigth=5, adapt=True)
    o_fall_off_zzBrainstem = fall_off(Po, "zzBrainstem", high_dose_level=6000, low_dose_level=2000, distance=2, weigth=5, adapt=False)
    o_fall_off_zzEyes = fall_off(Po, "zzEyes", high_dose_level=6000, low_dose_level=2000, distance=2, weigth=5, adapt=False)
    o_max_eud_zzOptic = max_eud(Po, "zzOptic", dose_level=1500, eud_parameter=10, weigth=5)
    o_max_eud_zzParotid_Lt = max_eud(Po, "zzParotid_Lt", dose_level=3500, eud_parameter=10, weigth=5)
    o_max_eud_zzParot_Rt = max_eud(Po, "zzParotid_Rt", dose_level=3500, eud_parameter=10, weigth=5)
    o_max_eud_zzEars = max_eud(Po, "zzEars", dose_level=4300, eud_parameter=10, weigth=5)
    o_max_eud_zzPost = max_eud(Po, "zzPost", dose_level=2000, eud_parameter=10, weigth=5)
    o_max_dvh_zzLips = max_dvh(Po, "zzLips", dose_level=2000, percent_volume=0, weigth=5)
    o_max_dvh_zzMid = max_dvh(Po, "zzMid", dose_level=4500, percent_volume=0, weigth=5)
    o_max_dvh_zzCord = max_dvh(Po, "zzCord", dose_level=4000, percent_volume=0, weigth=5)
    o_max_dvh_lens_lt = max_dvh(Po, lens_lt, dose_level=500, percent_volume=0, weigth=5)
    o_max_dvh_lens_rt = max_dvh(Po, lens_rt, dose_level=500, percent_volume=0, weigth=5)
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
            for i in range(0,3):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            o_max_eud_zzOral = max_eud(Po, "zzOral", dose_level=2200, eud_parameter=5, weigth=5)
            o_max_eud_zzPost = max_eud(Po, "zzPost", dose_level=2500, eud_parameter=5, weigth=5)
            max_eud(Po, "zzMid2",dose_level=35*100, eud_parameter=10, weigth=5)
            for i in range(0,1):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            max_eud(Po,"zzParotid_Rt",dose_level=22*100, eud_parameter=10, weigth=5)
            max_eud(Po,"zzParotid_Lt",dose_level=22*100, eud_parameter=10, weigth=5)
            max_dvh(Po,"zzBrain", dose_level=28*100, percent_volume=0, weigth=5)
            max_dvh(Po,"zzMid2", dose_level=30*100, percent_volume=0, weigth=5)
            max_eud(Po, "zzMid2",dose_level=25*100, eud_parameter=10, weigth=5)
            for i in range(0,2):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            max_dvh(Po,"zzMid", dose_level=40*100, percent_volume=0, weigth=5)
            max_dvh(Po,"zzMid3", dose_level=27*100, percent_volume=0, weigth=5)
            max_eud(Po,"zzOral2",dose_level=20*100, eud_parameter=10, weigth=5)
            for i in range(0,2):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()          
            ############################################################
            #Loop optimize algorithum
            ############################################################
            zDose54 = case.PatientModel.CreateRoi(Name="zz54-", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            beamset = get_current('BeamSet')
            threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (77.1/100)
            zDose54.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
            zDose60 = case.PatientModel.CreateRoi(Name="zz60-", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            beamset = get_current('BeamSet')
            threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (85.7/100)
            zDose60.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
            zDose70 = case.PatientModel.CreateRoi(Name="zz70-", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            beamset = get_current('BeamSet')
            threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (100/100)
            zDose70.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
            zDose54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zz54-"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv54], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                    'Anterior': 0.3, 'Posterior': 0.3, 
                                                                    'Right': 0.3, 'Left': 0.3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
            zDose54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zz54-"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv60,ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.8, 'Inferior': 0.8, 
                                                                    'Anterior': 0.8, 'Posterior': 0.8, 
                                                                    'Right': 0.8, 'Left': 0.8 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
            zDose60.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zz60-"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv60], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                    'Anterior': 0.3, 'Posterior': 0.3, 
                                                                    'Right': 0.3, 'Left': 0.3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
            zDose60.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zz60-"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                                    'Anterior': 0.5, 'Posterior': 0.5, 
                                                                    'Right': 0.5, 'Left': 0.5 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })                                       
            zDose70.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zz70-"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv70], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                    'Anterior': 0.3, 'Posterior': 0.3, 
                                                                    'Right': 0.3, 'Left': 0.3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })   
            max_dvh(Po,"zz54-", dose_level=51*100, percent_volume=0, weigth=10)
            max_dvh(Po,"zz60-", dose_level=57*100, percent_volume=0, weigth=10)
            max_dvh(Po,"zz70-", dose_level=66*100, percent_volume=0, weigth=10)
            for i in range(0,2):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
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