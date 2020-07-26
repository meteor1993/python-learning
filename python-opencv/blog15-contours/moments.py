import cv2 as cv

img = cv.imread("number.png")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cnt = contours[0]
# 获取图像矩
M = cv.moments(cnt)
print(M)

# 质心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

print(f'轮廓质心为：[{cx}, {cy}]')

# 轮廓面积
area = cv.contourArea(cnt)
print(f'轮廓面积为:{area}')

# 轮廓周长
perimeter = cv.arcLength(cnt, True)
print(f'轮廓周长为:{perimeter}')