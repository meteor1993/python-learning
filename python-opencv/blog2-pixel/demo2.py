import cv2 as cv

# 彩色图像读取
color_img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)

print(color_img[20, 30])

blue = color_img[20, 30, 0]
print(blue)

green = color_img[20, 30, 1]
print(green)

red = color_img[20, 30, 2]
print(red)

# 显示图片
cv.imshow("color_img", color_img)

# 等待输入
cv.waitKey()
cv.destroyAllWindows()