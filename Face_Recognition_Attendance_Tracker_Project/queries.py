#importing packages
from email import message
from logging import RootLogger
from tkinter import*
#used for making gui applications
from tkinter import ttk
from turtle import back 
#tookit
from PIL import Image, ImageTk
#used for images
from tkinter import messagebox
#importing mysql
import mysql.connector
#importing opencv
import cv2
from chatbot_model import chatwithus

class Queries:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #__________________________________________#
        #__________________________________________#

        #@TOP_label to be inserted on top of the background image
        title_label=Label(self.root,text="CHATBOT", font = ("ALEGREYA",40,"bold"),bg="black",fg="white")

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)

        #@label to be inserted on top of the background image
        label=Label(self.root,text="Feel Free to Contact Us:", font = ("ALEGREYA",20,"bold"),bg="light blue",fg="black")
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        label.place(x=600, y=80,width=400,height=58)

        #@INSERT images 
        image_to_insert = Image.open(r"images_to_be_used\image15.png") 
        image_to_insert=image_to_insert.resize((1000,800),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_to_insert)
        #making label
        label_image = Label(self.root,image=self.picture)
        #placing label on the window
        label_image.place(x=40,y=150, width = 1300, height = 800) #startx, starty, width, height

        
        #__________________________________________#
        #__________________________________________#

        #@FRAME
        main_frame = Frame(label_image, bd=2, bg="#f0f1f1") #border=2
        main_frame.place(x=950,y=20,width=370, height=50) #placing the frame

        #__________________________________________#
        #__________________________________________#

        # Email Information       
        developer_label = Label(main_frame, text = "Email: faceRecog@domain.com", font = ("ALEGREYA",15,"bold"), bg="#f0f1f1") #no editing
        developer_label.place(x=0,y=0, width = 370, height = 50) #startx, starty, width, height

        #==============CHATBOT===================#
        #@chatbot'CLICK' 
        image_chat_insert = Image.open(r"images_to_be_used\image17.png") 
        image_chat_insert=image_chat_insert.resize((200,230),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.photochat=ImageTk.PhotoImage(image_chat_insert)
        #making BUTTON
        button_chat = Button(label_image, image = self.photochat, cursor = "hand2",command=self.chat_bot)
        button_chat.place(x=1100, y=430, width = 190, height = 225)

        button_chat_1 = Button(label_image, text = "CHATBOT", cursor = "hand2",command=self.chat_bot, font = ("ALEGREYA",14,"bold"),bg="black",fg="white")
        button_chat_1.place(x=1101, y=654, width = 189, height = 40)

        #==============CHATBOT===================#
        

    def chat_bot(self):
        self.new_window=Toplevel(self.root)
        self.app=chatwithus(self.new_window)


#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = Queries(root) #class name
    root.mainloop()
    
