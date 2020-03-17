import matplotlib.pyplot as plt
import numpy as np

# 处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

x_data = np.array([2011,2012,2013,2014,2015,2016,2017])
y_data = np.array([58000,60200,63000,71000,84000,90500,107000])
y_data_1 = np.array([78000,80200,93000,101000,64000,70500,87000])

plt.title(label='xxx 公司 xxx 产品销量')

plt.bar(x_data, y_data, width=0.3, alpha=0.6, facecolor = 'pink', edgecolor = 'blue', lw=1, label='产品销量')
plt.bar(x_data, y_data_1, bottom=y_data, width=0.3, alpha=0.6, facecolor = 'blue', edgecolor = 'blue', lw=1, label='用户增长数')

plt.legend()

plt.savefig("bar_demo_3.png")