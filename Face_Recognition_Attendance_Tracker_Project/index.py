#importing packages
from logging import RootLogger
from multiprocessing import parent_process
from time import strftime
from tkinter import*
#used for making gui applications
from tkinter import ttk
import tkinter 
#tookit
from PIL import Image, ImageTk
#used for images
from time import strftime
from datetime import datetime
import os
#importing part1_employee
from part1_employee import Employee
from image_training import Model_Training
from faceRecognition import face_Recognition
from attendanceManagement import attendance_management
from Developer import Developer
from queries import Queries

class FaceRecognition:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")


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
        title_label=Label(bg_label,text="FACE RECOGNITION APP", font = ("ALEGREYA",40,"bold"),bg="white",fg="black")
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)

        #<>>><><><><><><><><>____TIME____<><><><><><><><><><><><>
        
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_label,font = ("ALEGREYA",20,"bold"),background="white",foreground="black")
        lbl.place(x=1290,y=2,width=187,height=50)
        time()
        #__________________________________________#
#__________________________________________#

        #@EMPLOYEE 'CLICK' 
        image2_insert = Image.open(r"images_to_be_used\image2.png") 
        image2_insert=image2_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage2=ImageTk.PhotoImage(image2_insert)

        #making BUTTON
        button2 = Button(bg_label, image = self.photoimage2, command = self.employee_details, cursor = "hand2")
        button2.place(x=200, y=100, width = 220, height = 220)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

        #EMPLOYEEText 'CLICK'
        #making BUTTON
        button2_1 = Button(bg_label, text = "EMPLOYEE DETAILS", command = self.employee_details, cursor = "hand2", font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button2_1.place(x=200, y=300, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@face detection 'CLICK' 
        image3_insert = Image.open(r"images_to_be_used\image3.png") 
        image3_insert=image3_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage3=ImageTk.PhotoImage(image3_insert)

        #making BUTTON
        button3 = Button(bg_label, image = self.photoimage3, cursor = "hand2", command=self.face_model_data)
        button3.place(x=500, y=100, width = 220, height = 220)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #face detectionText 'CLICK'
        #making BUTTON
        button3_1 = Button(bg_label, text = "FACE DETECTION", cursor = "hand2", command=self.face_model_data, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button3_1.place(x=500, y=300, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@ATTENDANCE 'CLICK' 
        image4_insert = Image.open(r"images_to_be_used\image4.png") 
        image4_insert=image4_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage4=ImageTk.PhotoImage(image4_insert)

        #making BUTTON
        button4 = Button(bg_label, image = self.photoimage4, cursor = "hand2", command = self.attendance_model_data)
        button4.place(x=800, y=100, width = 220, height = 220)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #ATTENDANCEText 'CLICK'
        #making BUTTON
        button4_1 = Button(bg_label, text = "ATTENDANCE", cursor = "hand2", command = self.attendance_model_data, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button4_1.place(x=800, y=300, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@QUERIES 'CLICK' 
        image5_insert = Image.open(r"images_to_be_used\image5.png") 
        image5_insert=image5_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage5=ImageTk.PhotoImage(image5_insert)

        #making BUTTON
        button5 = Button(bg_label, image = self.photoimage5, cursor = "hand2", command=self.query_data)
        button5.place(x=1100, y=100, width = 220, height = 225)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #QUERIESText 'CLICK'
        #making BUTTON
        button5_1 = Button(bg_label, text = "CHATBOT", cursor = "hand2", command = self.query_data, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button5_1.place(x=1100, y=300, width = 220, height = 40)

        #__________________________________________#

#__________________________________________#

        #@TRAINING 'CLICK' 
        image6_insert = Image.open(r"images_to_be_used\image6.png") 
        image6_insert=image6_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage6=ImageTk.PhotoImage(image6_insert)

        #making BUTTON
        button6 = Button(bg_label, image = self.photoimage6, cursor = "hand2", command=self.training_the_data)
        button6.place(x=200, y=430, width = 220, height = 225)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #TRAININGText 'CLICK'
        #making BUTTON
        button6_1 = Button(bg_label, text = "DATA TRAINING", cursor = "hand2", command=self.training_the_data, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button6_1.place(x=200, y=630, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@PHOTOGRAPHS 'CLICK' 
        image7_insert = Image.open(r"images_to_be_used\image7.png") 
        image7_insert=image7_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage7=ImageTk.PhotoImage(image7_insert)

        #making BUTTON
        button7 = Button(bg_label, image = self.photoimage7, cursor = "hand2", command = self.open_image)
        button7.place(x=500, y=430, width = 220, height = 225)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #PHOTOGRAPHSText 'CLICK'
        #making BUTTON
        button7_1 = Button(bg_label, text = "PHOTOGRAPHS", cursor = "hand2", command = self.open_image, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button7_1.place(x=500, y=630, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@DEVELOPER 'CLICK' 
        image8_insert = Image.open(r"images_to_be_used\image8.png") 
        image8_insert=image8_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage8=ImageTk.PhotoImage(image8_insert)

        #making BUTTON
        button8 = Button(bg_label, image = self.photoimage8, cursor = "hand2", command=self.developer_data)
        button8.place(x=800, y=430, width = 220, height = 225)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #ADMINText 'CLICK'
        #making BUTTON
        button8_1 = Button(bg_label, text = "DEVELOPER", cursor = "hand2", command=self.developer_data, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button8_1.place(x=800, y=630, width = 220, height = 40)

        #__________________________________________#
#__________________________________________#

        #@LEAVE 'CLICK' 
        image9_insert = Image.open(r"images_to_be_used\image9.png") 
        image9_insert=image9_insert.resize((220,220),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photoimage9=ImageTk.PhotoImage(image9_insert)

        #making BUTTON
        button9 = Button(bg_label, image = self.photoimage9, cursor = "hand2",command=self.Exit_button)
        button9.place(x=1100, y=430, width = 220, height = 225)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #LEAVEText 'CLICK'
        #making BUTTON
        button9_1 = Button(bg_label, text = "LEAVE", cursor = "hand2",command=self.Exit_button, font = ("ALEGREYA",14,"bold"),bg="white",fg="black")
        button9_1.place(x=1100, y=630, width = 220, height = 40)

#>>>>>>>>>>>>>>>>>>>OPENS_IMAGES<<<<<<<<<<<<<<<<<<<<<
    def open_image(self):
        os.startfile("data")

    def Exit_button(self):
            self.Exit_button=tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to leave?", parent=self.root)
            if self.Exit_button>0:
                self.root.destroy()
            else:
                return

        #__________________________________________#
#__________________________________________#
        
        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def training_the_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Model_Training(self.new_window)

        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def face_model_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_Recognition(self.new_window)

        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def attendance_model_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_management(self.new_window)

        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

        #>>>>>>>>>>>>>>>>>>>FUNCTION~BUTTONS<<<<<<<<<<<<<<<<<<<<<
    def query_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Queries(self.new_window)


#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = FaceRecognition(root) #class name
    root.mainloop()
    