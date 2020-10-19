import pyrebase
import json

firebaseConfig = {
    'apiKey': "AIzaSyBfc47Ji9QYXE8kkHt-uPyqAc97A05Axrw",
    'authDomain': "logindemo-c1fa2.firebaseapp.com",
    'databaseURL': "https://logindemo-c1fa2.firebaseio.com",
    'projectId': "logindemo-c1fa2",
    'storageBucket': "logindemo-c1fa2.appspot.com",
    'messagingSenderId': "242968190442",
    'appId': "1:242968190442:web:d82972eb21d1f2c8e0e693",
    'measurementId': "G-P8PHX0F432"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()



subjects = {
            "SE":{
                    'A':{'DE':0, 'DM':0,'DSA':0,'MP':0,'OOP':0},
                    'B':{'DE':0, 'DM':0,'DSA':0,'MP':0,'OOP':0},
                    'C':{'DE':0, 'DM':0,'DSA':0,'MP':0,'OOP':0}
                },
         
            "TE":{
                'A':{'CN':0,'DBMS':0,'ISEE':0,'TOC':0}, 
                'B':{'CN':0,'DBMS':0,'ISEE':0,'TOC':0},
                'C':{'CN':0,'DBMS':0,'ISEE':0,'TOC':0}
                },
          
            "BE":{
                'A':{'S1':0,'S2':0,'S3':0,'S4':0,'S5':0},
                'B':{'S1':0,'S2':0,'S3':0,'S4':0,'S5':0},
                'C':{'S1':0,'S2':0,'S3':0,'S4':0,'S5':0}               
                }
                            
            
            }




def reset_count(year,div):
    year=year.upper()
    div=div.upper()
    # Serializing json  
    db.child(year).child(div).set(subjects[year][div])
    
def reset_all():
    db.set(subjects)

def updateLectureCount(year,div,sub):
    year=year.upper()
    div=div.upper()
    sub=sub.upper()

    # This will get real time values of count 
    curr_count =db.get().val()
    json_object = json.dumps(curr_count, indent = 4) 
    with open("LectureCount.json", "w") as outfile: 
        outfile.write(json_object)


    with open("LectureCount.json", "r") as jsonFile:
        data = json.load(jsonFile)

    print(data[year])
    curr_value=data[year][(div)][sub]
    data[year][div][sub]=str(int(curr_value)+1)

    # Write the updated valuein db
    db.set(data)

    with open("LectureCount.json", "w+") as jsonFile:
        json.dump(data, jsonFile,indent=4)

    return data[year][div][sub]


# reset_count('te','b')
# print("My lecture Count is =", updateLectureCount('TE','b','toc'))
# reset_all()


