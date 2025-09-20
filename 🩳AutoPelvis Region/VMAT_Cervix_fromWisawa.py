from connect import *
from tkinter import *
from tkinter import ttk

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")


#import Couch
#case.PatientModel.CreateStructuresFromTemplate(SourceTemplate=db.TemplatePatientModels['N3,N4 VersaHD couch'], SourceExaminationName="CT 1", SourceRoiNames=["Foam Core", "Surface couch"], SourcePoiNames=["Origin"], AssociateStructuresByName=True, TargetExamination=examination, InitializationOption="AlignImageCenters")

#case.PatientModel.CreateStructuresFromTemplate(SourceTemplate=patient_db.LoadTemplatePatientModel(templateName = 'N3,N4 VersaHD couch', lockMode = 'Read'|'Write'|None,)# AssociateStructuresByName=True, TargetExamination=examination, InitializationOption="AlignImageCenters")

root = Tk()
root.title('Plan design')
root.geometry('400x450')

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
except:
 combo_variableCT = StringVar()
 combo_CT = ['HOST-768005', 'CTAWP100076']
 comboMac = ttk.Combobox(root, values = combo_CT, textvariable= combo_variableCT)
 comboMac.grid(column=1,row=0)
 comboMac.config(width=27, height =2)
def get_CT_Curve():
 CT_Curve=examination.EquipmentInfo.ImagingSystemReference
 if CT_Curve.ImagingSystemName == "CTAWP100076":
  print('Use CT3')
 elif CT_Curve.ImagingSystemName == "HOST-768005":
  print('Use CT1')
 else:
  Select_CT = combo_variableCT.get()
  if Select_CT == "Siemens 120kVp":
   CT_Curve.ImagingSystemName = "Siemens 120kVp"
  elif Select_CT == "Philips RT Big Bore 120kV":
   CT_Curve.ImagingSystemName = "Philips RT Big Bore 120kV"

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
textNumF.insert(0,"25")

