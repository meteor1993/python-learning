import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 读取图片
img = cv.imread("maliao_noise.jpg", cv.IMREAD_UNCHANGED)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(rgb_img, -1, kernel)

titles = ['Source Image', 'filter2D Image']
images = [rgb_img, dst]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()