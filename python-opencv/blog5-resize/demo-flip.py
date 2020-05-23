import cv2 as cv
import matplotlib.pyplot as plt

# 读取图片 由 GBR 转 RGB
img = cv.imread('maliao.jpg')
src = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 图像翻转
# flipCode 为 0 ，则以 X 轴为对称轴翻转，如果 fliipCode > 0 则以 Y 轴为对称轴翻转，如果 flipCode < 0 则在 X 轴、 Y 轴方向同时翻转。
img1 = cv.flip(src, 0)
img2 = cv.flip(src, 1)
img3 = cv.flip(src, -1)

# plt 显示图形
titles = ['Source', 'Img1', 'Img2', 'Img3']
images = [src, img1, img2, img3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()