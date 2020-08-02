import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("xueshan.jpg")
# 参数:原图像 通道[0]-B 掩码 BINS为256 像素范围0-255
histB = cv.calcHist([img], [0], None, [256], [0, 255])
histG = cv.calcHist([img], [1], None, [256], [0, 255])
histR = cv.calcHist([img], [2], None, [256], [0, 255])

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

plt.plot(histB, color='b')
plt.plot(histG, color='g')
plt.plot(histR, color='r')
plt.show()
