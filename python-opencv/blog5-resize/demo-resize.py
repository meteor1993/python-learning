import cv2 as cv

#读取图片
src = cv.imread('maliao.jpg')
print(src.shape)

#图像缩放
result = cv.resize(src, (300, 150))
print(result.shape)

#显示图像
cv.imshow("src", src)
cv.imshow("result", result)

#等待显示
cv.waitKey()
cv.destroyAllWindows()