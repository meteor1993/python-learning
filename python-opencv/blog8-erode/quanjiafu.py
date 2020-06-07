import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
source = cv.imread('demo.png', cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5),np.uint8)

# 图像腐蚀
erode_img = cv.erode(source, kernel)

# 图像膨胀
dilate_result = cv.dilate(source, kernel)

# 显示结果
titles = ['Source Img','Erode Img','Dilate Img']
images = [source, erode_img, dilate_result]

# matplotlib 绘图
for i in range(3):
   plt.subplot(1, 3, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()