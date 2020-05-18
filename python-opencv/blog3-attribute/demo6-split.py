import cv2 as cv

img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

# 拆分通道
b, g, r = cv.split(img)

# 拆分通道使用 numpy 索引
# b = img[:, :, 0]
# g = img[:, :, 1]
# r = img[:, :, 2]

# 分别显示三个通道的图像
cv.imshow("B", b)
cv.imshow("G", g)
cv.imshow("R", r)

# 等待显示
cv.waitKey(0)
cv.destroyAllWindows()