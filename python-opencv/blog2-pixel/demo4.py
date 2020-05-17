import cv2 as cv

color_img = cv.imread("maliao.jpg", cv.IMREAD_COLOR)
color_img[50:100, 50:100] = [255, 255, 255]

cv.imshow("color_img", color_img)
cv.waitKey()
cv.destroyAllWindows()