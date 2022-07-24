class main:
    def returnbook(self):
        class retu(main):
            def __init__(self):
            
                self.frame=Frame(root,bd=0,relief='flat',bg='#ffe8ec',width=900,height=390)
                self.frame.place(x=0,y=110)
                
                self.f1 = Frame(self.frame, bg='#ffe8ec', width=500, height=200, bd=5, relief='flat')
                self.f1.place(x=200, y=15)
                
                self.ed = Frame(self.f1, bg='#581845', bd=0, relief='flat', width=130, height=35)
                self.ed.place(x=170, y=0)
                
                self.lac = Label(self.ed, text='RETURN BOOKS ', bg='#581845', fg='#fff', font=('Calibri', 12, 'bold'))
                self.lac.place(x=10, y=5)
                
                #ERP ID
                self.label8 = Label(self.f1, text='ERP ID', bg='#ffe8ec', fg='black', font=('Times New Roman', 11, 'bold'))
                self.label8.place(x=85, y=65)
                
                self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('Calibri', 8, 'bold'))
                self.entry4.place(x=188, y=65)
                
                #Return Button
                self.button9 = Button(self.f1, text='RETURN', bg='#581845', fg='#fff', width=8, height=0,
                                font=('Calibri', 12, 'bold'),command=self.retbook,activebackground="#000",activeforeground="#581845")
                self.button9.place(x=85, y=120)
                
                #Back Button (Clickable Image)
                self.backbt = Button(self.frame, width=60, bg='#ffe8ec', activebackground='#ffe8ec',
                                bd=0, relief='flat', command=self.cur)
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file='filename.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2,2)
                self.backbt.config(image=self.small_log)
                
            def retsucc(self):
                self.entry4.delete(0,END)
                cursor1 = dbstudents.cursor()
                cursor1.execute("UPDATE Students SET FromDate='',ToDate='',Charge='"+str(self.charge)+"' WHERE ERP='"+self.entry+"'")
                dbstudents.commit()
                messagebox.showinfo("Success","Charges Updated and Books Returned Succesfully")
                self.tom.destroy()
                
            def retbook(self):
                self.charge=0
                self.entry=self.entry4.get()
                
                cursor=dbstudents.cursor()
                cursor.execute("SELECT * FROM Students WHERE ERP='"+self.entry+"'")
                dbstudents.commit()
                
                self.data=cursor.fetchone()
                if self.data!=None:
                    if(int(self.data[11])>=1):
                        self.get_date = date.today()
                        cursor = dbstudents.cursor()
                        
                        cursor.execute("UPDATE Students SET NoBook = 0, SubmitDate='" + str(
                                self.get_date) + "' WHERE ERP='" + self.entry + "'")
                        dbstudents.commit()

                        cursor=dbstore.cursor()
                        cursor.execute("UPDATE Books SET Issue='', ID='' WHERE ID='"+self.entry+"'")
                        dbstore.commit()   
                        
                        from datetime import datetime
                        
                        cursor=dbstudents.cursor()
                        cursor.execute("SELECT * FROM Students WHERE ERP='"+self.entry+"'")
                        dbstudents.commit()
                        self.var=cursor.fetchone()
                        if self.var!=None:
                            self.a=self.var[8]
                            self.b=self.var[9]
                            formatStr='%Y-%m-%d'
                            delta1=datetime.strptime(self.a,formatStr)
                            delta2=datetime.strptime(self.b, formatStr)
                            delta=delta2-delta1
                            chm=delta.days
                            
                            if chm<=0:
                                messagebox.showinfo("Success","Books returned successfully")
                                self.entry4.delete(0,END)
                            
                            else:
                                self.tom=Tk()
                                self.tom.geometry("300x150+300+258")
                                self.tom.iconbitmap("filename.ico")
                                self.tom.title("Library System")
                                self.tom.resizable(0,0)
                                self.tom.configure(bg="#ffe8ec")
                                
                                self.lb=Label(self.tom,text="Name of Student: ",bg="#ffe8ec",fg="black",font=('Calibri',11,'bold'))
                                self.lb.place(x=5,y=20)
                                self.lb2=Label(self.tom,text=self.var[1],bg="#ffe8ec",fg="black",font=('Calibri',11,'bold'))
                                self.lb2.place(x=130,y=20)
                                
                                self.charge=(5*chm)+int(self.var[10])
                                self.lb3=Label(self.tom,text="Fine Charge: ",bg="#ffe8ec",fg="black",font=('Calibri',11,'bold'))
                                self.lb3.place(x=5,y=55)
                                
                                self.lc2 = Label(self.tom, text=self.charge, bg="#ffe8ec", fg="black", font=('Calibri',11,
                                                                                                                        'bold'))
                                self.lc2.place(x=130, y=55)
                                self.lc3 = Label(self.tom, text='Rs.', bg="#ffe8ec", fg="black",
                                                font=('Calibri', 11, 'bold'))
                                self.lc3.place(x=150, y=55)

                                self.tombtn = Button(self.tom,text='SUBMIT', background='#581845',foreground='white',font=('Calibri',12,'bold'),width=8,
                                                      activebackground='black',activeforeground='#581845',relief='flat',command=self.retsucc)

                                self.tombtn.place(x=5,y=90)
                                
                                self.tom.mainloop()
                               
                            cursor1 = dbstudents.cursor()
                            cursor1.execute("UPDATE Students SET FromDate='',ToDate='', Charge='"+str(self.charge)+"' WHERE ERP='"+self.entry+"'")
                            dbstudents.commit()
                    else:
                        messagebox.showwarning("No Books Found","This student does not have any book issued!")
                        self.entry4.delete(0,END)
                        
                else:
                        messagebox.showerror("Invalid ERP ID","This student doesn't exist!")
                        self.entry4.delete(0,END)
        object=retu()
