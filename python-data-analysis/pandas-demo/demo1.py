import numpy as np
import pandas as pd

dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 查看头部数据
print(df.head(1))
# 查看尾部数据
print(df.tail(2))
# 获取索引
print(df.index)
# 获取列名
print(df.columns)
# 查看数据的统计摘要
print(df.describe())
# 转置数据
print(df.T)
# 参考 https://www.jianshu.com/p/f0ed06cd5003
# 两种排序 sort_index() 和 sort_values()
df1 = pd.DataFrame({'b' :[1,2,3,2],'a':[4,3,2,1],'c':[1,3,8,2]},index=[2,0,1,3])
print(df1)
# sort_values() 排序
# 按 b 列升序排序
print(df1.sort_values(by='b'))
# 先按 b 列降序，再按 a 列升序排序
print(df1.sort_values(by=['b','a'],axis=0,ascending=[False,True]))
# 按行 3 升序排列,必须指定 axis = 1
print(df1.sort_values(by=3,axis=1))
# 按行 3 升序，行 0 降排列
print(df1.sort_values(by=[3,0],axis=1,ascending=[True,False]))
# sort_index() 排序
# 默认按「行标签」升序排列
print(df1.sort_index())
# 按「列标签」升序排列
print(df1.sort_index(axis=1))
# 先按 b 列「降序」排列，因为 b 列中有相同值，相同值再按 a 列的「升序」排列
print(df1.sort_index(by=['b','a'],ascending=[False,True]))
# 先按 a 列「降序」排列，而 a 列中没有相同值，因此这里按 b 列的「升序」排列不起作用。
print(df1.sort_index(by=['a','b'],ascending=[False,True]))