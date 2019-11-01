str1 = open('F:/project/python-learning/base-data-def/Demo.py', mode='r').read()
# print(str1)


str2 = '好好学习，天天向上'
# print(type(str2))
a = str2.encode('utf-8')
# print(type(a))
# print(a.decode('utf-8'))
# 报错，无法使用 gbk 解码 utf-8 编码的内容
# print(a.decode('gbk'))

import os
os.chdir('F:/project')
# file = open('test.txt', mode='a+')
# print(file.read())
# file.write('\n关注公众号，好好学习，天天向上')
# file.close()

file = open('test.txt')
print(file.read())
print(file.read())