import cv2
import numpy as np
from PIL import Image
import os
from get_yml import *




recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
path1 = '../Dataset'
for classes in os.listdir(path1):
    path2=os.path.join(path1,classes)
    for division in os.listdir(path2):
        path=os.path.join(path2,division)
        def getLabels(path):
            faceslist=[]
            ids=[]
            for id in os.listdir(path):
                for image in os.listdir(os.path.join(path,id)):
                    PIL_img = Image.open(os.path.join(os.path.join(path,id),image))
                    img_numpy = np.array(PIL_img,'uint8')
                    print(img_numpy)
                    faces = detector.detectMultiScale(img_numpy)
                    for (x,y,w,h) in faces:               
                        faceslist.append(img_numpy[y:y+h,x:x+w])
                        ids.append(id.split('.')[0])
            return faceslist,ids
        print ("Model training please wait...... \n")
        faces,ids = getLabels(path)
        for i in range(0, len(ids)):
            ids[i] = int(ids[i])
        recognizer.train(faces, np.array(ids))
        recognizer.write('{}-{}.yml'.format(classes,division)) 
        # path_cloud = 'yml/'+classes+'/'+division+'/'+classes+'-'+division+'.yml'
        put_yml(classes,division)
        print("\n\n ---  Model Trained And Uploaded Success Fully ---")
