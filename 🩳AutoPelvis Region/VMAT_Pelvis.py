from connect import *
from tkinter import *
from tkinter import ttk

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('Plan design')
root.geometry('400x440')

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
lbTotalDose1 = Label(root, text= 'Fill Total Dose 1 (Gy)')
lbTotalDose1.grid(column=0 ,row=3)
lbTotalDose1.config(width=27, height =2)
TotalDose_Gy1 = StringVar()
textTotalDose1 = Entry(root, textvariable = TotalDose_Gy1)
textTotalDose1.grid(column=1,row=3)
textTotalDose1.config(width=27)

lbTotalDose2 = Label(root, text= 'Fill Total Dose 2 (Gy)')
lbTotalDose2.grid(column=0 ,row=4)
lbTotalDose2.config(width=27, height =2)
TotalDose_Gy2 = StringVar()
textTotalDose2 = Entry(root, textvariable = TotalDose_Gy2)
textTotalDose2.grid(column=1,row=4)
textTotalDose2.config(width=27)

lbTotalDose3 = Label(root, text= 'Fill Total Dose 3 (Gy)')
lbTotalDose3.grid(column=0 ,row=5)
lbTotalDose3.config(width=27, height =2)
TotalDose_Gy3 = StringVar()
textTotalDose3 = Entry(root, textvariable = TotalDose_Gy3)
textTotalDose3.grid(column=1,row=5)
textTotalDose3.config(width=27)

#Test open patient
try:
    patient = get_current('Patient')
except:
    messagebox.showinfo('No patient selected. \nScript terminated')
    exit()
 
#Combobox for select Roi for dose prescription
lbRoiPre = Label(root, text = 'Prescription to')
lbRoiPre.grid(column=0,row=6)
lbRoiPre.config(width=27, height =2)
combo_variableRoiPre = StringVar()
combo_valuesRoiPre = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
comboRoiPre = ttk.Combobox(root, values= combo_valuesRoiPre, textvariable=combo_variableRoiPre)
comboRoiPre.grid(column=1,row=6)
comboRoiPre.config(width=27, height =20)

#Combobox for select isocenter to center of Roi or poi
lbIso = Label(root, text= 'Isocenter placment')
lbIso.grid(column=0 , row=7)
lbIso.config(width=27, height =2)
combo_variableIso = StringVar()
combo_Iso = ['Center of Roi', 'Poi(Origin)']
comboIso = ttk.Combobox(root, values = combo_Iso, textvariable= combo_variableIso)
comboIso.grid(column=1,row=7)
comboIso.config(width=27, height =5)

#Combobox for select photon energy
lbPhotonE = Label(root, text= 'Select photon energy')
lbPhotonE.grid(column=0 , row=8)
lbPhotonE.config(width=27, height =2)
combo_variablePhotonE = StringVar()
combo_PhotonE = ['6', '10', '6 FFF', '10 FFF']
comboPhotonE = ttk.Combobox(root, values = combo_PhotonE, textvariable= combo_variablePhotonE)
comboPhotonE.grid(column=1,row=8)
comboPhotonE.config(width=27, height =5)

#For match ROI to optimization
ptv1 = "PTV1"
ctv1 = "CTV1"
ptv2 = "PTV2"
ctv2 = "CTV2"
ptv3 = "PTV3"
ctv3 = "CTV3"
body = "BODY"
bladder = "Bladder"
sigmoid = "Sigmoid"
bowel = "Small bowel"
rectum = "Rectum"
kidney_lt = "Kidney Lt"
kidney_rt = "Kidney Rt"
liver = "Liver"
perineum = "Perineum"
femur_lt = "Femoral Head Lt"
femur_rt = "Femoral Head Rt"


