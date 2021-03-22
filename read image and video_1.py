import cv2
import numpy as np
# Read and show images

img=cv2.imread('Resources/pic5.jpeg')
print(img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Read video

frameWidth=640
frameHeight=480

cap=cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success,img= cap.read()
    cv2.imshow("Image",img)
    if cv2.waitKey(1) and 0xFF== ord('q'):
        break