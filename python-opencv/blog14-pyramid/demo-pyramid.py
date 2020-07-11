import cv2 as cv

#高斯金字塔
def gaussian_pyramid(image):
    level = 3      #设置金字塔的层数为3
    temp = image.copy()  #拷贝图像
    gaussian_images = []  #建立一个空列表
    for i in range(level):
        dst = cv.pyrDown(temp)   #先对图像进行高斯平滑，然后再进行降采样（将图像尺寸行和列方向缩减一半）
        gaussian_images.append(dst)  #在列表末尾添加新的对象
        cv.imshow("gaussian"+str(i), dst)
        temp = dst.copy()
    return gaussian_images


#拉普拉斯金字塔
def laplacian_pyramid(image):
    gaussian_images = gaussian_pyramid(image)    #做拉普拉斯金字塔必须用到高斯金字塔的结果
    level = len(gaussian_images)
    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            expand = cv.pyrUp(gaussian_images[i], dstsize = image.shape[:2])
            laplacian = cv.subtract(image, expand)
            # 展示差值图像
            cv.imshow("laplacian_down_"+str(i), laplacian)
        else:
            expand = cv.pyrUp(gaussian_images[i], dstsize = gaussian_images[i-1].shape[:2])
            laplacian = cv.subtract(gaussian_images[i-1], expand)
            # 展示差值图像
            cv.imshow("laplacian_down_"+str(i), laplacian)


src = cv.imread('maliao.jpg')
print(src.shape)
# 先将图像转化成正方形，否则会报错
input_image = cv.resize(src, (560, 560))
# 设置为 WINDOW_NORMAL 可以任意缩放
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', input_image)
laplacian_pyramid(input_image)
cv.waitKey(0)
cv.destroyAllWindows()