import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('maliao.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Sobel 算子
x = cv.Sobel(grayImage, cv.CV_16S, 1, 0)
y = cv.Sobel(grayImage, cv.CV_16S, 0, 1)

# 转 uint8 ,图像融合
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图形
titles = ['原始图像', 'Sobel 算子']
images = [rgb_img, Sobel]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()