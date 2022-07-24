class main:
    def show(self):
        class test(main):
            def __init__(self):
            
                self.fc = Frame(root, bg='#ffe8ec', width=900, height=390)
                self.fc.place(x=0, y=110)
                self.popframe=Frame(self.fc,width=180,height=30,bg='#edb40d')
                self.popframe.place(x=360,y=0)
                self.lbn=Label(self.popframe,bg='#edb40d',text='BOOKS INFORMATION',fg='#fff',font=('Calibri',12,
                                                                                                'bold'))
                self.lbn.place(x=8,y=4)
            
                #Back Button (Clickable Image)    
                self.backbt = Button(self.fc,width=30, bg='#ffe8ec',activebackground='#ffe8ec',
                                bd=0, relief='flat', command=self.cur)
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file='filename.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(3, 3)
                self.backbt.config(image=self.small_log)

                self.table_frame=Frame(self.fc,bg='#ffe8ec',bd=1,relief='flat')
                self.table_frame.place(x=0,y=30,width=900,height=360)

                self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
                self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
                self.book_table=ttk.Treeview(self.table_frame,columns=("Book ID","Title","Author","Edition",
                                                                        "Price"),
                                xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                self.scroll_x.pack(side=BOTTOM,fill=X)
                self.scroll_y.pack(side=RIGHT, fill=Y)
                self.scroll_x.config(command=self.book_table.xview)
                self.scroll_y.config(command=self.book_table.yview)

                self.book_table.heading("Book ID",text="Book ID")
                self.book_table.heading("Title", text="Title")
                self.book_table.heading("Author", text="Author")
                self.book_table.heading("Edition", text="Edition")
                self.book_table.heading("Price", text="Price")
                self.book_table['show']='headings'
                self.book_table.column("Book ID",width=200)
                self.book_table.column("Title", width=200)
                self.book_table.column("Author", width=200)
                self.book_table.column("Edition", width=120)
                self.book_table.column("Price", width=110)
                self.book_table.pack(fill=BOTH,expand=1)
                self.fetch_data()
                
            def fetch_data(self):
                cursor=dbstore.cursor()
                cursor.execute("SELECT * FROM Books")
                self.rows=cursor.fetchall()
                if len(self.rows)!=0:
                        for self.row in self.rows:
                                self.book_table.insert('',END,values=self.row)
                dbstore.commit()
                
        oc=test()
