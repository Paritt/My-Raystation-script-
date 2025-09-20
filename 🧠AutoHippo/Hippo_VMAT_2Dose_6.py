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
textNumF.insert(0, "10")

#textbox for insert Dose prescription
lbTotalDose = Label(root, text= 'Fill Primary Dose (Gy)')
lbTotalDose.grid(column=0 ,row=3)
lbTotalDose.config(width=27, height =2)
TotalDose_Gy = StringVar()
textTotalDose = Entry(root, textvariable = TotalDose_Gy)
textTotalDose.grid(column=1,row=3)
textTotalDose.config(width=27)
textTotalDose.insert(0, "30")

#Test open patient
try:
    patient = get_current('Patient')
except:
    messagebox.showinfo('No patient selected. \nScript terminated')
    exit()
 
#Combobox for select Roi for dose prescription
lbRoiPre = Label(root, text = 'Prescription Primary Dose to')
lbRoiPre.grid(column=0,row=4)
lbRoiPre.config(width=27, height =2)
combo_variableRoiPre = StringVar()
combo_valuesRoiPre = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
comboRoiPre = ttk.Combobox(root, values= combo_valuesRoiPre, textvariable=combo_variableRoiPre)
comboRoiPre.grid(column=1,row=4)
comboRoiPre.config(width=27, height =20)

#textbox for insert Dose prescription
lbTotalDose = Label(root, text= 'Fill Dose Boost (Gy)')
lbTotalDose.grid(column=0 ,row=5)
lbTotalDose.config(width=27, height =2)
TotalDose_Gy_boost = StringVar()
textTotalDose_b = Entry(root, textvariable = TotalDose_Gy_boost)
textTotalDose_b.grid(column=1,row=5)
textTotalDose_b.config(width=27)
textTotalDose_b.insert(0, "Fill if Boost")

 
#Combobox for select Roi for dose prescription
lbRoiPre = Label(root, text = 'Prescription Dose Boost to')
lbRoiPre.grid(column=0,row=6)
lbRoiPre.config(width=27, height =2)
combo_variableRoiPre_b = StringVar()
combo_valuesRoiPre_b = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
combo_valuesRoiPre_b.insert(0,"--None--")
comboRoiPre_b = ttk.Combobox(root, values= combo_valuesRoiPre_b, textvariable=combo_variableRoiPre_b)
comboRoiPre_b.grid(column=1,row=6)
comboRoiPre_b.config(width=27, height =20)
comboRoiPre_b.set("--None--")

#Combobox for select isocenter to center of Roi or poi
lbIso = Label(root, text= 'Isocenter placment')
lbIso.grid(column=0 , row=7)
lbIso.config(width=27, height =2)
combo_variableIso = StringVar()
combo_Iso = [i.Name for i in patient.Cases[0].PatientModel.PointsOfInterest]
comboIso = ttk.Combobox(root, values = combo_Iso, textvariable= combo_variableIso)
comboIso.grid(column=1,row=7)
comboIso.config(width=27, height =5)

#Combobox for select photon energy
lbPhotonE = Label(root, text= 'Select photon energy')
lbPhotonE.grid(column=0 , row=8)
lbPhotonE.config(width=27, height =2)
combo_variablePhotonE = StringVar()
combo_PhotonE = ['6', '10', '6 FFF']
comboPhotonE = ttk.Combobox(root, values = combo_PhotonE, textvariable= combo_variablePhotonE)
comboPhotonE.grid(column=1,row=8)
comboPhotonE.config(width=27, height =5)
comboPhotonE.set('6 FFF')


#For match ROI to optimization
hippo_r = "Hippocampus_R"
hippo_l = "Hippocampus_L"
#hippo_tol = "Hippocampus"
#hippo_plus = "Hippo+5mm"
chiasm = "Optic Chiasm"
brainstem = "Brainstem"
cord = "Spinal Cord"
optic_r = "Optic Nerve Rt"
optic_l = "Optic Nerve Lt"
eye_r = "Eye Rt"
eye_l = "Eye Lt"
lg_r = "Lacrimal Gland Rt"
lg_l = "Lacrimal Gland Lt"
len_r = "Lens Rt"
len_l = "Lens Lt"
brain = "Brain"
body = "BODY"

