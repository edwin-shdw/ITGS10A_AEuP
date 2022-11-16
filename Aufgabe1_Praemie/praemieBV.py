# install tkinter via pip
from tkinter import *
from tkinter import ttk
from tkinter import Tk

PROGRAM_NAME = "Praemie"
WINDOW_SIZE = "250x200"

def calc():
    try:
        try:
            seniority = int(seniority_Entry.get())
            if seniority < 0:
                setResultMsg("Alter kleiner Null macht keinen Sinn!", "red")
                return
        except: errorMsg = "Dienstalter ist ungültig!"
        try:
            age = int(age_Entry.get())
            if age < 0:
                setResultMsg("Alter kleiner Null macht keinen Sinn!", "red")
                return
        except: errorMsg = "Alter ist ungültig!"
        if seniority > age:
            setResultMsg("Länger im Dienst als Alt, macht keinen Sinn!", "red")
            return
        if seniority >= 6:
            bonus = 80 + seniority * 20
            if age > 50:
                bonus += 50
        else:
            if seniority >= 1:
                bonus = 200
            else: bonus = 0
        setResultMsg(f"Die Prämie beträgt {bonus}€")
    except: 
        errorMsg = "Ungültige Eingabe!"
        setResultMsg(errorMsg, "red")

def setResultMsg(msg, color="green"):
    global resultMsg_Label
    result_Label.set(msg)
    resultMsg_Label = Label(mainframe, textvariable=result_Label, wraplength=140, fg=color).grid(column=1, row=6, pady=(10, 0))

root = Tk()
root.title(PROGRAM_NAME)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.geometry(WINDOW_SIZE)

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky='')

ttk.Label(mainframe, text="Dienstalter:").grid(column=1, row=1, sticky='w')
seniority_Entry = IntVar()
ttk.Entry(mainframe, textvariable=seniority_Entry).grid(column=1, row=2)
ttk.Label(mainframe, text="Alter:").grid(column=1, row=3, sticky='w')
age_Entry = IntVar()
ttk.Entry(mainframe, textvariable=age_Entry).grid(column=1, row=4)
ttk.Button(mainframe, text="Berechne", command=calc).grid(column=1, row=5)

result_Label = StringVar()
resultMsg_Label = Label(mainframe, textvariable=result_Label, wraplength=140, fg="green").grid(column=1, row=6, pady=(10, 0))

root.mainloop()
