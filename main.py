from tkinter import *
from tkinter import ttk
import sqlite3
import addbook, addmember, givebook


conn= sqlite3.connect('library.db')
cur = conn.cursor()

class Main(object):
    def __init__(self, master):
        self.master = master

        def displayStatistics(evt):
            count_books = cur.execute("SELECT count(book_id) FROM Books").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM Members").fetchall()
            taken_books = cur.execute("SELECT count(book_status) FROM Books WHERE book_status=1").fetchall()
            print(count_books)
            self.lbl_book_count.config(text="Total : "+str(count_books[0][0])+" books in library")
            self.lbl_member_count.config(text="Total member : "+str(count_members[0][0])+" members in library")
            self.lbl_taken_count.config(text="Taken : "+str(taken_books[0][0]))
            displayBooks(self)


        def displayBooks(self):
            books = cur.execute("SELECT * FROM Books").fetchall()
            count = 0
            
            self.list_books.delete(0,END)
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0])+ "-" +book[1])
                count +=1

            def bookInfor(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split("-")[0]
                book = cur.execute("SELECT * FROM Books WHERE book_id =?",(id,))
                book_infor = book.fetchall()
                print(book_infor)
                self.list_details.delete(0,'end')
                self.list_details.insert(0,"Book Name : " + book_infor[0][1])
                self.list_details.insert(1,"Author Name : " + book_infor[0][2])
                self.list_details.insert(2,"Page : " + book_infor[0][3])
                self.list_details.insert(3,"Language : " + book_infor[0][4])
                if book_infor[0][5] == 0:
                    self.list_details.insert(4,"Status : Available")
                else:
                    self.list_details.insert(4,"Status : Not Available")

            def doubleClick(evt):
                global given_id
                value = str(self.list_books.get(self.list_books.curselection()))
                given_id = value.split('-')[0]
                give_book = GiveBook()

            self.list_books.bind('<<ListboxSelect>>',bookInfor)
            self.tabs.bind('<<NotebookTabChanged>>',displayStatistics)
            # self.tabs.bind('<ButtonRelease-1',displayBooks) 
            self.list_books.bind('<Double-Button-1>',doubleClick)

        #frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
        #top_frames
        topFrame = Frame(mainFrame,width=1350,height=200,bg='#f8f8f8',relief=SUNKEN,borderwidth=1)
        topFrame.pack(side=TOP,fill=X)
        #center_frame
        centerFrame = Frame(mainFrame,width=1350,relief=RIDGE,bg='#f8f8f8',height=680)
        centerFrame.pack(side=TOP)
        #center-left_Frame
        centerLeftFrame = Frame(centerFrame,width=800,height=700,bg='#f8f8f8',borderwidth=2,relief='sunken')
        centerLeftFrame.pack(side=LEFT)
        #center-right_Frame
        centerRightFrame = Frame(centerFrame,width=550,height=700,bg='#f8f8f8',borderwidth=2,relief='sunken')
        centerRightFrame.pack()

        #search bar
        search_bar = LabelFrame(centerRightFrame,width=540,height=75,text="Search Box",bg='#C6DEF1',font='Calibri 14 bold')
        search_bar.config(fg="black")
        search_bar.pack(fill=BOTH)
        # self.lbl_search = Label(search_bar,text="Search :",font='arial 12 bold',bg='#9bc9ff',fg='black')
        # self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search = Entry(search_bar,width=31,bd=2,bg='#9bc9ff',font='arial 15 bold',fg='black')
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=5,pady=5)
        self.btn_search = Button(search_bar,text="Search :",font='arial 12 bold',bg='#9bc9ff',command=self.searchBooks)
        self.btn_search.grid(row=0,column=0,pady=10)

        #list bar
        list_bar = LabelFrame(centerRightFrame,width=540,height=175,text="List Box",bg='#C6DEF1',font='Calibri 14 bold')
        # list_bar.config(fg="black")
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar,text="Short By:", font='times 14 bold',bg='#C6DEF1',fg='black')
        lbl_list.grid(row=0,column=0,pady=5)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar,text="All Books", var=self.listChoice,value=1,bg='#C6DEF1',fg='black')
        rb2 = Radiobutton(list_bar,text="In Stock", var=self.listChoice,value=2,bg='#C6DEF1',fg='black')
        rb3 = Radiobutton(list_bar,text="Borrowed", var=self.listChoice,value=3,bg='#C6DEF1',fg='black')
        rb1.grid(row=0,column=1,padx=0)
        rb2.grid(row=0,column=2,padx=0)
        rb3.grid(row=0,column=3,padx=0)
        btn_list = Button(list_bar,text="List Books",font='arial 12 bold',bg='#9bc9ff',command=self.listBooks)
        btn_list.grid(row=1,column=0,pady=5)

        #title and image
        image_bar = Frame(centerRightFrame,width=440,height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar,text="Welcome to our Library",font="Calibri 30 bold")
        self.title_right.grid(row=0,padx=10,pady=10)
        self.img_library = PhotoImage(file='icons/library-management.png')
        self.lblImg = Label(image_bar,image=self.img_library)
        self.lblImg.grid(row=1,padx=30)

