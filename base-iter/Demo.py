from collections.abc import Iterable

print(isinstance('geekdigging', Iterable))
print(isinstance([], Iterable))
print(isinstance([], Iterable))
print(isinstance({x for x in range(5)}, Iterable))
print(isinstance(123, Iterable))

list1 = [1, 2, 3, 4]
# 错误使用方式
# next(list1)

from collections.abc import Iterator

list1 = iter(list1)
print(type(list1))

print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
# StopIteration 异常
# print(next(list1))

set1 = {1, 2, 3, 4, 5}
set1 = iter(set1)
print(next(set1))
print(next(set1))
print(next(set1))
print(next(set1))
print(next(set1))