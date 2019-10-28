# 演示集合不可变元素
set1 = {1, 2, 3, 'Python', (1, 'geekdigging')}
print(set1)
print(type(set1))

# 演示不可重复
set2 = {1, 2, 2}
print(set2)

# 演示空集合
set3 = set()
print(set3)
print(type(set3))

# 使用 list 创建集合
list1 = [1, 1, 2, 2, 3, 4]
set4 = set(list1)
print(set4)

# 使用 tuple 创建集合
tup1 = (1, 1, 2, 2, 3, 4)
set5 = set(tup1)
print(set5)

# 使用字符串创建集合
str1 = 'geekdigging'
set6 = set(str1)
print(set6)