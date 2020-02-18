import numpy as np
import pandas as pd

dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 获取单列，获得 Series
print(df['A'])
# 行切片
print(df[0:3])
print(df['20200101' : '20200103'])

# loc，可以使用 column 名和 index 名进行定位
# 用标签提取一行数据
print(df.loc[dates[0]])
# 用标签提取多列数据
print(df.loc[:, ['A', 'B']])
# 用标签进行切片操作，同时制定行与列的结束点
print(df.loc['20200101':'20200103', ['A', 'B']])
# 返回一行中的两列
print(df.loc['20200101', ['A', 'B']])
# 获取某个标量值
print(df.loc[dates[0], 'A'])

# iloc，即 index locate 用 index 索引进行定位，所以参数是整型
# 用整数位置选择
print(df.iloc[3])
# 使用整数按行和列进行切片操作
print(df.iloc[3:5, 0:2])
# 