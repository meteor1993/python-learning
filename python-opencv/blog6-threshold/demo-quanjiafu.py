import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img=cv.imread('maliao.jpg')
lenna_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 阈值化处理
ret1, thresh1=cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
ret2, thresh2=cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY_INV)
ret3, thresh3=cv.threshold(gray_img, 127, 255, cv.THRESH_TRUNC)
ret4, thresh4=cv.threshold(gray_img, 127, 255, cv.THRESH_TOZERO)
ret5, thresh5=cv.threshold(gray_img, 127, 255, cv.THRESH_TOZERO_INV)

# 显示结果
titles = ['Gray Img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [gray_img, thresh1, thresh2, thresh3, thresh4, thresh5]

# matplotlib 绘图
for i in range(6):
   plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()
