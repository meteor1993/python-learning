import pandas as pd

# 数据导入
epidemic_dxy = pd.read_excel("epidemic_dxy.xlsx")

print(epidemic_dxy.groupby(['continents']))

print(epidemic_dxy.groupby(['continents']).count())

# pd.set_option('display.max_columns', None)
print(epidemic_dxy.groupby(['continents']).sum())

print(epidemic_dxy.groupby(['continents'])['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount'].sum())

print(epidemic_dxy.groupby(epidemic_dxy['continents'])['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount'].sum())

print(epidemic_dxy.groupby([epidemic_dxy['continents'], epidemic_dxy['provinceName']])['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount'].sum())

print(epidemic_dxy.groupby(epidemic_dxy['continents'])['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount'].aggregate(['count', 'sum']))

new_dataframe = epidemic_dxy.groupby(epidemic_dxy['continents'])['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount'].sum().reset_index()

print(new_dataframe)