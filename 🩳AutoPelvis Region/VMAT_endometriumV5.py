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
root.geometry('400x400')

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
combo_machine = ['N3_VersaHD', 'N4_VersaHD']
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
combo_Iso = ['Center of Roi', 'Poi(Origin)']
comboIso = ttk.Combobox(root, values = combo_Iso, textvariable= combo_variableIso)
comboIso.grid(column=1,row=5)
comboIso.config(width=27, height =5)

#Combobox for select photon energy
lbPhotonE = Label(root, text= 'Select photon energy')
lbPhotonE.grid(column=0 , row=6)
lbPhotonE.config(width=27, height =2)
combo_variablePhotonE = StringVar()
combo_PhotonE = ['6', '10', '6 FFF', '10 FFF']
comboPhotonE = ttk.Combobox(root, values = combo_PhotonE, textvariable= combo_variablePhotonE)
comboPhotonE.grid(column=1,row=6)
comboPhotonE.config(width=27, height =5)

#For match ROI to optimization
Opt1 = "PTV 45"
Opt2 = "CTV E"
Opt3 = "CTV P"
Opt4 = "Bladder"
Opt5 = "Rectum"
Opt6 = "Sigmoid"
Opt7 = "Small bowel"
Opt8 = "BODY"
def Button_MatchRoi():
 Sub_root1 = Toplevel()
 Sub_root1.title('Match Roi')
 Sub_root1.geometry('320x350')
 ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
 #Match PTV45
 lbMatchRoi1 = Label(Sub_root1, text= 'PTV 45')
 lbMatchRoi1.grid(column=0 , row=0)
 lbMatchRoi1.config(width=15, height =2)
 if "PTV 45" in ListRoi:
  lbMatchRoiOpt1 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt1.grid(column=1 , row=0)
  lbMatchRoiOpt1.config(width=27, height =2)
 else:
  combo_Opt1 = StringVar()
  comboOpt1 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt1)
  comboOpt1.grid(column=1,row=0)
  comboOpt1.config(width=27, height =20)
 #Match CTV E
 lbMatchRoi2 = Label(Sub_root1, text= 'CTV E')
 lbMatchRoi2.grid(column=0 , row=1)
 lbMatchRoi2.config(width=15, height =2)
 if "CTV E" in ListRoi:
  lbMatchRoiOpt2 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt2.grid(column=1 , row=1)
  lbMatchRoiOpt2.config(width=27, height =2)
 else:
  combo_Opt2 = StringVar()
  comboOpt2 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt2)
  comboOpt2.grid(column=1,row=1)
  comboOpt2.config(width=27, height =20)
 #Match CTV P
 lbMatchRoi3 = Label(Sub_root1, text= 'CTV P')
 lbMatchRoi3.grid(column=0 , row=2)
 lbMatchRoi3.config(width=15, height =2)
 if "CTV P" in ListRoi:
  lbMatchRoiOpt3 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt3.grid(column=1 , row=2)
  lbMatchRoiOpt3.config(width=27, height =2)
 else:
  combo_Opt3 = StringVar()
  comboOpt3 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt3)
  comboOpt3.grid(column=1,row=2)
  comboOpt3.config(width=27, height =20) 
 #Match Bladder
 lbMatchRoi4 = Label(Sub_root1, text= 'Bladder')
 lbMatchRoi4.grid(column=0 , row=3)
 lbMatchRoi4.config(width=15, height =2)
 if "Bladder" in ListRoi:
  lbMatchRoiOpt4 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt4.grid(column=1 , row=3)
  lbMatchRoiOpt4.config(width=27, height =2)
 else:
  combo_Opt4 = StringVar()
  comboOpt4 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt4)
  comboOpt4.grid(column=1,row=3)
  comboOpt4.config(width=27, height =20)
 #Match Rectum
 lbMatchRoi5 = Label(Sub_root1, text= 'Rectum')
 lbMatchRoi5.grid(column=0 , row=4)
 lbMatchRoi5.config(width=15, height =2)
 if "Rectum" in ListRoi:
  lbMatchRoiOpt5 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt5.grid(column=1 , row=4)
  lbMatchRoiOpt5.config(width=27, height =2)
 else:
  combo_Opt5 = StringVar()
  comboOpt5 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt5)
  comboOpt5.grid(column=1,row=4)
  comboOpt5.config(width=27, height =20)
 #Match Sigmoid
 lbMatchRoi6 = Label(Sub_root1, text= 'Sigmoid')
 lbMatchRoi6.grid(column=0 , row=5)
 lbMatchRoi6.config(width=15, height =2)
 if "Sigmoid" in ListRoi:
  lbMatchRoiOpt6 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt6.grid(column=1 , row=5)
  lbMatchRoiOpt6.config(width=27, height =2)
 else:
  combo_Opt6 = StringVar()
  comboOpt6 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt6)
  comboOpt6.grid(column=1,row=5)
  comboOpt6.config(width=27, height =20)
 #Match Small bowel
 lbMatchRoi7 = Label(Sub_root1, text= 'Small Bowel')
 lbMatchRoi7.grid(column=0 , row=6)
 lbMatchRoi7.config(width=15, height =2)
 if "Small Bowel" in ListRoi:
  lbMatchRoiOpt7 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt7.grid(column=1 , row=6)
  lbMatchRoiOpt7.config(width=27, height =2)
 else:
  combo_Opt7 = StringVar()
  comboOpt7 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt7)
  comboOpt7.grid(column=1,row=6)
  comboOpt7.config(width=27, height =20)
 #Match Body
 lbMatchRoi8 = Label(Sub_root1, text= 'BODY')
 lbMatchRoi8.grid(column=0 , row=7)
 lbMatchRoi8.config(width=15, height =2)
 if "BODY" in ListRoi:
  lbMatchRoiOpt8 = Label(Sub_root1, text= 'Matched')
  lbMatchRoiOpt8.grid(column=1 , row=7)
  lbMatchRoiOpt8.config(width=27, height =2)
 else:
  combo_Opt8 = StringVar()
  comboOpt8 = ttk.Combobox(Sub_root1, values = ListRoi, textvariable= combo_Opt8)
  comboOpt8.grid(column=1,row=7)
  comboOpt8.config(width=27, height =20)
 #Cancel Button in Sub_root1
 def Button_Cancel_sub1():
  Sub_root1.destroy()
 buttCancelSub1 = Button(Sub_root1 , text = 'Cancel', command = Button_Cancel_sub1)
 buttCancelSub1.grid(column=0,row=8,pady=15)
 buttCancelSub1.config(width=10)
 #Apply Button in Sub_root1
 def Button_Apply_sub1():
  global Opt1  
  global Opt2
  global Opt3  
  global Opt4  
  global Opt5  
  global Opt6 
  global Opt7  
  global Opt8  
  if "PTV 45" in ListRoi:
   Opt1 = "PTV 45"
  else:
   Opt1 = combo_Opt1.get()
  if "CTV E" in ListRoi:
   Opt2 = "CTV E"
  else:
   Opt2 = combo_Opt2.get()
  if "CTV P" in ListRoi:
   Opt3 = "CTV P"
  else:
   Opt3 = combo_Opt3.get()

  if "Bladder" in ListRoi:
   Opt4 = "Bladder"
  else:
   Opt4 = combo_Opt4.get()
  if "Rectum" in ListRoi:
   Opt5 = "Rectum"
  else:
   Opt5 = combo_Opt5.get()
  if "Sigmoid" in ListRoi:
   Opt6 = "Sigmoid"
  else:
   Opt6 = combo_Opt6.get()
  if "Small Bowel" in ListRoi:
   Opt7 = "Small Bowel"
  else:
   Opt7 = combo_Opt7.get()
  if "BODY" in ListRoi:
   Opt8 = "BODY"
  else:
   Opt8 = combo_Opt8.get()
  Sub_root1.destroy()
 buttApplySub1 = Button(Sub_root1 , text = 'Apply', command = Button_Apply_sub1)
 buttApplySub1.grid(column=1,row=8,pady=15)
 buttApplySub1.config(width=10)
 
