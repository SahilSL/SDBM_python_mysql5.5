from email.mime import application
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATED BY : SAHIL S. LOKHANDE
# PROJECT NAME : STUDENT DATABASE MANAGEMENT SYSTEM USING SQL AND PYTHON TKINTER
# COLLEGE : PRIYADARSHI COLLEGE OF ENGINEERING, NAGPUR
# COMPANY NAME : IBASE TECHNOLOGIES, AMRAVATI
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

class Connector_Database:
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "STUDENT DATABASE MANAGEMENT - © SSL",)
        self.root.geometry("1060x611+300+0")
        self.root.resizable(width= False, height = False)
        
        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='#990033') #cadet blue
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row = 1, column = 0)
        
        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="#990033" ,relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)
        
        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="#990033" ,relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2 ,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
#===============================================================================================================================================
        
        StudentID=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Gender=StringVar()
        Mobile=StringVar()
        
#===============================================================================================================================================

        def iExit():
                iExit = tkinter.messagebox.askyesno("MYSQL Connection","Confirm if you want to exit")
                if iExit > 0:
                        root.destroy()
                        return
                
        def Reset():
                self.entStudentID.delete(0,END)
                self.entFirstname.delete(0,END)
                self.entSurname.delete(0,END)
                self.entAddress.delete(0,END)
                Gender.set("")
                self.entMobile.delete(0,END)
                
        def addData():
                if StudentID.get()=="" or Firstname.get()=="" or Surname.get()=="":
                        tkinter.messagebox.showerror("MYSQL Connection","Enter Correct Details")
                else:
                        sqlCon = pymysql.connect(host="localhost",user="root",password="root", database="SDBM")
                        cur = sqlCon.cursor()
                        cur.execute("insert into stable values(%s,%s,%s,%s,%s,%s)",(StudentID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),))
                        sqlCon.commit()
                        sqlCon.close()
                        tkinter.messagebox.showinfo("MYSQL Connection","Entered Recored Stored & Save Successfully !!!")
                        
        def DisplayData():
                sqlCon = pymysql.connect(host="localhost",user="root",password="root", database="SDBM")
                cur = sqlCon.cursor()
                cur.execute("select * from stable")
                result=cur.fetchall()
                if len(result)!=0:
                        self.student_records.delete(*self.student_records.get_children())
                        for row in result:
                                self.student_records.insert('',END,values=row)
                sqlCon.commit()
                sqlCon.close()
                #tkinter.messagebox.showinfo("Data Entry","Fetching Successful")
                
        def StudentInfo(ev):
                viewInfo = self.student_records.focus()
                studData = self.student_records.item(viewInfo)
                row = studData['values']
                StudentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobile.set(row[5])
 
 
        def update():
                sqlCon = pymysql.connect(host="localhost",user="root",password="root", database="SDBM")
                cur = sqlCon.cursor()
                cur.execute("update stable set firstname=%s,surname=%s,address=%s,gender=%s,mobile=%s where stdid=%s",( Firstname.get(), Surname.get(),Address.get(),Gender.get(),Mobile.get(),StudentID.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("MYSQL Connection","Record Updated Successfully !!!")         
                
        
        def delete():
                sqlCon = pymysql.connect(host="localhost",user="root",password="root", database="SDBM")
                cur = sqlCon.cursor()
                cur.execute("delete from stable where stdid=%s",StudentID.get())
                
                sqlCon.commit()
                DisplayData() #################check thus
                sqlCon.close()
                tkinter.messagebox.showinfo("MYSQL Connection","Record Deleted Successfully !!!")     
                Reset()
                
        
        def search():
                try:
                        sqlCon = pymysql.connect(host="localhost",user="root",password="root", database="SDBM")
                        cur = sqlCon.cursor()
                        cur.execute("select * from stable where stdid=%s",StudentID.get())
                        row=cur.fetchone()
                        StudentID.set(row[0])
                        Firstname.set(row[1])
                        Surname.set(row[2])
                        Address.set(row[3])
                        Gender.set(row[4])
                        Mobile.set(row[5])
                        
                        sqlCon.commit()
                        
                except:
                        tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                        Reset()
                sqlCon.close()
        
#===============================================================================================================================================
        
        self.lbltitle=Label(TitleFrame, font=('Courier New', 28 ,'bold','underline'),text="STUDENT DATABASE MANAGEMENT SYSTEM",bd=7)
        self.lbltitle.grid(row=0,column=0, padx=132)
        
#=============================================================================================================================================== 
        self.lblStudentID=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="Student ID :",bd=7)
        self.lblStudentID.grid(row=0,column=0, sticky=W, padx=5)
        self.entStudentID=Entry(LeftFrame1, font=('arial', 12 ,'bold'),bd=5, width=44, justify='left',textvariable=StudentID)
        self.entStudentID.grid(row=0,column=1, sticky=W, padx=5)
        
        self.lblFirstname=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="First Name  :",bd=7)
        self.lblFirstname.grid(row=1,column=0, sticky=W, padx=5)
        self.entFirstname=Entry(LeftFrame1, font=('arial', 12 ,'bold'),bd=5, width=44, justify='left',textvariable=Firstname)
        self.entFirstname.grid(row=1,column=1, sticky=W, padx=5)
        
        self.lblSurname=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="Surname    :",bd=7)
        self.lblSurname.grid(row=2,column=0, sticky=W, padx=5)
        self.entSurname=Entry(LeftFrame1, font=('arial', 12 ,'bold'),bd=5, width=44, justify='left',textvariable=Surname)
        self.entSurname.grid(row=2,column=1, sticky=W, padx=5)
        
        self.lblAddress=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="Address     :",bd=7)
        self.lblAddress.grid(row=3,column=0, sticky=W, padx=5)
        self.entAddress=Entry(LeftFrame1, font=('arial', 12 ,'bold'),bd=5, width=44, justify='left', textvariable=Address)
        self.entAddress.grid(row=3,column=1)
        
        self.lblGender=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="Gender       :",bd=5)
        self.lblGender.grid(row=4,column=0, sticky=W, padx=5)
        self.cboGender=ttk.Combobox(LeftFrame1, font=('arial', 12 ,'bold'), width=43, state='readonly', textvariable=Gender)
        self.cboGender['value']=(' ','Female','Male')
        self.cboGender.current(0)        
        self.cboGender.grid(row=4,column=1)
        
        self.lblMobile=Label(LeftFrame1, font=('arial', 12 ,'bold'),text="Mobile         :",bd=5)
        self.lblMobile.grid(row=5,column=0, sticky=W, padx=5)
        self.entMobile=Entry(LeftFrame1, font=('arial', 12 ,'bold'),bd=5, width=44, textvariable=Mobile)
        self.entMobile.grid(row=5,column=1, sticky=W, padx=5)
        
