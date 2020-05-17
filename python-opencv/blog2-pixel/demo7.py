import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('maliao.jpg', cv.IMREAD_COLOR)
plt.imshow(img)
plt.show()