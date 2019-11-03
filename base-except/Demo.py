def division(x, y):
    try:
        return x / y
    except:
        print('程序报错啦！！！')
        return None

print(division(15, 5))

def division1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('程序报错啦！！！')
        return None

print(division1(15, 0))

def division2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('您输出的除数为 0 ！！！')
        return None
    except TypeError:
        print('您输出的参数类型非法！！！')
        return None

print(division2('python', 0))

def division3(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('您输出的除数为 0 ！！！')
        return None
    except TypeError:
        print('您输出的参数类型非法！！！')
        return None
    finally:
        print('你一定能看到我！！！')

print(division3(15, 3))
print(division3('python', 0))