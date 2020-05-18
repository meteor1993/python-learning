import cv2 as cv

img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

# 获取 ROI 区域
face = img[10:175, 100:260]
# 图像赋值
img[0:165, 0:160] = face

# 原始图像显示
cv.imshow("demo", img)

#等待显示
cv.waitKey(0)
cv.destroyAllWindows()