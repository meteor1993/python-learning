import numpy as np
import pandas as pd

s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)

s1 = pd.Series(np.random.randn(5))
print(s1)

d = {'b': 1, 'a': 0, 'c': 2}
s2 = pd.Series(d)
print(s2)

s3 = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s3)

s4 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print(s4)

print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 1]])
# 打印 e 的幂次方， e 是一个常数为 2.71828
print (np.exp(s))
# 打印 s 里每个元素的开方
print (np.sqrt(s))
print(s.dtype)
print(s.array)
print(s.to_numpy())

print(s['a'])
s['e'] = 12.
print(s)

print('e' in s)
print('f' in s)
# 抛出 KeyError 异常
# print(s['f'])

print(s.get('f'))
print(s.get('f', np.nan))

print(s[1:] + s[:-1])

s5 = pd.Series(np.random.randn(5), name='my_series')
print(s5)
print(s5.name)
print(id(s5))

# 重命名 series
s6 = s5.rename("my_series_different")
print(s6)
print(id(s6))