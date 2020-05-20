import cv2 as cv

# 读取图像
img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

# 图像类型转换
result = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# 图像展示
cv.imshow("img", img)
cv.imshow("result", result)

# 等待显示
cv.waitKey()
cv.destroyAllWindows()