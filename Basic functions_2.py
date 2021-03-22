import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread("images/lena.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32) / 25  # matrix that modify pixel intensity

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                 # converting BGR to Gray scale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0) #smoothing images
imgFilter=cv2.filter2D(img,-1,kernel)  # filtering images
imgCanny=cv2.Canny(img,150,200) # detecting images
imgDialation= cv2.dilate(imgCanny,kernel,iterations=1)  # increase thickness of edges
imgEroded= cv2.erode(imgDialation,kernel,iterations=1)   # increase thinness of edges


images=[img,imgGray,imgBlur,imgFilter,imgCanny,imgDialation,imgEroded]
titles=['image','Gray scale','Blur','Filter','Canny','Dialation','Erosion']
siz=len(titles)

for i in range(0,siz):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()