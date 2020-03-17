import matplotlib.pyplot as plt

# 处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

x_data = [2011,2012,2013,2014,2015,2016,2017]
y_data = [58000,60200,63000,71000,84000,90500,107000]
y_data_1 = [78000,80200,93000,101000,64000,70500,87000]

plt.title(label='xxx 公司 xxx 产品销量')
# 设置标题
plt.plot(x_data, y_data, linestyle = '-.', label = '产品销量')
plt.plot(x_data, y_data_1, label = '用户增长数')
# 开启网格线
plt.grid(True)
# 设置图例
plt.legend()
# 文件保存
plt.savefig("plot_demo.png")