#==============================================================  Table Treeview  ======================================================================
        scroll_y=Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.student_records=ttk.Treeview(LeftFrame, height=12, columns=("stdid","firstname","surname","address","gender","mobile"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.student_records.heading("stdid", text="StudentID")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("address", text="Address")
        self.student_records.heading("gender", text="Gender")
        self.student_records.heading("mobile", text="Mobile")
        
        self.student_records['show']='headings'
        
        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("address", width=100)
        self.student_records.column("gender", width=70)
        self.student_records.column("mobile", width=70)
        
        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>",StudentInfo)
        DisplayData() #if you uncomment this then there is no use of display button
        #gggggggg
        


#==============================================================================================================================================
        self.btnAddNew=Button(RightFrame1a, font=('arial',16,'bold'),text="Add New",bd=4, pady=1, padx=24, width=8, height=2, command=addData).grid(row=0,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a, font=('arial',16,'bold'),text="Refresh Table",bd=4, pady=1, padx=24, width=8, height=2, command=DisplayData).grid(row=1,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1a, font=('arial',16,'bold'),text="Update",bd=4, pady=1, padx=24, width=8, height=2, command=update).grid(row=2,column=0,padx=1)
        self.btnDelete=Button(RightFrame1a, font=('arial',16,'bold'),text="Delete",bd=4, pady=1, padx=24, width=8, height=2, command=delete).grid(row=3,column=0,padx=1)    
        self.btnSearch=Button(RightFrame1a, font=('arial',16,'bold'),text="Search",bd=4, pady=1, padx=24, width=8, height=2, command=search).grid(row=4,column=0,padx=1)    
        self.btnReset=Button(RightFrame1a, font=('arial',16,'bold'),text="Reset",bd=4, pady=1, padx=24, width=8, height=2, command=Reset).grid(row=5,column=0,padx=2)    
        self.btnExit=Button(RightFrame1a, font=('arial',16,'bold'),text="Exit",bd=4, pady=1, padx=24, width=8, height=2, command=iExit).grid(row=6,column=0,padx=1)    
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    application = Connector_Database(root)
    root.mainloop()