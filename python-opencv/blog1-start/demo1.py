import cv2 as cv

# 读取图像
img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)
cv.imshow("read_img", img)
# 灰度图像
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("gray_img",img_gray)
# 二值图像
ret, binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("binary_img", binary)

cv.waitKey()