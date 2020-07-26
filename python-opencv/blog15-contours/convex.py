import cv2 as cv

img = cv.imread("number.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cnt = contours[0]
# 绘制轮廓
image = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
cv.drawContours(image, contours, -1, (0, 0 , 255), 2)

# 寻找凸包，得到凸包的角点
hull = cv.convexHull(cnt)

# 绘制凸包
cv.polylines(image, [hull], True, (0, 255, 0), 2)

print(cv.isContourConvex(hull))

cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()