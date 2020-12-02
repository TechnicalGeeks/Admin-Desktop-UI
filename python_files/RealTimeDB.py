import csv 
import pyrebase
from datetime import *
from getTotalLectureCount import *
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

subjects = {"SE":{'name':'null','DE':0, 'DM':0,'DSA':0,'MP':0,'OOP':0},"TE":{'name':'null','CN':0,'DBMS':0,'ISEE':0,'TOC':0}, "BE":{'name':'null','S1':0,'S2':0,'S3':0,'S4':0,'S5':0}}



""" 
Columns in Csv 
 Year	roll_no	Div	name	
  
  """
def AddNewDataset():
    with open('Sinfo.csv','r') as f:
        csvfile = csv.reader(f, delimiter=',')
        next(csvfile, None)
        for lines in csvfile:
            subjects[str(lines[0])]['name']=str(lines[3])
            db.child(str(lines[0])).child(str(lines[2])).child(str(lines[1])).set(subjects[str(lines[0])])
        

def AddnewStudent(year,div,roll,name):
    with open(r'Sinfo.csv','a+',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([str(year),str(roll),str(div),str(name)])

    subjects[str(year)]['name']=str(name)
    db.child(str(year)).child(str(div)).child(str(roll)).set(subjects[str(year)])    

def inputs():
    name = input("Enter Name:- ")
    year = input("Enter Year:- ")
    divn = input("Enter Division:- ")
    roll_no = input("Enter Roll:- ")
    AddnewStudent(year=year,name=name,roll=roll_no,div=divn)


def getAttendance(year,div): 
    x = datetime.now()
    file_name=str(x.strftime("%d-%m-AttendanceReport.csv"))

    # Generate Attendance in CSV format
    f = open(file_name,'w' ,newline='')
    writer = csv.writer(f)
    # writer.writerow(subjects[str(year)])
    print(subjects[str(year)].keys())
    
    # headings =[]
    # heading = subjects[str(year)].keys()
    # for head in heading:
    #     headings.append(str(head))

    # headings.insert(0,"Roll_Number")
    # print(headings)
    # writer.writerow(headings)

    roll_list = db.child(str(year)).child(str(div)).get()
    for rollno in roll_list.each():
        row =[ ]
        print(rollno.key())
        # Get Roll number
        row.append(str(rollno.key()))
        print(rollno.val()['name'])
        row.append(rollno.val()['name'])
        # for sub in rollno.val():
        #     # Get Sub  Name And ATTENDANCE
        #     if str(sub) != 'name':
        #         print(sub,rollno.val()[str(sub)])
        #         row.append(rollno.val()[str(sub)])
           
        print(row)
        writer.writerow(row)
        print("*****************")   
    f.close()


def updateAttendance(year,div,sub):
        year=year.upper()
        div=div.upper()
        sub=sub.upper()
        print("--------  Updating LEcture Count T0 Firebase ------ ")
        total_lec =updateLectureCount(year=year,div=div,sub=sub)
        if int(total_lec)!=0:
            pre_lec = int(total_lec)-1
        else:
            pre_lec=0    
        gen_att  = open('temporary.csv','r')
        csvreader= csv.reader(gen_att)
        for roll in csvreader:
            print(roll[0],roll[2])
            temp=db.child(str(year)).child(str(div)).child(str(roll[0])).get()

            if roll[2] == 'present' :
                # get Current count+1
                print("Attendance Before :- ",temp.val()[str(sub)])
                print("Present hai : -")
                attendend=0
                new_attend=0
                
                attendend = round((int(temp.val()[str(sub)])*int(pre_lec))/100)
                new_attend = attendend+1
                upd_attendance = new_attend*100/int (total_lec)
                upd_attendance=round(upd_attendance)
                print("Attendance After : ",upd_attendance)


                # demo=str(int(temp.val()[str(sub)])+100)
                db.child(str(year)).child(str(div)).child(str(roll[0])).update({str(sub):str(upd_attendance)})
                # print("After update",demo)
            else:
                # Attendance update nahi ki hai abhi tak
                print("Absent hai : -")
                attendend = round((int(temp.val()[str(sub)])*int(pre_lec))/100)
                new_attend = attendend
                upd_attendance = new_attend*100/int (total_lec)
                upd_attendance=round(upd_attendance)
                print("Attendance After : ",upd_attendance)

                db.child(str(year)).child(str(div)).child(str(roll[0])).update({str(sub):str(upd_attendance)})

                pass


# AddNewDataset()
# inputs()
# getAttendance('TE','B')
# updateAttendance('TE','B','CN')    











