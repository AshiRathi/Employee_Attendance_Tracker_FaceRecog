from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from pip import main

class chatwithus:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("450x680+1020+210") #setting height and width 2240x1400+0+0 of the window 
        self.root.title("Chat With Us: Mr. ChatBot") 
        self.root.bind('<Return>',self.enter_works)
        self.root.wm_iconbitmap("face.ico")


        #_________________MAIN_FRAME____________________________#
        #@MAIN_FRAME
        main_frame = Frame(self.root, bd=2, bg="#f0f1f1", width=340) #border=4
        main_frame.pack()

        #__________________TOP_LABEL________________________#
        
        #@ image 
        image_insert_chat = Image.open(r"images_to_be_used\mr_chat_IMAGE.jpg") 
        image_insert_chat=image_insert_chat.resize((120,84),Image.ANTIALIAS) #resize images and convert from highlevel to lowlevel image
        self.picturechat=ImageTk.PhotoImage(image_insert_chat)

        title_label = Label(main_frame,relief=RAISED, anchor='nw', width=450, compound=LEFT,image=self.picturechat, text="ChatBot",font = ("ARIAL",40,"bold"),bg="white",fg="black")
        #placing label on the window
        title_label.pack(side=TOP)

        #_______________SCROLL_AREA_________________________#
        self.scroll_bar_y=ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text=Text(main_frame, width=65,height=22,bd=2,relief=RAISED,font=("ARIAL",15),yscrollcommand=self.scroll_bar_y.set)
        self.scroll_bar_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        #_______________frame_________________________#

        button_frame= Frame(self.root, bd=2, bg="#f0f1f1",width=450)
        button_frame.pack()

        #_______________text_label_________________________#

        text_label=Label(button_frame,text="Input Text:", font = ("ARIAL",12,"bold"),bg="#f0f1f1",fg="black")
        text_label.grid(row=0, column=0,padx=5,sticky=W)

        #_______________entry_box_________________________#
        self.entry=StringVar()
        self.entry_var=ttk.Entry(button_frame,textvariable=self.entry,width=27,font = ("ARIAL",12,"bold"))
        self.entry_var.grid(row=0,column=1,padx=5,sticky=W)

        #_______________send_button_________________________#
        self.send=Button(button_frame,text="Ask",command=self.ask,width=3,font = ("ARIAL",12,"bold"),bg="black",fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        #_______________clear_button_________________________#
        self.clear=Button(button_frame,text="Clear",command=self.clear_button,width=8,font = ("ARIAL",12,"bold"),bg="black",fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        #_______________text_label_________________________#

        self.msg=''
        self.text_label_1=Label(button_frame,text=self.msg, font = ("ARIAL",12,"bold"),bg="#f0f1f1",fg="red")
        self.text_label_1.grid(row=1, column=1,padx=5,sticky=W)

        #_______________function_________________________#

    def enter_works(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear_button(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def ask(self):
        ask='\t\t\t'+'Me: '+self.entry.get()
        self.text.insert(END,'\n'+ask)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.message="*Please enter text above"
            self.text_label_1.config(text=self.message,fg='red')
        else:
            self.message='' 
            self.text_label_1.config(text=self.message,fg='red')
        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: Hi, How may I help you?'+'\n',END)

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: Hello, How may I help you?'+'\n',END)

        elif(self.entry.get()=='how are you?'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot:Good, What about you?'+'\n',END)
        
        elif(self.entry.get()=='good'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: Amazing!'+'\n',END)
        
        elif(self.entry.get()=='who created you?'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: FaceRecognition_System_Creator'+'\n',END)

        elif(self.entry.get()=='can you speak any other languages?'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: I am still learning them'+'\n',END)

        elif(self.entry.get()=='what is face recognition?'):
            self.text.insert(END,'\n\n'+'Mr.ChatBot: Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition systems can be used to identify people in photos, videos, or in real-time.'+'\n',END)
        
        elif(self.entry.get()=='how does face recognition work?'):
            self.text.insert(END,'\n\n'+'Step 1: Face detection\nStep 2: Face analysis\nStep 3: Converting the image to data\nStep 4: Finding a match\n'+'\n',END)

        elif(self.entry.get()=='how is face recognition used?'):
            self.text.insert(END,'\n\n'+'The technology is used for a variety of purposes. These include:\nUnlocking phones\nAirports and border control\nFinding missing persons\nImproving retail experiences\nHealthcare\nRecognizing drivers, etc'+'\n',END)
        else:
            self.text.insert(END,'\n\n'+'Mr.ChatBot: Sorry, didn\'t get that?'+'\n',END)
            


#__________________________________________#
#__________________________________________#
if __name__ =="__main__":
    root = Tk() #calling the toolkit
    obj = chatwithus(root) #class name
    root.mainloop()
    