def Button_MatchRoi():
    Sub_root1 = Toplevel()
    Sub_root1.title('Match Roi')
    Sub_root1.geometry('320x670')
    ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]

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
            return combo_ROI

    combo_ptv1 = lbMatch(Sub_root1, ListRoi, roi = ptv1, row_n = 0)
    combo_ctv1 = lbMatch(Sub_root1, ListRoi, roi = ctv1, row_n = 1)
    combo_ptv2 = lbMatch(Sub_root1, ListRoi, roi = ptv2, row_n = 2)
    combo_ctv2 = lbMatch(Sub_root1, ListRoi, roi = ctv2, row_n = 3)
    combo_ptv3 = lbMatch(Sub_root1, ListRoi, roi = ptv3, row_n = 4)
    combo_ctv3 = lbMatch(Sub_root1, ListRoi, roi = ctv3, row_n = 5)
    combo_body = lbMatch(Sub_root1, ListRoi, roi = body, row_n = 6)
    combo_bladder = lbMatch(Sub_root1, ListRoi, roi = bladder, row_n = 7)
    combo_sigmoid = lbMatch(Sub_root1, ListRoi, roi = sigmoid, row_n = 8)
    combo_bowel = lbMatch(Sub_root1, ListRoi, roi = bowel, row_n = 9)
    combo_rectum = lbMatch(Sub_root1, ListRoi, roi = rectum, row_n = 10)
    combo_kidney_lt = lbMatch(Sub_root1, ListRoi, roi = kidney_lt, row_n = 11)
    combo_kidney_rt = lbMatch(Sub_root1, ListRoi, roi = kidney_rt, row_n = 12)
    combo_liver = lbMatch(Sub_root1, ListRoi, roi = liver, row_n = 13)
    combo_perineum = lbMatch(Sub_root1, ListRoi, roi = perineum, row_n = 14)
    combo_femur_lt = lbMatch(Sub_root1, ListRoi, roi = femur_lt, row_n = 15)
    combo_femur_rt = lbMatch(Sub_root1, ListRoi, roi = femur_rt, row_n = 16)

    #Cancel Button in Sub_root1
    def Button_Cancel_sub1():
        Sub_root1.destroy()

    buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
    buttCancelSub1.grid(column=0,row=17,pady=15)
    buttCancelSub1.config(width=10)

 #Apply Button in Sub_root1
    def Button_Apply_sub1():
        global ptv1
        global ctv1
        global ptv2
        global ctv2
        global ptv3
        global ctv3
        global body
        global bladder
        global sigmoid
        global bowel
        global rectum
        global kidney_lt
        global kidney_rt
        global liver
        global perineum
        global femur_lt
        global femur_rt

        def apply(roi, combo_roi):
            try:
               roi = combo_roi.get()
            except:
               roi = combo_roi

        apply(ptv1, combo_ptv1)
        apply(ctv1, combo_ctv1)
        apply(ptv2, combo_ptv2)
        apply(ctv2, combo_ctv2)
        apply(ptv3, combo_ptv3)
        apply(ctv3, combo_ctv3)
        apply(body,combo_body)
        apply(bladder,combo_bladder)
        apply(sigmoid, combo_sigmoid)
        apply(bowel, combo_sigmoid)
        apply(rectum, combo_rectum)
        apply(kidney_lt, combo_kidney_lt)
        apply(kidney_rt, combo_kidney_rt)
        apply(liver, combo_liver)
        apply(perineum, combo_perineum)
        apply(femur_lt, combo_femur_lt)
        apply(femur_rt, combo_femur_rt)

        Sub_root1.destroy()

    buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
    buttApplySub1.grid(column=1,row=17,pady=15)
    buttApplySub1.config(width=10)
 
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=9)
lbMatchRoi.config(width=27, height =2)
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = [ptv1,ctv1,ptv2,ctv2,ptv3,ctv3,body,bladder,sigmoid,bowel,rectum,kidney_lt,kidney_rt,liver,perineum,femur_lt,femur_rt]
print(ListRoi)

for roi in ListRoiOpt:
	if roi in ListRoi:
	    lbMatchRoi2 = Label(root, text= 'Already match roi')
	    lbMatchRoi2.grid(column=1 , row=9)
	    lbMatchRoi2.config(width=27, height =2)
	    continue
	else:
	    buttMatch = Button(root, text = 'Match ROI', command = Button_MatchRoi)
	    buttMatch.grid(column=1,row=9,padx=10,pady=5)
	    buttMatch.config(width=15)
	    break

