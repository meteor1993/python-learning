tuple1 = "Python", "Java", 2011, 2015
print(tuple1)

tuple2 = ("Python", "Java", 2011, 2015)
print(tuple2)
print(type(tuple2))

tuple3 = ("Python", "Java", [1 ,2, 'python', 'java'], 2011, 2015)
print(tuple3)

tuple4 = (0 ,1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple4)
# 索引
print(tuple4[2])
# 索引
print(tuple4[-2])
# 切片
print(tuple4[0:8:2])
# 切片
print(tuple4[8:1:-1])

tuple5 = (2333, '98k')
# 连接
print(tuple4 + tuple5)
# 循环
for index in tuple4:
    print(index)
# 查找元素是否存在
print(1 in tuple4)
print(11 in tuple4)
# 删除元组
# del tuple5
# print(tuple5)

# 取最大
print(max(tuple4))
# 取最小
print(min(tuple4))
# 元组长度
print(len(tuple4))
# 修改元组
# tuple4[0] = 11

# 相互转化
print(type(tuple4))
print(list(tuple4))
print(type(list(tuple4)))
list1 = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

# 元组解包
tuple6 = (1, 2, 3)
print(tuple6)
a, b, c = tuple6
print(a, b, c)