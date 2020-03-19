import matplotlib.pyplot as plt

# 中文和负号的正常显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']

# 让本科学历离圆心远一点
explode = [0,0,0.1,0,0]

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 自定义颜色
colors=['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555'] # 自定义颜色

# 绘制饼图
plt.pie(x=edu,  # 绘图数据
    explode = explode,  # 突出显示大专人群
    labels = labels,  # 添加教育水平标签
    colors = colors,  # 设置饼图的自定义填充色
    autopct = '%.1f%%',  # 设置百分比的格式，这里保留一位小数
    )

# 添加图标题
plt.title('xxx 公司员工教育水平分布')

# 保存图形
plt.savefig('pie_demo.png')