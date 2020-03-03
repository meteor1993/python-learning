import pandas as pd

# 数据导入
epidemic_dxy = pd.read_excel("epidemic_dxy.xlsx")

df = pd.pivot_table(epidemic_dxy, values='currentConfirmedCount', index='continents', aggfunc='sum')

print(df)

df1 = pd.pivot_table(epidemic_dxy, values='currentConfirmedCount', index='continents', columns='provinceName', aggfunc='sum')

print(df1)

df2 = pd.pivot_table(epidemic_dxy, values='currentConfirmedCount', index=['continents', 'createTime'], columns='provinceName', aggfunc='sum')
print(df2)