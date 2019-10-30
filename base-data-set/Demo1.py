set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 7, 9}

# 求交集
set3 = set1.intersection(set2)
print('交集：', set3)

# 求并集
set4 = set1.union(set2)
print('并集：', set4)

# 做差
set5 = set1.difference(set2)
print('做差：', set5)

set6 = {1, 2, 3}
set6.add(4)
print(set6)
set6.add('python')
print(set6)
set6.add((1, 2))
print(set6)

set7 = {1, 2}
set7.update({3, 4, 'python', (4, 5)})
print(set7)

set7.pop()
print(set7)

set8 = {1, 2, 3, 4}
set8.remove(4)
print(set8)
# 删除不存在元素，报错
# set8.remove(9)

set8.discard(9)
print(set8)

set9 = {1, 2, 3}
set9.clear()
print(set9)

set10 = {1, 2, 3}
set11 = {1, 2}
set12 = {4, 5}
print(set10.isdisjoint(set11))
print(set10.isdisjoint(set12))

print(set11.issubset(set10))
print(set12.issubset(set10))

print(set10.issuperset(set11))
print(set10.issuperset(set12))