from urllib import request, error
import socket

# 访问明显不存在的地址，报错：Not Found
try:
    response = request.urlopen('https://www.geekdigging.com/aa')
except error.URLError as e:
    print(e.reason)

# 访问超时，报错：timed out
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.001)
except error.URLError as e:
    print(e.reason)

# 异常类型示例
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 访问明显不存在的地址，使用 HTTPError 捕捉异常
try:
    response = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

# 优化异常捕捉代码
try:
    response = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Success!')