def Button_MatchRoi():
    Sub_root1 = Toplevel()
    Sub_root1.title('Match Roi')
    Sub_root1.geometry('320x600')
    ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
    ListRoi.insert(0,"----")

    def lbMatch(root_frame=Sub_root1,  List = ListRoi, roi = 'ROI', row_n = 0):
        lbMatchROI = Label(root_frame, text= roi)
        lbMatchROI.grid(column=0 , row=row_n)
        lbMatchROI.config(width=15, height =2)
        if roi in ListRoi:
            lbMatchROI = Label(root_frame, text= 'Matched')
            lbMatchROI.grid(column=1 , row=row_n)
            lbMatchROI.config(width=27, height =2)
            return roi
        else:
            combo_ROI = StringVar()
            comboROI = ttk.Combobox(root_frame, values = ListRoi, textvariable= combo_ROI)
            comboROI.grid(column=1,row=row_n)
            comboROI.config(width=27, height =20)
            return comboROI

    #combo_ptv = lbMatch(Sub_root1, ListRoi, roi = ptv, row_n = 0)
    #combo_ptv_boost = lbMatch(Sub_root1, ListRoi, roi = ptv_boost, row_n = 1)
    combo_hippo_r = lbMatch(Sub_root1, ListRoi, roi = hippo_r, row_n = 2)
    combo_hippo_l = lbMatch(Sub_root1, ListRoi, roi = hippo_l, row_n = 3)
    #combo_hippo_tol = lbMatch(Sub_root1, ListRoi, roi = hippo_tol, row_n = 2)
    #combo_hippo_plus = lbMatch(Sub_root1, ListRoi, roi = hippo_plus, row_n = 3)
    combo_chiasm = lbMatch(Sub_root1, ListRoi, roi = chiasm, row_n = 4)
    combo_brainstem = lbMatch(Sub_root1, ListRoi, roi = brainstem, row_n = 5)
    combo_cord = lbMatch(Sub_root1, ListRoi, roi = cord, row_n = 6)
    combo_optic_r = lbMatch(Sub_root1, ListRoi, roi = optic_r, row_n = 7)
    combo_optic_l = lbMatch(Sub_root1, ListRoi, roi = optic_l, row_n = 8)
    combo_eye_r = lbMatch(Sub_root1, ListRoi, roi = eye_r, row_n = 9)
    combo_eye_l = lbMatch(Sub_root1, ListRoi, roi = eye_l, row_n = 10)
    combo_lg_r = lbMatch(Sub_root1, ListRoi, roi = lg_r, row_n = 11)
    combo_lg_l = lbMatch(Sub_root1, ListRoi, roi = lg_l, row_n = 12)
    combo_len_r = lbMatch(Sub_root1, ListRoi, roi = len_r, row_n = 13)
    combo_len_l = lbMatch(Sub_root1, ListRoi, roi = len_l, row_n = 14)
    combo_brain = lbMatch(Sub_root1, ListRoi, roi = brain, row_n = 15)
    combo_body = lbMatch(Sub_root1, ListRoi, roi = body, row_n = 16)

    #Cancel Button in Sub_root1
    def Button_Cancel_sub1():
        Sub_root1.destroy()

    buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
    buttCancelSub1.grid(column=0,row=17,pady=15)
    buttCancelSub1.config(width=10)

    #Apply Button in Sub_root1
    def Button_Apply_sub1():
        global hippo_r
        global hippo_l
        #global hippo_tol
        #global hippo_plus
        global chiasm
        global brainstem
        global cord
        global optic_r
        global optic_l
        global eye_r
        global eye_l
        global lg_r
        global lg_l
        global len_r
        global len_l
        global brain
        global body

        def apply(roi, combo_roi):
            try:
               roi = combo_roi.get()
               return roi
            except:
               roi = combo_roi
               return roi

        hippo_r = apply(hippo_r, combo_hippo_r)
        hippo_l = apply(hippo_l, combo_hippo_l)
        #hippo_tol = apply(hippo_tol, combo_hippo_tol)
        #hippo_plus = apply(hippo_plus, combo_hippo_plus)
        chiasm = apply(chiasm, combo_chiasm)
        brainstem = apply(brainstem, combo_brainstem)
        cord = apply(cord, combo_cord)
        optic_r = apply(optic_r, combo_optic_r)
        optic_l = apply(optic_l, combo_optic_l)
        eye_r = apply(eye_r, combo_eye_r)
        eye_l = apply(eye_l, combo_eye_l)
        lg_r = apply(lg_r, combo_lg_r)
        lg_l = apply(lg_l, combo_lg_l)
        len_r = apply(len_r, combo_len_r)
        len_l = apply(len_l, combo_len_l)
        brain = apply(brain, combo_brain)
        body = apply(body, combo_body)
        Sub_root1.destroy()

    buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
    buttApplySub1.grid(column=1,row=17,pady=15)
    buttApplySub1.config(width=10)
 
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=12)
lbMatchRoi.config(width=27, height =2)
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = [hippo_r, hippo_l, chiasm, brainstem, cord, optic_r, optic_l, eye_r, eye_l, lg_r, lg_l, len_r, len_l, brain, body]
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
 
