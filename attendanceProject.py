import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path='ImageAttendance'
Images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for i in myList:
    currImg=cv2.imread(f'{path}/{i}')
    Images.append(currImg)
    classNames.append(i.split('.')[0])
print(classNames)
formatTime='%D:%H:%M:%S'
def findEncoding(images):
    encodeList=[]
    for i in images:
        i=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(i)[0])
    return encodeList
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myList=f.readlines()
        nameList=[]
        for i in myList:
            nameList.append(i.split(',')[0])
        if name not in nameList:
            f.writelines(f'\n{name},{datetime.now().strftime(formatTime)}')

encodeList=findEncoding(Images)
print('Encoding Complete')

cap=cv2.VideoCapture(0)
while 1:
    success,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.50,0.50)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    currFaceFrame=face_recognition.face_locations(imgS)
    currEncodeFrame=face_recognition.face_encodings(imgS)
    for encodeFace,faceLoc in zip(currEncodeFrame,currFaceFrame):
        matches=face_recognition.compare_faces(encodeList,encodeFace)
        facedis=face_recognition.face_distance(encodeFace,encodeList)
        print(facedis)
        matchIndex=np.argmin(facedis)
        if matches[matchIndex]:
            print('You are '+classNames[matchIndex])
            markAttendance(classNames[matchIndex])
            y2,x1,y1,x2 =faceLoc
            y2, x1, y1, x2 =y2*2,x1*2,y1*2,x2*2
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)
            #cv2.rectangle(img, (x1, y1-35), (x2, y2), (255, 0, 255), cv2.FILLED)
            cv2.putText(img,classNames[matchIndex],(x1+6,y1+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
