a = 0

def print_1():
    a = 1
    print('a =', a)

    def print_2():
        a = 2
        print('a =', a)

print_1()
print('a =', a)