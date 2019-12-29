from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime 

class PrintReceipt():

               
                tree.insert("",1,"",text=firname,values=(secname,add,PoCo,dinak,Tele))


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
    Num = Label(window1,text="Telephone")
    dateLabel = Label(window1,text="DATE")
    

    

    #inputs
    refnumEntry = Entry(window1)
    FnameEntry = Entry(window1)
    LnameEntry = Entry(window1)
    addressEntry = Entry(window1)
    PostCodeEntry = Entry(window1)
    NumEntry = Entry(window1)
    dateEntry = Entry(window1)
    ReceiptButton = Button(window1,text="Print Receipt", command=ReceiptButton)    
    #paddling
    heading.grid(row=0,column=2,padx=10,pady=10)
    refnum.grid(row=1,column=1,padx=10,pady=10)
    Fname.grid(row=2,column=1,padx=10,pady=10)
    Lname.grid(row=3,column=1,padx=10,pady=10)
    address.grid(row=4,column=1,padx=10,pady=10)
    PostCode.grid(row=5,column=1,padx=10,pady=10)
    Num.grid(row=6,column=1,padx=10,pady=10)
    refnumEntry.grid(row=1,column=2,padx=10,pady=10)
    FnameEntry.grid(row=2,column=2,padx=10,pady=10)
    LnameEntry.grid(row=3,column=2,padx=10,pady=10)
    addressEntry.grid(row=4,column=2,padx=10,pady=10)
    PostCodeEntry.grid(row=5,column=2,padx=10,pady=10)
    NumEntry.grid(row=6,column=2,padx=10,pady=10)
    dateEntry.grid(row=7,column=2,padx=10,pady=10)
    ReceiptButton.grid(row=7,column=3)
 

    global firname
    global secname
    global add
    global PoCo
    global dinak
    global Tele
    
    firname = FnameEntry.get()
    secname = LnameEntry.get()
    add     = addressEntry.get()
    PoCo    = PostCodeEntry.get()
    dinak   = dateEntry.get()
    Tele    = NumEntry.get()
    

#####################TreeView###############################################
    tree = ttk.Treeview(window1)
    tree["columns"] = ("one","two","three","four","five")
    tree.column("#0",width=270, minwidth=270)
    tree.column("one",width=150, minwidth=150)
    tree.column("two",width=400, minwidth=200)
    tree.column("three",width=400,minwidth=200)
    tree.column("four",width=400,minwidth=200)
    tree.column("five",width=400,minwidth=200)
    
    
    tree.heading("#0",text="Patient")
    tree.heading("one",text="Firstname")
    tree.heading("two",text="Surname")
    tree.heading("three",text="Address")
    tree.heading("four",text="Date")
    tree.heading("five",text="Telephone")


    
    
    window1.mainloop()

def window2():
    return


def LoginSystem():
    user = root.Username.get()
    pas = root.Password.get()
    
    if (user == str(123456) and pas == str(123456)):
        root.button1.config(state = NORMAL)
        root.button2.config(state = NORMAL)
    else:
        root.button1.config(state = DISABLED)
        root.button2.config(state = DISABLED)
        root.Username.set("")
        root.Password.set("")
        tkinter.messagebox.askyesno("Pharmacy Managment System","You have Entered a wrong login details!")

def Reset():
    root.Username.set("")
    root.Password.set("")

def Exit():
    root.iExit = tkinter.messagebox.askyesno("Pharmacy Managment System","Confirm if you want to Exit?")
    if root.iExit > 0:
        root.destroy()
    else :
        return 
    

root = Tk()
root.title("Pharmacy Management System")
root.geometry('1350x750+0+0')
root.frame = Frame(root)
#root.frame.pack(side = CENTRE)

root.Username = StringVar()
root.Password = StringVar()
myLabel = Label(root,text="Pharmacy Management System",font=('arial',40,'bold'),bd=20)
username = Label(root,text="Username")
password = Label(root,text="Password")
userEntry =  Entry(root,textvariable = root.Username)
passEntry = Entry(root,textvariable =root.Password )


root.button1 = Button(root,text="Patients Registration",state = DISABLED, command=window1)
root.button2 = Button(root,text="Hospital Managment System",state = DISABLED,command=window2)
root.button3 = Button(root,text="LOGIN",command=LoginSystem)
button4 = Button(root,text="RESET",command = Reset)
button5 = Button(root,text="EXIT",command = Exit)


myLabel.grid(row=0,column=2,columnspan=3)
username.grid(row=1,column=2)
password.grid(row=3,column=2)
userEntry.grid(row=1,column=3)
passEntry.grid(row=3,column=3)
root.button1.grid(row=7,column=2)
root.button2.grid(row=7,column=3)
root.button3.grid(row=4,column=2)
button4.grid(row=4,column=3)
button5.grid(row=4,column=4)

#myLabel.pack()
#username.pack()
#password.pack()

root.mainloop()
