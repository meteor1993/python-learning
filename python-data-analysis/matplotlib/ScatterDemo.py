import matplotlib.pyplot as plt
import numpy as np

# 处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

x_data = np.array([2011,2012,2013,2014,2015,2016,2017])
y_data = np.array([58000,60200,63000,71000,84000,90500,107000])

plt.scatter(x_data, y_data, s = 100, c = 'green', marker='o', edgecolor='black', alpha=0.5, label = '产品销量')

plt.legend()

plt.savefig("scatter_demo.png")