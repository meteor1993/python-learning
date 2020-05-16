import cv2 as cv

# 读取图片
img = cv.imread("maliao.jpg", 1)

# 显示图片
cv.imshow("demo", img)

# 等待输入
cv.waitKey(0)
cv.destroyAllWindows()

# 图片写入
cv.imwrite("demo.jpg", img)