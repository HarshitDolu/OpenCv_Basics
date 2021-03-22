# Hough transform is a technique to detect any shape, if you represent that shape in
#mathematical form.

#Standard Hough Transform : using hough lines method
import cv2
import numpy as np

img=cv2.imread("images/sudoku.jpg")
img1=cv2.resize(img,(512,512))
img2=img1.copy()
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,100,apertureSize=3)
edges2=cv2.Canny(gray2,50,100,apertureSize=3)
lines=cv2.HoughLines(edges, 1, np.pi/180 ,200)  # polar coordinate
#(imgsrc, distance reso, theta, threshold)

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)

    x0=a*rho  # top left corner of image
    y0=b*rho

    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))

    cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)


lines1=cv2.HoughLinesP(edges2,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for l in lines1:
    x1,y1,x2,y2= l[0]
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("image_standard_HT",img1)
cv2.imshow('image_Probablistic_HT',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