lbMatchRoi = Label(root, text= 'Check Roi')
lbMatchRoi.grid(column=0 , row=7)
lbMatchRoi.config(width=27, height =2)
ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListRoiOpt = ["PTV 45","CTV E","CTV P","Bladder","Rectum","Sigmoid","Small bowel","BODY"]
print(ListRoi)
for roi in ListRoiOpt:
 if roi in ListRoi:
  
  lbMatchRoi2 = Label(root, text= 'Already match roi')
  lbMatchRoi2.grid(column=1 , row=7)
  lbMatchRoi2.config(width=27, height =2)
  continue
 else:
  buttMatch = Button(root, text = 'Match ROI', command = Button_MatchRoi)
  buttMatch.grid(column=1,row=7,padx=10,pady=5)
  buttMatch.config(width=15)
  break

#Cancel Button
def Button_Cancel():
 root.destroy()
buttCancel = Button(root, text = 'Cancel', command = Button_Cancel)
buttCancel.grid(column=0,row=8,padx=10,pady=25)
buttCancel.config(width=15)  

#Add cost fuction for optimization
def AddCostFucn():
 plan = get_current("Plan")
 Po = plan.PlanOptimizations[0]
 DosePrescription = float(TotalDose_Gy.get()) * 100
 with CompositeAction('Add optimization function'):
   AddCostFunc0 = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName=Opt1) #PTV45
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.00445)
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.Weight = 300
 with CompositeAction('Add optimization function'):
   AddCostFunc1 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt1) #PTV45
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.0556)
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.Weight = 400
 with CompositeAction('Add optimization function'):
   AddCostFunc2 = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=Opt2) #CTV E
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.00445)
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.Weight = 800
 with CompositeAction('Add optimization function'):
   AddCostFunc3 = Po.AddOptimizationFunction(FunctionType="MinDose", RoiName=Opt3) #CTV P
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.00445)
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.Weight = 800
#optimized Bladder
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc4 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt4) 
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.02778)
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.Weight = 10
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc5 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt4) 
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.77778)
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[5].DoseFunctionParameters.Weight = 10  
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc6 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt4) 
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.44445)
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.LowDoseDistance = 2.5
   Po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 20 
 with CompositeAction('Add optimization function Bladder'):
   AddCostFunc7 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt4)
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.26667)
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.LowDoseDistance = 6
   Po.Objective.ConstituentFunctions[7].DoseFunctionParameters.Weight = 10
