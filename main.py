from tkinter import messagebox
from tkinter.constants import *

from constants import *
import customtkinter as ctk


# method to convert the length unit
def convert_length(value, unit_from, unit_to):
    m = value * convertToMeter[unit_from]
    res = m * convertFromMeter[unit_to]
    return res


def convert():
    # Accessing the input value from the valueEntry widget
    global input_value
    try:
        input_value = float(valueEntry.get())
    except ValueError:
        messagebox.showerror('Error', 'Not a number!!')
    unit_from = unitFromCombo.get()  # Assuming you have a combo box for unit selection
    unit_to = unitToCombo.get()  # Assuming you have another combo box for unit selection

    result = convert_length(input_value, unit_from, unit_to)
    resultLabel.configure(text=f"{result:.2f} {unit_to}")


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
                              values=['Length', 'Weight', 'Heat'],
                              width=100)
systemCombo.pack(padx=10, pady=12, side=RIGHT)

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
