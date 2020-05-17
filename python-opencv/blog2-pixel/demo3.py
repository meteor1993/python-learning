import cv2 as cv

# 灰度图像读取
gray_img = cv.imread("maliao.jpg", cv.IMREAD_GRAYSCALE)
print(gray_img[20, 30])
# 像素赋值
gray_img[20, 30] = 255
print(gray_img[20, 30])

# 彩色图像读取
color_img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)
print(color_img[20, 30])
# 像素依次赋值
color_img[20, 30, 0] = 255
color_img[20, 30, 1] = 255
color_img[20, 30, 2] = 255
print(color_img[20, 30])
# 像素一次赋值
color_img[20, 30] = [0, 0, 0]
print(color_img[20, 30])