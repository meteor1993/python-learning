# 示例 1

# width = input("请输入长方形的宽：")
# height = input("请输入长方形的高：")
# area = int(width) * int(height)
# print("长方形的面积为：", area)

# 示例 2

# weight = input("请输入当前的体重：")
#
# if float(weight) >= 200:
#     print("你和加菲猫一样肥！！")
# else:
#     print("你还是很苗条的么！！")

# 示例 3

# weight = input("请输入您当前的体重：")
#
# if float(weight) >= 200:
#     print("你和加菲猫一样肥！！")
# elif float(weight) >= 100:
#     print("你的身材真棒！！")
# else:
#     print("有点瘦哦，要多吃肉！！")

# 示例 4
gender = input("请输入您的性别（M或者F）:")
height = input("请输入您的身高：")

if gender == 'M':
    if float(height) >= 185:
        print("海拔太高了，可能会导致缺氧！！！")
    elif float(height) >= 175:
        print("男神身高！！！")
    else:
        print("哥们，该补钙了！！！")
else:
    if float(height) >= 175:
        print("您可以去当模特了！！！")
    elif float(height) >= 165:
        print("女神身高，您是一位美丽的女孩子！！！")
    else:
        print("美女，多晒晒太阳吧！！！")