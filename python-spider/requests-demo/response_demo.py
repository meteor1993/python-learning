import requests

r = requests.get('https://www.baidu.com')
print(type(r.content), r.content)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)