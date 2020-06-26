import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('maliao.jpg')
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 灰度化处理图像
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 高斯滤波
gaussian_blur = cv.GaussianBlur(gray_image, (3, 3), 0)

# Roberts 算子
kernelx = np.array([[-1, 0], [0, 1]], dtype = int)
kernely = np.array([[0, -1], [1, 0]], dtype = int)
x = cv.filter2D(gaussian_blur, cv.CV_16S, kernelx)
y = cv.filter2D(gaussian_blur, cv.CV_16S, kernely)
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Roberts = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# Prewitt 算子
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv.filter2D(gaussian_blur, cv.CV_16S, kernelx)
y = cv.filter2D(gaussian_blur, cv.CV_16S, kernely)
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# Sobel 算子
x = cv.Sobel(gaussian_blur, cv.CV_16S, 1, 0)
y = cv.Sobel(gaussian_blur, cv.CV_16S, 0, 1)
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 拉普拉斯算法
dst = cv.Laplacian(gaussian_blur, cv.CV_16S, ksize = 3)
Laplacian = cv.convertScaleAbs(dst)

# 展示图像
titles = ['Source Image', 'Gaussian Image', 'Roberts Image',
          'Prewitt Image','Sobel Image', 'Laplacian Image']
images = [rgb_img, gaussian_blur, Roberts, Prewitt, Sobel, Laplacian]
for i in np.arange(6):
   plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]), plt.yticks([])
plt.show()