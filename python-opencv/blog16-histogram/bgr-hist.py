import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("tiankong.jpg")
color = ('b', 'g', 'r')

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()