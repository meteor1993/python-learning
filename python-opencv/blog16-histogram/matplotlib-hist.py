import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("maliao.jpg")

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

plt.hist(img.ravel(), 256, [0, 256])
plt.show()