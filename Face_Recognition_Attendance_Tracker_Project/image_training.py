#importing packages
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
import numpy as np 
#reference

#LBPH Algorithm:https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b: http://www.scholarpedia.org/article/Local_Binary_Patterns

#__________________________________________#
#__________________________________________#

class Model_Training:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #__________________________________________#
        #__________________________________________#

        #@TOP_label to be inserted on top of the background image
        title_label=Label(self.root,text="DATASET TRAINING", font = ("ALEGREYA",40,"bold"),bg="black",fg="white")
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=58)

        #__________________________________________#
        #__________________________________________#

        #@INSERT images 
        image_to_insert = Image.open(r"images_to_be_used\image1.jpeg") 
        image_to_insert=image_to_insert.resize((1490,720),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture=ImageTk.PhotoImage(image_to_insert)
        #making label
        label_image = Label(self.root,image=self.picture)
        #placing label on the window
        label_image.place(x=40,y=150, width = 1400, height = 720) #startx, starty, width, height

        #__________________________________________#
        #__________________________________________#

        #@MAKING BUTTON
        button = Button(self.root, text = "Click here to train the data", command = self.training_classifier, cursor = "hand2", font = ("ALEGREYA",29,"bold"),bg="lightblue",fg="black")
        button.place(x=40, y=70, width = 1400, height = 60)

        #__________________________________________#
        #__________________________________________#

    def training_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehension

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') #convert to grayscale image
                #convert image to grids
                imageNp=np.array(img, 'uint8') #datatype
                id=int(os.path.split(image)[1].split('.')[1])

                #index 0: C:\Users\ashir\Desktop\Face_Recognition_Project_Python\data\
                #index 1: user.1.1.jpg

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13 #press enter to close the opened window
            #convert ids to numpy
            ids=np.array(ids) #enhances perform
            #__________________________________________#
            #training the classifier + saving
            clf=cv2.face.LBPHFaceRecognizer_create()
            #algorithm
            clf.train(faces,ids)
            clf.write("classifier_data.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Dataset Training Is Completed", parent=self.root)


#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = Model_Training(root) #class name
    root.mainloop()
#__________________________________________#