#Cancel Button
def Button_Cancel():
   root.destroy()

buttCancel = Button(root, text = 'Cancel', command = Button_Cancel)
buttCancel.grid(column=0,row=10,padx=10,pady=25)
buttCancel.config(width=15)  

def create_contour_from_dose(dose, dose_level, name):
	roi = case.PatientModel.CreateRoi(Name=f"{name}", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print(f"Create {name}")
   
def create_virtual():
   #Creat virtual organ : zz Ant
   VirtualAnt = case.PatientModel.CreateRoi(Name="zz Ant", Color="Yellow", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [bladder,sigmoid,bowel], 
                                                 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 6, 'Posterior': 0, 
                                                                    'Right': 3, 'Left': 3 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv1,ptv2,ptv3], 
                                                 'MarginSettings': { 'Type': "Expand", 'Superior': 1,'Inferior': 1, 
                                                                    'Anterior': 1, 'Posterior': 2, 
                                                                    'Right': 2, 'Left': 2 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                                                         'Anterior': 0, 'Posterior': 0, 
                                                                                         'Right': 3, 'Left': 3 })
   VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [body, "zz Ant"], 
                                                 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv1,ptv2,ptv3], 
                                                 'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
                                                                    'Anterior': 1.5, 'Posterior': 10, 
                                                                    'Right': 1.5, 'Left': 1.5 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                          'Anterior': 0, 'Posterior': 0, 
                                                          'Right': 0, 'Left': 0 })
   
   #Creat virtual organ : zz RingPTV
   VirtualRing = case.PatientModel.CreateRoi(Name="zz RingPTV", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                     ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [ptv1,ptv2,ptv3], 
                                                  'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
                                                                     'Anterior': 2, 'Posterior': 2, 
                                                                     'Right': 2, 'Left': 2 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [ptv1,ptv2,ptv3], 
                                                 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
                                                                    'Anterior': 1, 'Posterior': 0.5, 
                                                                    'Right': 0.5, 'Left': 0.5 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                          'Anterior': 0, 'Posterior': 0, 
                                                          'Right': 0, 'Left': 0 })
    #Creat virtual organ : zz Bladder
    VirtualBladder = case.PatientModel.CreateRoi(Name="zz Bladder", Color="Aqua", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    VirtualBladder.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [Opt5], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 5, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Opt1, Opt3], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
            'Anterior': 1.5, 'Posterior': 1, 'Right': 1.5, 'Left': 1.5 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Contract", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0.7, 'Left': 0.7 })
     #Creat virtual organ : z PTV 50.4+Organ
   VirtualPtv504Organ = case.PatientModel.CreateRoi(Name="z PTV 50.4+Organ", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualPtv504Organ.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
            'SourceRoiNames': [Opt6, Opt5, Opt7], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 
            'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 
            'SourceRoiNames': [Opt1], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     #Creat virtual organ : z PTV 54+Organ
   VirtualPtv54Organ = case.PatientModel.CreateRoi(Name="z PTV 54+Organ", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualPtv54Organ.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
            'SourceRoiNames': [Opt6, Opt5, Opt7], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 
            'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 
            'SourceRoiNames': [Opt3], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     #Creat virtual organ : z Organ-PTV54
   VirtualOrganSub54 = case.PatientModel.CreateRoi(Name="z Organ-PTV54", Color="SaddleBrown", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualOrganSub54.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union",
            'SourceRoiNames': [Opt6, Opt5, Opt7], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.2,
            'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union",
            'SourceRoiNames': [Opt1], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 
            'Anterior': 0.3, 'Posterior': 0.3, 'Right': 0.3, 'Left': 0.3 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     #Creat virtual organ : z PTV50.4
   VirtualPTV504 = case.PatientModel.CreateRoi(Name="z PTV50.4", Color="SaddleBrown", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualPTV504.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union",
            'SourceRoiNames': [Opt1], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0,
            'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union",
            'SourceRoiNames': [Opt3], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.4, 'Inferior': 0.4, 
            'Anterior': 0.4, 'Posterior': 0.4, 'Right': 0.4, 'Left': 0.4 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })  
     #Creat virtual organ : z Perineum
   VirtualPTV504 = case.PatientModel.CreateRoi(Name="z Perineum", Color="SaddleBrown", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualPTV504.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union",
            'SourceRoiNames': [Opt10], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.5,
            'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union",
            'SourceRoiNames': [Opt1, Opt3], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 1.2, 'Inferior': 1.2, 
            'Anterior': 1.2, 'Posterior': 1.2, 'Right': 1.2, 'Left': 1.2 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })  
   

#Add cost fuction for optimization
def AddCostFucn():
 plan = get_current("Plan")
 Po = plan.PlanOptimizations[0]
 DosePrescription1 = float(TotalDose_Gy1.get()) * 100
 DosePrescription2 = float(TotalDose_Gy2.get()) * 100 
 with CompositeAction('Add optimization function'):
   AddCostFunc0 = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName=Opt1) #PTV 50.4
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.Weight = 300
 with CompositeAction('Add optimization function'):
   AddCostFunc1 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt1) #PTV 50.4
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*1.005)
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*1.035)
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.LowDoseDistance = 0.4
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.Weight = 400  
 with CompositeAction('Add optimization function'):
   AddCostFunc2 = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=Opt2) #CTV 50.4
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.PercentVolume = 100
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.Weight = 800
 with CompositeAction('Add optimization function'):
   AddCostFunc3 = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName=Opt3) #PTV 54
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.008)
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.Weight = 300
 with CompositeAction('Add optimization function'):
   AddCostFunc4 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt3) #PTV 54
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.045)
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.Weight = 400
 with CompositeAction('Add optimization function'):
   AddCostFunc5 = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=Opt4) #CTV 54
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.01)
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.PercentVolume = 100
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.Weight = 800 
#optimized Bladder
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc6 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt5) 
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.02778)
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 10
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc7 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5) 
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1)
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.77778)
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.Weight = 10  
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc8 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5) 
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1)
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.44445)
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.LowDoseDistance = 2.5
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.Weight = 20 
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc9 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.26667)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.LowDoseDistance = 6
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.Weight = 10
#optimized z Organ-PTV54
 with CompositeAction('Add optimization function'):
   AddCostFunc10 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Organ-PTV54") 
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*1.035)
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.LowDoseDistance = 0.3
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.Weight = 10 
 with CompositeAction('Add optimization function'):
   AddCostFunc11 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z Organ-PTV54")
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.02778)
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.Weight = 50 
#optimized Sigmoid
 with CompositeAction('Add optimization function'):
   AddCostFunc12 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.035)
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.Weight = 50 
 with CompositeAction('Add optimization function'):
   AddCostFunc13 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.77778)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.Weight = 10
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
 with CompositeAction('Add optimization function'):
   AddCostFunc14 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.55556)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.LowDoseDistance = 2.5
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.Weight = 10
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.AdaptToTargetDoseLevels = True
#optimized Small bowel
 with CompositeAction('Add optimization function'):
   AddCostFunc15 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.5)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.LowDoseDistance = 1.0
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.Weight = 10
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.AdaptToTargetDoseLevels = True  
 with CompositeAction('Add optimization function'):
   AddCostFunc16 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.4)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.LowDoseDistance = 2.0
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.Weight = 20
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.AdaptToTargetDoseLevels = True     
 with CompositeAction('Add optimization function'):
   AddCostFunc17 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2)
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.25)
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.LowDoseDistance = 3.0
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.Weight = 20
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.AdaptToTargetDoseLevels = True
 with CompositeAction('Add optimization function'):
   AddCostFunc18 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.035)
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.Weight = 50 
#optimized BODY   
 with CompositeAction('Add optimization function'): 
   AddCostFunc19 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt9)
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.05556)
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.Weight = 300 
 with CompositeAction('Add optimization function'): 
   AddCostFunc20 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt9)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*1.005)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.7937)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.Weight = 10
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.AdaptToTargetDoseLevels = True 
 with CompositeAction('Add optimization function'):
   AddCostFunc21 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt9)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*1.005)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.5)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.LowDoseDistance = 2
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.AdaptToTargetDoseLevels = True
 with CompositeAction('Add optimization function'):
   AddCostFunc22 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt9)
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*1.005)
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.9)
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.LowDoseDistance = 0.5
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.Weight = 30
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.AdaptToTargetDoseLevels = True
 with CompositeAction('Add optimization function'):
   AddCostFunc23 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z RingPTV")
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*0.99)
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.77778)
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.LowDoseDistance = 0.5
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.Weight = 10
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.AdaptToTargetDoseLevels = True
 with CompositeAction('Add optimization function'):
   AddCostFunc24 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z RingPTV")
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.DoseLevel = int(DosePrescription1*0.98889)
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.Weight = 200
 with CompositeAction('Add optimization function'):
   AddCostFunc25 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV 50.4+Organ")
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.04)
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.Weight = 100
 with CompositeAction('Add optimization function'):
   AddCostFunc26 = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV 50.4+Organ")
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.PercentVolume = 95
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.Weight = 300
 with CompositeAction('Add optimization function'):
   AddCostFunc27 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Ant")
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1*0.5)
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.25)
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.Weight = 10
 with CompositeAction('Add optimization function z Organ-PTV54'):
   AddCostFunc28 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Organ-PTV54")
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.HighDoseLevel = int(DosePrescription2*1.005)
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.7937)
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.LowDoseDistance = 1.0
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.Weight = 30
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.AdaptToTargetDoseLevels = True
 with CompositeAction('Add optimization function'):
   AddCostFunc29 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z Organ-PTV54")
   Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.035)
   Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.Weight = 50
 with CompositeAction('Add optimization function z Bladder'):
   AddCostFunc30 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Bladder")
   Po.Objective.ConstituentFunctions[30].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1*0.62222)
   Po.Objective.ConstituentFunctions[30].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.4)
   Po.Objective.ConstituentFunctions[30].DoseFunctionParameters.LowDoseDistance = 1
   Po.Objective.ConstituentFunctions[30].DoseFunctionParameters.Weight = 20
 with CompositeAction('Add optimization function z PTV50.4'):
   AddCostFunc31 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z PTV50.4")
   Po.Objective.ConstituentFunctions[31].DoseFunctionParameters.HighDoseLevel = int(5375)
   Po.Objective.ConstituentFunctions[31].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*1.035)
   Po.Objective.ConstituentFunctions[31].DoseFunctionParameters.LowDoseDistance = 0.3
   Po.Objective.ConstituentFunctions[31].DoseFunctionParameters.Weight = 10
 with CompositeAction('Add optimization function'):
   AddCostFunc32 = Po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName="z PTV50.4")
   Po.Objective.ConstituentFunctions[32].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.04)
   Po.Objective.ConstituentFunctions[32].DoseFunctionParameters.PercentVolume = 1
   Po.Objective.ConstituentFunctions[32].DoseFunctionParameters.Weight = 300 
 with CompositeAction('Add optimization function z Perineum'):
   AddCostFunc33 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Perineum")
   Po.Objective.ConstituentFunctions[33].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1*0.69444)
   Po.Objective.ConstituentFunctions[33].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.45)
   Po.Objective.ConstituentFunctions[33].DoseFunctionParameters.LowDoseDistance = 1.2
   Po.Objective.ConstituentFunctions[33].DoseFunctionParameters.Weight = 30
   
