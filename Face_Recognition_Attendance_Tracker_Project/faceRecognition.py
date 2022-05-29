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
from time import strftime
from datetime import datetime
#importing opencv
import cv2
import os
import numpy as np 

#__________________________________________#
#__________________________________________#

class face_Recognition:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("2240x1400+0+0") #setting height and width of the window 
        self.root.title("Face Recognition App")
        self.root.wm_iconbitmap("face.ico")

        #__________________________________________#
        #__________________________________________#

        #@TOP_label to be inserted on top (1)
        title_label=Label(self.root,text="FACE RECOGNITION", font = ("ALEGREYA",40,"bold"),bg="black",fg="white")
        #placing label on the window
        title_label.place(x=0, y=0,width=1540,height=70)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #@INSERT images (1)
        image_to_insert_1 = Image.open(r"images_to_be_used\image12.png") 
        image_to_insert_1=image_to_insert_1.resize((750,750),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture1=ImageTk.PhotoImage(image_to_insert_1)
        #making label
        label_image1 = Label(self.root,image=self.picture1)
        #placing label on the window
        label_image1.place(x=0,y=60, width = 750, height = 750) #startx, starty, width, height

        #@INSERT images (2)
        image_to_insert_2 = Image.open(r"images_to_be_used\image13.png") 
        image_to_insert_2=image_to_insert_2.resize((700,680),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picture2=ImageTk.PhotoImage(image_to_insert_2)
        #making label
        label_image2 = Label(self.root,image=self.picture2)
        #placing label on the window
        label_image2.place(x=700,y=60, width = 800, height = 680) #startx, starty, width, height

        #__________________________________________#
        #__________________________________________#

        #@MAKING BUTTON (1)
        button = Button(self.root, text = "START", command=self.face_recognition_func, cursor = "hand2", font = ("ALEGREYA",30,"bold"),bg="darkblue",fg="white")
        button.place(x=600, y=780, width = 200, height = 60)

        #__________________________________________#
        #__________________________________________#
        #ATTENDANCE_FUNCTIOM_HERE
    def attendance(self,fetched_data_id,fetched_data_name,fetched_data_dept,fetched_data_team):
        with open(r"attendance\attendance.csv","r+",newline="\n") as f:
            myData_list = f.readlines()
            name_list=[]
            for line in myData_list:
                entry=line.split((","))
                name_list.append(entry[0])
            if((fetched_data_id not in name_list) and (fetched_data_name not in name_list) and (fetched_data_dept not in name_list) and (fetched_data_team not in name_list)):
                now=datetime.now()
                date1=now.strftime("%d/%m/%Y")
                dateString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{fetched_data_id},{fetched_data_name},{fetched_data_dept},{fetched_data_team},{dateString},{date1},Present")

        #__________________________________________#
        #__________________________________________#

        #FACE_RECOGNITION_FUNCTIONS_HERE
    def face_recognition_func(self):
        def boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coordinates=[]
            #rectangle 
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select EmpName from employee where EmpId="+str(id))
                fetched_data_name=my_cursor.fetchone()
                fetched_data_name="+".join(fetched_data_name)

                my_cursor.execute("select EmpId from employee where EmpId="+str(id))
                fetched_data_id=my_cursor.fetchone()
                fetched_data_id="+".join(fetched_data_id)

                my_cursor.execute("select Dept from employee where EmpId="+str(id))
                fetched_data_dept=my_cursor.fetchone()
                fetched_data_dept="+".join(fetched_data_dept)

                my_cursor.execute("select Team from employee where EmpId="+str(id))
                fetched_data_team=my_cursor.fetchone()
                fetched_data_team="+".join(fetched_data_team)

                if confidence>77:
                    cv2.putText(img,f"Id: {fetched_data_id}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Name: {fetched_data_name}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Department: {fetched_data_dept}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Team: {fetched_data_team}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.attendance(fetched_data_id,fetched_data_name,fetched_data_dept,fetched_data_team)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Detected",(x,y-17),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                coordinates=[x,y,w,h]

            return coordinates
            
        def recogni(img, clf, faceCascade):
            coordinates=boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier_data.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recogni(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_capture.release()
        cv2.destroyAllWindows()

        #__________________________________________#
        #__________________________________________#
        


#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = face_Recognition(root) #class name
    root.mainloop()
#__________________________________________#
