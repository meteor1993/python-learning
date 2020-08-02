import cv2 as cv
import numpy as np

img = cv.imread('clahe_src.jpg', 0)

# 全局直方图均衡
equ = cv.equalizeHist(img)

# 自适应直方图均衡
clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
cl1 = clahe.apply(img)

# 水平拼接三张图像
result1 = np.hstack((img, equ, cl1))

cv.imwrite('clahe_result.jpg', result1)