class main:
    def delete(self):
            class dele(main):
                def deletebooks(self):
               
                    self.ff = Frame(root, bg='#ffe8ec', width=900, height=390)
                    self.ff.place(x=0, y=110)
                    
                    self.f1 = Frame(self.ff, bg='#ffe8ec', width=500, height=200, bd=5, relief='flat')
                    self.f1.place(x=200, y=15)
                    
                    self.ed = Frame(self.f1, bg='#7ea310', bd=0, relief='flat', width=120, height=30)
                    self.ed.place(x=150, y=0)
                    
                    self.lac = Label(self.ed, text='DELETE BOOKS ', bg='#7ea310', fg='#213502', font=('Calibri', 12,'bold'))
                    self.lac.place(x=7, y=3)
                    
                    #Book ID
                    self.label8 = Label(self.f1, text='Book ID', bg='#ffe8ec', fg='black', font=('times new roman', 11, 'bold'))
                    self.label8.place(x=85, y=65)
                    self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('Calibri', 8, 'bold'))
                    self.entry4.place(x=188, y=65)
                    
                    #Delete Books Button
                    self.button9 = Button(self.f1, text='DELETE', bg='#7ea310', fg='#213502', width=8,
                              font=('Calibri', 12, 'bold'),command=self.deldata,relief='flat',activebackground='black',activeforeground='#7ea310')
                    self.button9.place(x=85, y=120)
                    
                    #Back Button (Clickable Image)
                    self.backbt = Button(self.ff,width=60, bg='#ffe8ec',activebackground='#ffe8ec',
                                      bd=0, relief='flat', command=self.cur)
                    self.backbt.place(x=0, y=0)
                    self.log = PhotoImage(file='filename.png')
                    self.backbt.config(image=self.log, compound=LEFT)
                    self.small_log = self.log.subsample(2,2)
                    self.backbt.config(image=self.small_log)
                    
                def deldata(self):
                    self.a=self.entry4.get()
                    
                    cursor=dbstore.cursor()
                    cursorv=dbstore.cursor()
                    cursorv.execute("SELECT * FROM BOOKS WHERE BookID='"+self.a+"'")
                    dbstore.commit()
                    self.validation=cursorv.fetchone()
                    
                    if(self.validation!=None):
                        cursor.execute("DELETE FROM Books WHERE BookID='"+self.a+"'")
                        dbstore.commit()
                        messagebox.showinfo('Succesful','The book is successfully removed from the store!')
                        self.entry4.delete(0,END)
                    else:
                        messagebox.showerror('Invalid Operation','This book does not exist!')
                        self.entry4.delete(0,END)
                        
            occ=dele()
            occ.deletebooks()
