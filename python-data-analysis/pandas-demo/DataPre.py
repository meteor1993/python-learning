import pandas as pd

# 相对路径
df = pd.read_excel("result_data.xlsx")
print(df)

print(df.info())

# 显示所有行
# pd.set_option('display.max_rows', None)
print(df.isnull())

print(df.dropna())

print(df.dropna(how="any"))

print(df.fillna(0))

print(df.fillna({'read_num': 10}))

print(df)
print(df.drop_duplicates())

print(df.drop_duplicates(subset='read_num'))

print(df.drop_duplicates(subset='plantform', keep='last'))

print(df.dtypes)

print(df['read_num'].dtypes)

print(df['fans_num'].astype('float64'))

df1 = pd.read_excel("demo.xlsx")
print(df1)

df1.columns = ['编号', '序号', '姓名', '消费金额']
print(df1)

print(df1.set_index('编号'))