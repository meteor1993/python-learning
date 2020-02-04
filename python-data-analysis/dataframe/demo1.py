import numpy as np
import pandas as pd

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

df1 = pd.DataFrame(d, index=['d', 'b', 'a'])
print(df1)

df2 = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(df2)

d1 = {'one': [1., 2., 3., 4.],
      'two': [4., 3., 2., 1.]}

df3 = pd.DataFrame(d1)
print(df3)

df4 = pd.DataFrame(d1, index=['a', 'b', 'c', 'd'])
print(df4)

d2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

df5 = pd.DataFrame(d2)
print(df5)

df6 = pd.DataFrame(d2, index=['first', 'second'], columns=['a', 'b'])
print(df6)

d3 = ({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
       ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
       ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
       ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
       ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})

df7 = pd.DataFrame(d3)
print(df7)

print('----------------------------- 分割线 ---------------------------------')

# 获取数据
print(df4)
# 按列获取
print(df4['one'])
# 按行获取
print(df4.loc['a'])
print(df4.iloc[0])

df4['three'] = df4['one'] * df4['two']
df4['flag'] = df4['one'] > 2
print(df4)

# 删除数据
del df4['two']
df4.pop('three')
print(df4)

# 插入数据
df4['foo'] = 'bar'
print(df4)

df4['one_trunc'] = df4['one'][:2]
print(df4)

df4.insert(1, 'bar', df4['one'])
print(df4)