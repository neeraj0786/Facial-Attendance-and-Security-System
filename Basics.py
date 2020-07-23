import cv2
import numpy as np
import face_recognition


imgElon=face_recognition.load_image_file("ImageBasics/ElonMusk.jpeg")
imgTest=face_recognition.load_image_file("ImageBasics/ElonMuskTest.jpeg")
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

imgLoc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (imgLoc[3], imgLoc[0]), (imgLoc[1], imgLoc[2]), (255, 0, 255), 2)

imgLocTest=face_recognition.face_locations(imgTest)[0]
encodeElonTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (imgLocTest[3],imgLocTest[0]),(imgLocTest[1],imgLocTest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeElon],encodeElonTest)
facedis=face_recognition.face_distance([encodeElon],encodeElonTest)
print(results,facedis)

cv2.putText(imgTest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
#cv2.imshow('Elon Musk', imgElon)
#cv2.imshow('Elon Test', imgTest)
#cv2.waitKey(0)



