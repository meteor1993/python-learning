import cv2 as cv
import numpy as np

img = cv.imread("dahai.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 灰度图均衡化
equ = cv.equalizeHist(gray)
# 水平拼接原图和均衡图
result1 = np.hstack((gray, equ))
cv.imwrite('grey_equ.png', result1)

# 彩色图像均衡化,需要分解通道 对每一个通道均衡化
(b, g, r) = cv.split(img)
bH = cv.equalizeHist(b)
gH = cv.equalizeHist(g)
rH = cv.equalizeHist(r)
# 合并每一个通道
equ2 = cv.merge((bH, gH, rH))
# 水平拼接原图和均衡图
result2 = np.hstack((img, equ2))
cv.imwrite('bgr_equ.png', result2)