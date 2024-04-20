from tkinter import *
from tkinter import messagebox
import sqlite3
conn =sqlite3.connect('library.db')
cur = conn.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False,False)

        ############Frames###########

        #Top Frame
        self.topFrame = Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        #Bottom Frame
        self.bottomFrame = Frame(self,height=600,bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        #heading, image
        self.top_image = PhotoImage(file='icons/adduser128.png')
        top_image_lbl = Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading = Label(self.topFrame,text='   Add Member ',font='Calibri 22 bold',fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ###############Entries and Labels#################
        #member name
        self.lbl_name = Label(self.bottomFrame,text='Name: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name = Entry(self.bottomFrame,width=30,bd=2)
        self.ent_name.insert(0,"Please enter member name")
        self.ent_name.place(x=150,y=40)
        #phone
        self.lbl_phone = Label(self.bottomFrame,text='Phone No: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_phone.place(x=40,y=80)
        self.ent_phone = Entry(self.bottomFrame,width=30,bd=2)
        self.ent_phone.insert(0,"Please enter Phone number")
        self.ent_phone.place(x=150,y=80)
        #email address
        self.lbl_email = Label(self.bottomFrame,text='Email: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_email.place(x=40,y=120)
        self.ent_email = Entry(self.bottomFrame,width=30,bd=2)
        self.ent_email.insert(0,"Please enter Email address")
        self.ent_email.place(x=150,y=120)
        
        #button
        button = Button(self.bottomFrame,text="Add Member",command=self.addMember)
        button.place(x=320,y=160)

    def addMember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()
        email = self.ent_email.get()
        
        if(name and phone and email !=""):
            try:
                query ="INSERT INTO 'Members' (member_name,member_phone,member_email) VALUES(?,?,?)"
                cur.execute(query,(name,phone,email))
                conn.commit()
                messagebox.showinfo("Success","Successfully added to Database",icon='info')
            except:
                messagebox.showerror("Error","Cant add to Database",icon='warning')
        else:
            messagebox.showerror("Error","Fields cant be empty",icon='warning')