import time

for i in range(0, 5):
    print(i)
    # time.sleep(1)

print(time.time())

print(time.localtime())

print(time.mktime(time.localtime()))

print(time.asctime(time.localtime()))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

import calendar

print(calendar.calendar(theyear=2020, w=2, l=1, c=6))

print(calendar.month(2019, 11))

print(calendar.monthlen(2019, 11))

print(calendar.weekday(2019, 11, 7))