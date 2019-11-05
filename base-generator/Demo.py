list1 = [x*x for x in range(10)]
print(list1)
# list2 列表创建语句慎重执行，先注释
# list2 = [x*x for x in range(1000000000000000000000000)]

generator1 = (x*x for x in range(1000000000000000000000000))
print(generator1)
print(type(generator1))

generator2 = (x*x for x in range(3))
print(next(generator2))
print(next(generator2))
print(next(generator2))
# print(next(generator2))

generator3 = (x*x for x in range(5))
for index in generator3:
    print(index)

def print_a(max):
    i = 0
    while i < max:
        i += 1
        yield i

a = print_a(10)
print(a)
print(type(a))

print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(a.__next__())
print(a.__next__())

def print_b(max):
    i = 0
    while i < max:
        i += 1
        args = yield i
        print('传入参数为：' + args)

b = print_b(20)
print(next(b))
print(b.send('Python'))

def print_c():
    while True:
        print('执行 A ')
        yield None
def print_d():
    while True:
        print('执行 B ')
        yield None

c = print_c()
d = print_d()
while True:
    c.__next__()
    d.__next__()