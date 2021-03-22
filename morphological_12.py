# on binary images
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("images/smarties.jpg",0)

_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((2,2),np.uint8)
dilation= cv2.dilate(mask,kernel,iterations=2)
erosion=cv2.erode(mask,kernel,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) # another name of erosion followed by dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) # first dilation then erosion
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) # dilation-erosion
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel) # img-opening

images=[img,mask,dilation,erosion,opening,closing,mg,th]
titles=['image','mask','dilation','erosion','opening','closing','gradient','tophat']
siz=len(titles)

for i in range(0,siz):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()