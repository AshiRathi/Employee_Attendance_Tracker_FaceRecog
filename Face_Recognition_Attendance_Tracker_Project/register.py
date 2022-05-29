from email import message
from tkinter import*
#used for making gui applications
from tkinter import ttk 
#tookit
from PIL import Image, ImageTk #pip install Pillow
#used for images
from tkinter import messagebox
#importing mysql
import mysql.connector
#importing opencv
import cv2

class Register:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #_________________variables_________________________#

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_passwordConfirm=StringVar()

        #_________________background_image_________________________#

        #@BACKGROUND IMAGE
        image_insert = Image.open(r"images_to_be_used\image9.jpg") 
        image_insert=image_insert.resize((2240,1400),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_insert)

        #making label
        bg_label = Label(self.root,image=self.picture)
        #placing label on the window
        bg_label.place(x=0,y=0, width = 2240, height = 1400) #startx, starty, width, height
        #_________________main_frame_________________________#

        #@MAIN_FRAME
        main_frame = Frame(bg_label, bd=2, bg="#f0f1f1") #border=2
        main_frame.place(x=80,y=100,width=1310, height=700) #placing the frame

        #__________________top_label________________________#

        #@First_label
        title_label=Label(main_frame,text="REGISTER", font = ("ALEGREYA",40,"bold"),bg="#f0f1f1",fg="black")
        
        #placing label on the window
        title_label.place(x=500, y=50,width=300,height=58)
        #_______________sub_label___________________________#

        #<><><><><>LABELS AND ENTRIES<><><><><>
        #SUB_FRAME
        username_frame = Frame(main_frame, bd=2, bg="#f0f1f1") #border=2
        username_frame.place(x=100,y=140,width=1290, height=600) #placing the frame
        #_________________first_name_________________________#

        #FIRSTNAME
        FIRSTNAME_label = Label(username_frame, text = "FIRST NAME: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        FIRSTNAME_label.grid(row=0,column=0, padx=10, pady=10, sticky=W) #rows and columns

        FIRSTNAME_entry = ttk.Entry(username_frame, textvariable=self.var_fname,width=22, font = ("ALEGREYA",18,"bold"))
        FIRSTNAME_entry.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        #________________last_name__________________________#

        #LASTNAME
        LASTNAME_label = Label(username_frame, text = "LAST NAME: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        LASTNAME_label.grid(row=0,column=1, padx=10, pady=10, sticky=W) #rows and columns

        LASTNAME_entry = ttk.Entry(username_frame, textvariable=self.var_lname, width=22, font = ("ALEGREYA",18,"bold"))
        LASTNAME_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #__________________contact_number________________________#

        #CONTACTNO
        CONTACTNO_label = Label(username_frame, text = "CONTACT NUMBER: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        CONTACTNO_label.grid(row=2,column=0, padx=10, pady=10, sticky=W) #rows and columns

        CONTACTNO_entry = ttk.Entry(username_frame, textvariable=self.var_contact, width=22, font = ("ALEGREYA",18,"bold"))
        CONTACTNO_entry.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        #_________________email_________________________#

        #EMAIL
        EMAIL_label = Label(username_frame, text = "EMAIL: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        EMAIL_label.grid(row=2,column=1, padx=10, pady=10, sticky=W) #rows and columns

        EMAIL_entry = ttk.Entry(username_frame, textvariable=self.var_email, width=22, font = ("ALEGREYA",18,"bold"))
        EMAIL_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        #_________________security_question_________________________#

        #SECURITY QUESTION
        SECURITY_QUE_label = Label(username_frame, text = "SECURITY QUESTION: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        SECURITY_QUE_label.grid(row=4,column=0, padx=10, pady=10, sticky=W) #rows and columns

        SECURITY_QUE_combobox = ttk.Combobox(username_frame, textvariable=self.var_securityQ, font = ("ALEGREYA",18,"bold"), state="readonly", width=20, height=12) 
        SECURITY_QUE_combobox["values"]=("SELECT", "BIRTH PLACE", "PET's NAME","NICK NAME")
        SECURITY_QUE_combobox.current(0) #Select Department
        SECURITY_QUE_combobox.grid(row=5,column=0, padx=10, pady=10, sticky=W) #rows and columns

        #__________________security_answer________________________#

        #SECURITY ANSWER
        SECURITY_ANS_label = Label(username_frame, text = "SECURITY ANSWER: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        SECURITY_ANS_label.grid(row=4,column=1, padx=10, pady=10, sticky=W) #rows and columns

        SECURITY_ANS_entry = ttk.Entry(username_frame, textvariable=self.var_securityA, width=22, font = ("ALEGREYA",18,"bold"))
        SECURITY_ANS_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        #___________________password_______________________#

        #PASSWORD
        PASSWORD_label = Label(username_frame, text = "PASSWORD: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        PASSWORD_label.grid(row=6,column=0, padx=10, pady=10, sticky=W) #rows and columns

        PASSWORD_entry = ttk.Entry(username_frame, textvariable=self.var_password, width=22, font = ("ALEGREYA",18,"bold"))
        PASSWORD_entry.grid(row=7, column=0, padx=10, pady=10, sticky=W)

        #__________________password_confirmation______________________#

        #CONFIRM PASSWORD
        CONFIRM_PASSWORD_label = Label(username_frame, text = "CONFIRM PASSWORD: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        CONFIRM_PASSWORD_label.grid(row=6,column=1, padx=10, pady=10, sticky=W) #rows and columns

        CONFIRM_PASSWORD_entry = ttk.Entry(username_frame, textvariable=self.var_passwordConfirm, width=22, font = ("ALEGREYA",18,"bold"))
        CONFIRM_PASSWORD_entry.grid(row=7, column=1, padx=10, pady=10, sticky=W)
        #________________register_image__________________________#

        #@REGISTER IMAGE
        register_insert = Image.open(r"images_to_be_used\image16.png") 
        register_insert=register_insert.resize((600,600),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture_register=ImageTk.PhotoImage(register_insert)

        #making label
        register_label = Label(username_frame,image=self.picture_register)
        #placing label on the window
        register_label.place(x=600,y=0, width = 600, height = 600) #startx, starty, width, height
        
        #_______________terms and conditions___________________________#

        #Checkbutton 1
        self.var_check=IntVar()
        check_button_1 = Checkbutton(username_frame, variable=self.var_check,text="I Agree To The Terms And Conditions",font = ("ALEGREYA",18,"bold"), onvalue=1,offvalue=0)
        check_button_1.place(x=10,y=440)

        #________________buttons__________________________#

        #REGISTER
        REGISTER_button = Button(username_frame,command=self.register_data, text = "REGISTER", width=20, font = ("ALEGREYA",15,"bold"), bd=0, relief=RIDGE, bg="BLACK", fg = "white")
        REGISTER_button.place(x=10, y=490, width=160, height=50)

        #LOGIN
        LOGIN_button_here = Button(username_frame, command=self.register_login,text = "LOGIN", width=20, font = ("ALEGREYA",15,"bold"), bd=0, relief=RIDGE, bg="BLACK", fg = "white")
        LOGIN_button_here.place(x=220, y=490, width=160, height=50)

        #________________FUNCTION_DECLARATIONS________________________#

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="SELECT":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.var_password.get()!=self.var_passwordConfirm.get():
            messagebox.showerror("Error","Password and Confirm Password must be same", parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agreement to the Terms and Conditions is mandatory", parent=self.root)
        #________________DATABASE_CONNECTIVITY________________________#
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
            my_cursor=conn.cursor()
            #validation
            query=("select * from registration where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_password.get(),
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration is successful", parent=self.root)

            #________________login_in_register__________________________#
    def register_login(self):
        self.root.destroy()        


#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = Register(root) #class name
    root.mainloop()
    