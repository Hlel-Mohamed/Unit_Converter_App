from tkinter import messagebox
from tkinter.constants import *

from constants import *
import customtkinter as ctk


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
    system = systemCombo.get()

    length_units = ['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD', 'MILE']
    mass_units = ['MG', 'G', 'KG', 'TON', 'POUND', 'OUNCE']
    temperature_units = ['C', 'F', 'K']

    if system == 'Length':
        units = length_units
    elif system == 'Mass':
        units = mass_units
    elif system == 'Temperature':
        units = temperature_units
    else:
        return

    unitFromCombo.configure(values=units)
    unitFromCombo.set(units[0])
    unitToCombo.configure(values=units)
    unitToCombo.set(units[0])


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()

    width = 500
    height = 400

    x = (root.winfo_screenwidth() / 2) - (width / 2)
    y = (root.winfo_screenheight() / 2) - (height / 2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.title("Unit Converter App")
    root.resizable(False, False)

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
                                    values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD',
                                            'MILE'],
                                    width=100)
    unitFromCombo.pack(padx=10, pady=12, side=RIGHT)
    unitFromCombo.set('M')

    outFrame = ctk.CTkFrame(master=frame)
    outFrame.pack(padx=20, pady=10)

    unitToCombo = ctk.CTkComboBox(master=outFrame,
                                  state="readonly",
                                  values=['NM', 'MM', 'CM', 'DM', 'M', 'DAM', 'HM', 'KM', 'INCH', 'FEET', 'YARD',
                                          'MILE'],
                                  width=100)
    unitToCombo.pack(padx=10, pady=12, side=RIGHT)
    unitToCombo.set('M')

    resultLabel = ctk.CTkLabel(master=outFrame, text="", width=140, bg_color="white", text_color="black",
                               font=("Roboto", 16))
    resultLabel.pack(padx=10, pady=12, side=LEFT)

    convertButton = ctk.CTkButton(master=frame, text="Convert", command=convert)
    convertButton.pack(padx=10, pady=12)

    root.mainloop()
