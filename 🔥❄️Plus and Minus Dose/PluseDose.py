from connect import *
from tkinter import *
from tkinter import ttk


plan = get_current("Plan")
case = get_current("Case")
patient = get_current('Patient')
examination = get_current("Examination")
root = Tk()

root.title('Pluse dose in X')
root.geometry('400x180')

def create_contour_from_dose(dose, dose_level, name, X):
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
def Button_Next():
	PluseDose = Pd.get()
	dose_level = float(PluseDose)
	name = Name.get()
	X = x_name.get()
	dose = plan.TreatmentCourse.TotalDose
	create_contour_from_dose(dose, dose_level, name, X)
	root.destroy()

#textbox for insert Pluse dose
lbPd = Label(root, text= 'Pluse dose (Gy)')
lbPd.grid(column=0 ,row=1)
lbPd.config(width=27, height =2)
Pd = StringVar()
textPd = Entry(root, textvariable = Pd)
textPd.grid(column=1,row=1)
textPd.config(width=27)

lbName = Label(root, text= 'Viurtual Name')
lbName.grid(column=0 ,row=2)
lbName.config(width=27, height =2)
Name = StringVar()
textName = Entry(root, textvariable = Name)
textName.grid(column=1,row=2)
textName.config(width=27)

ListRoi = [r.Name for r in patient.Cases[0].PatientModel.RegionsOfInterest]
lbX = Label(root, text= 'Pluse dose in')
lbX.grid(column=0 ,row=3)
lbX.config(width=27, height =2)
x_name = StringVar()
ComboX = ttk.Combobox(root, values = ListRoi, textvariable= x_name)
ComboX.grid(column=1,row=3)
ComboX.config(width=27)

buttNext = Button(root, text = 'Run', command = Button_Next)
buttNext.grid(column=1,row=4,padx=10,pady=25)
buttNext.config(width=15)

root.mainloop()