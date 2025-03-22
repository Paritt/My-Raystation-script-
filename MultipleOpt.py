# Script recorded 20 Feb 2025, 08:47:08

#   RayStation version: 16.0.0.847
#   Selected patient: ...

from connect import *
from tkinter import *
from tkinter import ttk


plan = get_current("Plan")
opt = plan.PlanOptimizations[0]
root = Tk()

root.title('Multiple OptimiZe')
root.geometry('400x100')

#textbox for insert No. of Continue
lbFac = Label(root, text= 'No. of optimize')
lbFac.grid(column=0 ,row=2)
lbFac.config(width=27, height =2)
NumF = StringVar()
textNumF = Entry(root, textvariable = NumF)
textNumF.grid(column=1,row=2)
textNumF.config(width=27)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate")
progress_bar.grid(column=0,row=3)


def Button_Next():
	NumberOfFractions = NumF.get()
	n = int(NumberOfFractions)
	total_iterations = n+1
	progress_bar["maximum"] = total_iterations
	progress_bar["value"] = 1
	root.update_idletasks()
	for i in range(0, n):
		opt.RunOptimization(ScalingOfSoftMachineConstraints=None)
		progress_bar["value"] += 1
		root.update_idletasks()
	root.destroy()
	
buttNext = Button(root, text = 'Run', command = Button_Next)
buttNext.grid(column=1,row=3,padx=10,pady=25)
buttNext.config(width=15)

root.mainloop()