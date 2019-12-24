from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://182.34.37.0:9999',
    'https': 'https://117.69.150.84:9999'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)