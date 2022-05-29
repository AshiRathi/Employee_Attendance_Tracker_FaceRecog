# Employee_Attendance_Tracker_FaceRecog + CHATBOT

The proposed project is a smart method for managing attendance and record-keeping using face recognition.

<img width="887" alt="image" src="https://user-images.githubusercontent.com/91864520/170822340-993f0ff3-2a6b-4637-b36c-2ab15cfb4250.png">

# INTRODUCTION:

Mr. Pablo Picasso, epitome of art, once quoted, “Who sees the human face correctly: the photographer, the mirror, or the painter?” - 
I'll add to it, its indeed the code. 

# FACE RECOGNITION:

Face is the representation of one’s identity. Today, it is considered to be the most natural of all biometric measurements . And for a good reason, we recognize ourselves not by looking at our fingerprints or irises, for example, but by looking at our faces.  Of course, other signatures via the human body also exist, such as fingerprints, iris scans, voice recognition, digitization of veins in the palm, and behavioral measurements.
Why face recognition, then? 
Facial biometrics continues to be the preferred biometric benchmark. That is because it is easy to deploy and implement and there is no physical interaction with the end-user. Moreover, face detection and face match processes for verification/identification are speedy.
How does face recognition work? 
Facial technology systems can vary, but in general, they tend to include four operational steps:

Step 1: Face detection

Step 2: Face analysis

Step 3: Converting the image to data

Step 4: Finding a match from the existing database

# ATTENDANCE TRACKING:

Every organization requires a robust and stable system to record the attendance of their students. and every the organization have their method to do so, some are taking attendance manually with a sheet of paper and some have adopted biometrics systems such as fingerprints, RFID cardreader, Iris system to mark the attendance. In the RFID card system, each employee is assigned a card with their the corresponding identity but there is a chance of card loss or an unauthorized person may misuse the card for fake attendance. While in other biometrics such as fingerprint, iris or voice recognition, they all are not 100% accurate.

# METHODOLOGY:

<img width="887" alt="image" src="https://user-images.githubusercontent.com/91864520/170822225-3eecc5be-5c01-4103-93f3-37530e7b4aa6.png">

<img width="887" alt="image" src="https://user-images.githubusercontent.com/91864520/170822236-8a4e4cda-1271-4b4f-bd20-552ceb36ff52.png">

<img width="888" alt="image" src="https://user-images.githubusercontent.com/91864520/170822244-957fd6df-7668-4693-9b1e-364249d81029.png">

<img width="888" alt="image" src="https://user-images.githubusercontent.com/91864520/170822258-324bff40-a9e3-45de-9bfd-bc2fcabb8dde.png">

<img width="888" alt="image" src="https://user-images.githubusercontent.com/91864520/170822289-8ede0240-9063-410c-808f-0acdf63bc340.png">

<img width="888" alt="image" src="https://user-images.githubusercontent.com/91864520/170822293-89b7f507-ce3b-4a29-b457-a3fd19f7df83.png">

<img width="886" alt="image" src="https://user-images.githubusercontent.com/91864520/170822306-252bcddb-2d0d-4f25-8a45-8e88a22986b8.png">

# LIBRARIES:

- Numpy - could be a library for Python, adding support for multi-dimensional arrays and matrices, in conjunction with an enormous assortment of high-level mathematical functions to operate on these arrays.
- Pandas - is a fast, powerful, flexible, and easy to use open-source data analysis and manipulation tool, built on top of the Python programming language.
- Haar Cascade - is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of features proposed by Paul Viola and Michael Jones in their paper "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001.
- Datetime - It’s a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and info.
- Face_Recognition - Recognize and manipulate faces from Python or the command line with the world’s simplest face recognition library. 
- OpenCV - a library of programming functions primarily geared toward real-time computer vision.
pip install opencv-contrib-python
pip install numpy
pip install pandas
pip install Pillow

# INSTRUCTIONS TO RUN:

- First download or clone the project
- Import the project to your favourite IDE
- Create a python enviroment
- Install all the packages
- Run the project using the command line or your IDE Run Button

# REQUIREMENTS:

MySql:
- PASSWORD: 1234

Login Page:
- USERNAME: bb@gmail.com
- PASSWORD: bb

<img width="887" alt="image" src="https://user-images.githubusercontent.com/91864520/170822780-1ca066ea-7ba4-4297-b73c-12bcc8b44571.png">

<img width="887" alt="image" src="https://user-images.githubusercontent.com/91864520/170822830-4a20716a-e26b-4d40-9cf3-5909f45a4286.png">

Used: tkinter, pillow, mysql, cv2, time, os, datetime, numpy, opencv, haarcascade_frontalface_default.xml, tcl86t.dll, tk86t.dll

Database: MySql

Languages: Python and MySql

Face Recognition Algorithms: Haar Cascade, LBPH (Local Binary Pattern Histogram)


Softwares Used - VS CODE, MySql Workbench, Git

pip install numpy
pip install opencv-python
pip install pillow
pip install face_recognition

TO RUN:
- VISUAL STUDIO BUILD TOOLS Version 14 or above
- cx_freeze
- C:\Users\ashir\AppData\Local\Programs\Face Recognition\
- python setup.py bdist_msi

Following functionalities can be performed:
• Login
• Register new employees to the system
• Add employee photos to the training data set
• Train the model
• View attendance report of all employees. 
• Ask queries to the chatbot.

# RESOURCES:

The facial features are registered into the database folder by using the facial recognition xml file from the ‘OpenCV’ python library. Once the features are registered, the model is trained using the gathered features. The facial features are fetched from the database and the face of the student is recognized by comparing with existing values in the database. Facial Recognition is done using ‘OpenCV’ python library, particularly using ‘haarcascade’ code.

# LINKS:

GITHUB: https://github.com/AshiRathi/Employee_Attendance_Tracker_FaceRecog.git

PRESENTATION: [https://drive.google.com/file/d/1bv333gbraPcSkHkIgiVXbrX1JKuKNB8C/view?usp=sharing]

DRIVE: [https://drive.google.com/drive/folders/1kTIkgdzLBcqv38lmqN9JG8e4gWxAdDnU?usp=sharing]


# PROCESS:

<img width="884" alt="image" src="https://user-images.githubusercontent.com/91864520/170822320-da141c91-aca1-439d-9374-3da71f0219ce.png">

# REFERENCES:

<img width="886" alt="image" src="https://user-images.githubusercontent.com/91864520/170822325-01fad7d0-688e-43fe-9661-d860370d7093.png">
