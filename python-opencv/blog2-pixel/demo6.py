import cv2 as cv

# 读取彩色图像
color_img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)

print(color_img[20, 30])

color_img.itemset((20, 30, 0), 255)
color_img.itemset((20, 30, 1), 255)
color_img.itemset((20, 30, 2), 255)

print(color_img[20, 30])