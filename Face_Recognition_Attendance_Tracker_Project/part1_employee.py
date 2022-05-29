#importing packages
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

class Employee:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #__________________________________________#
#__________________________________________#    
    #>>>>>>>>>>>>>>>>>VARIABLES<<<<<<<<<<<<<<<<<<<<    
        self.var_dept=StringVar()
        self.var_project=StringVar()
        self.var_location=StringVar()
        self.var_shift=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_blood=StringVar()
        self.var_team=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_lead=StringVar()
        #__________________________________________#
#__________________________________________#

        #@BACKGROUND images 
        image_insert = Image.open(r"images_to_be_used\image1.jpg") 
        image_insert=image_insert.resize((2240,1400),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_insert)
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #making label
        bg_label = Label(self.root,image=self.picture)
        #placing label on the window
        bg_label.place(x=0,y=40, width = 2240, height = 1400) #startx, starty, width, height

        #__________________________________________#
#__________________________________________#

        #@TOP_label to be inserted on top of the background image
        title_label=Label(bg_label,text="EMPLOYEE MANAGEMENT", font = ("ALEGREYA",40,"bold"),bg="white",fg="black")
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)
        #__________________________________________#
#__________________________________________#

        #@MAIN_FRAME
        main_frame = Frame(bg_label, bd=2, bg="white") #border=2
        main_frame.place(x=0,y=70,width=1500, height=780) #placing the frame

        #__________________________________________#
