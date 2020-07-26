import cv2 as cv
import numpy as np

img = cv.imread("number.png")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cnt = contours[0]

# 外接正矩形
x, y, w, h = cv.boundingRect(cnt)
cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 外接最小矩形
min_rect = cv.minAreaRect(cnt)
print(min_rect)

box = cv.boxPoints(min_rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)

cv.imshow("draw", img)

cv.waitKey(0)
cv.destroyAllWindows()