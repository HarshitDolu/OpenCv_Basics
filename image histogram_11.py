# histogram is a graph that gives intensity distribution of image.

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("images/lena.png")

b, g, r =cv2.split(img)

#plt.hist(img1.ravel(),256,[0,256])
#hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

# y: total pixels
# x: intensity
cv2.imshow("image",img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

