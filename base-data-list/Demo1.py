list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 省略步长时默认为 1
print(list1[3:8])
# 步长为 2
print(list1[3:8:2])
# 从索引 3 开始取到最后
print(list1[3:])
# 从头开始取，取到索引 8 ，并且索引 8 娶不到
print(list1[:8])
# 取所有，步长为 3
print(list1[::3])
# 从索引 1 开始，取到倒数第 2 个，并且倒数第 2 个 取不到
print(list1[1:-2])
# 取所有
print(list1[:])
# 取逆序列表
print(list1[::-1])
# 取逆序，并且步长为 2
print(list1[8:1:-2])

list1.append("Python")
print(list1)

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2.append("Python")
list2.append("Python")
list2.append("Python")
list2.append(1)
print(list2.count("Python"))
print(list2.count(1))

list1.extend(list2)
print(list1)

print(list1.index("Python"))

list1.insert(0, "Hello")
print(list1)

list3 = [0, 1, 2]
list4 = [2, 2]
list3.insert(1, list4)
print(list3)

list3.pop()
print(list3)

list3.pop(1)
print(list3)

list5 = [1, 2, 3, 4, 4, 5]
list5.remove(4)
print(list5)
print(id(list5))
list5.reverse()
print(list5)
print(id(list5))
print(id(list5[::-1]))

list6 = [2, 5, 1, 9, 6, 3]
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)