import requests

proxies = {
    'http': 'http://59.52.186.117:9999',
    'https': 'https://222.95.241.6:3000',
}
try:
    response = requests.get('https://httpbin.org/get', proxies = proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)