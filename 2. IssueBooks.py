import smtplib
import sqlite3
import time
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date

class main:
    def issuebook(self):
        class test(main):
        
            max=0
            n = 1
            def issue(self):
                self.f = Frame(root, bg='#ffe8ec', width=900, height=390)
                self.f.place(x=0, y=110)
                
                self.fmi=Canvas(self.f,bg='#ffe8ec',width=900,height=390,bd=0,relief='flat')
                self.fmi.place(x=0,y=0)
                
                self.fc=Frame(self.fmi,bg='#ffe8ec',width=338,height=230,bd=4,relief='flat')
                self.fc.place(x=70,y=20)
                
                self.ffbll=Frame(self.fc,bg='#00203f', bd=2,relief='flat', width=210,height=40)
                self.ffbll.place(x=50,y=0)
                
                self.lc=Label(self.ffbll,text='STUDENT  INFORMATION',bg='#00203f',fg='#adefd1',font=('Arial',12,'bold'))
                self.lc.place(x=0,y=6)    
                
                #ERP ID of student
                self.lb = Label(self.fc, text='ERP ID', bg='#ffe8ec', fg='black', font=('times new roman', 11, 'bold'))
                self.lb.place(x=15, y=90)
                
                self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                self.em2.place(x=105, y=90)
                
                #Submit Button for ERP ID
                self.bt = Button(self.fc, text='SUBMIT', width=8, bg='#00203f', fg='#adefd1', font=('Canara', 12, 'bold'),
                             bd=5,relief='flat',command=self.check, activeforeground='#00203f',activebackground='#adefd1')
                self.bt.place(x=15,y=160)
                
                #Back Button (clickable image)
                self.backbt = Button(self.fmi,width=60, bg='#ffe8ec',activebackground='#ffe8ec',bd=0, relief='flat',
                                       command=self.issueback)
                self.backbt.place(x=5, y=5)
                self.log = PhotoImage(file='filename.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)
                
            def check(self):
                self.b=self.em2.get()
                
                cursor=dbstudents.cursor()
                cursor.execute("SELECT * FROM Students WHERE ERP='"+self.b+"'")
                self.var=cursor.fetchone()
                if self.var!=None:
                    self.fmii=Canvas(self.f,bg='#ffe8ec',width=338,height=90,bd=0,relief='flat')
                    self.fmii.place(x=70,y=255)
                    
                    #Name
                    self.lb1=Label(self.fmii,text='Name :',fg='black',bg ='#ffe8ec',font=('Calibri',12,'bold'))
                    self.lb1.place(x=5,y=5)
                    self.lb2 = Label(self.fmii, text=self.var[1],fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb2.place(x=70, y=5)
                    
                    #Course
                    self.lb3 = Label(self.fmii, text='Course :',fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb3.place(x=5, y=25)
                    self.lb4 = Label(self.fmii, text=self.var[2],fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb4.place(x=70, y=25)
                    
                    #Year
                    self.lb5 = Label(self.fmii, text='Year :', fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb5.place(x=5, y=45)
                    self.lb6 = Label(self.fmii, text=self.var[3], fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb6.place(x=70, y=45)
                    
                    #Contact
                    self.lb7 = Label(self.fmii, text='Contact :', fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb7.place(x=5, y=65)
                    self.lb8 = Label(self.fmii, text=self.var[6],fg='black',bg ='#ffe8ec', font=('Calibri', 12, 'bold'))
                    self.lb8.place(x=70, y=65)
                    
                    #IssueBooks
                    self.fr=Frame(self.fmi,bg='#ffe8ec',bd=5,relief='flat',width=338,height=250)
                    self.fr.place(x=420,y=20)
                    self.ff=Frame(self.fr,bg='#adefd1',bd=2,relief='flat',width=140,height=40)
                    self.ff.place(x=80,y=0)
                    
                    self.lb=Label(self.ff,text='ISSUE BOOK',bg='#adefd1',fg='#00203f',font=('Arial',12,'bold'))
                    self.lb.place(x=13,y=5)
                    
                    #Book ID
                    self.tt=Label(self.fr,text='BOOK ID',bg='#ffe8ec',fg='#00203f',font=('times new roman',11,'bold'))
                    self.tt.place(x=30,y=90)
                    self.e1 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                    self.e1.place(x=130, y=90)
                    
                    #Submit Button for BookID
                    self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12,
                                                                    'bold'),bd=5,relief='flat',command=self.data,activeforeground='#adefd1',activebackground='#00203f')
                    self.bt1.place(x=15, y=160)
                
                else:
                    messagebox.showwarning('Warning','This student is not registered !')
                    
            def issueback(self):
                try:
                    self.boot.destroy()
                    self.cur()
                except Exception as e:
                    self.cur()
                    
            repeat=0
            
            def data(self):
                self.b=self.em2.get()
                cursor=dbstudents.cursor()
                cursor.execute("SELECT * FROM Students WHERE ERP='"+self.b+"'")
                self.var=cursor.fetchone()
                self.flag=0
                if(int(self.var[11])>=3):
                    try:
                        self.boot.destroy()
                        messagebox.showerror("Unable to process request","You exceed the limit of Books per student!")
                        self.flag=1
                        self.cur()

                    except Exception as e:
                        messagebox.showerror("Unable to process request","You exceed the limit of Books per student!")
                        self.flag=1
                        self.cur()
                
                self.vva=self.e1.get()
                   
                cursor=dbstore.cursor()
                cursor.execute("SELECT * FROM Books WHERE BookID='"+self.vva+"'")
                dbstore.commit()
                self.value=cursor.fetchone()
                
                if self.value!=None:
                   if(self.flag!=1):
                        self.boot=Tk()
                        self.boot.title("Issue Books")
                        self.boot.iconbitmap("filename.ico")
                        self.boot.configure(bg='#ffe8ec')
                        self.boot.geometry("370x450+880+30")
                        self.boot.resizable(0,0)
                        test.repeat=1
                        
                        self.lb=Label(self.boot,text='Title:',bg='#ffe8ec',fg='black',font=('Calibri',12,'bold'))
                        self.lb.place(x=30,y=30)
                        self.lbn = Label(self.boot, text=self.value[1], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                        self.lbn.place(x=120,y=30)
                        self.lb = Label(self.boot, text='Author:', bg='#ffe8ec', fg='black', font=('Calibri', 12,
                                                                                                'bold'))
                        self.lb.place(x=30, y=60)
                        self.lbn = Label(self.boot, text=self.value[2], bg='#ffe8ec', fg='black', font=('Calibri', 12,
                                                                                                'bold'))
                        self.lbn.place(x=120, y=60)
                        self.lb = Label(self.boot, text='Edition:', bg='#ffe8ec', fg='black', font=('Calibri', 12,
                                                                                                'bold'))
                        self.lb.place(x=30, y=90)
                        self.lbn = Label(self.boot, text=self.value[3], bg='#ffe8ec', fg='black', font=('Calibri', 12,
                                                                                                'bold'))

                        self.lbn.place(x=120, y=90)
                        
                        self.label = Label(self.fr, text='ADD MORE BOOKS ', bg='#ffe8ec', fg='black', font=('times new romman', 11,
                                                                                                        'bold'))
                        self.label.place(x=15, y=220)
                        
                        #Radio Button
                        self.it1=Radiobutton(self.fr,text='YES',bg='#ffe8ec',variable='radio',value=1,command=self.yes)
                        self.it1.place(x=170,y=220)

                        self.it2 = Radiobutton(self.fr, text='NO',bg='#ffe8ec', variable='radio', value=2,command=self.no)
                        self.it2.place(x=240, y=220)

                        #ISSUED button
                        self.button1 = Button(self.boot, text='ISSUE', bg='#adefd1', fg='#00203f', width=10, height=0,
                                        font=('Canara', 11, 'bold'), activebackground='#00203f',activeforeground='#adefd1',command=self.issued)
                        self.button1.place(x=30, y=400)

                        self.btn = Button(self.boot, text='SEND MAIL', bg='#adefd1', fg='#00203f', width=10, height=0,
                                        font=('Canara', 11, 'bold'),activebackground='#00203f',activeforeground='#adefd1', command=self.mail)
                        self.btn.place(x=160, y=400)
                        
                        #Date - Calendar
                        self.x = date.today()

                        self.cal = Calendar(self.boot, selectmode="day", bg='black',year=2022,month=3,day=30)
                        self.cal.place(x=20,y=150)
                        

                        btn1 = Button(self.boot, text="CONFIRM DATE",command=self.get_data,  bg='#343148',
                                font=('Canara', 11,'bold'),
                                fg='#d7c49e',activebackground='black', activeforeground='#d7c49e', relief='flat')
                        btn1.place(x=90,y=350)

                        self.boot.mainloop()
                
                else:
                    messagebox.showerror('Book Not Found','No such book exists!')
                    self.e1.delete(0,END)
                    
            
            def get_data(self):
                self.datecon=self.cal.selection_get()   
                
            def yes(self):
                self.n=self.n+1
               
                self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12,'bold'),bd=5,relief='flat',command=self.data,activeforeground='#adefd1',activebackground='#00203f',state=ACTIVE)
                self.bt1.place(x=15, y=160)

                self.e1.delete(0, END)
                #self.e2.delete(0, END)
                
                self.max=self.max-1
                
            def no(self):
                self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12,'bold'),bd=5,relief='flat',command=self.data,activeforeground='#adefd1',activebackground='#00203f',state=DISABLED)
                self.bt1.place(x=15, y=160)
                
            def issued(self):
                self.datecon=self.cal.selection_get()
               
                self.ac=self.e1.get()
                cursor=dbstore.cursor()
                    
                cursor.execute("UPDATE Books SET Issue='Issued', ID='"+self.b+"' WHERE "
                                                                                    "BookID='"+self.ac+"'")
                dbstore.commit()
                
                if self.n<=3:
                    book=dbstudents.cursor()
                    self.erpid1=self.em2.get()
                    book.execute("SELECT * FROM Students WHERE ERP='"+self.erpid1+"'")
                    self.issuevar=book.fetchone()
                    self.sum=self.issuevar[11]+1
                    book.execute("UPDATE Students SET NoBook='"+str(self.sum)+"' WHERE ERP='"+self.b+"' ")
                    dbstudents.commit()
                
                comm=dbstudents.cursor()
                comm.execute("UPDATE Students SET FromDate='"+str(self.x)+"', ToDate='"+str(self.datecon)+"' , SubmitDate='' WHERE ERP='"+self.b+"'")
                dbstudents.commit()
                
                messagebox.showinfo('Library Management System', 'YOUR BOOK HAS BEEN ISSUED')
                self.boot.destroy()
                self.e1.delete(0, END)
                
            
            def mail(self):

                self.erpid=self.em2.get()
                cursor=dbstudents.cursor()
                cursor.execute("SELECT * FROM Students WHERE ERP='"+self.erpid+"'")
                self.var=cursor.fetchone()
                sender = "libraryauthority@gmail.com"
                reciever =self.var[5]
                with open("passwordfilename.txt",'r') as file:
                    password=file.read()
                message = """FROM: LIBRARY DEPARTMENT
                          TO : Library Issued Books Department
                          Subject: Hello Student! Your book has been Issued"""
                try:
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.login(sender, password)
                    server.sendmail(sender, reciever, message)
                    print("ok")
                    messagebox.showinfo("Library System","Send mail Successfully !")
                except Exception as e:
                    pass
                    
        obissue=test()
        obissue.issue()
