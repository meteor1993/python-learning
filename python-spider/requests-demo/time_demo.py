import requests

r = requests.get("https://www.geekdigging.com/", timeout = 1)
print(r.status_code)