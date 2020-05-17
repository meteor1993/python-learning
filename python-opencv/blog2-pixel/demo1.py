import cv2 as cv

# 灰度图像读取
gray_img = cv.imread("maliao.jpg", cv.IMREAD_GRAYSCALE)
print(gray_img[20, 30])

# 显示图片
cv.imshow("gray_img", gray_img)

# 等待输入
cv.waitKey()
cv.destroyAllWindows()