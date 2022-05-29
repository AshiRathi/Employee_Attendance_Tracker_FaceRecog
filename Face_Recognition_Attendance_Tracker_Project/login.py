from tkinter import*
#used for making gui applications
from tkinter import ttk
from tkinter import commondialog 
#tookit
from PIL import Image, ImageTk #pip install Pillow
#used for images
from tkinter import messagebox
#importing mysql
import mysql.connector
#importing opencv
import cv2
from register import *
from index import FaceRecognition 

def main():
    window=Tk()
    app=Login_Window(window)
    window.mainloop()



class Login_Window:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Login")
        self.root.wm_iconbitmap("face.ico")
        #__________________________________________#

        #@BACKGROUND IMAGE
        image_insert = Image.open(r"images_to_be_used\image9.jpg") 
        image_insert=image_insert.resize((2240,1400),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_insert)

        #making label
        bg_label = Label(self.root,image=self.picture)
        #placing label on the window
        bg_label.place(x=0,y=0, width = 2240, height = 1400) #startx, starty, width, height
        #__________________________________________#

        #@MAIN_FRAME
        main_frame = Frame(bg_label, bd=2, bg="#f0f1f1") #border=2
        main_frame.place(x=400,y=100,width=690, height=700) #placing the frame

        #__________________________________________#

        #@Login IMAGE
        login_insert = Image.open(r"images_to_be_used\image1.png") 
        login_insert=login_insert.resize((200,200),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture_login=ImageTk.PhotoImage(login_insert)

        #making label
        login_label = Label(main_frame,image=self.picture_login)
        #placing label on the window
        login_label.place(x=259,y=19, width = 200, height = 200) #startx, starty, width, height
        
        #__________________________________________#

        #@TOP_label
        title_label=Label(main_frame,text="WELCOME", font = ("ALEGREYA",30,"bold"),bg="#f0f1f1",fg="black")
        
        #placing label on the window
        title_label.place(x=210, y=220,width=300,height=58)
        #__________________________________________#

        #@USERNAME

        #USERNAME_FRAME
        username_frame = Frame(main_frame, bd=2, bg="#f0f1f1") #border=2
        username_frame.place(x=20,y=300,width=690, height=400) #placing the frame

        username_label = Label(username_frame, text = "USERNAME: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        username_label.grid(row=0,column=0, padx=5, pady=10, sticky=W) #rows and columns

        self.username_entry = ttk.Entry(username_frame, width=35, font = ("ALEGREYA",18,"bold"))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        #__________________________________________#

        #@PASSWORD

        password_label = Label(username_frame, text = "PASSWORD: ", font = ("ALEGREYA",18,"bold"), bg="#f0f1f1") #no editing
        password_label.grid(row=1,column=0, padx=5, pady=10, sticky=W) #rows and columns

        self.password_entry = ttk.Entry(username_frame, width=35, font = ("ALEGREYA",18,"bold"))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        #__________________________________________#

        #LOGIN
        LOGIN_button = Button(username_frame, command=self.login_now, text = "LOGIN", width=20, font = ("ALEGREYA",15,"bold"), bd=3, relief=RIDGE, bg="darkblue", fg = "white")
        LOGIN_button.place(x=270, y=150, width=100, height=50)

        #REGISTER
        REGISTER_button = Button(username_frame, command=self.register_now,text = "REGISTER", width=20, font = ("ALEGREYA",15,"bold"), borderwidth=0,bg="#f0f1f1", fg = "black")
        REGISTER_button.place(x=240, y=220, width=150, height=50)

        #FORGOT PASSWORD
        FORGOT_button = Button(username_frame, command = self.forgot_password,text = "FORGOT PASSWORD", width=20, font = ("ALEGREYA",15,"bold"), borderwidth=0, bg="#f0f1f1", fg = "black")
        FORGOT_button.place(x=200, y=290, width=230, height=50)
    
        #__________________________________________#

        #@@@@ FUNCTIONS @@@@

    def register_now(self):
        self.variable_window=Toplevel(self.root)
        self.app=Register(self.variable_window)

    def login_now(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error","All fields required", parent=self.root)
        elif self.username_entry.get()=="uuuu" and self.password_entry.get()=="pppp":
            messagebox.showinfo("Success","Login Successful", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registration where email=%s and password=%s",(
                self.username_entry.get(),
                self.password_entry.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Are you sure you want to login?", parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=FaceRecognition(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()


    #==============================RESET_PASSWORD=============#

    def reset_password_now(self):
        if self.SECURITY_QUE_combobox_reset.get()=="SELECT":
            messagebox.showerror("Error", "Select the appropriate security question", parent=self.root2)
        elif self.SECURITY_ANS_entry_reset.get()=="":
            messagebox.showerror("Error", "Please enter the security answer", parent=self.root2)
        elif self.PASSWORD_NEW_entry.get()=="":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from registration where email=%s and securityQ=%s and securityA=%s")
            value=(self.username_entry.get(),self.SECURITY_QUE_combobox_reset.get(),self.SECURITY_ANS_entry_reset.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter valid details", parent=self.root2)
            else:
                query=("update registration set password=%s where email=%s")
                value=(self.PASSWORD_NEW_entry.get(), self.username_entry.get(),)
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password Reset Successful", parent=self.root2)
                self.root2.destroy()
                
    #==============================FORGOT_PASSWORD=============#
    def forgot_password(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error", "Email address required for changing password", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from registration where email=%s")
            value=(self.username_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter a valid Email ID", parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel() #new window
                self.root2.title("Reset Password")
                self.root2.geometry("500x550+490+190")

            
                #_________________label_________________________#

                l=Label(self.root2,text="RESET PASSWORD",font = ("ALEGREYA",25,"bold"), bg="#f0f1f1")
                l.place(x=80,y=40, width = 340, height = 40)

                #_________________security_question_________________________#

                #SECURITY QUESTION
                SECURITY_QUE_label_reset = Label(self.root2, text = "SECURITY QUESTION: ", font = ("ALEGREYA",16,"bold"), bg="#f0f1f1") #no editing
                SECURITY_QUE_label_reset.place(x=50,y=130, width = 240, height = 30) #startx, starty, width, height

                self.SECURITY_QUE_combobox_reset = ttk.Combobox(self.root2, font = ("ALEGREYA",16,"bold"), state="readonly", width=20, height=16) 
                self.SECURITY_QUE_combobox_reset["values"]=("SELECT", "BIRTH PLACE", "PET's NAME","NICK NAME")
                self.SECURITY_QUE_combobox_reset.current(0) #Select Department
                self.SECURITY_QUE_combobox_reset.place(x=55,y=170, width = 240, height = 30) #startx, starty, width, height

                #__________________security_answer______________________#

                #SECURITY ANSWER
                SECURITY_ANS_label_reset = Label(self.root2, text = "SECURITY ANSWER: ", font = ("ALEGREYA",16,"bold"), bg="#f0f1f1") #no editing
                SECURITY_ANS_label_reset.place(x=44,y=220, width = 240, height = 30) #startx, starty, width, height

                self.SECURITY_ANS_entry_reset = ttk.Entry(self.root2, width=22, font = ("ALEGREYA",16,"bold"))
                self.SECURITY_ANS_entry_reset.place(x=54,y=270, width = 240, height = 30) #startx, starty, width, height

                #___________________password_______________________#

                #PASSWORD
                PASSWORD_NEW_label = Label(self.root2, text = "PASSWORD: ", font = ("ALEGREYA",16,"bold"), bg="#f0f1f1") #no editing
                PASSWORD_NEW_label.place(x=5,y=310, width = 240, height = 30) #startx, starty, width, height

                self.PASSWORD_NEW_entry = ttk.Entry(self.root2, width=22, font = ("ALEGREYA",16,"bold"))
                self.PASSWORD_NEW_entry.place(x=54,y=350, width = 240, height = 30) #startx, starty, width, height

                #________________buttons__________________________#

                #REGISTER
                reset_button = Button(self.root2, command=self.reset_password_now,text = "RESET PASSWORD", width=20, font = ("ALEGREYA",16,"bold"), bd=0, relief=RIDGE, bg="BLACK", fg = "white")
                reset_button.place(x=127, y=420, width=240, height=40)

#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    main()
    