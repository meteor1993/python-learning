import urllib.request

response = urllib.request.urlopen('https://www.geekdigging.com/')
# 打印内容太长，先注释
# print(response.read().decode('utf-8'))

print(type(response))