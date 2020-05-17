import cv2 as cv

# 读取灰度图像
gray_img = cv.imread("maliao.jpg", cv.IMREAD_GRAYSCALE)
print(gray_img.item(20, 30))

# 读取彩色图像
color_img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)

blue = color_img.item(20, 30, 0)
print(blue)

green = color_img.item(20, 30, 1)
print(green)

red = color_img.item(20, 30, 2)
print(red)