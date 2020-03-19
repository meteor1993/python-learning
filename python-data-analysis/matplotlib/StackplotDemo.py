import matplotlib.pyplot as plt

# 处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

x_data = [2011,2012,2013,2014,2015,2016,2017]
y_data = [58000,60200,63000,71000,84000,90500,107000]
y_data_1 = [78000,80200,93000,101000,64000,70500,87000]

plt.title(label='xxx 公司 xxx 产品销量')

plt.stackplot(x_data, y_data, y_data_1, labels=['产品销量', '用户增长数'])

plt.legend()

plt.savefig("stackplot_demo.png")