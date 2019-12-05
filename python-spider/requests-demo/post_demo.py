import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.geekdigging.com/'
}

params = {
    'name': 'geekdigging',
    'age': '18'
}

r = requests.post('https://httpbin.org/post', data = params, headers = headers)
print(r.text)