from urllib.parse import urlparse

o = urlparse('https://www.baidu.com/s?ie=UTF-8&wd=python')
print(type(o))
print(o)