#####################################################-----Tool Bar----###########################################################                       
        #add book button
        self.iconbook=PhotoImage(file='icons/add.png')
        self.btnbook = Button(topFrame, text='  Add Book',image=self.iconbook,compound=LEFT,font='arial 12 bold',padx=10, command=self.addBook)
        self.btnbook.pack(side=LEFT)
        #add member button
        self.iconmember = PhotoImage(file='icons/add_user.png')
        self.btnmember = Button(topFrame, text='  Add Member',image=self.iconmember,compound=LEFT,font='arial 12 bold',padx=10, command=self.addMember)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)
        #give book button
        self.icongive = PhotoImage(file='icons/giving.png')
        self.btngive = Button(topFrame, text='  Give Book',font='arial 12 bold',padx=10,image=self.icongive, compound=LEFT, command=self.giveBook)
        self.btngive.pack(side=LEFT)

######################################################-----Tab----###############################################################  
        #--tab1
        self.tabs = ttk.Notebook(centerLeftFrame,width=900,height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/search.png')
        self.tab2_icon = PhotoImage(file='icons/cloud.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text="Library Management",image=self.tab1_icon,compound=LEFT)
        self.tabs.add(self.tab2,text="Statistics",image=self.tab2_icon,compound=LEFT)

        # list books
        self.list_books = Listbox(self.tab1,width=40,height=38,bd=2,font='Calibri 12 bold')
        self.sb = Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=5,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S+E)

        #list details
        self.list_details = Listbox(self.tab1,width=55,height=38,bd=2,font='Calibri 12 bold')
        self.list_details.grid(row=0,column=2,padx=(10,0),pady=5,sticky=N)

         #--tab2
         #statistics
        self.lbl_book_count = Label(self.tab2,pady=20,font='Calibri 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2,pady=20,font='Calibri 14 bold')
        self.lbl_member_count.grid(row=1,stick=W)
        self.lbl_taken_count =  Label(self.tab2,pady=20,font='Calibri 14 bold')
        self.lbl_taken_count.grid(row=2,stick=W)

        #functions
        displayBooks(self)
        displayStatistics(self)        

    def addBook(self):
        add = addbook.AddBook()
    def addMember(self):
        member = addmember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM Books WHERE book_name LIKE ?", ('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count = 0
        for book in search:
            self.list_books.insert(count,str(book[0])+ "-"+book[1])
            count += 1

    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks =cur.execute("SELECT * FROM Books").fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in allbooks:
                self.list_books.insert(count,str(book[0]) + "-"+book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM Books WHERE book_status =?",(0,)).fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in books_in_library:
                self.list_books.insert(count,str(book[0]) + "-"+book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * FROM Books WHERE book_status =?",(1,)).fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in taken_books:
                self.list_books.insert(count,str(book[0]) + "-"+book[1])
                count += 1

    def giveBook(self):
        give_book = givebook.GiveBook()    

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False,False)
        global given_id
        print()
        self.book_id = int(given_id)
        query = "SELECT * FROM Books"
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
        heading = Label(self.topFrame,text='   Add Member ',font='Calibri 22 bold',fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ###############Entries and Labels#################
        #Book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame,text='Book Name: ',font='Calibri 15 bold',fg='white',bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name['values']=book_list
        self.combo_name.current(self.book_id-1)
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
                cur.execute(query,(book_name,member_name))
                conn.commit()
                messagebox.showinfo("Success","Successfully added to database!",icon='info')
                cur.execute("UPDATE Books SET book_status =? WHERE book_id =?",(1,self.book_id))
                conn.commit()
            except:
                messagebox.showerror("Error","Cant add to database",icon='warning')
        else:
            messagebox.showerror("Error","Fields cant be empty",icon='warning')



def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/Library.ico')
    root.mainloop()

if __name__ == '__main__':
    main()