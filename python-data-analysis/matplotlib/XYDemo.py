import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']

x_data = [2011,2012,2013,2014,2015,2016,2017]
y_data = [58000,60200,63000,71000,84000,90500,107000]

# plt.xlabel('年份', labelpad=50, fontsize='xx-large', fontweight='bold', rotation='vertical', backgroundcolor='red')
# plt.ylabel('销量', labelpad=50)

# plt.xticks(x_data)
# plt.yticks(y_data)

# plt.xlim(2011, 2020)
# plt.ylim(50000, 90000)

plt.title(label='xxx 公司 xxx 产品销量')

plt.plot(x_data, y_data, label = '折线图')
plt.bar(x_data, y_data, label = '柱状图')

plt.legend()

# plt.axis("off")

# plt.grid(b=True, axis='x')

plt.show()