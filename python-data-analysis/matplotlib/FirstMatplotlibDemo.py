import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(figsize=(6, 6))
#
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)


x = np.arange(4)
y = np.arange(4)

# 绘制折线图
plt.subplot2grid((2,2),(0,0))
plt.plot(x, y)

# 绘制柱状图
plt.subplot2grid((2,2),(0,1))
plt.bar(x, y)

# plt.show()

# 绘制折线图
plt.subplot(221)
plt.plot(x, y)

# 绘制柱状图
plt.subplot(222)
plt.bar(x, y)

# plt.show()

fig, axes = plt.subplots(2, 2)
# 绘制折线图
axes[0,0].plot(x,y)
# 绘制柱状图
axes[0,1].bar(x,y)
plt.show()