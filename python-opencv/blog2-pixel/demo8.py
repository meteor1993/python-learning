import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('maliao.jpg',cv.IMREAD_COLOR)

# method1
b,g,r=cv.split(img)
img2=cv.merge([r,g,b])
plt.imshow(img2)
plt.show()

# method2
img3=img[:,:,::-1]
plt.imshow(img3)
plt.show()

# method3
img4=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img4)
plt.show()