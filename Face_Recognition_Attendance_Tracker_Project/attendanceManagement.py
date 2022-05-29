#importing packages
from ast import expr_context
import csv
from email import message
from logging import RootLogger
from tkinter import*
#used for making gui applications
from tkinter import ttk 
#tookit
from PIL import Image, ImageTk
#used for images
from tkinter import messagebox
#importing mysql
import mysql.connector
#importing opencv
import cv2
import os
import csv
from tkinter import filedialog

mydata_list=[]
class attendance_management:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #__________________________________________#

    #VARIABLES

        self.var_attend_id=StringVar()
        self.var_empname=StringVar()
        self.var_dept=StringVar()
        self.var_team=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend_status=StringVar()


        #__________________________________________#    

        #@(1) TOP_label to be inserted on top of the background image 
        title_label=Label(self.root,text="ATTENDANCE MANAGEMENT", font = ("ALEGREYA",40,"bold"),bg="white",fg="black")
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #@(2) MAIN_FRAME
        main_frame = Frame(self.root, bd=2, bg="white") #border=2
        main_frame.place(x=0,y=70,width=1500, height=780) #placing the frame

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@(3) LABEL_FRAME_LEFT_INDENT
        
        Label_Frame_Left = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Attendance Details",font = ("ALEGREYA",12,"bold"))
        Label_Frame_Left.place(x=15, y=10, width=740, height=700)

        left_inside_frame = Frame(Label_Frame_Left, bd=2, relief = RIDGE, bg="white") #border=2
        left_inside_frame.place(x=7,y=30,width=720, height=500) #placing the frame

        #@3.1: 
        #@ATTENDANCE_ID
        attendance_ID_label = Label(left_inside_frame, text = "Attendance Id: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        attendance_ID_label.grid(row=0,column=0, padx=5, pady=10, sticky=W) #rows and columns

        attendance_ID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_id ,font = ("ALEGREYA",12,"bold"))
        attendance_ID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #EMP_NAME
        emp_name_label = Label(left_inside_frame, text = "Employee Name: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        emp_name_label.grid(row=0,column=2, padx=5, pady=10, sticky=W) #rows and columns

        emp_name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_empname,font = ("ALEGREYA",12,"bold"))
        emp_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #TEAM
        team_label = Label(left_inside_frame, text = "Team: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        team_label.grid(row=1,column=2, padx=5, pady=10, sticky=W) #rows and columns

        team_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_team, font = ("ALEGREYA",12,"bold"))
        team_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #DEPARTMENT
        dept_label = Label(left_inside_frame, text = "Department: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        dept_label.grid(row=1,column=0, padx=5, pady=10, sticky=W) #rows and columns

        dept_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_dept, font = ("ALEGREYA",12,"bold"))
        dept_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #TIME
        time_label = Label(left_inside_frame, text = "Time: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        time_label.grid(row=2,column=0, padx=5, pady=10, sticky=W) #rows and columns

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_time, font = ("ALEGREYA",12,"bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #DATE
        date_label = Label(left_inside_frame, text = "Date: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        date_label.grid(row=2,column=2, padx=5, pady=10, sticky=W) #rows and columns

        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_date, font = ("ALEGREYA",12,"bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #ATTENDANCE
        attendance_label = Label(left_inside_frame, text = "Attendance Status: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        attendance_label.grid(row=3,column=0) #rows and columns

        self.attendance_combobox = ttk.Combobox(left_inside_frame, width=18, textvariable=self.var_attend_status,font = ("ALEGREYA",12,"bold"), state="readonly") 
        
        #adding values
        self.attendance_combobox["values"]=("Status", "Present", "Absent")
        self.attendance_combobox.grid(row=3,column=1, pady=10) #rows and columns
        self.attendance_combobox.current(0) #Select Blood Group

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #buttons ka frame 
        #x=7,y=30,width=720, height=500
        
        button_frame_new = Frame(left_inside_frame, bd=2, relief=RIDGE, bg = "white")
        button_frame_new.place(x=0, y=250, width=715, height=37)

        #import_CSV
        save_button = Button(button_frame_new, text = "Import CSV", command=self.import_CSV,width=23, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        save_button.grid(row=0, column=0)

        #exportCsv
        update_button = Button(button_frame_new, text = "Export CSV", command=self.exportCsv,width=23, font = ("ALEGREYA",12,"bold"), bg="black", fg="white")
        update_button.grid(row=0, column=1)

        # #Update
        # delete_button = Button(button_frame_new, text = "Update", width=17, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        # delete_button.grid(row=0, column=2)

        #Reset
        reset_button = Button(button_frame_new, text = "Reset", command=self.reset_func,width=23, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        reset_button.grid(row=0, column=2)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@(4) LABEL_FRAME_RIGHT_INDENT
        
        Label_Frame_Right = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Employee Details",font = ("ALEGREYA",12,"bold"))
        Label_Frame_Right.place(x=770, y=10, width=690, height=700)

        table_frame_new = Frame(Label_Frame_Right, bd=2, relief=RIDGE, bg = "white")
        table_frame_new.place(x=20, y=30, width=650, height=500)

        #scroll_bar + table
        #@Scroll_Bar
        scroll_bar_x=ttk.Scrollbar(table_frame_new,orient=HORIZONTAL)
        scroll_bar_y=ttk.Scrollbar(table_frame_new,orient=VERTICAL)
        
        self.attendance_table=ttk.Treeview(table_frame_new, column=("id", "name", "dept", "team", "time","date","attendance"),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        scroll_bar_x.config(command=self.attendance_table.xview)
        scroll_bar_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id",text="Attendance ID")
        self.attendance_table.heading("name",text="Employee Name")
        self.attendance_table.heading("dept",text="Department")
        self.attendance_table.heading("team",text="Team")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance Status")

        self.attendance_table["show"]="headings"

        #setting col widths
        self.attendance_table.column("id",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("dept",width=100)
        self.attendance_table.column("team",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("attendance",width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_Cursor)
       

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #~~~~~~~~~~~~~~~~FETCH DATA (IMPORT)~~~~~~~~~~~~~~~~~~~~~~#
    def fetch_Data(self,rows): #dete existing data in table and then insert data 
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    #import csv
    def import_CSV(self):
        global mydata_list
        mydata_list.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File", "*.*")),parent=self.root)
        with open(fin) as my_file:
            csvread=csv.reader(my_file,delimiter=",")
            for i in csvread:
                mydata_list.append(i)
            self.fetch_Data(mydata_list)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata_list)<1:
                messagebox.showerror("No Data","No Data Found in the table to export", parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File", "*.*")),parent=self.root)
            with open(fin,mode="w",newline="\n") as my_file:
                export_write=csv.writer(my_file,delimiter=",")
                for i in mydata_list:
                    export_write.writerow(i) 
                messagebox.showinfo("Data Export", "Your data was exported successfully to "+os.path.basename(fin)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)                

    def get_Cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_empname.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_team.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attend_status.set(rows[6])


    def reset_func(self):
        self.var_attend_id.set("")
        self.var_empname.set("")
        self.var_dept.set("")
        self.var_team.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend_status.set("Status")
            

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



        




#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = attendance_management(root) #class name
    root.mainloop()
    