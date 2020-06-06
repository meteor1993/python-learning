import cv2 as cv

source = cv.imread("zhaopian.jpg")
dst = cv.bilateralFilter(src=source, d=-1, sigmaColor=30, sigmaSpace=15)

cv.imshow("source", source)
cv.imshow("dst", dst)

cv.waitKey()
cv.destroyAllWindows()