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
# 用整数列表按位置切片
print(df.iloc[[1, 2, 4], [0, 2]])
# 整行切片
print(df.iloc[1:3, :])
# 整列切片
print(df.iloc[:, 1:3])
# 获取某个标量值 同上
print(df.iloc[1, 1])

# at 使用方法与 loc 类似，但是比 loc 有更快的访问数据的速度，而且只能访问单个元素，不能访问多个元素。
print(df.at[dates[0], 'A'])

# iat iat 对于 iloc 的关系就像 at 对于 loc 的关系，是一种更快的基于索引位置的选择方法，同 at 一样只能访问单个元素。
print(df.iat[1, 1])

# 用单列的值选择数据
print(df[df.A > 0])

# 选择 df 里满足条件的值
print(df[df < 0])

