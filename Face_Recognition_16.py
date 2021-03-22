import cv2
import numpy as np
import face_recognition

# load images
# step 1
imgHar=face_recognition.load_image_file('images/lena.png')
imgHar=cv2.cvtColor(imgHar,cv2.COLOR_BGR2RGB)


imgTest=face_recognition.load_image_file('images/lena.png')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

# step 2
faceLoc =face_recognition.face_locations(imgHar)[0] # 4 values
encodeHar=face_recognition.face_encodings(imgHar)[0]
cv2.rectangle(imgHar,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


faceLocTest =face_recognition.face_locations(imgTest)[0] # 4 values
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

# encodings 128 measurements in backend
# face distance similarity
#lower distance, better match

#encoding match
results=face_recognition.compare_faces([encodeHar],encodeTest)

# face distance
faceDis=face_recognition.face_distance([encodeHar],encodeTest)
#print(results)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
#print(imgTest.shape)

imgHar=cv2.resize(imgHar,(0,0),None,0.5,0.5)
cv2.imshow('Harshit Jain',imgHar)
cv2.imshow('Harshit Test',imgTest)

cv2.waitKey(0)