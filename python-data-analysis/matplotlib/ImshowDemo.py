import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10, 10)
plt.imshow(x, cmap=plt.cm.hot)

# 显示右边颜色条
plt.colorbar()

plt.savefig('imshow_demo.png')
