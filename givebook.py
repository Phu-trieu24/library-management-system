from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


conn= sqlite3.connect('library.db')
cur = conn.cursor()

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False,False)
        
        query = "SELECT * FROM Books WHERE book_status = 0"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) +"-"+book[1])

        query2 = "SELECT * FROM Members"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) +"-"+member[1])

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
        heading = Label(self.topFrame,text='   Lend a Book ',font='Calibri 22 bold',fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ###############Entries and Labels#################
        #Book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame,text='Book Name: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name['values']=book_list
        
        self.combo_name.place(x=190,y=42)
        
        #Membem name
        self.member_name = StringVar()
        self.lbl_phone = Label(self.bottomFrame,text='Member Name: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_phone.place(x=40,y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
        self.combo_member['values']=member_list 
        self.combo_member.place(x=190,y=82)
        
        #button
        button = Button(self.bottomFrame,text="Lend Book",command=self.lendBook)
        button.place(x=390,y=120)

    def lendBook(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()

        if(book_name and member_name !=""):
            try:
                query = "INSERT INTO 'Borrows' (bbook_id,bmember_id) VALUES(?,?)"
                self.book_id = book_name.split('-')[0]
                cur.execute(query,(book_name,member_name))
                conn.commit()
                messagebox.showinfo("Success","Successfully added to database!",icon='info')
                cur.execute("UPDATE Books SET book_status =? WHERE book_id =?",(1,self.book_id))
                conn.commit()
            except:
                messagebox.showerror("Error","Cant add to database",icon='warning')
        else:
            messagebox.showerror("Error","Fields cant be empty",icon='warning')