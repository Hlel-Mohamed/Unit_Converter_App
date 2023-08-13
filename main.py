from tkinter import messagebox
from tkinter.constants import *

from constants import *
import customtkinter as ctk


# method to convert the length unit
def convert_length(value, unit_from, unit_to):
    m = value * convertToMeter[unit_from]
    res = m * convertFromMeter[unit_to]
    return res


def convert_mass(value, unit_from, unit_to):
    g = value * convertToGram[unit_from]
    res = g * convertFromGram[unit_to]
    return res


def convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return value
    conversion_function = conversion_factors.get((unit_from, unit_to))
    return conversion_function(value)


def convert():
    try:
        input_value = float(valueEntry.get())
    except ValueError:
        messagebox.showerror('Error', 'Not a number!!')
        return
    unit_from = unitFromCombo.get()
    unit_to = unitToCombo.get()

    system_type = systemCombo.get()
    result = 0.0

    if system_type == "Length":
        result = convert_length(input_value, unit_from, unit_to)
    elif system_type == "Mass":
        result = convert_mass(input_value, unit_from, unit_to)
    elif system_type == "Temperature":
        result = convert_temperature(input_value, unit_from, unit_to)
    else:
        messagebox.showerror('Error', 'Choose a system!!')
    resultLabel.configure(text=f"{result:.2f} {unit_to}")


def change_system(event):
    if systemCombo.get() == 'Length':
        unitFromCombo.configure(values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD', 'MILE'])
        unitFromCombo.set('M')
        unitToCombo.configure(values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD', 'MILE'])
        unitToCombo.set('M')
    elif systemCombo.get() == 'Mass':
        unitFromCombo.configure(values=['MG', 'G', 'KG', 'TON', 'POUND', 'OUNCE'])
        unitFromCombo.set('G')
        unitToCombo.configure(values=['MG', 'G', 'KG', 'TON', 'POUND', 'OUNCE'])
        unitToCombo.set('G')
    elif systemCombo.get() == 'Temperature':
        unitFromCombo.configure(values=['C', 'F', 'K'])
        unitFromCombo.set('C')
        unitToCombo.configure(values=['C', 'F', 'K'])
        unitToCombo.set('C')


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x400")
root.title("Unit Converter App")

frame = ctk.CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

mainLabel = ctk.CTkLabel(master=frame, text="Unit Converter", font=("Roboto", 24))
mainLabel.pack(padx=10, pady=12)

sysFrame = ctk.CTkFrame(master=frame)
sysFrame.pack(padx=20, pady=10)

systemCombo = ctk.CTkComboBox(master=sysFrame,
                              state="readonly",
                              values=['Length', 'Mass', 'Temperature'],
                              width=100,
                              command=change_system)
systemCombo.pack(padx=10, pady=12, side=RIGHT)
systemCombo.set('Length')

inFrame = ctk.CTkFrame(master=frame)
inFrame.pack(padx=20, pady=10)

valueEntry = ctk.CTkEntry(master=inFrame, placeholder_text="Input")
valueEntry.pack(padx=10, pady=12, side=LEFT)

unitFromCombo = ctk.CTkComboBox(master=inFrame,
                                state="readonly",
                                values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD', 'MILE'],
                                width=100)
unitFromCombo.pack(padx=10, pady=12, side=RIGHT)
unitFromCombo.set('M')

outFrame = ctk.CTkFrame(master=frame)
outFrame.pack(padx=20, pady=10)

unitToCombo = ctk.CTkComboBox(master=outFrame,
                              state="readonly",
                              values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD', 'MILE'],
                              width=100)
unitToCombo.pack(padx=10, pady=12, side=RIGHT)
unitToCombo.set('M')

resultLabel = ctk.CTkLabel(master=outFrame, text="", width=140, bg_color="white", text_color="black",
                           font=("Roboto", 16))
resultLabel.pack(padx=10, pady=12, side=LEFT)

convertButton = ctk.CTkButton(master=frame, text="Convert", command=convert)
convertButton.pack(padx=10, pady=12)

root.mainloop()
