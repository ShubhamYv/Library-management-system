class main:
    def addbook(self):
        class temp(main):
            def book(self):
            
                self.fm=Frame(root,bg='#ffe8ec',width=900,height=390)
                self.fm.place(x=0,y=110)
                
                self.fm1=Frame(self.fm,bg='#ffe8ec',width=500,height=360,bd=5,relief='flat')
                self.fm1.place(x=200,y=15)
                
                #Back Button (clickable image)
                self.backbt = Button(self.fm, width=60, bg='#ffe8ec', bd=0, relief='flat',command=self.cur,activeforeground='black',activebackground='#ffe8ec')
                self.backbt.place(x=2, y=7)
                self.log = PhotoImage(file='filename.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                self.fll=Frame(self.fm1,width=150,height=40,bg='#ff6690')
                self.fll.place(x=150,y=15)
                self.ll=Label(self.fll,text='ADD BOOKS',fg='#fff',bg='#ff6690',font=('Canara',12,'bold'),width=15)
                self.ll.place(x=0,y=8)
                
                #ID
                self.lb=Label(self.fm1,text='ID',fg='black',bg='#ffe8ec',font=('times new roman',11,'bold'))
                self.lb.place(x=70,y=90)
                
                #Title
                self.lb2 = Label(self.fm1, text='Title', fg='black', bg='#ffe8ec', font=('times new roman', 11, 'bold'))
                self.lb2.place(x=70, y=130)
                
                #Author
                self.lb3 = Label(self.fm1, text='Author', fg='black', bg='#ffe8ec', font=('times new roman', 11, 'bold'))
                self.lb3.place(x=70, y=170)
                
                #Edition
                self.lb4= Label(self.fm1, text='Edition', fg='black', bg='#ffe8ec', font=('times new roman', 11, 'bold'))
                self.lb4.place(x=70, y=210)
                
                #Price
                self.lb5 = Label(self.fm1, text='Price', fg='black', bg='#ffe8ec', font=('times new roman', 11, 'bold'))
                self.lb5.place(x=70, y=250)
                
                #Entries
                self.ee1=Entry(self.fm1,width=25,bd=4,relief='groove',font=('Calibri',11,'bold'))
                self.ee1.place(x=180,y=88)
                
                self.ee2=Entry(self.fm1,width=25,bd=4,relief='groove',font=('Calibri',11,'bold'))
                self.ee2.place(x=180,y=130)
                
                self.ee3=Entry(self.fm1,width=25,bd=4,relief='groove',font=('Calibri',11,'bold'))
                self.ee3.place(x=180,y=170)
                
                self.ee4=Entry(self.fm1,width=25,bd=4,relief='groove',font=('Calibri',11,'bold'))
                self.ee4.place(x=180,y=210)
                
                self.ee5=Entry(self.fm1,width=25,bd=4,relief='groove',font=('Calibri',11,'bold'))
                self.ee5.place(x=180,y=250)
                
                #Submit Button
                self.bt=Button(self.fm1,text='SUBMIT',width=8,fg='white',bg='#ff6690',font=('Canara',12,'bold'),bd=3,
                          relief='flat',command=self.submit1,activebackground='black',activeforeground='#ff6690')
                self.bt.place(x=70,y=300)
              
             
            #Submit Button function 
            def submit1(self):
                try:
                    self.id=self.ee1.get()
                    self.ttl=self.ee2.get()
                    self.aut=self.ee3.get()
                    self.edi=self.ee4.get()
                    self.pri=self.ee5.get()
                    
                    if(self.id and self.ttl and self.aut and self.edi and self.pri):
                        cursor=dbstore.cursor()
                        cursor.execute("INSERT INTO Books(BookID,Title,Author,Edition,Price) values(?,?,?,?,?)",(self.id,
                                                                                                        self.ttl,self.aut,self.edi,self.pri))
                        dbstore.commit()
                        
                        messagebox.showinfo("Success","Book has been added to the library succesfully")
                        
                        #clear the entries after succesful operation
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")
                    
                except Exception as e:
                        messagebox.showerror("Error", "Enter Valid Details")
                        
            def clear(self):
                self.ee1.delete(0,END)
                self.ee2.delete(0,END)
                self.ee3.delete(0,END)
                self.ee4.delete(0,END)
                self.ee5.delete(0,END)
         
        #create object to invoke function       
        obj=temp()
        obj.book()
