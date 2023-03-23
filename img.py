# Import Required Library
from tkinter import *
from tkcalendar import Calendar
import datetime
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk as itk


# Create object
root = Tk()   
root.geometry("650x600")
root.minsize(570,570)
root.maxsize(550,550)
root.title("Date Calculator")
root.iconbitmap("calendar.ico")
img = PhotoImage(file="top_bar.png")
lbl_img = Label(root, imag=img)
lbl_img.pack()





#Déclaration de fonction
#def caldate():
        
 
 
#Create Frames





#Def var
stardate = StringVar()
start_date = StringVar()
adSu = StringVar()
days = StringVar()
newDate = StringVar()
endDate = StringVar()
numDays = StringVar()

#Frame_1
#Dropdown Menu
dropMenu = [
    "Add",
    "Sub"
]

adSu = StringVar()
adSu.set ("Add")

adSuMe = OptionMenu(root, adSu, *dropMenu)
adSuMe.pack()

#Create label
stardate_lbl = Label(text="Start Date")
stardate_lbl.place(x=40, y=70)

adSu_lbl = Label(text="Add/Subtract")
adSu_lbl.place(x=20, y=120)

days_lbl = Label(text="Days")
days_lbl.place(x=60, y=180)

newDate_lbl = Label(text="New Date")
newDate_lbl.place(x=70, y=230)

#Create Entry
stardate_entry = Entry(textvariable=stardate, width="40")
adSu_entry = Entry(textvariable=adSu, width="40")
days_entry = Entry(textvariable=days, width="40")
newDate_entry = Entry(textvariable=newDate, width="40")

#Place
stardate_entry.place(x=150, y=70, width=100)
adSuMe.place(x=180, y=120, width=70) 
days_entry.place(x=150, y=180, width=100)
newDate_entry.place(x=150, y=230, width=100)

#Create button
#submit_btn = Button(root, text="New Date", command=calculator, width="50", height="1")
#submit_btn.place(x=200, y=530)


#frame_2
#Create label
start_date_lbl = Label(text="Start Date")
start_date_lbl.place(x=320, y=70)

endDate_lbl = Label(text="End Date")
endDate_lbl.place(x=320, y=120)

numDays_lbl = Label(text="Number of Days")
numDays_lbl.place(x=320, y=230)


#Create Entry
start_date_entry = Entry(textvariable=start_date, width="40")
endDate_entry = Entry(textvariable=endDate, width="40")
numDays_entry = Entry(textvariable=numDays, width="40")


#Place
start_date_entry.place(x=430, y=70, width=100)
#endDate.place(x=100, y=120, width=70) 
#numDays.place(x=170, y=190, width=100)


#Create button
#submit_btn = Button(root, text="New Date", command=calculator, width="50", height="1")
#submit_btn.place(x=200, y=530)


root.mainloop()