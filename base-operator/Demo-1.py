# 对应《小白学 Python（6）：基础运算符（下）》示例代码

a = 10
b = 20

c = a + b
print("c = a + b 的值为：", c)

c += a
print("c += a 的值为：", c)

c *= a
print("c *= a 的值为：", c)

c /= a
print("c /= a 的值为：", c)

c = 2
c %= a
print("c %= a 的值为：", c)

c **= a
print("c **= a 的值为：", c)

c //= a
print("c //= a 的值为：", c)

print(True and True)
# True
print(True and False)
# False
print(True or True)
# True
print(True or False)
# True
print(False or False)
# False
print(not True)
# False
print(not False)
# True

str = "asdfghjkl"

if 'a' in str:
    print('a 在字符串 str 中')
else:
    print('a 不在字符串 str 中')

if 'a' not in str:
    print('a 不在字符串 str 中')
else:
    print('a 在字符串 str 中')

a = 20
b = 20

if a is b:
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if id(a) == id(b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if a is not b:
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")