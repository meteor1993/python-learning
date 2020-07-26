import cv2 as cv

img = cv.imread("number.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cnt = contours[0]

# 绘制最小外接圆
# (x, y), radius = cv.minEnclosingCircle(cnt)
# center = (int(x), int(y))
# radius = int(radius)
# cv.circle(img, center, radius, (0, 255, 0), 2)
#
# cv.imshow("img", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# 绘制椭圆
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (0, 255, 0), 2)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()