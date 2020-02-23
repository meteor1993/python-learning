import pandas as pd

# 相对路径
df = pd.read_excel("result_data.xlsx")
print(df)

# 绝对路径
df = pd.read_excel("D:/Development/Projects/python-learning/python-data-analysis/pandas-demo/result_data.xlsx")
print(df)

# 指定 sheet 名
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name='result_data')
print(df)

# 指定 sheet 名
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name=0)
print(df)

# 指定导入行数
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name=0, nrows=100)
print(df)

# 指定行索引
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name=0, index_col=5)
print(df)

# 指定列索引
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name=0, header=1)
print(df)

# 指定导入列
df = pd.read_excel(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.xlsx", sheet_name=0, usecols=[0, 1, 2])
print(df)

# 导入 csv 的数据
df = pd.read_csv(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.csv")
print(df)

# 指定编码格式
df = pd.read_csv(r"D:\Development\Projects\python-learning\python-data-analysis\pandas-demo\result_data.csv", encoding='utf-8')
print(df)

# 导入 pymsql
import pymysql

con = pymysql.connect(host='cdb-1dydsrwm.bj.tencentcdb.com',
                         port=10224,
                         user='root',
                         password='wsy@123456',
                         db='blog_data',
                         charset='utf8mb4')

sql = 'select * from result_data'

df = pd.read_sql(sql, con)
print(df)

# 获取前几行
print(df.head(5))

print(df.shape)

print(df.describe())