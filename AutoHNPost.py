from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('Post')
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
        
ptv54 = "PTV 54"
ptv57 = "PTV 57"
ptv60 = "PTV 60"
ptv66 = "PTV 66"
ptv70 = "PTV 70"
cord = "Spinal Cord"
constrict_mus = "Constrict Muscle"
cricoid = "Cricoid"
larynx = "Larynx"
body = "BODY"
   

combo_ptv54 = lbMatch_and_set(root, ListTarget, roi = ptv54, row_n = 0,column_n = 0, setNone = False)
combo_ptv57 = lbMatch_and_set(root, ListTarget, roi = ptv57, row_n = 1,column_n = 0)
combo_ptv60 = lbMatch_and_set(root, ListTarget, roi = ptv60, row_n = 2,column_n = 0)
combo_ptv66 = lbMatch_and_set(root, ListTarget, roi = ptv66, row_n = 3,column_n = 0)
combo_ptv70 = lbMatch_and_set(root, ListTarget, roi = ptv70, row_n = 4,column_n = 0)
combo_cord = lbMatch_and_set(root, ListRoi, roi = cord, row_n = 5,column_n = 0, setNone = False)
combo_constrict_mus = lbMatch_and_set(root, ListRoi, roi = constrict_mus, row_n = 6,column_n = 0, setNone = False)
combo_cricoid = lbMatch_and_set(root, ListRoi, roi = cricoid, row_n = 7,column_n = 0, setNone = False)
combo_larynx = lbMatch_and_set(root, ListRoi, roi = larynx, row_n = 8,column_n = 0, setNone = False)
combo_body = lbMatch_and_set(root, ListRoi, roi = body, row_n = 9,column_n = 0, setNone = False)

def creatre_all_target():
    ptv1 = combo_ptv54.get()
    ptv2 = combo_ptv57.get()
    ptv3 = combo_ptv60.get()
    ptv4 = combo_ptv66.get()
    ptv5 = combo_ptv70.get()
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
    cord = combo_cord.get()
    constrict_mus = combo_constrict_mus.get()
    cricoid = combo_cricoid.get()
    larynx = combo_larynx.get()
    if "zzPost" in ListRoi:
        case.PatientModel.RegionsOfInterest["zzPost"].DeleteRoi() 
    # zPost
    zPost = case.PatientModel.CreateRoi(Name="zzPost", Color="White", Type="Control",
                                                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    zPost.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [cord], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 10, 'Posterior': 10, 
                                                                'Right': 3, 'Left': 3 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzAll_Target"], 
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
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zzAll_Target"], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 15, 'Posterior': 15, 
                                                                'Right': 15, 'Left': 15 } }, 
                                ResultOperation="Intersection", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                                   
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
    
    print("Delete zzAll_Target")                                                    
    case.PatientModel.RegionsOfInterest["zzAll_Target"].DeleteRoi()                                                    

def Create():
    body = combo_body.get()
    cord = combo_cord.get()
    constrict_mus = combo_constrict_mus.get()
    cricoid = combo_cricoid.get()
    larynx = combo_larynx.get()
    if body not in ListRoi:
        messagebox.showerror("ERROR", "Please match BODY")
    if cord not in ListRoi:
        messagebox.showerror("ERROR", "Please match Spinal Cord")
    if constrict_mus not in ListRoi:
        messagebox.showerror("ERROR", "Please match Constrict Muscle")
    if cricoid not in ListRoi:
        messagebox.showerror("ERROR", "Please match Cricoid")    
    if larynx not in ListRoi:
        messagebox.showerror("ERROR", "Please match Larynx")    
    creatre_all_target()
    create_post()
    root.destroy()

butt = Button(root, text = 'Create', command = Create)
butt.grid(column=1,row=10)
butt.config(width=15)

root.mainloop()