import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import sys
from joblib import dump ,load

path='ImageAttendance'
Images=[]
myList=os.listdir(path)
print(myList)
classNames = []
for i in myList:
    currImg=cv2.imread(f'{path}/{i}')
    Images.append(currImg)
    classNames.append(i.split('.')[0])

print(classNames)
dump(classNames,'names.joblib')

def findEncoding(images):
    encodeList=[]
    for i in images:
        i=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(i)[0])
    return encodeList
encodeList = findEncoding(Images)
dump(encodeList,'enc.joblib')

