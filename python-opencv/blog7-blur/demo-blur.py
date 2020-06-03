import cv2 as cv
import matplotlib.pyplot as plt

# 读取图片
img = cv.imread("maliao_noise.jpg", cv.IMREAD_UNCHANGED)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 均值滤波
blur_img = cv.blur(rgb_img, (3, 3))
# blur_img = cv.blur(img, (5, 5))
# blur_img = cv.blur(img, (10, 10))
# blur_img = cv.blur(img, (20, 20))

titles = ['Source Image', 'Blur Image']
images = [rgb_img, blur_img]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()