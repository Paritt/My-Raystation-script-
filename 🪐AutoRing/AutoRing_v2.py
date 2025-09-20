from connect import *
from tkinter import *
from tkinter import ttk, messagebox
import time

case = get_current("Case")
examination = get_current("Examination")
db = get_current("PatientDB")

root = Tk()
root.title('The One (Click) Ring')
root.geometry('800x230')

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
lbDistance = Label(root, text = 'Distance from target boarder/other rings (cm)')
lbDistance.grid(column=2, row=1)
lbDistance.config(width=40, height=2)
lbRingWidth = Label(root, text = 'Ring Width (cm)')
lbRingWidth.grid(column=3, row=1)
lbRingWidth.config(width=15, height=2)

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
lbPtv1 = Label(root, text = 'PTV Lv.1 (Lowest Dose)')
lbPtv1.grid(column=0,row=2)
lbPtv1.config(width=27, height =2)
Ptv1 = StringVar()
comboPtv1 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv1)
comboPtv1.grid(column=1,row=2)
comboPtv1.config(width=27, height =20)
dis1 = StringVar()
distance1 = Entry(root, textvariable = dis1)
distance1.grid(column=2,row=2)
distance1.config(width=30)
distance1.insert(0,'0.3')
wid1 = StringVar()
width1 = Entry(root, textvariable= wid1)
width1.grid(column=3,row=2)
width1.config(width=15)
width1.insert(0, '1')

#PTV Lv.2
lbPtv2 = Label(root, text = 'PTV Lv.2')
lbPtv2.grid(column=0,row=3)
lbPtv2.config(width=27, height =2)
Ptv2 = StringVar()
comboPtv2 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv2)
comboPtv2.grid(column=1,row=3)
comboPtv2.config(width=27, height =20)
comboPtv2.set("--None--")
dis2 = StringVar()
distance2 = Entry(root, textvariable = dis2)
distance2.grid(column=2,row=3)
distance2.config(width=30)
distance2.insert(0,'0.3')
wid2 = StringVar()
width2 = Entry(root, textvariable= wid2)
width2.grid(column=3,row=3)
width2.config(width=15)
width2.insert(0, '1')

#PTV Lv.3
lbPtv3 = Label(root, text = 'PTV Lv.3')
lbPtv3.grid(column=0,row=4)
lbPtv3.config(width=27, height =2)
Ptv3 = StringVar()
comboPtv3 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv3)
comboPtv3.grid(column=1,row=4)
comboPtv3.config(width=27, height =20)
comboPtv3.set("--None--")
dis3 = StringVar()
distance3 = Entry(root, textvariable = dis3)
distance3.grid(column=2,row=4)
distance3.config(width=30)
distance3.insert(0,'0.3')
wid3 = StringVar()
width3 = Entry(root, textvariable= wid3)
width3.grid(column=3,row=4)
width3.config(width=15)
width3.insert(0, '1')

#PTV Lv.4
lbPtv4 = Label(root, text = 'PTV Lv.4 (Highest Dose)')
lbPtv4.grid(column=0,row=5)
lbPtv4.config(width=27, height =2)
Ptv4 = StringVar()
comboPtv4 = ttk.Combobox(root, values= list_ptv, textvariable=Ptv4)
comboPtv4.grid(column=1,row=5)
comboPtv4.config(width=27, height =20)
comboPtv4.set("--None--")
dis4 = StringVar()
distance4 = Entry(root, textvariable = dis4)
distance4.grid(column=2,row=5)
distance4.config(width=30)
distance4.insert(0,'0.3')
wid4 = StringVar()
width4 = Entry(root, textvariable= wid4)
width4.grid(column=3,row=5)
width4.config(width=15)
width4.insert(0, '1')

def Ring(Roi1,dis,virname,color, wid):
    list_roi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
    zVir = case.PatientModel.CreateRoi(Name=virname, Color=color, Type="Control",
                                            TissueName=None, RbeCellTypeName=None, RoiMaterial=None)                                        
    zVir.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", 
                                ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [Roi1], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': str(float(dis)+float(wid)), 'Inferior': str(float(dis)+float(wid)), 
                                                                'Anterior': str(float(dis)+float(wid)), 'Posterior': str(float(dis)+float(wid)), 
                                                                'Right': str(float(dis)+float(wid)), 'Left': str(float(dis)+float(wid)) } }, 
                                ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [Roi1], 
                                            'MarginSettings': { 'Type': "Expand", 'Superior': dis, 'Inferior': dis, 
                                                                'Anterior': dis, 'Posterior': dis, 
                                                                'Right': dis, 'Left': dis } }, 
                                ResultOperation="Subtraction", 
                                ResultMarginSettings={ 'Type': "Expand", 'Superior': 0,'Inferior': 0, 
                                                        'Anterior': 0, 'Posterior': 0, 
                                                        'Right': 0, 'Left': 0 })

def crop(virname,Roi2,dis):
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

def intersec_body(virname,body,color):
    list_roi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
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
    


class virtual_PTV:
    def __init__(self,i_source,i_distance,i_virtual_name,i_color,i_wid):
        self._source = i_source
        self._distance = i_distance
        self._virname = i_virtual_name
        self._color = i_color
        self._wid = i_wid
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
    @property        
    def wid(self):
        return self._wid                                   

def run():
    ptv1 = comboPtv1.get()
    d1 = distance1.get()
    w1 = width1.get()
    ptv2 = comboPtv2.get()
    d2 = distance2.get()
    w2 = width2.get()
    ptv3 = comboPtv3.get()
    d3 = distance3.get()
    w3 = width3.get()
    ptv4 = comboPtv4.get()
    d4 = distance4.get()
    w4 = width4.get()
    body = comboBody.get()

    c_ptv1 = virtual_PTV(ptv1,d1,f'zzRing_{ptv1}','White',w1)
    c_ptv2 = virtual_PTV(ptv2,d2,f'zzRing_{ptv2}', 'White',w2)
    c_ptv3 = virtual_PTV(ptv3,d3,f'zzRing_{ptv3}', 'White',w3)
    c_ptv4 = virtual_PTV(ptv4,d4,f'zzRing_{ptv4}', 'White',w4)

    sub_list = [c_ptv1,c_ptv2,c_ptv3,c_ptv4]
    for s in sub_list :
        print(s.source)
    target_list = [c_ptv1,c_ptv2,c_ptv3,c_ptv4]

    for s in sub_list :
        if s.source != "--None--":
            print(s.source)
            print(len(target_list))
            Ring(s.source,dis=s.distance,virname=s.virtual_name,color=s.color,wid=s.wid)
            intersec_body(s.virtual_name,body,s.color)
        else:
            continue
    for s in sub_list :
        if s.source != "--None--":
            for t in target_list:
                if t.source != s.source and s.source != "--None--" and t.source != "--None--":
                    print(s.virtual_name)
                    print(t.source)
                    crop(s.virtual_name,t.virtual_name,s.distance)
                    crop(s.virtual_name,t.source,s.distance)
                else:
                    continue
            print('popping')
            target_list.pop(0)
            print(len(target_list))
            print('end loop')
        else:
            continue
    
    root.destroy()


butt = Button(root, text = 'FORGE', command = run)
butt.grid(column=3,row=6)
butt.config(width=15)

root.mainloop()
