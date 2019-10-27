import copy

dict1 = {'name': 'geekdigging', 'age': 2}

print(dict1.keys())
print(list(dict1.keys()))
print(type(list(dict1.keys())))

print(dict1.values())
print(list(dict1.values()))
print(type(list(dict1.values())))

print(dict1.items())
print(list(dict1.items()))
print(type(list(dict1.items())))

print(dict1.get('name'))
print(dict1.get('geekdigging'))

print(dict1.pop('age'))
print(dict1)

dict1.setdefault('age')
print(dict1)

dict2 = {'sex': 'male'}
dict1.update(dict2)
print(dict1)

dict2.clear()
print(dict2)

dict3 = {'name': 'geekdigging', 'age': [1, 2, 3]}
# 浅拷贝: 引用对象
dict4 = dict3
print(id(dict3))
print(id(dict4))
# 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dict5 = dict3.copy()
dict3['age'].remove(1)
print(dict3)
print(dict5)
print(id(dict3))
print(id(dict5))

dict3 = {'name': 'geekdigging', 'age': [1, 2, 3]}
dict6 = copy.deepcopy(dict3)
dict3['age'].remove(1)
print(dict3)
print(dict6)
print(id(dict3))
print(id(dict6))