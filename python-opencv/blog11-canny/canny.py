import cv2 as cv
from matplotlib import pyplot as plt

# 图像读入
img = cv.imread('maliao.jpg', 0)
edges = cv.Canny(img, 100, 200)

# 显示结果
titles = ['Original Img', 'Edge Img']
images = [img, edges]

# matplotlib 绘图
for i in range(2):
   plt.subplot(1, 2, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()