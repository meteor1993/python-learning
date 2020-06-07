import cv2 as cv
import numpy as np

# 图像读取
source = cv.imread("test.png", cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5),np.uint8)

# 进行图像腐蚀，默认迭代 1 次
dst = cv.erode(source, kernel, iterations=5)

# 图像显示
cv.imshow("source", source)
cv.imshow("dst", dst)

# 等待操作
cv.waitKey(0)
cv.destroyAllWindows()