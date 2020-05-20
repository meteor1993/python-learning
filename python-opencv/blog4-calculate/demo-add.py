import cv2 as cv

# 读取图像
img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

test = img

# Numpy 加法
result1 = img + test

# OpenCV 加法
result2 = cv.add(img, test)

# 显示图像
cv.imshow("img", img)
cv.imshow("result1", result1)
cv.imshow("result2", result2)

# 等待显示
cv.waitKey()
cv.destroyAllWindows()