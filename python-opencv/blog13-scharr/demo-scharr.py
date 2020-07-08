import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("maliao.jpg")
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Scharr 算子
x = cv.Scharr(gray_img, cv.CV_16S, 1, 0) # X 方向
y = cv.Scharr(gray_img, cv.CV_16S, 0, 1) # Y 方向
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Scharr = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示图形
plt.rcParams['font.sans-serif']=['SimHei']

titles = ['原始图像', 'Scharr 算子']
images = [rgb_img, Scharr]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
