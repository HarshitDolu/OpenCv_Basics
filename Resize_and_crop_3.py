#Resize and crop
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("images/lena.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)

imgResize=cv2.resize(img,(1000,500))
imgCropped=img[0:200,200:500]

#v2.imshow("Image", img)
#cv2.imshow("Image Resize",imgResize)
#cv2.imshow("Image Cropped", imgCropped)

images=[img,imgResize,imgCropped]
titles=['image','Resize','Cropped']
siz=len(titles)

for i in range(0,siz):
    plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)