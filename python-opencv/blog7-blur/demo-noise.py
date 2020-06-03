import cv2 as cv
import numpy as np

# 读取图片
img = cv.imread("maliao.jpg", cv.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 加噪声
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

cv.imshow("noise", img)

# 图像保存
cv.imwrite("maliao_noise.jpg", img)

# 等待显示
cv.waitKey()
cv.destroyAllWindows()