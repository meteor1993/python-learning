import cv2 as cv

src = cv.imread("maliao.jpg")

# BGR 图像转灰度
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 二值图像处理
r, b = cv.threshold(gray_img, 127, 255, cv.THRESH_TOZERO)

# 显示图像
cv.imshow("src", src)
cv.imshow("result", b)

# 等待显示
cv.waitKey(0)
cv.destroyAllWindows()