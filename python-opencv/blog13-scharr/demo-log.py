import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread("maliao.jpg")
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 先通过高斯滤波降噪
gaussian = cv.GaussianBlur(gray_img, (3, 3), 0)

# 再通过拉普拉斯算子做边缘检测
dst = cv.Laplacian(gaussian, cv.CV_16S, ksize=3)
LOG = cv.convertScaleAbs(dst)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图形
titles = ['原始图像', 'LOG 算子']
images = [rgb_img, LOG]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
