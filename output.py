from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import stroke as strk
import diabetes as dbts

def comandan():
    validation()
    scanning()

def validation():
    height = entry_height.get()
    weight = entry_weight.get()
    blood_pressure = entry_blood_pressure.get()
    cholesterol = entry_cholesterol.get()
    blood_sugar = entry_blood_sugar.get()

    if len(height)==0 or len(weight)==0 or len(blood_pressure)==0 or len(cholesterol)==0 or len(blood_sugar)==0:
        messagebox.showerror('error', 'data tidak boleh kosong')
    else:
        try:
            if int(height) < 0 or int(weight) < 0 or int(blood_pressure) < 0 or int(cholesterol) < 0 or int(blood_sugar) < 0:
                messagebox.showerror('error', 'data yang diinput tidak boleh negatif')
                
        except:
            messagebox.showerror('error', 'data yang diinput kan harus berupa bilangan bulat')


def scanning():
    height = int(entry_height.get())
    weight = int(entry_weight.get())
    blood_pressure = int(entry_blood_pressure.get())
    cholesterol = int(entry_cholesterol.get())
    blood_sugar = int(entry_blood_sugar.get())

    height = height/100
    idx_bmi = weight / height**2

    if idx_bmi <= 30.0 :
        

        result_stroke = strk.stroke_checking(blood_pressure, cholesterol, blood_sugar)
        print(f"Stroke Chance: {result_stroke}")

        result_diabetes = dbts.diabetes_checking(idx_bmi, cholesterol, blood_sugar)
        print(f"Diabetes Chance: {result_diabetes}")
        
        
    else:
        messagebox.showerror('error', "tinggi atau berat badan anda tidak valid")



window = Tk()
window.title("Medical Checkup")

frame = Frame(window, padx=10, pady=10)

label_judul = Label(frame, text="Medical Checkup", font=('verdana',15))

label_height = Label(frame, text="Tinggi badan(cm): ", font=('verdana',12))
entry_height = Entry(frame, font=('verdana',12))

label_weight = Label(frame, text="Berat badan(kg): ", font=('verdana',12))
entry_weight = Entry(frame, font=('verdana',12))

label_blood_pressure = Label(frame, text="Tekanan darah(mHg): ", font=('verdana',12))
entry_blood_pressure = Entry(frame, font=('verdana',12))

label_cholesterol = Label(frame, text="Kolestrol(mg): ", font=('verdana',12))
entry_cholesterol = Entry(frame, font=('verdana',12))

label_blood_sugar = Label(frame, text="Gula darah(mg): ", font=('verdana',12))
entry_blood_sugar = Entry(frame, font=('verdana',12))


button_insert = Button(frame, text="Insert", font=('verdana',14), bg='light green', command=comandan)


label_judul.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

label_height.grid(row=1, column=0, sticky='e')
entry_height.grid(row=1, column=1, pady=10, padx=10)

label_weight.grid(row=2, column=0, sticky='e')
entry_weight.grid(row=2, column=1, pady=10, padx=10)

label_blood_pressure.grid(row=3, column=0, sticky='e')
entry_blood_pressure.grid(row=3, column=1, pady=10, padx=10)

label_cholesterol.grid(row=4, column=0, sticky='e')
entry_cholesterol.grid(row=4, column=1, pady=10, padx=10)

label_blood_sugar.grid(row=5, column=0, sticky='e')
entry_blood_sugar.grid(row=5, column=1, pady=10, padx=10)

button_insert.grid(row=6,column=0, columnspan=2, pady=10, padx=10)

frame.grid(row=0, column=0)

window.mainloop()