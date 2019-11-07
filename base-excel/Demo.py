import xlrd
import datetime

# 打开execl
workbook = xlrd.open_workbook('test.xlsx')

# 输出所有 sheet 的名字
print(workbook.sheet_names())
# 获取所有的 sheet
print(workbook.sheets())
# 根据索引获取 sheet
print(workbook.sheet_by_index(1))
# 根据名字获取 sheet
print(workbook.sheet_by_name('1班'))

sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)

# 获取第 2 行内容
print(sheet1.row_values(1))
# 获取第 3 列内容
print(sheet1.col_values(2))

cell1 = sheet1.cell(1, 1).value
# 行索引
cell2 = sheet1.row(1)[1].value
cell3 = sheet1.cell(1, 2).value
# 列索引
cell4 = sheet1.col(2)[1].value
print(cell1, cell2, cell3, cell4)

date_value = xlrd.xldate_as_datetime(sheet1.cell_value(5, 3), workbook.datemode)
print(type(date_value), date_value)

date_tulp = xlrd.xldate_as_tuple(sheet1.cell_value(5, 3), workbook.datemode)
print(type(date_tulp), date_tulp)
year, month, day, hour, minute, second = date_tulp
print(datetime.datetime(year, month, day, hour, minute, second))

# 求平均作业开始

yunwen_list = []
shuxue_list = []
yingyu_list = []
for sheet in workbook.sheets():
    # 获取语文分数
    for value in sheet1.col_values(1):
        # 这里取巧，如果类型是 float ，则加入 yunwen_list 中
        if type(value) == float:
            yunwen_list.append(value)

    # 获取数学分数
    for value in sheet1.col_values(2):
        if type(value) == float:
            shuxue_list.append(value)

    # 获取英语分数
    for value in sheet1.col_values(2):
        if type(value) == float:
            yingyu_list.append(value)

# 定义求平均数方法
def averagenum(lists):
    nsum = 0
    for i in range(len(lists)):
        nsum += lists[i]
    # 保留两位小数
    return round(nsum / len(lists), 2)

print('语文平均分为：', averagenum(yunwen_list))
print('数学平均分为：', averagenum(shuxue_list))
print('英语平均分为：', averagenum(yingyu_list))