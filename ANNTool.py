import tkinter as tk
from tkinter import ttk
import GUI_parts as parts
import numpy as np

window = tk.Tk()
window.title('Predict Porosity')
window.geometry('400x300')

on_calc = False
def calculate():
    global on_calc
    if on_calc == False:
        on_calc == True
        var_label.set('Now you get a predicted porosity by ANN')
        material = com_mat.get()
        material_code = parts.encode_material(material)
        group = com_group.get()
        group_code = parts.encode_group(group).reshape(1, 3)
        fluid = com_fluid.get()
        fluid_code = parts.encode_fluid(fluid).reshape(1, 3)
        Volume_Fraction = np.array(float(e_VF.get())).reshape(1, 1)
        input_code = np.hstack([group_code, material_code, fluid_code, Volume_Fraction])
        porosity = parts.predict_porosity(input_code)
        var_output.set(porosity[0][0])

on_clear = False
def clear():
    global on_clear
    if on_clear == False:
        on_clear == True
        var_label.set('Please input your parameters')
        var_output.set('')

def getUpdateData(event):
    global com_mat, com_group, category
    com_mat['values'] = category[com_group.get()]

# frames
frame_root = tk.Frame(window)
frame_1 = tk.Frame(frame_root, width=400, height=200).place(x=0, y=0, anchor='nw')

# refer to the dictionary
list_ceramic, list_metal, list_polymer = parts.Materals_list()
category = {'ceramic': list_ceramic,
            'metal': list_metal,
            'polymer': list_polymer}

# design inputs entry boxes (Group, categorical value)
l_group = tk.Label(frame_1,
           text='Material Group',
           width=20, height=2).place(x=40, y=40, anchor='nw')
com_group = ttk.Combobox(frame_1,
           width=20, height=2)
com_group["values"] = list(category.keys())
com_group.current(0)
com_group.bind("<<ComboboxSelected>>", getUpdateData)
com_group.place(x=200, y=50, anchor='nw')

# design inputs entry boxes (Material, categorical value)
l_material = tk.Label(frame_1,
           text='Solid Material',
           width=20, height=2).place(x=40, y=70, anchor='nw')
com_mat = ttk.Combobox(frame_1,
           width=20, height=2)
com_mat.place(x=200, y=80, anchor='nw')

# design inputs entry boxes (Fluid, categorical value)
l_fluid = tk.Label(frame_1,
           text='Solvent',
           width=20, height=2).place(x=40, y=100, anchor='nw')
com_fluid = ttk.Combobox(frame_1,
           width=20, height=2)
com_fluid["values"] = ("water", "camphene", "TBA")
com_fluid.current(0)
# com_group.bind("<<ComboboxSelected>>", get_group)
com_fluid.place(x=200, y=110, anchor='nw')

# design inputs entry boxes (Volume fraction, a numerical value)
l_VF = tk.Label(frame_1,
           text='Volume Fraction of Solid',
           width=20, height=2).place(x=40, y=130, anchor='nw')
default_VF = tk.StringVar()
default_VF.set('0.9')
e_VF = tk.Entry(frame_1, text=default_VF)
e_VF.place(x=200, y=140, anchor='nw')

# label of instruction
var_label = tk.StringVar() # text storage
var_label.set('Please input your parameters')
l = tk.Label(frame_1,
           textvariable=var_label,
           font=('Arial', 10),
           width=50, height=2)
l.place(x=10, y=0, anchor='nw')

# labe of output
var_l_output = tk.StringVar()
var_l_output.set('Predicted Porosity')
l_output = tk.Label(frame_1,
           textvariable=var_l_output,
           width=50, height=2)
l_output.place(x=25, y=190, anchor='nw')
var_output = tk.StringVar()
output = tk.Label(frame_1,
                  textvariable=var_output,
                  borderwidth=2,
                  bg='white',
                  font=('Arial', 10),
                  width=15, height=2)
output.place(x=140, y=220, anchor='nw')

# button of calculation
b_calc = tk.Button(frame_1,
              text='Calculate',
              width=15, height=2,
              command=calculate)
b_calc.place(x=10, y=220, anchor='nw')

# button of clear
b_clear = tk.Button(frame_1,
              text='Clear',
              width=15, height=2,
              command=clear)
b_clear.place(x=280, y=220, anchor='nw')


window.mainloop()