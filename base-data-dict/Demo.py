dict1 = {'name': 'geekdigging', 'age': 2}
print(dict1)
print(type(dict1))

dict2 = {(1, 2, 3): '123', 'name': 'geekdigging', 2: [1, 2, 3]}
print(dict2)
print(type(dict2))

dict3 = dict(name = 'geekdigging', age = 2)
print(dict3)
print(type(dict3))

# 语法错误，注释
# dict4 = dict(1 = 'geekdigging', 2 = 2)

print(dict1['name'])
# 键不存在示例，报错 KeyError
# print(dict1['geekdigging'])

str = 'geekdigging'

if str in dict1:
    print(dict1['geekdigging'])
else:
    print('您查询的键', str, '不存在')

# 添加
dict1['a'] = 18
print(dict1)
# 更新
dict1['name'] = 'www.geekdigging.com'
print(dict1)
# 删除
del dict1['a']
print(dict1)