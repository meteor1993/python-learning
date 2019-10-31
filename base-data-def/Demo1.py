a = 0

def print_1():
    # a = 1
    print('a1 =', a)

    def print_2():
        a = 2
        print('a2 =', a)

    print_2()

print('a3 =', a)
print_1()

add = lambda x,y: x + y

print(add(1, 2))

max_num = lambda x,y: x if x >= y else y

print(max_num(5, 9))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print('10的阶乘为：', factorial(10))