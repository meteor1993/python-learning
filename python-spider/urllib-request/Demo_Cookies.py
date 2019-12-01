import http.cookiejar, urllib.request

# 实例化cookiejar对象
cookie = http.cookiejar.CookieJar()
# 使用 HTTPCookieProcessor 构建一个 handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建Opener
opener = urllib.request.build_opener(handler)
# 发起请求
response = opener.open('https://www.baidu.com/')
print(cookie)
for item in cookie:
    print(item.name + ' = ' + item.value)

# cookies 保存 Mozilla 型文件示例
filename = 'cookies_mozilla.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print('cookies_mozilla 保存成功')

# cookies 保存 LWP 型文件示例
filename = 'cookies_lwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print('cookies_lwp 保存成功')

# 请求是使用 Mozilla 型文件
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies_mozilla.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))