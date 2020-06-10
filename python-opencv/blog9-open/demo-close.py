import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
source = cv.imread("demo_noise_black.jpg", cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5),np.uint8)

# 图像膨胀
dilate_result = cv.dilate(source, kernel)

# 图像腐蚀
erode_img = cv.erode(dilate_result, kernel)

# 显示结果
titles = ['Source Img','Dilate Img','Erode Img']
images = [source, dilate_result, erode_img]

# matplotlib 绘图
for i in range(3):
   plt.subplot(1, 3, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()