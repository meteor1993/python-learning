import urllib.request, urllib.parse
import json
request = urllib.request.Request('https://www.geekdigging.com/')
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

url = 'https://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Content-Type': 'application/json;encoding=utf-8',
    'Host': 'geekdigging.com'
}
data = {
    'name': 'geekdigging',
    'hello':'world'
}
data = bytes(json.dumps(data), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))