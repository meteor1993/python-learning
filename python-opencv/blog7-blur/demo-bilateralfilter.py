import cv2 as cv
import matplotlib.pyplot as plt

# 读取图片
img = cv.imread('maliao_noise.jpg')
source = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 方框滤波
result = cv.bilateralFilter(source, 3)

# 显示图形
titles = ['Source Image', 'medianBlur Image']
images = [source, result]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()