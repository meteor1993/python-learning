import cv2 as cv

img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

# 拆分通道
b, g, r = cv.split(img)

# 合并图像通道
m = cv.merge([b, g, r])

cv.imshow('merge', m)

# 等待显示
cv.waitKey(0)
cv.destroyAllWindows()