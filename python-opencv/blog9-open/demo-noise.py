import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv.imread("demo.png", cv.IMREAD_UNCHANGED)
source = cv.cvtColor(img, cv.COLOR_BGR2RGB)
rows, cols, chn = source.shape

# 加噪声-白点噪声
for i in range(500):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    source[x, y, :] = 255

# 图像保存 白点噪声图像
cv.imwrite("demo_noise_white.jpg", source)
print("白点噪声添加完成")

# 重新读取图像
img1 = cv.imread("demo.png", cv.IMREAD_UNCHANGED)
source1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

# 加噪声-黑点噪声
for i in range(1000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    source1[x, y, :] = 0

# 图像保存 黑点噪声图像
cv.imwrite("demo_noise_black.jpg", source1)
print("黑点噪声添加完成")

# 显示结果
titles = ['White Img','Black Img']
images = [source, source1]

# matplotlib 绘图
for i in range(2):
   plt.subplot(1, 2, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()
