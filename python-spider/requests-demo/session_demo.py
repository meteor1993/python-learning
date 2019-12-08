import requests

requests.get('https://httpbin.org/cookies/set/number/123456789')
r = requests.get('https://httpbin.org/cookies')
print(r.text)

# Session 示例代码
s = requests.Session()
s.get('https://httpbin.org/cookies/set/number/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)