#textbox for insert Dose prescription
lbTotalDose1 = Label(root, text= 'Fill Total dose1 (Gy)')
lbTotalDose1.grid(column=0 ,row=3)
lbTotalDose1.config(width=27, height =2)
TotalDose1_Gy = StringVar()
textTotalDose1 = Entry(root, textvariable = TotalDose1_Gy)
textTotalDose1.grid(column=1,row=3)
textTotalDose1.config(width=27)
textTotalDose1.insert(0,"45")
lbTotalDose2 = Label(root, text= 'Fill Total dose2 (Gy)')
lbTotalDose2.grid(column=0 ,row=4)
lbTotalDose2.config(width=27, height =2)
TotalDose2_Gy = StringVar()
textTotalDose2 = Entry(root, textvariable = TotalDose2_Gy)
textTotalDose2.grid(column=1,row=4)
textTotalDose2.config(width=27)
textTotalDose2.insert(0,"55")
lbTotalDose3 = Label(root, text= 'Fill Total dose3 (Gy)')
lbTotalDose3.grid(column=0 ,row=5)
lbTotalDose3.config(width=27, height =2)
TotalDose3_Gy = StringVar()
textTotalDose3 = Entry(root, textvariable = TotalDose3_Gy)
textTotalDose3.grid(column=1,row=5)
textTotalDose3.config(width=27)
textTotalDose3.insert(0,"57.5")

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
OptPTV45 = "PTV 45"
OptCTVE = "CTV E"
OptCTVP = "CTV P"
OptPTV55 = "PTV 55"
OptCTV55 = "CTV 55"
OptPTV575 = "PTV 57.5"
OptCTV575 = "CTV 57.5"
OptBladder = "Bladder"
OptRectum = "Rectum"
OptSigmoid = "Sigmoid"
OptSmallBowel = "Small bowel"
OptKidneyLRt = "Kidney Lt"
OptKidneyLt = "Kidney Rt"
OptBODY = "BODY"
def Button_MatchRoi():
 Sub_root1 = Toplevel()
 Sub_root1.title('Match Roi')
 Sub_root1.geometry('320x570')
 ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
 #Match PTV45
 lbMatchRoi1 = Label(Sub_root1, text= 'PTV 45')
 lbMatchRoi1.grid(column=0 , row=0)
 lbMatchRoi1.config(width=15, height =2)
 if "PTV 45" in ListRoi:
  lbMatchRoiOptPTV45 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptPTV45.grid(column=1 , row=0)
  lbMatchRoiOptPTV45.config(width=27, height =2)
 else:
  combo_OptPTV45 = StringVar()
  comboOptPTV45 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptPTV45)
  comboOptPTV45.grid(column=1,row=0)
  comboOptPTV45.config(width=27, height =20)
 #Match CTV E
 lbMatchRoi2 = Label(Sub_root1, text= 'CTV E')
 lbMatchRoi2.grid(column=0 , row=1)
 lbMatchRoi2.config(width=15, height =2)
 if "CTV E" in ListRoi:
  lbMatchRoiOptCTVE = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptCTVE.grid(column=1 , row=1)
  lbMatchRoiOptCTVE.config(width=27, height =2)
 else:
  combo_OptCTVE = StringVar()
  comboOptCTVE = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptCTVE)
  comboOptCTVE.grid(column=1,row=1)
  comboOptCTVE.config(width=27, height =20)
 #Match CTV P
 lbMatchRoi3 = Label(Sub_root1, text= 'CTV P')
 lbMatchRoi3.grid(column=0 , row=2)
 lbMatchRoi3.config(width=15, height =2)
 if "CTV P" in ListRoi:
  lbMatchRoiOptCTVP = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptCTVP.grid(column=1 , row=2)
  lbMatchRoiOptCTVP.config(width=27, height =2)
 else:
  combo_OptCTVP = StringVar()
  comboOptCTVP = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptCTVP)
  comboOptCTVP.grid(column=1,row=2)
  comboOptCTVP.config(width=27, height =20) 
 #Match PTV 55
 lbMatchRoi4 = Label(Sub_root1, text= 'PTV 55')
 lbMatchRoi4.grid(column=0 , row=3)
 lbMatchRoi4.config(width=15, height =2)
 if "PTV 55" in ListRoi:
  lbMatchRoiOptPTV55 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptPTV55.grid(column=1 , row=3)
  lbMatchRoiOptPTV55.config(width=27, height =2)
 else:
  combo_OptPTV55 = StringVar()
  comboOptPTV55 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptPTV55)
  comboOptPTV55.grid(column=1,row=3)
  comboOptPTV55.config(width=27, height =20)
 #Match CTV 55
 lbMatchRoi5 = Label(Sub_root1, text= 'CTV 55')
 lbMatchRoi5.grid(column=0 , row=4)
 lbMatchRoi5.config(width=15, height =2)
 if "CTV 55" in ListRoi:
  lbMatchRoiOptCTV55 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptCTV55.grid(column=1 , row=4)
  lbMatchRoiOptCTV55.config(width=27, height =2)
 else:
  combo_OptCTV55 = StringVar()
  comboOptCTV55 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptCTV55)
  comboOptCTV55.grid(column=1,row=4)
  comboOptCTV55.config(width=27, height =20)  
 #Match PTV 57.5
 lbMatchRoi6 = Label(Sub_root1, text= 'PTV 57.5')
 lbMatchRoi6.grid(column=0 , row=5)
 lbMatchRoi6.config(width=15, height =2)
 if "PTV 57.5" in ListRoi:
  lbMatchRoiOptPTV575 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptPTV575.grid(column=1 , row=5)
  lbMatchRoiOptPTV575.config(width=27, height =2)
 else:
  combo_OptPTV575 = StringVar()
  comboOptPTV575 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptPTV575)
  comboOptPTV575.grid(column=1,row=5)
  comboOptPTV575.config(width=27, height =20)
 #Match CTV 57.5
 lbMatchRoi7 = Label(Sub_root1, text= 'CTV 57.5')
 lbMatchRoi7.grid(column=0 , row=6)
 lbMatchRoi7.config(width=15, height =2)
 if "CTV 57.5" in ListRoi:
  lbMatchRoiOptCTV575 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptCTV575.grid(column=1 , row=6)
  lbMatchRoiOptCTV575.config(width=27, height =2)
 else:
  combo_OptCTV575 = StringVar()
  comboOptCTV575 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptCTV575)
  comboOptCTV575.grid(column=1,row=6)
  comboOptCTV575.config(width=27, height =20) 
 #Match Bladder
 lbMatchRoi8 = Label(Sub_root1, text= 'Bladder')
 lbMatchRoi8.grid(column=0 , row=7)
 lbMatchRoi8.config(width=15, height =2)
 if "Bladder" in ListRoi:
  lbMatchRoiOptBladder = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptBladder.grid(column=1 , row=7)
  lbMatchRoiOptBladder.config(width=27, height =2)
 else:
  combo_OptBladder = StringVar()
  comboOptBladder = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptBladder)
  comboOptBladder.grid(column=1,row=7)
  comboOptBladder.config(width=27, height =20)
 #Match Rectum
 lbMatchRoi9 = Label(Sub_root1, text= 'Rectum')
 lbMatchRoi9.grid(column=0 , row=8)
 lbMatchRoi9.config(width=15, height =2)
 if "Rectum" in ListRoi:
  lbMatchRoiOptRectum = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptRectum.grid(column=1 , row=8)
  lbMatchRoiOptRectum.config(width=27, height =2)
 else:
  combo_OptRectum = StringVar()
  comboOptRectum = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptRectum)
  comboOptRectum.grid(column=1,row=8)
  comboOptRectum.config(width=27, height =20)
 #Match Sigmoid
 lbMatchRoi10 = Label(Sub_root1, text= 'Sigmoid')
 lbMatchRoi10.grid(column=0 , row=9)
 lbMatchRoi10.config(width=15, height =2)
 if "Sigmoid" in ListRoi:
  lbMatchRoiOptSigmoid = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptSigmoid.grid(column=1 , row=9)
  lbMatchRoiOptSigmoid.config(width=27, height =2)
 else:
  combo_OptSigmoid = StringVar()
  comboOptSigmoid = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptSigmoid)
  comboOptSigmoid.grid(column=1,row=9)
  comboOptSigmoid.config(width=27, height =20)
 #Match Small bowel
 lbMatchRoi11 = Label(Sub_root1, text= 'Small Bowel')
 lbMatchRoi11.grid(column=0 , row=10)
 lbMatchRoi11.config(width=15, height =2)
 if "Small Bowel" in ListRoi:
  lbMatchRoiOptSmallBowel = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptSmallBowel.grid(column=1 , row=10)
  lbMatchRoiOptSmallBowel.config(width=27, height =2)
 else:
  combo_OptSmallBowel = StringVar()
  comboOptSmallBowel = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptSmallBowel)
  comboOptSmallBowel.grid(column=1,row=10)
  comboOptSmallBowel.config(width=27, height =20)
 #Match Kidney Lt
 lbMatchRoi12 = Label(Sub_root1, text= 'Kidney Lt')
 lbMatchRoi12.grid(column=0 , row=11)
 lbMatchRoi12.config(width=15, height =2)
 if "Kidney Lt" in ListRoi:
  lbMatchRoiOptKidneyLRt = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptKidneyLRt.grid(column=1 , row=11)
  lbMatchRoiOptKidneyLRt.config(width=27, height =2)
 else:
  combo_OptKidneyLRt = StringVar()
  comboOptKidneyLRt = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptKidneyLRt)
  comboOptKidneyLRt.grid(column=1,row=11)
  comboOptKidneyLRt.config(width=27, height =20)
 #Match Kidney Rt
 lbMatchRoi13 = Label(Sub_root1, text= 'Kidney Rt')
 lbMatchRoi13.grid(column=0 , row=12)
 lbMatchRoi13.config(width=15, height =2)
 if "Kidney Rt" in ListRoi:
  lbMatchRoiOptKidneyLt = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptKidneyLt.grid(column=1 , row=12)
  lbMatchRoiOptKidneyLt.config(width=27, height =2)
 else:
  combo_OptKidneyLt = StringVar()
  comboOptKidneyLt = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptKidneyLt)
  comboOptKidneyLt.grid(column=1,row=12)
  comboOptKidneyLt.config(width=27, height =20)   
 #Match Body
 lbMatchRoi14 = Label(Sub_root1, text= 'BODY')
 lbMatchRoi14.grid(column=0 , row=13)
 lbMatchRoi14.config(width=15, height =2)
 if "BODY" in ListRoi:
  lbMatchRoiOptBODY = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOptBODY.grid(column=1 , row=13)
  lbMatchRoiOptBODY.config(width=27, height =2)
 else:
  combo_OptBODY = StringVar()
  comboOptBODY = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_OptBODY)
  comboOptBODY.grid(column=1,row=13)
  comboOptBODY.config(width=27, height =20)
 #Cancel Button in Sub_root1
 def Button_Cancel_sub1():
  Sub_root1.destroy()
 buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
 buttCancelSub1.grid(column=0,row=14,pady=15)
 buttCancelSub1.config(width=10)
 #Apply Button in Sub_root1
 def Button_Apply_sub1():
  global OptPTV45  #PTV 45
  global OptCTVE  #CTV E
  global OptCTVP  #CTV P
  global OptPTV55  #PTV 55
  global OptCTV55  #CTV 55
  global OptPTV575  #PTV 57.5
  global OptCTV575  #CTV 57.5
  global OptBladder  #Bladder
  global OptRectum  #Rectum
  global OptSigmoid #Sigmoid
  global OptSmallBowel #Small bowel
  global OptKidneyLRt #Kidney Lt
  global OptKidneyLt #Kidney Rt
  global OptBODY #BODY

  if "PTV 45" in ListRoi:
   OptPTV45 = "PTV 45"
  else:
   OptPTV45 = combo_OptPTV45.get()
  if "CTV E" in ListRoi:
   OptCTVE = "CTV E"
  else:
   OptCTVE = combo_OptCTVE.get()
  if "CTV P" in ListRoi:
   OptCTVP = "CTV P"
  else:
   OptCTVP = combo_OptCTVP.get()
  if "PTV 55" in ListRoi:
   OptPTV55 = "PTV 55"
  else:
   OptPTV55 = combo_OptPTV55.get()
  if "CTV 55" in ListRoi:
   OptCTV55 = "CTV 55"
  else:
   OptCTV55 = combo_OptCTV55.get()
  if "PTV 57.5" in ListRoi:
   OptPTV575 = "PTV 57.5"
  else:
   OptPTV575 = combo_OptPTV575.get()
  if "CTV 57.5" in ListRoi:
   OptCTV575 = "CTV 57.5"
  else:
   OptCTV575 = combo_OptCTV575.get()
  if "Bladder" in ListRoi:
   OptBladder = "Bladder"
  else:
   OptBladder = combo_OptBladder.get()
  if "Rectum" in ListRoi:
   OptRectum = "Rectum"
  else:
   OptRectum = combo_OptRectum.get()
  if "Sigmoid" in ListRoi:
   OptSigmoid = "Sigmoid"
  else:
   OptSigmoid = combo_OptSigmoid.get()
  if "Small Bowel" in ListRoi:
   OptSmallBowel = "Small Bowel"
  else:
   OptSmallBowel = combo_OptSmallBowel.get()
  if "Kidney Lt" in ListRoi:
   OptKidneyLRt = "Kidney Lt"
  else:
   OptKidneyLRt = combo_OptKidneyLRt.get()
  if "Kidney Rt" in ListRoi:
   OptKidneyLt = "Kidney Rt"
  else:
   OptKidneyLt = combo_OptKidneyLt.get()   
  if "BODY" in ListRoi:
   OptBODY = "BODY"
  else:
   OptBODY = combo_OptBODY.get()
  Sub_root1.destroy()
 buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
 buttApplySub1.grid(column=1,row=14,pady=15)
 buttApplySub1.config(width=10)
 
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=9)
lbMatchRoi.config(width=27, height =2)
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = ["PTV 45","CTV E","CTV P","PTV 55","CTV 55","PTV 57.5","CTV 57.5","Bladder","Rectum","Sigmoid","Small bowel","Kidney Lt","Kidney Rt","BODY"]
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

