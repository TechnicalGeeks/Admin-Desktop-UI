import cv2
import csv
import numpy as np
import os 
from datetime import datetime

import pyrebase
from getTotalLectureCount import *
from get_yml import *
from fractions import Fraction

firebaseConfig = {
    'apiKey': "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
    'authDomain': "proxy-detection-1df22.firebaseapp.com",
    'databaseURL': "https://proxy-detection-1df22.firebaseio.com",
    'projectId': "proxy-detection-1df22",
    'storageBucket': "proxy-detection-1df22.appspot.com",
    'messagingSenderId': "17187188207",
    'appId': "1:17187188207:web:63e8c1f5b50862b1c59a1a",
    'measurementId': "G-EPTQX1DS4L"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


x = datetime.now()
file_name=str(x.strftime("%d-%m-AttendanceReport.csv"))
def getAttendance(year,div): 
    # Generate Attendance in CSV format
    f = open(file_name,'w' ,newline='')
    writer = csv.writer(f)
    print(subjects[str(year)].keys())
    roll_list = db.child(str(year)).child(str(div)).get()
    for rollno in roll_list.each():
        row =[ ]
        print(rollno.key())
        # Get Roll number
        row.append(str(rollno.key()))
        print(rollno.val()['name'])
        row.append(rollno.val()['name'])
        row.append("Absent")
        print(row)
        writer.writerow(row)
        print("*****************")   
    f.close()
getAttendance('TE','B')


recognizer = cv2.face.LBPHFaceRecognizer_create()
yml_path =get_yml('TE','B')
recognizer.read(yml_path)
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
names={}
path='Dataset/TE/B'
for id in os.listdir(path):
    names[int(id.split('.')[0])]=id.split(".")[1]

print(names)    
cam = cv2.VideoCapture(0)
cap = cv2.VideoCapture("https://192.168.0.100:8080/video")

cam.set(3, 640) 
cam.set(4, 480) 

cap.set(3, 480) 
cap.set(4, 420)
 
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

dminW = 0.1*cap.get(3)
dminH = 0.1*cap.get(4)

def listToString(s):   
    str1 = ""     
    for ele in s:  
        str1=str1+ele+","
    str1=str1[:-1]    
    return str1 

def markAttendance(id,name):
    with open(file_name,'r+') as file:
        currentAtt = file.readlines()
        no=0
        for line in currentAtt:
            line=line.split(',')
            if id==int(line[0]):
                print("Marked")
                line[2]="present\n"
            currentAtt[no]=listToString(line)
            no=no+1
        file.close()
        with open(file_name, 'w') as file:
            file.writelines(currentAtt)

def demarkAttendance(id,name):
    with open (file_name,'r+') as file: 
        currentAtt = file.readlines()
        no=0
        for line in currentAtt:
            line=line.split(',')
            if id==int(line[0]):
                print("Demark")
                line[2]="BacktoAbsent\n"
            currentAtt[no]=listToString(line)
            no=no+1
        file.close()
        with open(file_name, 'w') as file:
            file.writelines(currentAtt)
        
while True:

    ret, img =cam.read()
    dret,dimg= cap.read()
    
    

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dgray = cv2.cvtColor(dimg,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )
    dfaces = faceCascade.detectMultiScale( 
        dgray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(dminW), int(dminH)),
    )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        # print(id)
        if (confidence < 80):
            name = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            markAttendance(id,name)
        else:
            name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(
                    img, 
                    str(name), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    img, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )                    
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

    for(x,y,w,h) in dfaces:
        cv2.rectangle(dimg, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(dgray[y:y+h,x:x+w])
        if (confidence < 80):
            name = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            demarkAttendance(id,name)
        else:
            name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(
                    dimg, 
                    str(name), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    dimg, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )  
    
    
    
    dimg = cv2.resize(dimg,(720,480)) 
    img = cv2.resize(img,(720,480))
    cv2.imshow('WebCam',img)         
    cv2.imshow('Pcam',dimg) 
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cap.release()
cv2.destroyAllWindows()
