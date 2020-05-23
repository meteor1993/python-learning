import cv2 as cv

#读取图片
src = cv.imread('maliao.jpg')

# 原图的高、宽
rows, cols = src.shape[:2]

# 绕图像的中心旋转
# 参数：旋转中心 旋转度数 scale
M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
#
dst = cv.warpAffine(src, M, (cols, rows))

# 显示图像
cv.imshow("src", src)
cv.imshow("dst", dst)

# 等待显示
cv.waitKey()
cv.destroyAllWindows()