#Next Button
def Button_Next():
 try:
  current = float(NumF.get())
  try:
   current = float(TotalDose1_Gy.get())
   if examination.Name == 'CT Plan':
    print('CT name is CT Plan already')
   else:
    examination.Name = 'CT Plan'
   get_CT_Curve()
   ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
   #Creat virtual Target: z PTV45
   with CompositeAction('ROI algebra (z PTV45)'):
    if "z PTV45" in ListRoi:
     print("Already have z PTV45")
    else:
     VirtualPTV45 = case.PatientModel.CreateRoi(Name="z PTV45", Color="Blue", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPTV45.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptPTV45], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV55], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.5,
              'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     VirtualPTV45.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              ["z PTV45"], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV575], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.7,
              'Inferior': 0.7, 'Anterior': 0.7, 'Posterior': 0.7, 'Right': 0.7, 'Left': 0.7 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })           
   #Creat virtual Target: z PTV55
   with CompositeAction('ROI algebra (z PTV55)'):
    if "z PTV55" in ListRoi:
     print("Already have z PTV55")
    else:
     VirtualPTV55 = case.PatientModel.CreateRoi(Name="z PTV55", Color="Blue", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPTV55.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptPTV55], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptBladder, OptRectum, OptSigmoid, OptSmallBowel], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.2,
              'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     VirtualPTV55.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              ["z PTV55"], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptCTV55], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0,
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
   #Creat virtual Target: z PTV55+OARs
   with CompositeAction('ROI algebra (z PTV55+OARs)'):
    if "z PTV55+OARs" in ListRoi:
     print("Already have z PTV55+OARs")
    else:
     VirtualPTV55OARs = case.PatientModel.CreateRoi(Name="z PTV55+OARs", Color="Blue", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPTV55OARs.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptPTV55], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptBladder, OptRectum, OptSigmoid, OptSmallBowel], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.1,
              'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
              ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     VirtualPTV55OARs.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              ["z PTV55+OARs"], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptCTV55], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0,
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })              
   #Creat virtual Target: z PTV57.5
   with CompositeAction('ROI algebra (z PTV57.5)'):
    if "z PTV57.5" in ListRoi:
     print("Already have z PTV57.5")
    else:
     VirtualPTV575 = case.PatientModel.CreateRoi(Name="z PTV57.5", Color="Blue", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPTV575.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptPTV575], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptBladder, OptRectum, OptSigmoid, OptSmallBowel], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.2,
              'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     VirtualPTV575.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              ["z PTV57.5"], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptCTV575], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0,
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
   #Creat virtual Target: z PTV57.5+OARs
   with CompositeAction('ROI algebra (z PTV57.5+OARs)'):
    if "z PTV57.5+OARs" in ListRoi:
     print("Already have z PTV57.5+OARs")
    else:
     VirtualPTV575OARs = case.PatientModel.CreateRoi(Name="z PTV57.5+OARs", Color="Blue", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPTV575OARs.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptPTV575], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptBladder, OptRectum, OptSigmoid, OptSmallBowel], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0.1,
              'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
              ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
     VirtualPTV575OARs.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              ["z PTV57.5+OARs"], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptCTV575], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 0,
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })                 
   #Creat virtual organ : z Ant
   with CompositeAction('ROI algebra (z Ant)'):
    if "z Ant" in ListRoi:
     print("Already have z Ant")
    else:
     VirtualAnt = case.PatientModel.CreateRoi(Name="z Ant", Color="Yellow", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [OptBladder, OptSigmoid, OptSmallBowel], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 6, 'Posterior': 0, 'Right': 3, 'Left': 3 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV45, OptPTV55, OptPTV575], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 1,
              'Inferior': 1, 'Anterior': 1, 'Posterior': 2, 'Right': 2, 'Left': 2 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 3, 'Left': 3 })
     VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 
              'SourceRoiNames': [OptBODY, "z Ant"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV45, OptPTV55, OptPTV575], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 'Anterior': 1.5, 
              'Posterior': 10, 'Right': 1.5, 'Left': 1.5 } }, ResultOperation="Subtraction", 
              ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 
              'Posterior': 0, 'Right': 0, 'Left': 0 })
   #Creat virtual organ : z RingPTV
   with CompositeAction('ROI algebra (z RingPTV)'):
    if "z RingPTV" in ListRoi:
     print("Already have z RingPTV")
    else:
     VirtualRing = case.PatientModel.CreateRoi(Name="z RingPTV", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
              'SourceRoiNames': [OptPTV45,OptPTV55,OptPTV575], 'MarginSettings': { 'Type': "Expand", 'Superior': 3, 'Inferior': 3, 
              'Anterior': 3, 'Posterior': 3, 'Right': 3, 'Left': 3 } }, ExpressionB={ 'Operation': "Union", 
              'SourceRoiNames': [OptPTV45,OptPTV55,OptPTV575], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
              'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", 
              ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 
              'Right': 0, 'Left': 0 })
     VirtualRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
              'SourceRoiNames': ["z RingPTV"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 
              'SourceRoiNames': [OptPTV55,OptPTV575], 'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
              'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ResultOperation="Subtraction", 
              ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 
              'Right': 0, 'Left': 0 })
   #Creat virtual organ : z Bladder
   with CompositeAction('ROI algebra (z Bladder)'):
    if "z Bladder" in ListRoi:
     print("Already have z Bladder")
    else:   
     VirtualBladder = case.PatientModel.CreateRoi(Name="z Bladder", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualBladder.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
            'SourceRoiNames': [OptBladder], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 5, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV45,OptPTV55,OptPTV575], 'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
            'Anterior': 1.5, 'Posterior': 1, 'Right': 1.5, 'Left': 1.5 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Contract", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0.7, 'Left': 0.7 })
   #Creat virtual organ : z PTV45+Organ
   with CompositeAction('ROI algebra (z PTV45+Organ)'):
    if "z PTV45+Organ" in ListRoi:
     print("Already have z PTV45+Organ")
    else:   
     VirtualPtv45Organ = case.PatientModel.CreateRoi(Name="z PTV45+Organ", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
     VirtualPtv45Organ.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
            'SourceRoiNames': [OptBladder, OptRectum, OptSigmoid, OptSmallBowel], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 
            'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 
            'SourceRoiNames': ["z PTV45"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
            'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })

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
   TotalDose = float(TotalDose1_Gy.get()) * 100
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
   #Optimizatiob part
   plan = get_current("Plan")
   Po = plan.PlanOptimizations[0]
   DosePrescription1 = float(TotalDose1_Gy.get()) * 100
   DosePrescription2 = float(TotalDose2_Gy.get()) * 100
   DosePrescription3 = float(TotalDose3_Gy.get()) * 100 
   with CompositeAction('Add optimization function'):
    NumPo = 0
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName=OptPTV45) #z PTV45
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMinDvhPTV45 = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV45") #z PTV45
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.0556)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 400
    OptWeightMaxPTV45 = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName="z PTV45") #z PTV45
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.04)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 3
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 400   
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=OptCTVE) #CTV E
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 800
    OptWeightMinCTVE = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=OptCTVP) #CTV P
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 800
    OptWeightMinCTVP = NumPo
   #optimized PTV55
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV55") #z PTV55
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMinDvhPTV55 = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV55+OARs") #z PTV55+OARs
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription2*0.975)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV55") #z PTV55
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.06)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMaxPTV55 = NumPo    
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV55+OARs") #z PTV55+OAR
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription2*0.997)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMaxPTV55OAR = NumPo    
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=OptCTV55) #z CTV55
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription2*1.005)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 100
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 800
    OptWeightMinCTV55 = NumPo 
   #optimized PTV57.5
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV57.5") #z PTV57.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMinDvhPTV575 = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV57.5+OARs") #z PTV57.5+OARs
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*0.975)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV57.5") #z PTV57.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.06)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMaxPTV575 = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV57.5+OARs") #z PTV57.5+OARs
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*0.995)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300
    OptWeightMaxPTV575OAR = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName= OptCTV575) #z CTV57.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.005)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 100
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 800
    OptWeightMinCTV575 = NumPo     
   #optimized Bladder
   with CompositeAction('Add optimization function Bladder'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=OptBladder) 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.02778)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    OptWeightMaxBladder = NumPo
   with CompositeAction('Add optimization function Bladder'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBladder) 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.5217)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function Bladder'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBladder) 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.347)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 3
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 20
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function Bladder'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBladder)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.217)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function z Bladder'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Bladder")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3*0.48)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.26)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 1.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   #optimized Rectum
   with CompositeAction('Add optimization function Rectum'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptRectum) 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.5217)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 0.6
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 30
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
   with CompositeAction('Add optimization function Rectum'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptRectum)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.347)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 1.2
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 30
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function Rectum'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=OptRectum)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.02778)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50
    OptWeightMaxRectum = NumPo
   #optimized Sigmoid
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=OptSigmoid)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.02778)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50
    OptWeightMaxSigmoid = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptSigmoid)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.5217)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 1.2
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptSigmoid)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.347)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
   #optimized Small Bowel
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptSmallBowel)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.5217)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 1.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 10 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptSmallBowel)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription3*0.347)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 20
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptSmallBowel)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(12)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 3.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 20 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True   
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=OptSmallBowel)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.02778)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50 
    OptWeightMaxSmallBowel = NumPo
   #optimized BODY
   with CompositeAction('Add optimization function'): 
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=OptBODY)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription3*1.05556)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 300 
   with CompositeAction('Add optimization function'): 
    NumPo = NumPo+1
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBODY)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(2500)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBODY)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 1.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 20 
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.AdaptToTargetDoseLevels = True    
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptBODY)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription3)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.95556)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 0.3
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 30
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z RingPTV")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(4000)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(3500)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 0.5
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z RingPTV")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*0.98889)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV45+Organ")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.04)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 500
    OptWeightMaxPTV45Organ = NumPo
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV45+Organ")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.00445)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 95
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 200
   with CompositeAction('Add optimization function'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Ant")
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1*0.82223)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.27778)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2.0
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 50
   with CompositeAction('Add optimization function Rectum'):
    NumPo = NumPo+1  
    AddCostFunc = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=OptRectum)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.HighDoseLevel = int(DosePrescription1)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseLevel = int(DosePrescription1*0.33334)
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.LowDoseDistance = 2.0
    Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 30
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   if "z D45+" in ListRoi:
      case.PatientModel.RegionsOfInterest['z D45+'].DeleteRoi()
   roi45 = case.PatientModel.CreateRoi(Name="z D45+", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   beamset = get_current('BeamSet')
   threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
   roi45.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
   roi45.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
       ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [OptPTV45], 
       'MarginSettings': { 'Type': "Contract", 'Superior': 0.1, 'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
       ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["z D45+"],
       'MarginSettings': { 'Type': "Expand", 'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
       ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
       'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
   print("Create D45+")
   with CompositeAction('Add optimization function'):
     NumPo = NumPo+1
     AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z D45+")
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.005)
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 98
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 500
     print("Add optimization done!(D45+)")
   Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   patient.Save()
   plan.SetCurrent()
   beam_set.SetCurrent()
   #loop optimization
   DosePrescription1 = float(TotalDose1_Gy.get()) * 100
   DosePrescription2 = float(TotalDose2_Gy.get()) * 100
   DosePrescription3 = float(TotalDose3_Gy.get()) * 100
   #print(OptWeightMinCTVE,OptWeightMinCTVP,OptWeightMinDvhPTV45,OptWeightMinDvhPTV55,OptWeightMinDvhPTV575,OptWeightMaxPTV45,OptWeightMaxBladder,OptWeightMaxRectum,OptWeightMaxSigmoid,OptWeightMaxSmallBowel,OptWeightMaxPTV45Organ)
   for o in range(1,6):
    MinCtvE = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=OptCTVE, DoseValues=[int(DosePrescription1)])
    MinCtvP = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=OptCTVP, DoseValues=[int(DosePrescription1)])
    MinDvhPtv45 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="z PTV45", DoseValues=[int(DosePrescription1)])
    MaxPtv45 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV45", RelativeVolumes=[0])
    MinDvhPtv55 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="z PTV55", DoseValues=[int(DosePrescription2)])
    MaxPtv55 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV55", RelativeVolumes=[0])
    MaxPtv55OAR = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV55+OARs", RelativeVolumes=[0.05])
    MinCtv55 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=OptCTV55, DoseValues=[int(DosePrescription2)])
    MinDvhPtv575 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="z PTV57.5", DoseValues=[int(DosePrescription3)])
    MaxPtv575 = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV57.5", RelativeVolumes=[0])
    MaxPtv575OAR = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV57.5+OARs", RelativeVolumes=[0])
    MinCtv575 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=OptCTV575, DoseValues=[int(DosePrescription3)])
    MaxBladder = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=OptBladder, RelativeVolumes=[0])
    MaxRectum = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=OptRectum, RelativeVolumes=[0])
    MaxSigmoid = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=OptSigmoid, RelativeVolumes=[0])
    MaxSmallBowel = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=OptSmallBowel, RelativeVolumes=[0])
    MaxPtv45Organ = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName="z PTV45+Organ", RelativeVolumes=[0])
    if MinCtvE[0] < 0.999951:
     Po.Objective.ConstituentFunctions[OptWeightMinCTVE].DoseFunctionParameters.Weight = 800*(2**o)
    if MinCtvP[0] < 0.999951:
     Po.Objective.ConstituentFunctions[OptWeightMinCTVP].DoseFunctionParameters.Weight = 800*(2**o) #OptWeightMinCTV55
    if MinDvhPtv45[0] < 0.95:
     Po.Objective.ConstituentFunctions[OptWeightMinDvhPTV45].DoseFunctionParameters.Weight = 300*(2**o)
    if MinDvhPtv55[0] < 0.95:
     Po.Objective.ConstituentFunctions[OptWeightMinDvhPTV55].DoseFunctionParameters.Weight = 300*(2**o)
    if MaxPtv55[0] < int(DosePrescription2)*1.06:
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV55].DoseFunctionParameters.Weight = 300*(2**o) 
    if MaxPtv55OAR[0] < int(DosePrescription2):
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV55OAR].DoseFunctionParameters.Weight = 300*(2**o)
    if MinCtv55[0] < 0.98:
     Po.Objective.ConstituentFunctions[OptWeightMinCTV55].DoseFunctionParameters.Weight = 800*(2**o)     
    if MinDvhPtv575[0] < 0.95:
     Po.Objective.ConstituentFunctions[OptWeightMinDvhPTV575].DoseFunctionParameters.Weight = 300*(2**o)
    if MaxPtv575[0] < int(DosePrescription3)*1.06:
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV575].DoseFunctionParameters.Weight = 300*(2**o) 
    if MaxPtv575OAR[0] < int(DosePrescription3)*0.995:
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV575OAR].DoseFunctionParameters.Weight = 800*(2**o)
    if MinCtv575[0] < 0.96:
     Po.Objective.ConstituentFunctions[OptWeightMinCTV575].DoseFunctionParameters.Weight = 800*(2**o)     
    if MaxPtv45 > int(DosePrescription1)*1.075:
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV45].DoseFunctionParameters.Weight = 400+(200*o)
    if MaxBladder[0] > int(DosePrescription1)*1.046:
     Po.Objective.ConstituentFunctions[OptWeightMaxBladder].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxRectum[0] > int(DosePrescription1)*1.046:
     Po.Objective.ConstituentFunctions[OptWeightMaxRectum].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSigmoid[0] > int(DosePrescription1)*1.046:
     Po.Objective.ConstituentFunctions[OptWeightMaxSigmoid].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSmallBowel[0] > int(DosePrescription1)*1.046:
     Po.Objective.ConstituentFunctions[OptWeightMaxSmallBowel].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxPtv45Organ[0] > int(DosePrescription1)*1.045:
     Po.Objective.ConstituentFunctions[OptWeightMaxPTV45Organ].DoseFunctionParameters.Weight = 50+(10*(2**o))
    
   
    if MinCtvE[0] < 0.999951 or MinCtvP[0] < 0.999951 or MinDvhPtv45[0] < int(DosePrescription1) or MaxBladder[0] > int(DosePrescription3)*1.046 or MaxRectum[0] > int(DosePrescription3)*1.046 or MaxSigmoid[0] > int(DosePrescription3)*1.046 or MaxSmallBowel[0] > int(DosePrescription3)*1.046:
    	## Run optimize
    	Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
   
   ## Check Dose 105% area
   dose105 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName="z PTV45", DoseValues=[int(DosePrescription1)*1.05])
   if dose105 > 0.05:
    if "z Dose_105%" in ListRoi:
      case.PatientModel.RegionsOfInterest['z Dose_105%'].DeleteRoi()   
    roi = case.PatientModel.CreateRoi(Name="z Dose_105%", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    beamset = get_current('BeamSet')
    threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (105/100)
    roi.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level)
    if "z Dose_105%OAR" in ListRoi:
      case.PatientModel.RegionsOfInterest['z Dose_105%OAR'].DeleteRoi()      
    roi2 = case.PatientModel.CreateRoi(Name="z Dose_105%OAR", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    roi2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
       ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["z Dose_105%"], 
       'MarginSettings': { 'Type': "Expand", 'Superior': 0.1, 'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
       ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptBladder,OptSigmoid,OptSmallBowel,OptRectum],
       'MarginSettings': { 'Type': "Expand", 'Superior': 0.1,'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
       ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 
       'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    roi2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
       ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["z Dose_105%OAR"], 
       'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
       ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV55,OptPTV575],
       'MarginSettings': { 'Type': "Expand", 'Superior': 1,'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } },
       ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
       'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
       ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["z Dose_105%"], 
       'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
       ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [OptPTV55,OptPTV575],
       'MarginSettings': { 'Type': "Expand", 'Superior': 1,'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, 
       ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
       'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    print("Create D105%")
    #Add cost function 105%
    with CompositeAction('Add optimization function'):
     NumPo = NumPo+1
     AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName="z Dose_105%")
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.04)
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 1
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 500
     NumPo = NumPo+1
     AddCostFunc = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z Dose_105%OAR")
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.035)
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 100
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 1000
    if "z D45++" in ListRoi:
      case.PatientModel.RegionsOfInterest['z D45++'].DeleteRoi()      
    roi45_2 = case.PatientModel.CreateRoi(Name="z D45++", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    threshold_level45_2 = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue
    roi45_2.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = threshold_level45_2)
    roi45_2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
       ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [OptCTVE,OptCTVP], 
       'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 'Anterior': 0.3, 'Posterior': 0.3, 'Right': 0.3, 'Left': 0.3 } }, 
       ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["z D45++"],
       'MarginSettings': { 'Type': "Contract", 'Superior': 0.1,'Inferior': 0.1, 'Anterior': 0.1, 'Posterior': 0.1, 'Right': 0.1, 'Left': 0.1 } }, 
       ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
       'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    Po.RunOptimization(ScalingOfSoftMachineConstraints=None)    
    print("Create D45++")       
    with CompositeAction('Add optimization function'):   
     NumPo = NumPo+1    
     AddCostFunc = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName="z D45++")
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.DoseLevel = int(DosePrescription1*1.006)
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.PercentVolume = 100
     Po.Objective.ConstituentFunctions[NumPo].DoseFunctionParameters.Weight = 5000     
     print("Add optimization done!")
    Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
        
   root.destroy()
  except:
   textTotalDose.delete(0,END)
   textTotalDose.insert(0,"ERROR")
 except:
  textNumF.delete(0,END)
  textNumF.insert(0,"ERROR")
buttNext = Button(root, text = 'Next', command = Button_Next)
buttNext.grid(column=1,row=10,padx=10,pady=25)
buttNext.config(width=15)
  
root.mainloop()