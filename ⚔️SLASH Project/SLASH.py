from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('SLASH!')
root.geometry('750x230')

def show_error():
    messagebox.showerror("ERROR", "Sorry, please check execution details")

try:
    patient = get_current('Patient')
except:
    messagebox.showinfo('No patient selected. \nScript terminated')
    exit()

list_ptv = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest if r.Type == 'Ctv' or r.Type == 'Ptv' or r.Type == 'Gtv']
list_roi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
list_ptv.insert(0,"--None--")

#Head
lbVirName = Label(root, text = 'Virtual Name')
lbVirName.grid(column=2,row=1)
lbVirName.config(width=27, height =2)
lbDistance = Label(root, text = 'Subtract distance (cm)')
lbDistance.grid(column=3, row=1)
lbDistance.config(width=20, height=2)

#Botton
lbBody = Label(root, text = 'BODY')
lbBody.grid(column=0,row=6)
body= StringVar()
comboBody = ttk.Combobox(root, values= list_roi, textvariable=body)
comboBody.grid(column=1,row=6)
comboBody.config(width=27, height =20)
if "BODY" in list_roi:
    comboBody.set("BODY")

#PTV Lv.1
lbPtv1 = Label(root, text = 'PTV Lv.1')
lbPtv1.grid(column=0,row=2)
lbPtv1.config(width=27, height =2)
Ptv1 = StringVar()
comboPtv1 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv1)
comboPtv1.grid(column=1,row=2)
comboPtv1.config(width=27, height =20)
vname1 = StringVar()
Ptv1_vname = Entry(root, textvariable = vname1)
Ptv1_vname.grid(column=2,row=2)
Ptv1_vname.config(width=27)
dis1 = StringVar()
distance1 = Entry(root, textvariable = dis1)
distance1.grid(column=3,row=2)
distance1.config(width=15)
distance1.insert(0,'0.3')

#PTV Lv.2
lbPtv2 = Label(root, text = 'PTV Lv.2')
lbPtv2.grid(column=0,row=3)
lbPtv2.config(width=27, height =2)
Ptv2 = StringVar()
comboPtv2 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv2)
comboPtv2.grid(column=1,row=3)
comboPtv2.config(width=27, height =20)
vname2 = StringVar()
Ptv2_vname = Entry(root, textvariable = vname2)
Ptv2_vname.grid(column=2,row=3)
Ptv2_vname.config(width=27)
dis2 = StringVar()
distance2 = Entry(root, textvariable = dis2)
distance2.grid(column=3,row=3)
distance2.config(width=15)
distance2.insert(0,'0.3')

#PTV Lv.3
lbPtv3 = Label(root, text = 'PTV Lv.3')
lbPtv3.grid(column=0,row=4)
lbPtv3.config(width=27, height =2)
Ptv3 = StringVar()
comboPtv3 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv3)
comboPtv3.grid(column=1,row=4)
comboPtv3.config(width=27, height =20)
comboPtv3.set("--None--")
vname3 = StringVar()
Ptv3_vname = Entry(root, textvariable = vname3)
Ptv3_vname.grid(column=2,row=4)
Ptv3_vname.config(width=27)
dis3 = StringVar()
distance3 = Entry(root, textvariable = dis3)
distance3.grid(column=3,row=4)
distance3.config(width=15)
distance3.insert(0,'0.3')

#PTV Lv.4
lbPtv4 = Label(root, text = 'PTV Lv.4')
lbPtv4.grid(column=0,row=5)
lbPtv4.config(width=27, height =2)
Ptv4 = StringVar()
comboPtv4 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv4)
comboPtv4.grid(column=1,row=5)
comboPtv4.config(width=27, height =20)
comboPtv4.set("--None--")
vname4 = StringVar()
Ptv4_vname = Entry(root, textvariable = vname4)
Ptv4_vname.grid(column=2,row=5)
Ptv4_vname.config(width=27)
dis4 = StringVar()
distance4 = Entry(root, textvariable = dis4)
distance4.grid(column=3,row=5)
distance4.config(width=15)
distance4.insert(0,'0.3')


def Sub(Roi1,Roi2,dis,virname,color):
    list_roi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
    if virname in list_roi:
        case.PatientModel.RegionsOfInterest[virname].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [virname], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Roi2], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': dis, 'Inferior': dis, 
                                                                'Anterior': dis, 'Posterior': dis, 
                                                                'Right': dis, 'Left': dis } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })                                               
    else:
        zVir = case.PatientModel.CreateRoi(Name=virname, Color=color, Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)                                        
        zVir.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [Roi1], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 
                                                                'Anterior': 0, 'Posterior': 0, 
                                                                'Right': 0, 'Left': 0 } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Roi2], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': dis, 'Inferior': dis, 
                                                                'Anterior': dis, 'Posterior': dis, 
                                                                'Right': dis, 'Left': dis } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })

def intersec_body(Roi1,virname,body,color):
    list_roi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
    if virname in list_roi:
        case.PatientModel.RegionsOfInterest[virname].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [virname], 
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
    else:
        zVir = case.PatientModel.CreateRoi(Name=virname, Color=color, Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)                                        
        zVir.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [Roi1], 
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


class virtual_PTV:
    def __init__(self,i_source,i_distance,i_virtual_name,i_color):
        self._source = i_source
        self._distance = i_distance
        self._virname = i_virtual_name
        self._color = i_color
    @property    
    def source(self):
        return self._source
    @property        
    def distance(self):
        return self._distance
    @property        
    def virtual_name(self):
        return self._virname     
    @property        
    def color(self):
        return self._color                                   

def run():
    ptv1 = comboPtv1.get()
    d1 = distance1.get()
    vname1 = Ptv1_vname.get()
    ptv2 = comboPtv2.get()
    d2 = distance2.get()
    vname2 = Ptv2_vname.get()
    ptv3 = comboPtv3.get()
    d3 = distance3.get()
    vname3 = Ptv3_vname.get()
    ptv4 = comboPtv4.get()
    vname4 = Ptv4_vname.get()
    body = comboBody.get()

    c_ptv1 = virtual_PTV(ptv1,d1,vname1,'Green')
    c_ptv2 = virtual_PTV(ptv2,d2,vname2, 'Yellow')
    c_ptv3 = virtual_PTV(ptv3,d3,vname3, 'Blue')
    c_ptv4 = virtual_PTV(ptv4,0,vname4, 'Red')

    sub_list = [c_ptv1,c_ptv2,c_ptv3,c_ptv4]
    for s in sub_list :
        print(s.source)
    target_list = [c_ptv1,c_ptv2,c_ptv3,c_ptv4]

    for s in sub_list :
        if s.source != "--None--":
            print(s.source)
            print(len(target_list))
            for t in target_list:
                if t.source != s.source and s.source != "--None--" and t.source != "--None--":
                    print(s.virtual_name)
                    print(t.source)
                    Sub(s.source,t.source,dis=s.distance,virname=s.virtual_name,color=s.color)
                    intersec_body(s.source,s.virtual_name,body,s.color)
                else:
                    intersec_body(s.source,s.virtual_name,body,s.color)
                    continue
            print('popping')
            target_list.pop(0)
            print(len(target_list))
            print('end loop')
        else:
            continue
    
    root.destroy()


butt = Button(root, text = 'Run', command = run)
butt.grid(column=3,row=6)
butt.config(width=15)

root.mainloop()
