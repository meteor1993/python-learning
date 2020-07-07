import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv.imread("maliao.jpg")
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#高斯滤波
gaussianBlur = cv.GaussianBlur(gray_img, (3,3), 0)

#阈值处理
ret, binary = cv.threshold(gaussianBlur, 127, 255, cv.THRESH_BINARY)

#Scharr算子
x = cv.Scharr(gray_img, cv.CV_32F, 1, 0) #X方向
y = cv.Scharr(gray_img, cv.CV_32F, 0, 1) #Y方向
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Scharr = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

#LOG算子
gaussian = cv.GaussianBlur(gray_img, (3,3), 0) #先通过高斯滤波降噪
dst = cv.Laplacian(gaussian, cv.CV_16S, ksize = 3) #再通过拉普拉斯算子做边缘检测
LOG = cv.convertScaleAbs(dst)

#效果图
titles = ['Source Image', 'Gray Image', 'Scharr Image', 'LOG Image']
images = [rgb_img, gray_img, Scharr,  LOG]

for i in np.arange(4):
   plt.subplot(2, 2, i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
