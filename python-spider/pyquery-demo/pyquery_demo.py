from pyquery import PyQuery
import requests

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

d = PyQuery(html)
print(d('p'))

d_url = PyQuery(url='https://www.geekdigging.com/', encoding='UTF-8')
print(d_url('title'))

r = requests.get('https://www.geekdigging.com/')
r.encoding = 'UTF-8'
d_requests = PyQuery(r.text)
print(d_requests('title'))

d_css = PyQuery(html)
print(d_css('.story .sister'))
print(type(d_css('.story .sister')))

# 查找子节点
items = d('body')
print('子节点：', items.find('p'))
print(type(items.find('p')))

# 查找父节点
items = d('#link1')
print('父节点：', items.parent())
print(type(items.parent()))

# 查找兄弟节点
items = d('#link1')
print('兄弟节点：', items.siblings())
print(type(items.siblings()))

a = d('a')
for item in a.items():
    print(item)

a_1 = d('#link1')
print(a_1.text())

a_2 = d('.story')
print(a_2.html())

attr_1 = d('#link1')
print(attr_1.attr('href'))

print(attr_1.attr.href)