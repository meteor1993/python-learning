import xlsxwriter
import datetime

workbook = xlsxwriter.Workbook('demo.xlsx')

sheet1 = workbook.add_worksheet('test_sheet')

workfomat = workbook.add_format()
# 字体加粗
workfomat.set_bold(True)
# 单元格边框宽度
workfomat.set_border(1)
# 对齐方式
workfomat.set_align('left')
# 格式化数据格式为小数点后两位
workfomat.set_num_format('0.00')

heads = ['', '语文', '数学', '英语']
datas = [
    ['小明', 76, 85, 95],
    ['小红', 85, 58, 92],
    ['小王', 98, 96, 91]
]

sheet1.write_row('A1', heads, workfomat)

sheet1.write_row('A2', datas[0], workfomat)
sheet1.write_row('A3', datas[1], workfomat)
sheet1.write_row('A4', datas[2], workfomat)

fomat1 = workbook.add_format({'num_format': 'yyyy/mm/dd/ hh:mm:ss'})

sheet1.write_datetime('E5', datetime.datetime(2019, 11, 9, 22, 44, 26), fomat1)

sheet1.insert_image('I6', 'wx.jpg')

chart = workbook.add_chart({'type': 'column'})

chart.add_series({'values': '=test_sheet!$B$2:$B$4'})
chart.add_series({'values': '=test_sheet!$C$2:$C$4'})
chart.add_series({'values': '=test_sheet!$D$2:$D$4'})

sheet1.insert_chart('A7', chart)

workbook.close()