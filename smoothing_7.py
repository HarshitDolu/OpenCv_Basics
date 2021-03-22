# smoothing images: remove noises and smooth edges
# low pass filters: removing noises, blurring
# HPF: find edges
# median filter is great when dealing with salt and pepper noise
# bilateral filter: preserve edges
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("images/water.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


kernel=np.ones((5,5),np.float32)/25

dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bfilter=cv2.bilateralFilter(img,9,75,75)


titles=['image','2D convulation','Blur','Gaussian Blur','median','Bilateral filter']
images=[img,dst,blur,gblur,median,bfilter]
siz=len(images)
for i in range(0,siz):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
