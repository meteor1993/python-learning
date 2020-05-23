import cv2 as cv
import numpy as np

#读取图片
src = cv.imread('maliao.jpg')
rows, cols = src.shape[:2]

# 定义移动距离
tx = 50
ty = 100

# 生成 M 矩阵
affine = np.float32([[1, 0, tx], [0, 1, ty]])
dst = cv.warpAffine(src, affine, (cols, rows))

# 显示图像
cv.imshow('src', src)
cv.imshow("dst", dst)

# 等待显示
cv.waitKey(0)
cv.destroyAllWindows()