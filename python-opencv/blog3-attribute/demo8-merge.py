import cv2 as cv
import numpy as np

# 读取图片
img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 拆分通道
b = img[:, :, 0]
g = np.zeros((rows,cols), dtype=img.dtype)
r = np.zeros((rows,cols), dtype=img.dtype)

# 合并图像通道
m = cv.merge([b, g, r])

cv.imshow('merge', m)

# 等待显示
cv.waitKey(0)
cv.destroyAllWindows()