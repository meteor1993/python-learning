a = 5
b = 10

c = a + b
print("1. c 的值为：", c)

c = a - b
print("2. c 的值为：", c)

c = a * b
print("3. c 的值为：", c)

c = a / b
print("4. c 的值为：", c)

c = a % b
print("5. c 的值为：", c)

c = a ** b
print("6. c 的值为：", c)

# 改变 a 和 b 的值

a = 10
b = 5

c = a // b
print("7. c 的值为：", c)

a = 1
b = 1.5
c = a + b
print("8. c 的值为：", c, "，c 的类型为：", type(c))

d = True
e = c + d
print("9. e 的值为：", e, "，e 的类型为：", type(e))

f = 2 + 4j
g = e + f
print("10. g 的值为：", g, "，g 的类型为：", type(g))

print("11. -1 的绝对值为：", abs(-1))

print("12. 创建的复数为：", complex(1, -2))

print("13. 商和余数为：", divmod(10, 3))

print("14. 浮点型转换：", float(1))

print("15. 10的3次幂为：", pow(10, 3))

print("16. 四舍五入为：", round(5.5))

print("17. 集合求和结果为：", sum({1, 2, 3 ,4}))

print("18. 整数20的二进制为：", bin(20))

print("19. 整数20的八进制为：", oct(20))

print("20. 整数20的十六进制为：", hex(20))

print("21. Unicode 为 97 的字符串：", chr(97))

print("22. 字符串 a 的 Unicode 码：", ord('a'))

print("23. 123 的 boolean 值为：", bool(123))

print("24. 空字符串的 boolean 的值为：", bool(''))

a = 5
b = 10

if (a == b):
    print("25. a 等于 b")
else:
    print("25. a 不等于 b")

if (a != b):
    print("26. a 不等于 b")
else:
    print("26. a 等于 b")

if (a < b):
    print("27. a 小于 b")
else:
    print("27. a 大于等于 b")

if (a > b):
    print("28. a 大于 b")
else:
    print("28. a 小于等于 b")

if (a <= b):
    print("29. a 小于等于 b")
else:
    print("29. a 大于  b")

if (b >= a):
    print("30. b 大于等于 a")
else:
    print("30. b 小于 a")

