from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('Ant')
root.geometry('330x400')

def show_error():
    messagebox.showerror("ERROR", "Sorry, please check execution details")

try:
    patient = get_current('Patient')
except:
    messagebox.showinfo('No patient selected. \nScript terminated')
    exit()

ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
ListTarget = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
ListTarget.insert(0,"--None--")

def lbMatch(root_frame=root,  List = ListRoi, roi = 'ROI', row_n = 0,column_n = 0):
        lbMatchROI = Label(root, text= roi)
        lbMatchROI.grid(column=column_n , row=row_n)
        lbMatchROI.config(width=15, height =2)
        combo_ROI = StringVar()
        comboROI = ttk.Combobox(root, values = ListRoi, textvariable= combo_ROI)
        comboROI.grid(column=column_n+1,row=row_n)
        comboROI.config(width=27, height =20)
        return comboROI
def set_default(comboROI, roi = 'ROI', List = ListRoi, setNone = True):
    if roi in List:
        print('Match')
        comboROI.set(roi)
    else:
        print('not match')
        if setNone:
            comboROI.set('--None--')
        else:
            comboROI.set('**MUST MATCH**')

def lbMatch_and_set(root_frame=root,  List = ListRoi, roi = 'ROI', row_n = 0,column_n = 0, setNone = True):
    comboROIn = lbMatch(root_frame=root,  List = ListRoi, roi = roi, row_n = row_n, column_n= column_n)
    set_default(comboROIn, roi, List, setNone = setNone)
    return comboROIn
        
ptv1 = "PTV 45"
ptv2 = "PTV 55"
ptv3 = "PTV 57.5"
ptv4 = "PTV 60"
ptv5 = "PTV 70"
sigmoid = "Sigmoid"
bladder = "Bladder"
bowel = "Small Bowel"
liver = "Liver"
body = "BODY"
   

combo_ptv1 = lbMatch_and_set(root, ListTarget, roi = ptv1, row_n = 0,column_n = 0, setNone = False)
combo_ptv2 = lbMatch_and_set(root, ListTarget, roi = ptv2, row_n = 1,column_n = 0)
combo_ptv3 = lbMatch_and_set(root, ListTarget, roi = ptv3, row_n = 2,column_n = 0)
combo_ptv4 = lbMatch_and_set(root, ListTarget, roi = ptv4, row_n = 3,column_n = 0)
combo_ptv5 = lbMatch_and_set(root, ListTarget, roi = ptv5, row_n = 4,column_n = 0)
combo_sigmoid = lbMatch_and_set(root, ListRoi, roi = sigmoid, row_n = 5,column_n = 0, setNone = False)
combo_bladder = lbMatch_and_set(root, ListRoi, roi = bladder, row_n = 6,column_n = 0, setNone = False)
combo_bowel = lbMatch_and_set(root, ListRoi, roi = bowel, row_n = 7,column_n = 0, setNone = False)
combo_liver = lbMatch_and_set(root, ListRoi, roi = liver, row_n = 8,column_n = 0, setNone = False)
combo_body = lbMatch_and_set(root, ListRoi, roi = body, row_n = 9,column_n = 0, setNone = False)

def creatre_all_target():
    ptv1 = combo_ptv1.get()
    ptv2 = combo_ptv2.get()
    ptv3 = combo_ptv3.get()
    ptv4 = combo_ptv4.get()
    ptv5 = combo_ptv5.get()
    target_list = [ptv1,ptv2,ptv3,ptv4,ptv5]
    all_target_list = []
    for p in target_list:
        if p in ListRoi:
            all_target_list.append(p)
        else:
            continue
    print(all_target_list)
    print("Create All Target")
    if "zzAll_Target" in ListRoi:
        case.PatientModel.RegionsOfInterest["zzAll_Target"].DeleteRoi()            
    # zzAll_Target
    zAll_target = case.PatientModel.CreateRoi(Name="zzAll_Target", Color="Black", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    for i in range(len(all_target_list)):
        zAll_target.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["zzAll_Target"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [all_target_list[i]], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 0, 'Posterior': 0, 
                                                                    'Right': 0, 'Left': 0 } }, 
                                    ResultOperation="Union", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                            'Anterior': 0, 'Posterior': 0, 
                                                            'Right': 0, 'Left': 0 })                                            
def create_post():
    body = combo_body.get()
    sigmoid = combo_sigmoid.get()
    bladder = combo_bladder.get()
    bowel = combo_bowel.get()
    liver = combo_liver.get()
    if "zzAnt" in ListRoi:
        case.PatientModel.RegionsOfInterest["zzAnt"].DeleteRoi() 
    #Creat virtual organ : z Ant
    VirtualAnt = case.PatientModel.CreateRoi(Name="zzAnt", Color="White", Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [sigmoid, bladder, bowel, liver], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                    'Anterior': 6, 'Posterior': 0, 
                                                                    'Right': 3, 'Left': 3 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzAll_Target"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 1,'Inferior': 1, 
                                                                   'Anterior': 1, 'Posterior': 2, 
                                                                   'Right': 2, 'Left': 2 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                          'Anterior': 0, 'Posterior': 0, 
                                                          'Right': 3, 'Left': 3 })
    VirtualAnt.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                    ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [body, "zzAnt"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                     'Anterior': 0, 'Posterior': 0, 
                                                                     'Right': 0, 'Left': 0 } }, 
                                    ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzAll_Target"], 
                                                'MarginSettings': { 'Type': "Expand", 'Superior': 1.5, 'Inferior': 1.5, 
                                                                   'Anterior': 1.5, 'Posterior': 10, 
                                                                   'Right': 1.5, 'Left': 1.5 } }, 
                                    ResultOperation="Subtraction", 
                                    ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                          'Anterior': 0, 'Posterior': 0, 
                                                          'Right': 0, 'Left': 0 })
    print("Delete zzAll_Target")                                                    
    case.PatientModel.RegionsOfInterest["zzAll_Target"].DeleteRoi()                                                    

def Create():
    body = combo_body.get()
    sigmoid = combo_sigmoid.get()
    bladder = combo_bladder.get()
    bowel = combo_bowel.get()
    liver = combo_liver.get()
    if body not in ListRoi:
        messagebox.showerror("ERROR", "Please match BODY")
    if sigmoid not in ListRoi:
        messagebox.showerror("ERROR", "Please match Sigmoid")
    if bladder not in ListRoi:
        messagebox.showerror("ERROR", "Please match Bladder")    
    if bowel not in ListRoi:
        messagebox.showerror("ERROR", "Please match Small Bowel")
    if liver not in ListRoi:
        messagebox.showerror("ERROR", "Please match Liver")
    creatre_all_target()
    create_post()
    root.destroy()

butt = Button(root, text = 'Create', command = Create)
butt.grid(column=1,row=10)
butt.config(width=15)

root.mainloop()