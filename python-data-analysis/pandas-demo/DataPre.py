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