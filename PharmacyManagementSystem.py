from tkinter import *
#import tkinter.messsagebox
from tkinter import ttk
import random
import time;
import datetime 

def window1():
    #labels
    window1 = Toplevel()
    window1.title("Patients Registration")
    window1.geometry('1350x750+0+0')
    window1.frame = Frame(window1)
    heading = Label(window1,text="Patient Registration System",font=('arial',40,'bold'),bd=20)
    refnum = Label(window1,text="Refrence number")
    Fname = Label(window1,text="First Name")
    Lname = Label(window1,text="Last Name")
    address = Label(window1,text="Address")
    PostCode = Label(window1,text="Postal Code")
    Num = Label(window1,text="Number")
    
    #inputs
    refnumEntry = Entry(window1)
    FnameEntry = Entry(window1)
    LnameEntry = Entry(window1)
    addressEntry = Entry(window1)
    PostCodeEntry = Entry(window1)
    NumEntry = Entry(window1)
    
    
    #paddling
    heading.grid(row=0,column=2)
    refnum.grid(row=1,column=1)
    Fname.grid(row=2,column=1)
    Lname.grid(row=3,column=1)
    address.grid(row=4,column=1)
    PostCode.grid(row=5,column=1)
    Num.grid(row=6,column=1)
    refnumEntry.grid(row=1,column=2)
    FnameEntry.grid(row=2,column=2)
    LnameEntry.grid(row=3,column=2)
    addressEntry.grid(row=4,column=2)
    PostCodeEntry.grid(row=5,column=2)
    NumEntry.grid(row=6,column=2)
    window.mainloop()

def window2():
    return


root = Tk()
root.title("Pharmacy Management System")
root.geometry('1350x750+0+0')
root.frame = Frame(root)
#root.frame.pack()


myLabel = Label(root,text="Pharmacy Management System",font=('arial',40,'bold'),bd=20)
username = Label(root,text="Username")
password = Label(root,text="Password")
userEntry =  Entry(root)
passEntry = Entry(root)


button1 = Button(root,text="Patients Registration",command=window1)
button2 = Button(root,text="Hospital Managment System",command=window2)
button3 = Button(root,text="LOGIN")
button4 = Button(root,text="RESET")
button5 = Button(root,text="EXIT")


myLabel.grid(row=0,column=2,columnspan=3)
username.grid(row=1,column=2)
password.grid(row=3,column=2)
userEntry.grid(row=1,column=3)
passEntry.grid(row=3,column=3)
button1.grid(row=7,column=2)
button2.grid(row=7,column=3)
button3.grid(row=4,column=2)
button4.grid(row=4,column=3)
button5.grid(row=4,column=4)

#myLabel.pack()
#username.pack()
#password.pack()


root.mainloop()