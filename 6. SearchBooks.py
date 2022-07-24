class main:
    def search(self):
            class demt(main):
                def delmdata(self):

                    self.fc = Frame(root, bg='#ffe8ec', width=900, height=390)
                    self.fc.place(x=0, y=110)
                    
                    self.fc1 = Frame(self.fc, bg='#ffe8ec', width=500, height=200, bd=5, relief='flat')
                    self.fc1.place(x=200, y=15)
                    
                    self.edm = Frame(self.fc1, bg='#b76e79', bd=0, relief='flat', width=130, height=35)
                    self.edm.place(x=140, y=0)
                    
                    self.lac = Label(self.edm, text='SEARCH BOOKS ', bg='#b76e79', fg='#fff', font=('Calibri', 12, 'bold'))
                    self.lac.place(x=8, y=5)
                    
                    #Book ID
                    self.label8 = Label(self.fc1, text='Book ID', bg='#ffe8ec', fg='black', font=('Times New Roman', 11, 'bold'))
                    self.label8.place(x=85, y=65)
                    self.entryl= Entry(self.fc1, width=30, bd=4, relief='groove', font=('Calibri', 8, 'bold'))
                    self.entryl.place(x=188, y=65)
                    
                    #Search Button
                    self.butto = Button(self.fc1, text='SEARCH', bg='#b76e79', fg='#fff', width=8,
                                    font=('Calibri', 12, 'bold'),command=self.srch,relief='flat',activebackground='black',activeforeground='#b76e79')
                    self.butto.place(x=85, y=120)
                    
                    #Back Button (Clickable Image)
                    self.backbt = Button(self.fc,width=60, bg='#ffe8ec',activebackground='#ffe8ec',bd=0, relief='flat', command=self.cur)
                    self.backbt.place(x=0, y=0)
                    self.log = PhotoImage(file='filename.png')
                    self.backbt.config(image=self.log, compound=LEFT)
                    self.small_log = self.log.subsample(2, 2)
                    self.backbt.config(image=self.small_log)
                    
                def srch(self):
                    self.emp=self.entryl.get()
                    
                    cursor=dbstore.cursor()
                    cursor.execute("SELECT * FROM Books WHERE BookID='"+self.emp+"'")
                    dbstore.commit()
                    self.srval=cursor.fetchone()
                    
                    if self.srval!=None:
                        self.top=Tk()
                        self.top.title("Library System")
                        self.top.iconbitmap("filename.ico")
                        self.top.geometry("400x200+335+250")
                        self.top.resizable(0, 0)
                        self.top.configure(bg='#ffe8ec')

                        self.frm=Frame(self.top,bg='#b76e79',width=100,height=35)
                        self.frm.place(x=100,y=10)

                        self.mnlb=Label(self.frm,bg='#b76e79',fg='#fff',text="AVAILABLE",font=('Calibri',12,'bold'))
                        self.mnlb.place(x=9,y=5)

                        self.lb1 = Label(self.top, text='Title: ', bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lb1.place(x=85,y=70)
                        self.lb2=Label(self.top,text=self.srval[1],bg='#ffe8ec', fg='black',font=('Calibri',12,'bold'))
                        self.lb2.place(x=165,y=70)

                        self.lb3 = Label(self.top, text='Author: ', bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lb3.place(x=85, y=110)
                        self.lb4 = Label(self.top, text=self.srval[2], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lb4.place(x=165, y=110)

                        self.lb5 = Label(self.top, text='Edition: ',bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lb5.place(x=85, y=150)
                        self.lb6 = Label(self.top, text=self.srval[3], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lb6.place(x=165, y=150)
                        self.entryl.delete(0,END)
                        
                    else:
                        messagebox.showwarning('Invalid Data','This book does not exists!')
                        self.entryl.delete(0,END)
                
            object=demt()
            object.delmdata()
