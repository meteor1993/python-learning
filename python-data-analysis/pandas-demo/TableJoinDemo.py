import pandas as pd

df1 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet1')
print(df1)

df2 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet2')
print(df2)

print(pd.merge(df1, df2))

df3 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet3')
print(df3)

print(pd.merge(df1, df3, on='编号'))

df4 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet4')
print(df4)

print(pd.merge(df4, df3, on='编号'))

df5 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet5')
print(df5)

# 内连接
print(pd.merge(df5, df3, on='编号', how='inner'))

# 左连接
print(pd.merge(df5, df3, on='编号', how='left'))

# 右连接
print(pd.merge(df5, df3, on='编号', how='right'))

# 外连接
print(pd.merge(df5, df3, on='编号', how='outer'))

df6 = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet6')
print(df6)

# 纵向拼接
print(pd.concat([df5, df6]))

print(pd.concat([df5, df6], ignore_index=True))