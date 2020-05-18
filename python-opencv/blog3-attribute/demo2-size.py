import cv2 as cv

# 读取彩色图片
color_img = cv.imread("maliao.jpg", cv.IMREAD_ANYCOLOR)

print(color_img.size)

# 读取灰度图片
gray_img = cv.imread("maliao.jpg", cv.IMREAD_GRAYSCALE)

print(gray_img.size)