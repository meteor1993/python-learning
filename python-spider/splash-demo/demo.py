import requests

url = 'http://localhost:8050/render.html?url=https://www.jd.com'
response = requests.get(url)
print(response.text)

url = 'http://localhost:8050/render.png?url=https://www.jd.com&width=1000&height=700'
response = requests.get(url)
with open('jd.png', 'wb') as f:
    f.write(response.content)

url = 'http://localhost:8050/render.har?url=https://www.jd.com'
response = requests.get(url)
print(response.text)

url = 'http://localhost:8050/render.json?url=https://httpbin.org/get'
response = requests.get(url)
print(response.text)

url = 'http://localhost:8050/render.json?url=https://httpbin.org/get&html=1&har=1'
response = requests.get(url)
print(response.text)