list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ['a', 'b', 'c', 'd', 'e']
print(list2)

list3 = [1, 2, 3, 'a', 'b']
print(list3)

list4 = [1, 2.33, 'a', list3]
print(list4)

list5 = []
print(list5)

print(type(list4))

list1 = [1, 2, 3, 4, 5]
print(list1[0])
# 异常索引打印
# print(list1[5])

print(list1[-1])

print(list1 + list2)

for i in list1:
    print(i)

print(len(list1))

print(len(list1 + list2))

print('a' in list1)
print(1 in list1)