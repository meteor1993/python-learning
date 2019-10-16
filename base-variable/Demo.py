# 因 name 未定义，此处直接打印将会报错
# print(name)

name = "小明"

print(name)

name = "小红"

print(name)

del name

# 因上面已经删除了变量 name ，这里再打印将会报错该变量未定义
# print(name)

# print('123' + 123)

print('123' + str(123))

print(int('123') + 123)

print(123.5 + 123)

print(int(123.7))

print(int(123.7 + 0.5))

print(int(round(123.4)))

print(int(round(123.5)))