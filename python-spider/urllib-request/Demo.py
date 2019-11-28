import urllib.request

response = urllib.request.urlopen('https://www.geekdigging.com/')
# 打印内容太长，先注释
# print(response.read().decode('utf-8'))

print(type(response))
# 获取HTTP协议版本号(10 for HTTP/1.0, 11 for HTTP/1.1)
print(response.version)

# 获取响应码
print(response.status)
print(response.getcode())

# 获取响应描述字符串
print(response.reason)

# 获取实际请求的页面url(防止重定向用)
print(response.geturl())

# 获取特定响应头信息
print(response.getheader(name="Content-Type"))
# 获取响应头信息,返回二元元组列表
print(response.getheaders())
# 获取响应头信息,返回字符串
print(response.info())

# 读取响应体
print(response.readline().decode('utf-8'))
