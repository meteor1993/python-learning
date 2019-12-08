import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("https://www.geekdigging.com/", proxies = proxies)

proxies_socket = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}

requests.get("https://www.geekdigging.com/", proxies = proxies_socket)