def create_contour_from_dose(dose, dose_level):
	roi = case.PatientModel.CreateRoi(Name=f"z Dose_{dose_level}%", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print("Create D105%")
 
def add_105constrain(Name,DosePrescription1):
	plan = get_current("Plan")
	Po = plan.PlanOptimizations[0]
	print("Adding optimization function to D105%")
	with CompositeAction('Add optimization function'):
		AddCostFunc34 = Po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=Name)
		Po.Objective.ConstituentFunctions[34].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.045)
		Po.Objective.ConstituentFunctions[34].DoseFunctionParameters.PercentVolume = 1
		Po.Objective.ConstituentFunctions[34].DoseFunctionParameters.Weight = 500
	print("Add optimization done!")
            
#Next Button
def Button_Next():
 try:
  current = float(NumF.get())
  try:
   current = float(TotalDose_Gy1.get())
   if examination.Name == 'CT Plan':
    print('CT name is CT Plan already')
   else:
    examination.Name = 'CT Plan'
   get_CT_Curve()
   create_virtual()
   #Add plan
   plan = case.AddNewPlan(PlanName = 'VMAT', ExaminationName = 'CT Plan')
   beam_set = plan.AddNewBeamSet(Name='VMAT', ExaminationName = 'CT Plan', 
          MachineName = comboMac.get(), 
          Modality = 'Photons', 
          PatientPosition = 'HeadFirstSupine', 
          TreatmentTechnique = 'VMAT', 
          NumberOfFractions = NumF.get(),
          CreateSetupBeams=True, 
          UseLocalizationPointAsSetupIsocenter=False, 
          UseUserSelectedIsocenterSetupIsocenter=False)
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   #Add prescription
   TotalDose = float(TotalDose_Gy1.get()) * 100
   beam_set.AddRoiPrescriptionDoseReference(RoiName= comboRoiPre.get(),
                                         PrescriptionType= "DoseAtVolume",
                                         DoseValue= TotalDose,
                                         DoseVolume= 95,
                                         RelativePrescriptionLevel= 1)
   beam_set.SetDefaultDoseGrid(VoxelSize={'x': 0.2, 'y': 0.2, 'z': 0.2})
            #Isocenter placment
   Iso_StructureSet =  case.PatientModel.StructureSets['CT Plan']
   IsocenterPlacment = comboIso.get()
   IsoRoi = comboRoiPre.get()
   print(IsocenterPlacment)
   if IsocenterPlacment == 'Center of Roi':
     Iso_CenterRoi = Iso_StructureSet.RoiGeometries[IsoRoi].GetCenterOfRoi()
     isocenter = Iso_CenterRoi
   elif IsocenterPlacment == 'Poi(Origin)':
     Poi_name = 'Origin'
     Poi_position = Iso_StructureSet.PoiGeometries[Poi_name].Point
     isocenter = Poi_position
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   iso_data = beam_set.CreateDefaultIsocenterData(Position={'x': isocenter.x, 
                 'y': isocenter.y, 
                 'z': isocenter.z})
   PhotonE = comboPhotonE.get()
   
   Add_Beam1 = beam_set.CreateArcBeam(ArcStopGantryAngle=181, ArcRotationDirection="CounterClockwise", 
             BeamQualityId=PhotonE, IsocenterData= iso_data,
             Name="1", Description="CCW179-181", GantryAngle=179, CouchRotationAngle=0, 
             CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=350)
   plan.PlanOptimizations[0].OptimizationParameters.TreatmentSetupSettings[0].BeamSettings[0].ArcConversionPropertiesPerBeam.EditArcBasedBeamOptimizationSettings(CreateDualArcs=False, 
             FinalGantrySpacing=2, BurstGantrySpacing=None, MaxArcMU=None)
   beam_set.CopyAndReverseBeam(BeamName="1")
   beam_set.Beams['2'].Description = "CW181-179"   
   #Edit name description and gantryangle of setup field
   with CompositeAction('Update setup beam name (SB_Original, beam set: 3D_CRT)'):
    beam_set.PatientSetup.SetupBeams['SB1_1'].Name = "I1"
    beam_set.PatientSetup.SetupBeams['I1'].Description = "kV AP"
    beam_set.PatientSetup.SetupBeams['SB1_2'].Name = "I2"
    beam_set.PatientSetup.SetupBeams['I2'].Description = "kV Lt Lat"
    beam_set.PatientSetup.SetupBeams['SB1_3'].Name = "I3"
    beam_set.PatientSetup.SetupBeams['I3'].Description = "CBCT"
    beam_set.PatientSetup.SetupBeams['I3'].GantryAngle = 0   
   AddCostFucn()
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   plan = get_current("Plan")
   Po = plan.PlanOptimizations[0]
   Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   #loop optimization
   plan = get_current('Plan')
   Po = plan.PlanOptimizations[0]
   DosePrescription1 = float(TotalDose_Gy1.get()) * 100
   DosePrescription2 = float(TotalDose_Gy2.get()) * 100
   for o in range(1,6):
    MinCtv504 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=Opt2, DoseValues=[int(DosePrescription1)])
    MinCtv54 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=Opt4, DoseValues=[int(DosePrescription2)])
    MinDvhPtv504 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt1, RelativeVolumes=[0.95])
    MinDvhPtv54 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt3, RelativeVolumes=[0.95])
    MaxPtv54 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt3, RelativeVolumes=[0])
    MaxBladder = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt5, RelativeVolumes=[0])
    MaxSigmoid = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt6, RelativeVolumes=[0])
    MaxSmallBowel = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt7, RelativeVolumes=[0])
    MaxVirtualOrganSub54 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z Organ-PTV54", RelativeVolumes=[0])
    if MinCtv504[0] < 0.999951:
     Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.Weight = 800*(2**o)
    if MinCtv54[0] < 0.999951:
     Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.Weight = 800*(2**o)
    if MinDvhPtv504[0] < int(DosePrescription1):
     Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.Weight = 300*(2**o)
    if MinDvhPtv54[0] < int(DosePrescription1):
     Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.Weight = 300*(2**o)
    if MaxPtv54 > int(DosePrescription1)*1.075:
     Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.Weight = 400+(200*o)
    if MaxVirtualOrganSub54[0] > int(DosePrescription1)*1.046:
     Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxBladder[0] > int(DosePrescription2)*1.046:
     Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSigmoid[0] > int(DosePrescription2)*1.046:
     Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSmallBowel[0] > int(DosePrescription2)*1.046:
     Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.Weight = 50+(10*(2**o))
    
    if MinCtv504[0] < 0.999951 or MinCtv54[0] < 0.999951 or MinDvhPtv[0] < int(DosePrescription2) or MaxBladder[0] > int(DosePrescription2)*1.046 or MaxSigmoid[0] > int(DosePrescription2)*1.046 or MaxSmallBowel[0] > int(DosePrescription2)*1.046:
    	## Run optimize
    	Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
    
   ## Check Dose 105% area
   dose105 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="z PTV50.4", DoseValues=[int(DosePrescription1)*1.05])
   if dose105 > 0.05:
   	## Covert 105% to contour
   	create_contour_from_dose(plan.TreatmentCourse.TotalDose, 105)
   	add_105constrain("z Dose_105%",DosePrescription1)
   	case.PatientModel.RegionsOfInterest['z Dose_105%'].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
   			ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["z Dose_105%"], 
   			'MarginSettings': { 'Type': "Expand", 'Superior': 0, 
   			'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
   			ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Opt3], 
   			'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 
   			'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", 
   			ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
   	Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
        
   root.destroy()
  except:
   textTotalDose.delete(0,END)
   #textTotalDose.insert(0,"ERROR")
   def Button_Cancel_sub2():
    Sub_root2.destroy()     
   Sub_root2 = Toplevel()
   Sub_root2.title('Notification')
   Sub_root2.geometry('60x100')
   lbMatchNoti1 = Label(Sub_root2, text= 'ERROR')
   lbMatchNoti1.grid(column=0 , row=0)
   lbMatchNoti1.config(width=10, height =5)
   buttCancelSub2 = Button(Sub_root2 , text = 'OK', command = Button_Cancel_sub2)
   buttCancelSub2.grid(column=0,row=1,pady=5)
   buttCancelSub2.config(width=10) 
 except:
  textNumF.delete(0,END)
  textNumF.insert(0,"ERROR")
buttNext = Button(root, text = 'Next', command = Button_Next)
buttNext.grid(column=1,row=10,padx=10,pady=25)
buttNext.config(width=15)
  
root.mainloop()