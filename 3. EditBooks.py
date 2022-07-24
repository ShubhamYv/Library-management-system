class main:
    def edit(self):
        class editing(main):
            def edbooks(self):
            
                self.ffm=Frame(root,bg='#ffe8ec',width=900,height=390)
                self.ffm.place(x=0,y=110)
                
                self.fm1 = Frame(self.ffm, bg='#ffe8ec', width=500, height=200, bd=5, relief='flat')
                self.fm1.place(x=150, y=30)
                
                self.ed = Frame(self.fm1, bg='#1c1c1b', bd=0, relief='flat', width=160, height=35)
                self.ed.place(x=170,y=0)
                
                self.lab = Label(self.ed, text='EDIT BOOK DETAILS', bg='#1c1c1b', fg='#ce4a7e', font=('Calibri', 12,
                                                                                            'bold'))
                self.lab.place(x=9, y=5)
                
                #BookID
                self.label3=Label(self.fm1,text='Book ID',bg='#ffe8ec',fg='black',font=('Times New Roman',11,'bold'))
                self.label3.place(x=85,y=65)
                self.entry=Entry(self.fm1,width=30,bd=4,relief='groove',font=('Calibri',8,'bold'))
                self.entry.place(x=188,y=65)
                
                #Search Button
                self.button7 = Button(self.fm1, text='SEARCH', bg='#1c1c1b', fg='#ce4a7e', width=8,
                          font=('Calibri', 12, 'bold'),command=self.searchedit ,relief='flat',activebackground='#ce4a7e',activeforeground='#1c1c1b')
                self.button7.place(x=85,y=125)
                
                #Back Button (clickable image)
                self.backbt = Button(self.ffm, width=60, bg='#ffe8ec',activebackground='#ffe8ec',
                                  bd=0, relief='flat', command=self.cur)
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file='filename.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)
                
            def searchedit(self):
                self.datas=self.entry.get()
                cursor=dbstore.cursor()
                cursor.execute("SELECT * FROM Books WHERE BookID = '"+self.datas+"'" )
                dbstore.commit()
                self.val=cursor.fetchone()
                if self.val!=None:
                    self.edcat=Tk()
                    self.edcat.title("Library System")
                    self.edcat.geometry("300x360+600+230")
                    self.edcat.configure(bg='#ffe8ec')
                    self.edcat.iconbitmap("filename.ico")
                    
                    self.fc=Frame(self.edcat,bg='#1c1c1b',width=90,height=30)
                    self.fc.place(x=80,y=10)
                    
                    self.lab=Label(self.fc,bg='#1c1c1b',fg='#ce4a7e',text='EDIT BOOK',font=('Calibri',12,'bold'))
                    self.lab.place(x=3,y=3)
                    
                    #BookID
                    self.labid = Label(self.edcat, bg='#ffe8ec', fg='black', text='Book ID:', font=('Calibri', 12,
                                                                                               'bold'))
                    self.labid.place(x=30, y=60)
                    
                    #Title
                    self.labti = Label(self.edcat, bg='#ffe8ec', fg='black', text='Title:', font=('Calibri', 12,
                                                                                            'bold'))
                    self.labti.place(x=30, y=100)
                    
                    #Author
                    self.labaut = Label(self.edcat, bg='#ffe8ec', fg='black', text='Author:', font=('Calibri', 12,
                                                                                            'bold'))
                    self.labaut.place(x=30, y=140)
                    
                    #Edition
                    self.labed = Label(self.edcat, bg='#ffe8ec', fg='black', text='Edition:', font=('Calibri', 12,
                                                                                            'bold'))
                    self.labed.place(x=30, y=180)
                    
                    #Price
                    self.labpr = Label(self.edcat, bg='#ffe8ec', fg='black', text='Price:', font=('Calibri', 12,
                                                                                            'bold'))
                    self.labpr.place(x=30, y=220)


                    self.en1=Entry(self.edcat,width=20,bd=4,relief='groove',font=('Times New Roman',9,'bold'))
                    self.en1.place(x=110,y=60)
                    
                    self.en2 = Entry(self.edcat, width=20, bd=4, relief='groove',font=('Times New Roman',9,'bold'))
                    self.en2.place(x=110, y=100)
                    
                    self.en3 = Entry(self.edcat, width=20, bd=4, relief='groove',font=('Times New Roman',9,'bold'))
                    self.en3.place(x=110, y=140)
                    
                    self.en4 = Entry(self.edcat, width=20, bd=4, relief='groove',font=('Times New Roman',9,'bold'))
                    self.en4.place(x=110, y=180)
                    
                    self.en5 = Entry(self.edcat, width=20, bd=4, relief='groove',font=('Times New Roman',9,'bold'))
                    self.en5.place(x=110, y=220)
                    
                    #Submit Button for updating changes
                    self.butt = Button(self.edcat, text='SUBMIT', bg='#1c1c1b', fg='#ce4a7e', width=8,
                              font=('Calibri', 12, 'bold'),command=self.savedit,relief='flat')
                    self.butt.place(x=30, y=273)
                    
                    self.en1.insert(0, self.val[0])
                    self.en2.insert(0, self.val[1])
                    self.en3.insert(0, self.val[2])
                    self.en4.insert(0, self.val[3])
                    self.en5.insert(0, self.val[4])
                    
                    self.edcat.mainloop()
                
                else:
                    messagebox.showerror('Invalid Entry',"This Book doesn't exists!")
                    self.entry.delete(0,END)
                    
            def savedit(self):
                self.id = self.en1.get()
                self.ti = self.en2.get()
                self.au = self.en3.get()
                self.ed = self.en4.get()
                self.pi = self.en5.get()
                
                if(self.id and self.ti and self.au and self.ed and self.pi):
                    cursor= dbstore.cursor()
                    cursor.execute("UPDATE Books SET BookID='"+self.id+"', Title='"+self.ti+"',Author='"+self.au+"',Edition='"+self.ed+"',Price='"+self.pi+"' WHERE BookID='"+self.datas+"'")
                    dbstore.commit()
                    messagebox.showinfo('Changes Saved','Data has been updated successfully!')
                    self.edcat.destroy()
                    self.entry.delete(0,END)
                else:
                    messagebox.showerror('Error','Enter Valid Details')
                    self.entry.delete(0,END)
        obj=editing()
        obj.edbooks()
