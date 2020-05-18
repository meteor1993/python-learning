import cv2 as cv

img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)

face = img[10:175, 100:260]

# 原始图像显示
cv.imshow("demo", img)

# 马里奥的脸显示
cv.imshow("face", face)

#等待显示
cv.waitKey(0)
cv.destroyAllWindows()