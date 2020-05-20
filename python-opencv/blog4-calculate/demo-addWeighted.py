import cv2 as cv

# 读取图像
img1 = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)
img2 = cv.imread("rain.jpg", cv.IMREAD_UNCHANGED)

# 图像融合
img = cv.addWeighted(img1, 0.4, img2, 0.6, 10)

# 显示图像
cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img", img)

# 等待显示
cv.waitKey()
cv.destroyAllWindows()