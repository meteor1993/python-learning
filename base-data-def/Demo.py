def add(a, b):
    c = a + b
    return c


c = add(1, 2)
print(c)


def subtraction(a, b):
    return a - b


print(subtraction(b=5, a=10))


def division(a, b=1):
    return a / b


print(division(5))
print(division(10, 5))


def print_a(a, *b):
    print(a, b)


print_a(1, 2, 3, 4, 5, 6)


def print_b(a, **b):
    print_a(a, b)


print_b(1, q='q', w='w', e='e')

print_a(1)
print_b(1)