#optimized Rectum
 with CompositeAction('Add optimization function Rectum'):
   AddCostFunc8 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5) 
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.77778)
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.LowDoseDistance = 0.6
   Po.Objective.ConstituentFunctions[8].DoseFunctionParameters.Weight = 10 
 with CompositeAction('Add optimization function Rectum'):
   AddCostFunc9 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.44445)
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.LowDoseDistance = 1.2
   Po.Objective.ConstituentFunctions[9].DoseFunctionParameters.Weight = 30
 with CompositeAction('Add optimization function Rectum'):
   AddCostFunc10 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt5)
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.02778)
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.Weight = 50 
#optimized Small Bowel
 with CompositeAction('Add optimization function'):
   AddCostFunc11 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.02778)
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.Weight = 50 
 with CompositeAction('Add optimization function'):
   AddCostFunc12 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.77778)
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[12].DoseFunctionParameters.Weight = 10 
 with CompositeAction('Add optimization function'):
   AddCostFunc13 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt6)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.55556)
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.LowDoseDistance = 2.5
   Po.Objective.ConstituentFunctions[13].DoseFunctionParameters.Weight = 10 
#optimized BODY
 with CompositeAction('Add optimization function'):
   AddCostFunc14 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.77778)
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[14].DoseFunctionParameters.Weight = 10 
 with CompositeAction('Add optimization function'):
   AddCostFunc15 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.55556)
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.LowDoseDistance = 2.5
   Po.Objective.ConstituentFunctions[15].DoseFunctionParameters.Weight = 20 
 with CompositeAction('Add optimization function'):
   AddCostFunc16 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.26667)
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.LowDoseDistance = 3.5
   Po.Objective.ConstituentFunctions[16].DoseFunctionParameters.Weight = 20 
 with CompositeAction('Add optimization function'):
   AddCostFunc17 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt7)
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.02778)
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.Weight = 50 
 with CompositeAction('Add optimization function'): 
   AddCostFunc18 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName=Opt8)
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.05556)
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[18].DoseFunctionParameters.Weight = 300 
 with CompositeAction('Add optimization function'): 
   AddCostFunc19 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt8)
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.88889)
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[19].DoseFunctionParameters.Weight = 10 
 with CompositeAction('Add optimization function'):
   AddCostFunc20 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt8)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.5)
   Po.Objective.ConstituentFunctions[20].DoseFunctionParameters.LowDoseDistance = 1.5 
 with CompositeAction('Add optimization function'):
   AddCostFunc21 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt8)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.95556)
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.LowDoseDistance = 0.3
   Po.Objective.ConstituentFunctions[21].DoseFunctionParameters.Weight = 30
 with CompositeAction('Add optimization function'):
   AddCostFunc22 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z RingPTV")
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.88889)
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.LowDoseDistance = 0.3
   Po.Objective.ConstituentFunctions[22].DoseFunctionParameters.Weight = 5
 with CompositeAction('Add optimization function'):
   AddCostFunc23 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z RingPTV")
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.DoseLevel = int(DosePrescription*0.98889)
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[23].DoseFunctionParameters.Weight = 200
 with CompositeAction('Add optimization function'):
   AddCostFunc24 = Po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="z PTV+Organ")
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.04)
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.PercentVolume = 98
   Po.Objective.ConstituentFunctions[24].DoseFunctionParameters.Weight = 100
 with CompositeAction('Add optimization function'):
   AddCostFunc25 = Po.AddOptimizationFunction(FunctionType="MinDvh", RoiName="z PTV+Organ")
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.00445)
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.PercentVolume = 95
   Po.Objective.ConstituentFunctions[25].DoseFunctionParameters.Weight = 200
 with CompositeAction('Add optimization function'):
   AddCostFunc26 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Ant")
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.HighDoseLevel = int(DosePrescription*0.82223)
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.27778)
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.LowDoseDistance = 2.0
   Po.Objective.ConstituentFunctions[26].DoseFunctionParameters.Weight = 10
 with CompositeAction('Add optimization function Rectum'):
   AddCostFunc9 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=Opt5)
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.HighDoseLevel = int(DosePrescription)
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.33334)
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.LowDoseDistance = 2.0
   Po.Objective.ConstituentFunctions[27].DoseFunctionParameters.Weight = 30
 with CompositeAction('Add optimization function z Bladder'):
   AddCostFunc28 = Po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="z Bladder")
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.HighDoseLevel = int(DosePrescription*0.62222)
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.LowDoseLevel = int(DosePrescription*0.4)
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.LowDoseDistance = 1.5
   Po.Objective.ConstituentFunctions[28].DoseFunctionParameters.Weight = 10
   
