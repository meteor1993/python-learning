import numpy as np
import matplotlib.pyplot as plt

# 中文和负号的正常显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 使用ggplot的绘图风格
plt.style.use('ggplot')

# 构造数据
values = [3.2, 2.1, 3.5, 2.8, 3]
feature = ['攻击力', '防御力', '恢复力', '法术强度', '生命值']

N = len(values)
# 设置雷达图的角度，用于平分切开一个圆面
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# 为了使雷达图一圈封闭起来，需要下面的步骤
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

# 绘图
fig = plt.figure()
# 这里一定要设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2)
# 填充颜色
ax.fill(angles, values, alpha=0.25)
# 添加每个特征的标签
ax.set_thetagrids(angles * 180 / np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0, 5)
# 添加标题
plt.title('游戏人物属性')
# 添加网格线
ax.grid(True)
# 显示图形
plt.savefig('polar_demo.png')