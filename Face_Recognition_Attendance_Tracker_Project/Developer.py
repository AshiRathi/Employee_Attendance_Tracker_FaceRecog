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

class Developer:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")


        #__________________________________________#
        #__________________________________________#

        #@TOP_label to be inserted on top of the background image
        title_label=Label(self.root,text="INFO CORNER", font = ("ALEGREYA",40,"bold"),bg="black",fg="white")

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)

        #@label to be inserted on top of the background image
        label=Label(self.root,text="Developer Information", font = ("ALEGREYA",20,"bold"),bg="light blue",fg="black")
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        label.place(x=600, y=80,width=300,height=58)

        #__________________________________________#
        #__________________________________________#

        #@INSERT images 
        image_to_insert = Image.open(r"images_to_be_used\image7.jpg") 
        image_to_insert=image_to_insert.resize((1490,720),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_to_insert)
        #making label
        label_image = Label(self.root,image=self.picture)
        #placing label on the window
        label_image.place(x=40,y=150, width = 1400, height = 720) #startx, starty, width, height

        
        #__________________________________________#
        #__________________________________________#

        #@FRAME
        main_frame = Frame(label_image, bd=2, bg="#f0f1f1") #border=2
        main_frame.place(x=970,y=20,width=415, height=677) #placing the frame

        #__________________________________________#
        #__________________________________________#

        #@INSERT images 
        image_to_insert_develop = Image.open(r"images_to_be_used\image14.png") 
        image_to_insert_develop=image_to_insert_develop.resize((375,375),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture_insert_develop=ImageTk.PhotoImage(image_to_insert_develop)
        #making label
        label_image_developer= Label(main_frame,image=self.picture_insert_develop)
        #placing label on the window
        label_image_developer.place(x=31,y=20, width = 375, height = 375) #startx, starty, width, height

        #__________________________________________#
        #__________________________________________# 

        # Developer Information       

        developer_label = Label(main_frame, text = "Hello, My name is Developer1! ", font = ("ALEGREYA",15,"bold"), bg="#f0f1f1") #no editing
        developer_label.place(x=20,y=400, width = 370, height = 50) #startx, starty, width, height

        developer_label_2 = Label(main_frame, text = "Email: abcd@xyz.com", font = ("ALEGREYA",15,"bold"), bg="#f0f1f1") #no editing
        developer_label_2.place(x=20,y=460, width = 370, height = 50) #startx, starty, width, height

        developer_label_2 = Label(main_frame, text = "Phone: 9999999999", font = ("ALEGREYA",15,"bold"), bg="#f0f1f1") #no editing
        developer_label_2.place(x=20,y=520, width = 370, height = 50) #startx, starty, width, height

        developer_label_2 = Label(main_frame, text = "LinkedIn: https://www.linkedin.com/in/m/", font = ("ALEGREYA",15,"bold"), bg="#f0f1f1") #no editing
        developer_label_2.place(x=20,y=580, width = 379, height = 50) #startx, starty, width, height



#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = Developer(root) #class name
    root.mainloop()
    