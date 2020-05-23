import cv2 as cv

# 设定比例
scale = 0.5

#读取图片
src = cv.imread('maliao.jpg')
rows, cols = src.shape[:2]

#图像缩放
result = cv.resize(src, ((int(cols * scale), int(rows * scale))))
print(result.shape)

#显示图像
cv.imshow("src", src)
cv.imshow("result", result)

#等待显示
cv.waitKey()
cv.destroyAllWindows()