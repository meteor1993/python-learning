import pandas as pd

# 数据读取
df = pd.read_excel("table_join_exp.xlsx", sheet_name='Sheet1')

# 数据导出
df.to_excel(excel_writer=r'D:\Development\Projects\demo.xlsx')

df.to_excel(excel_writer=r'D:\Development\Projects\demo.xlsx',
            sheet_name='测试文档', # 创建 sheet 名称
            index=False,  # 设置索引不显示
            columns=['编号', '姓名'],  # 设置要导出的列
            encoding='utf-8', # 设置编码格式
            na_rep='0', # 缺失值处理
            inf_rep='inf'  # 无穷值处理
            )

df.to_csv(path_or_buf=r'D:\Development\Projects\demo.csv', # 设置导出路径
          index=False,  # 设置索引不显示
          sep=',', # 设置分隔符号
          na_rep='0', # 缺失值处理
          columns=['编号', '姓名'],  # 设置要导出的列
          encoding='utf-8', # 设置编码格式
          )