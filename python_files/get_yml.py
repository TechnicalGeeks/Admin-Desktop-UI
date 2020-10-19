import pyrebase
import os
import sys

config ={
    "apiKey": "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
    "authDomain": "proxy-detection-1df22.firebaseapp.com",
    "databaseURL": "https://proxy-detection-1df22.firebaseio.com",
    "projectId": "proxy-detection-1df22",
    "storageBucket": "proxy-detection-1df22.appspot.com",
    "messagingSenderId": "17187188207",
    "appId": "1:17187188207:web:63e8c1f5b50862b1c59a1a",
    "vmeasurementId": "G-EPTQX1DS4L"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_cloud = 'yml/'

def get_yml(year,div):
    year=year.upper()
    div=div.upper()
    yml_name = year+'-'+div+'.yml'
    yml = 'yml'+'/'+year+"/"+yml_name
    print(yml)
    if os.path.isfile(yml):
        print("Yes File Exists")
        return yml    

    elif os.path.isdir("yml"):
        if os.path.isdir("yml/"+year):
            print("In YEAR downloading")
            
        else:
            print("making folder of year")
            os.makedirs("yml/"+year)
        print("Downloading ....")
        # storage.child(yml).download(filename=yml,path=yml)    
        print("Yml downloaded Successfully as you dont hace yml folder")            

    else:
        os.makedirs("yml/"+year)
        print("Downloading ....")
        storage.child(yml).download(filename=yml,path=yml)    
        print("Yml downloaded Successfully as you dont hace yml folder")            

    if os.path.isfile(yml) != True:
        print("*************** FILE DONOT EXIST IN DATABASE *********")

    return yml


def put_yml(year,div):
    year=year.upper()
    div=div.upper()
    yml_name = year+'-'+div+'.yml'
    yml = 'yml'+'/'+year+"/"+yml_name
    local_path = yml_name
    # print(os.getcwd())
    # print(local_path)
    try:
        print("***  Uploading yml please wait ***\n Upoading . . . . . . . \n")
        storage.child(yml).put(yml_name)
        print("___ YML ____ Uploaded Succesfully")
        os.remove(yml_name)
        print(yml)
    except:
        print("Hey !!! yml file donot exist")

# get_yml('TE','B')        
# put_yml('TE','B')