def create_contour_from_dose(dose, dose_level):
	roi = case.PatientModel.CreateRoi(Name=f"z Dose_{dose_level}%", Color="Yellow", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	beamset = get_current('BeamSet')
	threshold_level = beamset.Prescription.PrimaryPrescriptionDoseReference.DoseValue * (dose_level/100)
	roi.CreateRoiGeometryFromDose(DoseDistribution = dose, ThresholdLevel = threshold_level)
	print("Create D105%")
 
def add_105constrain(Name,DosePrescription):
	plan = get_current("Plan")
	Po = plan.PlanOptimizations[0]
	print("Adding optimization function to D105%")
	with CompositeAction('Add optimization function'):
		AddCostFunc29 = Po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=Name)
		Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.DoseLevel = int(DosePrescription*1.045)
		Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.PercentVolume = 1
		Po.Objective.ConstituentFunctions[29].DoseFunctionParameters.Weight = 500
	print("Add optimization done!")
            
#Next Button
def Button_Next():
 try:
  current = float(NumF.get())
  try:
   current = float(TotalDose_Gy.get())
   if examination.Name == 'CT Plan':
    print('CT name is CT Plan already')
   else:
    examination.Name = 'CT Plan'
   get_CT_Curve()
   #Creat virtual organ : z Ant
   VirtualAnt = case.PatientModel.CreateRoi(Name="z Ant", Color="Yellow", Type="Control",
              TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
              ExpressionA={ 'Operation': "Union", 'SourceRoiNames': 
              [Opt6, Opt4, Opt7], 'MarginSettings': 
              { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
              'Anterior': 6, 'Posterior': 0, 'Right': 3, 'Left': 3 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Opt1], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 1,
              'Inferior': 1, 'Anterior': 1, 'Posterior': 2, 'Right': 2, 'Left': 2 } }, 
              ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 
              'Superior': 0,'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 3, 'Left': 3 })
   VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 
              'SourceRoiNames': [Opt8, "z Ant"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 
              'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
              ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Opt1], 
              'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 'Anterior': 1.5, 
              'Posterior': 10, 'Right': 1.5, 'Left': 1.5 } }, ResultOperation="Subtraction", 
              ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 
              'Posterior': 0, 'Right': 0, 'Left': 0 })
   #Creat virtual organ : z RingPTV
   VirtualRing = case.PatientModel.CreateRoi(Name="z RingPTV", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualRing.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
              'SourceRoiNames': [Opt1], 'MarginSettings': { 'Type': "Expand", 'Superior': 2, 'Inferior': 2, 
              'Anterior': 2, 'Posterior': 2, 'Right': 2, 'Left': 2 } }, ExpressionB={ 'Operation': "Union", 
              'SourceRoiNames': [Opt1], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 
              'Anterior': 1, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", 
              ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 
              'Right': 0, 'Left': 0 })
     #Creat virtual organ : z Bladder
   VirtualBladder = case.PatientModel.CreateRoi(Name="z Bladder", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualBladder.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [Opt4], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 5, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, 
            ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Opt1], 'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
            'Anterior': 1.5, 'Posterior': 1, 'Right': 1.5, 'Left': 1.5 } }, ResultOperation="Subtraction", 
            ResultMarginSettings={ 'Type': "Contract", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0.7, 'Left': 0.7 })

     #Creat virtual organ : z PTV+Organ
   VirtualPtvOrgan = case.PatientModel.CreateRoi(Name="z PTV+Organ", Color="White", Type="Control", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
   VirtualPtvOrgan.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 
            'SourceRoiNames': [Opt6, Opt4, Opt5, Opt7], 
            'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 
            'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 
            'SourceRoiNames': [Opt1], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
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
   TotalDose = float(TotalDose_Gy.get()) * 100
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
   DosePrescription = float(TotalDose_Gy.get()) * 100
   for o in range(1,6):
    MinCtvE = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=Opt2, DoseValues=[int(DosePrescription)])
    MinCtvP = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=Opt3, DoseValues=[int(DosePrescription)])
    MinDvhPtv = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt1, RelativeVolumes=[0.95])
    MaxPtv = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt1, RelativeVolumes=[0])
    MaxBladder = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt4, RelativeVolumes=[0])
    MaxRectum = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt5, RelativeVolumes=[0])
    MaxSigmoid = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt6, RelativeVolumes=[0])
    MaxSmallBowel = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=Opt7, RelativeVolumes=[0])
    if MinCtvE[0] < 0.999951:
     Po.Objective.ConstituentFunctions[2].DoseFunctionParameters.Weight = 800*(2**o)
    if MinCtvP[0] < 0.999951:
     Po.Objective.ConstituentFunctions[3].DoseFunctionParameters.Weight = 800*(2**o)
    if MinDvhPtv[0] < int(DosePrescription):
     Po.Objective.ConstituentFunctions[0].DoseFunctionParameters.Weight = 300*(2**o)
    if MaxPtv > int(DosePrescription)*1.085:
     Po.Objective.ConstituentFunctions[1].DoseFunctionParameters.Weight = 400+(200*o)
    if MaxBladder[0] > int(DosePrescription)*1.046:
     Po.Objective.ConstituentFunctions[4].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxRectum[0] > int(DosePrescription)*1.046:
     Po.Objective.ConstituentFunctions[10].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSigmoid[0] > int(DosePrescription)*1.046:
     Po.Objective.ConstituentFunctions[11].DoseFunctionParameters.Weight = 50+(10*(2**o))
    if MaxSmallBowel[0] > int(DosePrescription)*1.046:
     Po.Objective.ConstituentFunctions[17].DoseFunctionParameters.Weight = 50+(10*(2**o))
    
    if MinCtvE[0] < 0.999951 or MinCtvP[0] < 0.999951 or MinDvhPtv[0] < int(DosePrescription) or MaxBladder[0] > int(DosePrescription)*1.046 or MaxRectum[0] > int(DosePrescription)*1.046 or MaxSigmoid[0] > int(DosePrescription)*1.046 or MaxSmallBowel[0] > int(DosePrescription)*1.046:
    	## Run optimize
    	Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
    
   ## Check Dose 105% area
   dose105 = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=Opt1, DoseValues=[int(DosePrescription)*1.05])
   if dose105 > 0.05:
   	## Covert 105% to contour
   	create_contour_from_dose(plan.TreatmentCourse.TotalDose, 105)
   	add_105constrain("z Dose_105%",DosePrescription)
   	Po.RunOptimization(ScalingOfSoftMachineConstraints=None)
        
   root.destroy()
  except:
   textTotalDose.delete(0,END)
   textTotalDose.insert(0,"ERROR")
 except:
  textNumF.delete(0,END)
  textNumF.insert(0,"ERROR")
buttNext = Button(root, text = 'Next', command = Button_Next)
buttNext.grid(column=1,row=8,padx=10,pady=25)
buttNext.config(width=15)
  
root.mainloop()