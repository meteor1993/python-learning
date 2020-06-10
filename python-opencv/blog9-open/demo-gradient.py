import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
source = cv.imread("demo.png", cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5), np.uint8)

# 图像膨胀
dilate = cv.morphologyEx(source, cv.MORPH_DILATE, kernel)

# 图像腐蚀
erode = cv.morphologyEx(source, cv.MORPH_ERODE, kernel)

# 图像梯度运算
gradient = cv.morphologyEx(source, cv.MORPH_GRADIENT, kernel)

# 显示结果
titles = ['Source Img', 'Dilate Img', 'Erode Img', 'Gradient Img']
images = [source, dilate, erode, gradient]

# matplotlib 绘图
for i in range(4):
   plt.subplot(1, 4, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()