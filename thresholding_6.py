# segmentation  technique

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/sudoku.jpg',0)
img=cv2.resize(img,(512,512))
# simple thresholding
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)


# adaptive thresholding
# smaller region of images

th6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY,11,2)
th7=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C
                          ,cv2.THRESH_BINARY,11,2)

titles=['original image','Binary','Inv_Binary','Trunc','Tozero_Inv','Tozero','Adapt_mean','Adapt_Gaussian']
siz=len(titles)
images=[img,th1,th2,th3,th4,th5,th6,th7]

for i in range(0,siz):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()








