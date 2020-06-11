import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
source = cv.imread("demo_noise_black.jpg", cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5), np.uint8)

# 闭运算
close = cv.morphologyEx(source, cv.MORPH_CLOSE, kernel)

# 黑帽运算
dst = cv.morphologyEx(source, cv.MORPH_BLACKHAT, kernel)

# 构造显示结果数组
titles = ['Source Img','Close Img', 'Tophat Img']
images = [source, close, dst]

# matplotlib 绘图
for i in range(3):
   plt.subplot(1, 3, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()