#__________________________________________#
        
        #@LABEL_FRAME_LEFT_INDENT
        
        Label_Frame_Left = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Employee Details",font = ("ALEGREYA",12,"bold"))
        Label_Frame_Left.place(x=15, y=10, width=740, height=700)

        #@INSERT images 
        image2_insert = Image.open(r"images_to_be_used\image2.jpg") 
        image2_insert=image2_insert.resize((730,690),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture2=ImageTk.PhotoImage(image2_insert)
        #making label
        label_2 = Label(Label_Frame_Left,image=self.picture2)
        #placing label on the window
        label_2.place(x=8,y=0, width = 720, height = 667) #startx, starty, width, height

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@CURRENT_PROJ_INFOR >> ENROLLMENT_FRAME

        current_position_frame = LabelFrame(Label_Frame_Left, bd=2, bg="white", relief=RIDGE, text = "Current Project Information",font = ("ALEGREYA",12,"bold"))
        current_position_frame.place(x=8,y=0, width=720, height=150)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@DEPARTMENT >> CURRENT_POSITION

        department_label = Label(current_position_frame, text = "Department: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        department_label.grid(row=0,column=0, padx=10, pady=10, sticky=W) #rows and columns

        #combobox
        department_combobox = ttk.Combobox(current_position_frame, textvariable=self.var_dept, font = ("ALEGREYA",12,"bold"), state="readonly", width=24) 
        
        #adding values
        department_combobox["values"]=("Select Department", "Accounts and Finance", "HR", "Sales and marketing","Infrastructures","Research and development","Learning and development","IT services","Product development","Admin department","Security and transport")
        department_combobox.current(0) #Select Department
        department_combobox.grid(row=0,column=1, padx=2, pady=10, sticky=W) #rows and columns

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@PROJECT >> CURRENT_POSITION

        project_label = Label(current_position_frame, text = "Project: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        project_label.grid(row=0,column=2, padx=10, pady=10, sticky=W) #rows and columns

        #combobox

        project_combobox = ttk.Combobox(current_position_frame, textvariable=self.var_project, font = ("ALEGREYA",12,"bold"), state="readonly", width=24) 
        
        #adding values
        project_combobox["values"]=("Select Project", "Project1", "Project2", "Project3","Project4","Project5","Project6","Project7","Project8","Project9","Project10")
        project_combobox.current(0) #Select Department
        project_combobox.grid(row=0,column=3, padx=2, pady=10, sticky=W) #rows and columns

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@City >> CURRENT_POSITION

        city_label = Label(current_position_frame, text = "Location: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        city_label.grid(row=1,column=0, padx=10, pady=10, sticky=W) #rows and columns

        #combobox

        city_combobox = ttk.Combobox(current_position_frame, textvariable=self.var_location, font = ("ALEGREYA",12,"bold"), state="readonly", width=24) 
        
        #adding values
        city_combobox["values"]=("Select Team", "Ahmedabad", "Bangalore", "Chennai","New Delhi","Gurugram","Noida","Hyderabad","Kochi","Kolkata","Pune")
        city_combobox.current(0) #Select Department
        city_combobox.grid(row=1,column=1, padx=2, pady=10, sticky=W) #rows and columns

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@Shift >> CURRENT_POSITION

        shift_label = Label(current_position_frame, text = "Shift: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        shift_label.grid(row=1,column=2, padx=10, pady=10, sticky=W) #rows and columns

        #combobox

        shift_combobox = ttk.Combobox(current_position_frame, textvariable=self.var_shift, font = ("ALEGREYA",12,"bold"), state="readonly", width=24) 
        
        #adding values
        shift_combobox["values"]=("Select Shift", "Morning", "Evening")
        shift_combobox.current(0) #Select Department
        shift_combobox.grid(row=1,column=3, padx=2, pady=10, sticky=W) #rows and columns

        #__________________________________________#

        #@EMPLOYEE_TEAM_INFO >> ENROLLMENT_FRAME
        #frame
        employee_team_frame = LabelFrame(Label_Frame_Left, bd=2, bg="white", relief=RIDGE, text = "Employee Information",font = ("ALEGREYA",12,"bold"))
        employee_team_frame.place(x=8,y=160, width=720, height=510)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #labels
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #EMP_ID
        emp_ID_label = Label(employee_team_frame, text = "Employee Id: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        emp_ID_label.grid(row=0,column=0, padx=5, pady=10, sticky=W) #rows and columns

        emp_ID_entry = ttk.Entry(employee_team_frame, textvariable=self.var_id, width=20, font = ("ALEGREYA",12,"bold"))
        emp_ID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #EMP_NAME
        emp_name_label = Label(employee_team_frame, text = "Employee Name: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        emp_name_label.grid(row=0,column=2, padx=5, pady=10, sticky=W) #rows and columns

        emp_name_entry = ttk.Entry(employee_team_frame, textvariable=self.var_name, width=20, font = ("ALEGREYA",12,"bold"))
        emp_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #BLOOD_GROUP
        blood_group_label = Label(employee_team_frame, text = "Blood Group: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        blood_group_label.grid(row=1,column=0, padx=5, pady=10, sticky=W) #rows and columns

        #blood_group_entry = ttk.Entry(employee_team_frame, textvariable=self.var_blood, width=20, font = ("ALEGREYA",12,"bold"))
        #blood_group_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        blood_combobox = ttk.Combobox(employee_team_frame, textvariable=self.var_blood, font = ("ALEGREYA",12,"bold"), state="readonly", width=18) 
        
        #adding values
        blood_combobox["values"]=("Select Blood Group", "A+", "A-", "B+", "B-", "AB+", "AB-","O+","O-")
        blood_combobox.current(0) #Select Blood Group
        blood_combobox.grid(row=1,column=1, padx=10, pady=10, sticky=W) #rows and columns

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #TEAM
        team_label = Label(employee_team_frame, text = "Employee Team: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        team_label.grid(row=1,column=2, padx=5, pady=10, sticky=W) #rows and columns

        team_entry = ttk.Entry(employee_team_frame, textvariable=self.var_team, width=20, font = ("ALEGREYA",12,"bold"))
        team_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #EMAIL
        email_label = Label(employee_team_frame, text = "Email: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        email_label.grid(row=2,column=0, padx=5, pady=10, sticky=W) #rows and columns

        email_entry = ttk.Entry(employee_team_frame, textvariable=self.var_email, width=20, font = ("ALEGREYA",12,"bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #PHONE
        phone_label = Label(employee_team_frame, text = "Phone: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        phone_label.grid(row=2,column=2, padx=5, pady=10, sticky=W) #rows and columns

        phone_entry = ttk.Entry(employee_team_frame, textvariable=self.var_phone, width=20, font = ("ALEGREYA",12,"bold"))
        phone_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #ADDRESS
        address_label = Label(employee_team_frame, text = "Address: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        address_label.grid(row=3,column=0, padx=5, pady=10, sticky=W) #rows and columns

        address_entry = ttk.Entry(employee_team_frame, textvariable=self.var_address, width=20, font = ("ALEGREYA",12,"bold"))
        address_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #GENDER
        gender_label = Label(employee_team_frame, text = "Gender: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        gender_label.grid(row=3,column=2, padx=5, pady=10, sticky=W) #rows and columns

        gender_combobox = ttk.Combobox(employee_team_frame, textvariable=self.var_gender, font = ("ALEGREYA",12,"bold"), state="readonly", width=18) 
        
        #adding values
        gender_combobox["values"]=("Select Gender", "Female", "Male", "Non-binary", "Transgender", "I prefer not to say", "Other")
        gender_combobox.current(0) #Select Gender
        gender_combobox.grid(row=3,column=3, padx=10, pady=10, sticky=W) #rows and columns
      
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #DOB
        dob_label = Label(employee_team_frame, text = "Date Of Birth: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        dob_label.grid(row=4,column=0, padx=5, pady=10, sticky=W) #rows and columns

        dob_entry = ttk.Entry(employee_team_frame, textvariable=self.var_dob, width=20, font = ("ALEGREYA",12,"bold"))
        dob_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #LEAD
        lead_label = Label(employee_team_frame, text = "Lead Name: ", font = ("ALEGREYA",12,"bold"), bg="white") #no editing
        lead_label.grid(row=4,column=2, padx=5, pady=10, sticky=W) #rows and columns

        lead_entry = ttk.Entry(employee_team_frame, textvariable=self.var_lead, width=20, font = ("ALEGREYA",12,"bold"))
        lead_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #PHOTO_CAPTURE
        #RADIO BUTTON 1
        self.var_radio1=StringVar()
        radio_button_1 = ttk.Radiobutton(employee_team_frame, variable = self.var_radio1, text="Capture Photo Sample",value="Yes")
        radio_button_1.grid(row=6, column=0)

        #RADIO BUTTON 2
        radio_button_2 = ttk.Radiobutton(employee_team_frame, variable = self.var_radio1, text="Don't Capture Photo Sample",value="No")
        radio_button_2.grid(row=6, column=1)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #buttons ka frame 
        button_frame_new = Frame(employee_team_frame, bd=2, relief=RIDGE, bg = "white")
        button_frame_new.place(x=2, y=260, width=711, height=224)

        #save
        save_button = Button(button_frame_new, text = "Save", command = self.add_data, width=17, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        save_button.grid(row=0, column=0)

        #update
        update_button = Button(button_frame_new, text = "Update",command = self.update_data, width=17, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        update_button.grid(row=0, column=1)

        #delete
        delete_button = Button(button_frame_new, text = "Delete", command = self.delete_data, width=17, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        delete_button.grid(row=0, column=2)

        #reset
        reset_button = Button(button_frame_new, text = "Reset", command=self.reset_data, width=17, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        reset_button.grid(row=0, column=3)

        #buttons ka frame part 2
        button_frame_new = Frame(employee_team_frame, bd=2, relief=RIDGE, bg = "white")
        button_frame_new.place(x=2, y=300, width=711, height=224)

        #capture_photo_sample
        photo_button = Button(button_frame_new, text = "Capture Photo Sample", command=self.generate_dataset, width=70, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        photo_button.grid(row=1, column=0)

        #update_photo_sample
        # update_photo_button = Button(button_frame_new, text = "Update Captured Photo Sample", width=35, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white") 
        # update_photo_button.grid(row=1, column=1)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #@LABEL_FRAME_RIGHT_INDENT
        
        Label_Frame_Right = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Employee Details",font = ("ALEGREYA",12,"bold"))
        Label_Frame_Right.place(x=770, y=10, width=690, height=700)

        #@INSERT images 
        image3_insert = Image.open(r"images_to_be_used\image10.png") 
        image3_insert=image3_insert.resize((670,160),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture3=ImageTk.PhotoImage(image3_insert)
        #making label
        label_3 = Label(Label_Frame_Right,image=self.picture3)
        #placing label on the window
        label_3.place(x=8,y=0, width = 670, height = 100) #startx, starty, width, height

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #>>>>>>>>>>>>>>>>SEARCH & FIND<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #@EMPLOYEE_TEAM_INFO >> ENROLLMENT_FRAME
        #frame
        Search_and_find_frame = LabelFrame(Label_Frame_Right, bd=2, bg="white", relief=RIDGE, text = "Search Information",font = ("ALEGREYA",12,"bold"))
        Search_and_find_frame.place(x=8,y=160, width=670, height=100)

        # Search_label = Label(Search_and_find_frame, text = "Search By: ", font = ("ALEGREYA",14,"bold"), bg="white") #no editing
        # Search_label.grid(row=0,column=0, padx=10, pady=10, sticky=W) #rows and columns

        # #combobox
        # search_combobox = ttk.Combobox(Search_and_find_frame,font = ("ALEGREYA",12,"bold"), state="readonly", width=15) 
        # #adding values
        # search_combobox["values"]=("Select","Employee Id","Phone Number")
        # search_combobox.current(0) #Select 
        # search_combobox.grid(row=0,column=1, padx=2, pady=10, sticky=W) #rows and columns

        # #
        # search_entry = ttk.Entry(Search_and_find_frame, width=15, font = ("ALEGREYA",12,"bold"))
        # search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)


        # #search
        # searching_button = Button(Search_and_find_frame, text = "Search", width=7, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        # searching_button.grid(row=0, column=3, padx=4)

        # #Show All
        # showall_button = Button(Search_and_find_frame, text = "Show All", width=7, font = ("ALEGREYA",12,"bold"), bg="black", fg = "white")
        # showall_button.grid(row=0, column=4, padx=4)

        #__________________________________________#

        #@table_FRAME
        table_frame = Frame(Label_Frame_Right, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=8,y=250, width=670, height=400)

        #__________________________________________#
        #@Scroll_Bar
        scroll_bar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_bar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame, column=("dept", "project", "location", "shift", "id","name","blood","team","email","phone","address","gender","dob","lead"),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        scroll_bar_x.config(command=self.employee_table.xview)
        scroll_bar_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dept",text="Department")
        self.employee_table.heading("project",text="Project")
        self.employee_table.heading("location",text="Location")
        self.employee_table.heading("shift",text="Shift")
        self.employee_table.heading("id",text="EmployeeId")
        self.employee_table.heading("name",text="EmployeeName")
        self.employee_table.heading("blood",text="BloodGroup")
        self.employee_table.heading("team",text="Team")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("dob",text="DateOfBirth")
        self.employee_table.heading("lead",text="Lead")

        self.employee_table["show"]="headings"

        #setting widths for the table headings
        self.employee_table.column("dept",width=100)
        self.employee_table.column("project",width=100)
        self.employee_table.column("location",width=100)
        self.employee_table.column("shift",width=100)
        self.employee_table.column("id",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("blood",width=100)
        self.employee_table.column("team",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("lead",width=100)
    
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #__________________________________________#
#__________________________________________#

    #adding data to mysql database (function declarations)
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dept.get(),
                    self.var_project.get(),
                    self.var_location.get(),
                    self.var_shift.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_blood.get(),
                    self.var_team.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_lead.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Submitted Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    ##>>>>>>>>>>Fetch Data from the mysql database<<<<<<<<<<<<<<<<##
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from employee")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data: #inserting data into table
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ##>>>>>>>>>>GetCursor from data<<<<<<<<<<<<<<<<##
    def get_cursor(self,event=""):
        focus_cursor=self.employee_table.focus()
        content=self.employee_table.item(focus_cursor)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_project.set(data[1]),
        self.var_location.set(data[2]),
        self.var_shift.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_blood.set(data[6]),
        self.var_team.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_gender.set(data[11]),
        self.var_dob.set(data[12]),
        self.var_lead.set(data[13]),
        self.var_radio1.set(data[14])

    #>>>>>>>>>>>>>update function<<<<<<<<<<<<<<<
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update employee set Dept=%s, Project=%s, Location=%s, Shift=%s, EmpName=%s, Blood=%s, Team=%s, Email=%s, Phone=%s, Address=%s, Gender=%s, Dob=%s, LeadName=%s, PhotoSample=%s where EmpId=%s",(
                    self.var_dept.get(),
                    self.var_project.get(),
                    self.var_location.get(),
                    self.var_shift.get(),
                    self.var_name.get(),
                    self.var_blood.get(),
                    self.var_team.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_lead.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success", "Employee details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
        
    #delete_function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","EmployeeID is required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete the details", parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from employee where EmpId=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted the details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    #reset_function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_project.set("Select Project")
        self.var_location.set("Select Team")
        self.var_shift.set("Select Shift")
        self.var_id.set("")
        self.var_name.set("")
        self.var_blood.set("Select Blood Group")
        self.var_team.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_lead.set("")
        self.var_radio1.set("")

        #__________________________________________#
#__________________________________________#

        #GENERATE DATASET (TAKING IMAGE SAMPLES)
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update employee set Dept=%s, Project=%s, Location=%s, Shift=%s, EmpName=%s, Blood=%s, Team=%s, Email=%s, Phone=%s, Address=%s, Gender=%s, Dob=%s, LeadName=%s, PhotoSample=%s where EmpId=%s",(
                self.var_dept.get(),
                self.var_project.get(),
                self.var_location.get(),
                self.var_shift.get(),
                self.var_name.get(),
                self.var_blood.get(),
                self.var_team.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_lead.get(),
                self.var_radio1.get(),
                self.var_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

    #__________<<<<LOADING PREDEFINED DATA ON FACE FRONTALS FROM OPENCV FOR FACE DETECTION>>>>________________

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting image to grayscale
                    faces=face_classifier.detectMultiScale(gray_scale,1.3,5)
                    #Scaling factor = 1.3 (by delfault)
                    #Minimum neighbour = 5 (by default)

                    for(x, y, w, h) in faces:
                        #saving images in a folder
                        face_crop = img[y:y+h,x:x+w]
                        return face_crop

                cap = cv2.VideoCapture(0) #opening the web cam
                image_id=0
                while True:
                    ret, the_frame = cap.read()
                    if face_cropped(the_frame) is not None:
                        image_id+=1
                        face=cv2.resize(face_cropped(the_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) #passig face as input
                        file_name_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) 
                        #put text on the face
                        cv2.imshow("Final Image", face)

                    if cv2.waitKey(1)==13 or int(image_id)==100:
                        break #break out of the loop 

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset is completely generated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

        #__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = Employee(root) #class name
    root.mainloop()
    