def create_virtual():
    # zHippocampus_tol
    zHippo_tol = case.PatientModel.CreateRoi(Name="zzHippo_tol", Color="Yellow", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zHippo_tol.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [hippo_l, hippo_r], 
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
    # zHippo+5
    zHippo_plus = case.PatientModel.CreateRoi(Name="zzHippo_plus", Color="Aqua", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zHippo_plus.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzHippo_tol"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 
                                                            'Anterior': 0.5, 'Posterior': 0.5, 
                                                            'Right': 0.5, 'Left': 0.5 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ResultOperation="None", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })


    # zPTV
    zPTV = case.PatientModel.CreateRoi(Name="zzPTV", Color="Red", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzHippo_plus"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 
                                                            'Anterior': 0.2, 'Posterior': 0.2, 
                                                            'Right': 0.2, 'Left': 0.2 } }, 
                            ResultOperation="Subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    if ptv_boost in ListRoi:
        zPTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv_boost], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                            'Anterior': 1, 'Posterior': 1, 
                                                            'Right': 1, 'Left': 1 } }, 
                            ResultOperation="Subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })

    if ptv_boost in ListRoi:
        zRing_boost = case.PatientModel.CreateRoi(Name="zzRing_boost", Color="Red", Type="Control",
                                                    TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
        zRing_boost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv_boost], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                'Anterior': 1.3, 'Posterior': 1.3, 
                                                                'Right': 1.3, 'Left': 1.3 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv_boost], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
                                                                'Anterior': 0.3, 'Posterior': 0.3, 
                                                                'Right': 0.3, 'Left': 0.3 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                            
    # zPTV_uni
    zPTV_uni = case.PatientModel.CreateRoi(Name="zzPTV_uni", Color="Red", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPTV_uni.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzHippo_plus"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                            'Anterior': 1, 'Posterior': 1, 
                                                            'Right': 1, 'Left': 1 } }, 
                            ResultOperation="Subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    zPTV_uni.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV_uni"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [optic_r,optic_l,chiasm], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                            'Anterior': 1, 'Posterior': 1, 
                                                            'Right': 1, 'Left': 1 } }, 
                            ResultOperation="Subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })
    if ptv_boost in ListRoi:
        zPTV_uni.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                            ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzPTV_uni"], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 } }, 
                            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv_boost], 
                                        'MarginSettings': { 'Type': "Expand", 'Superior': 2.5, 'Inferior': 2.5, 
                                                            'Anterior': 2.5, 'Posterior': 2.5, 
                                                            'Right': 2.5, 'Left': 2.5 } }, 
                            ResultOperation="Subtraction", 
                            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                    'Anterior': 0, 'Posterior': 0, 
                                                    'Right': 0, 'Left': 0 })


    # zRing
    zRing = case.PatientModel.CreateRoi(Name="zzRing", Color="White", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                'Anterior': 2, 'Posterior': 2, 
                                                                'Right': 2, 'Left': 2 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
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
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zBS_PTV
    zBS_PTV = case.PatientModel.CreateRoi(Name="zzBS_PTV", Color="Pink", Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zBS_PTV.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [brainstem], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzHippo_tol"], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 8, 'Inferior': 8, 
                                                                'Anterior': 8, 'Posterior': 8, 
                                                                'Right': 8, 'Left': 8 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    # zFace
    zFace = case.PatientModel.CreateRoi(Name="zzFace", Color="Blue", Type="Control",
                                        TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zFace.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [eye_l,eye_r], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 10, 'Inferior': 10, 
                                                                'Anterior': 10, 'Posterior': 10, 
                                                                'Right': 10, 'Left': 10 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [brain], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                'Anterior': 2, 'Posterior': 2, 
                                                                'Right': 2, 'Left': 2 } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })
    zFace.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzFace"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [body], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })

    # Hippo_Contract
    zHippo_contract =  case.PatientModel.CreateRoi(Name="zzHippo_contract", Color="White", Type="Control",
                                                    TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zHippo_contract.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [hippo_l, hippo_r], 
                                            'MarginSettings': { 'Type': "Contract", 'Superior': 0.15, 'Inferior': 0.15, 
                                                                'Anterior': 0.15, 'Posterior': 0.15, 
                                                                'Right': 0.15, 'Left': 0.15 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ResultOperation="None", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                                                                                   
    

def addPlan():
    print("Creaste Plan")
    plan = case.AddNewPlan(PlanName = "AutoHippo VMAT", ExaminationName = 'CT Plan') 
    beam_set = plan.AddNewBeamSet(Name='AutoHippo VMAT', ExaminationName = 'CT Plan', 
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
    print("Get iso compleate")
    iso_data = beam_set.CreateDefaultIsocenterData(Position={'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z})
    patient.Save()
    plan.SetCurrent()
    beam_set.SetCurrent()

    #Add Beam
    print("Add Beam")
    PhotonE = comboPhotonE.get()
    Add_Beam1 = beam_set.CreateArcBeam(ArcStopGantryAngle=179, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="1", Description=f"1.CW181-179", GantryAngle=181, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=330)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[0].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=40, BurstGantrySpacing=None, MaxArcMU=None)
    print("Add Beam 1 compleate")
    Add_Beam2 = beam_set.CreateArcBeam(ArcStopGantryAngle=181, ArcRotationDirection="CounterClockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="2", Description=f"2.CCW179-181", GantryAngle=179, CouchRotationAngle=0, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=30)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[1].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=40, BurstGantrySpacing=None, MaxArcMU=None)
    print("Add Beam 2 compleate")
    Add_Beam3 = beam_set.CreateArcBeam(ArcStopGantryAngle=181, ArcRotationDirection="CounterClockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="3", Description=f"3.CCW179-10_c90", GantryAngle=10, CouchRotationAngle=90, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=30)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[2].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=40, BurstGantrySpacing=None, MaxArcMU=None)

    print("Add Beam 3 compleate")
    Add_Beam4 = beam_set.CreateArcBeam(ArcStopGantryAngle=10, ArcRotationDirection="Clockwise", 
                            BeamQualityId=PhotonE, IsocenterData= iso_data,
                            Name="4", Description=f"4.CW10-179_c90", GantryAngle=181, CouchRotationAngle=90, 
                            CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=330)
    plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[3].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, FinalGantrySpacing=2, MaxArcDeliveryTime=40, BurstGantrySpacing=None, MaxArcMU=None)
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

def max_dose_constraint(po, roi_name, dose_level, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName = roi_name, IsConstraint=True)
    o.DoseFunctionParameters.DoseLevel = dose_level

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

def target_eud(po, roi_name, dose_level, eud_parameter, weigth, beam_set_index=0):
    o = po.AddOptimizationFunction(FunctionType="TargetEud", RoiName = roi_name)
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
    db = get_current("PatientDB")
    Po = plan.PlanOptimizations[0]
    DosePrescription = float(TotalDose_Gy.get()) * 100
    print("Start adding cost function from template [Faro2025Hippo]")
    print("Load Template")
    #############################################################################
    #############################################################################
    ####################### Change Template name here ###########################
    #############################################################################
    template = db.LoadTemplateOptimizationFunctions(templateName='FaroHippov.2') 
    #############################################################################
    #############################################################################
    #############################################################################
    print("Apply Template")
    plan.PlanOptimizations[0].ApplyOptimizationTemplate(Template=template, AssociatedRoisAndPois={ 'Lacrimal Gland Lt': lg_l, 'Lacrimal Gland Rt': lg_r, 
                                                                                                    'Lens Lt': len_l, 'Lens Rt': len_r, 'Optic Chiasm': chiasm, 'Optic Nerve Lt': optic_l, 
                                                                                                    'Optic Nerve Rt': optic_r, 'Spinal Cord': cord, 'Eye Lt': eye_l, 'Eye Rt': eye_r, 
                                                                                                    'Brainstem': brainstem, 'zzPTV': "zzPTV", 'zzHippo_plus': "zzHippo_plus", 'zzHippo_tol': "zzHippo_tol", 
                                                                                                    'zzRing': "zzRing", 'BODY': body, 'zzPTV_uni': "zzPTV_uni" }, ReplaceExistingOptimizationFunctions=True)
                                                                        
    print("Finish add cost function")

def GetAbsoluteVolumeAtDose(plan,roi,dose):
	Vd = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName= roi, DoseValues=[dose])
	roi = case.PatientModel.StructureSets[0].RoiGeometries[roi]
	Vdcc = Vd*roi.GetRoiVolume()
	return Vdcc

def create_contour_from_dose(dose, dose_level, name):
	roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print(f"Create {name}") 

def create_plus_dose(dose, dose_level, name, X):
	roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = dose_level*100
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [X], 
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

            print("get PTV")
            global ptv
            ptv = comboRoiPre.get()
            print(ptv)
            global ptv_boost
            ptv_boost = comboRoiPre_b.get()
            print(ptv_boost)

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
            max_eud(Po, "zzHippo_tol",dose_level=10*100, eud_parameter=10, weigth=5)
            max_eud(Po, "zzHippo_plus",dose_level=16*100, eud_parameter=5, weigth=5)
            for i in range(0,1):
                Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
            patient.Save()
            plan.SetCurrent()
            beam_set.SetCurrent()
            DosePrescription = float(TotalDose_Gy.get()) * 100
            if ptv_boost in ListRoi:
                DosePrescription_boost = float(TotalDose_Gy_boost.get()) * 100
            ############################################################
            #Loop optimize algorithum
            ############################################################
            zDose105 = case.PatientModel.CreateRoi(Name="zzDose_105%", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
            beamset = get_current('BeamSet')
            threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (105/100)
            zDose105.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
            if ptv_boost in ListRoi:
                zDose105.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzDose_105%"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [f"{ptv_boost}"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 1.3, 'Inferior': 1.3, 
                                                                    'Anterior': 1.3, 'Posterior': 1.3, 
                                                                    'Right': 1.3, 'Left': 1.3 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })
            max_dvh(Po, "zzDose_105%", dose_level=DosePrescription*1.05, percent_volume=0.5, weigth=100)
            max_dose(Po, "zzDose_105%", dose_level=DosePrescription*1.06, weigth=350)
            zPlus_PTV = create_plus_dose(plan.TreatmentCourse.TotalDose, DosePrescription/100, f"zz+{DosePrescription/100}", X="zzPTV")
            min_dvh(Po, f"zz+{DosePrescription/100}", dose_level=DosePrescription*1.023, percent_volume=99.9, weigth=100)
            uniform_constraint(Po, "zzPTV_uni", stdv=1.5)
            if ptv_boost in ListRoi:
                zPlust_Boost = create_plus_dose(plan.TreatmentCourse.TotalDose, DosePrescription_boost/100, f"zz+{DosePrescription_boost/100}", X=ptv_boost)
                min_dvh(Po, f"zz+{DosePrescription_boost/100}", dose_level=DosePrescription_boost*1.023, percent_volume=99.9, weigth=100)
            for i in range(0,1):
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