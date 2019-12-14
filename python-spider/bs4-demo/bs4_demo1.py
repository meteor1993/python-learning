from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.find_all(name = "a"))
print(type(soup.find_all(name = "a")[0]))

for a in soup.find_all(name = "a"):
    print(a.string)

print(soup.find_all(attrs={'id': 'link1'}))
print(soup.find_all(attrs={'id': 'link2'}))
print(type(soup.find_all(attrs={'id': 'link1'})))
print(type(soup.find_all(attrs={'id': 'link2'})))

import re

print(soup.find_all(text=re.compile('sisters')))

print(soup.find_all(id='link1'))
print(soup.find_all(class_='title'))

print(soup.find_all(href=re.compile("elsie"), id='link1'))

print(soup.find(name = "a"))
print(type(soup.find(name = "a")))

print(soup.select('#link1'))
print(type(soup.select('#link1')[0]))
print(soup.select('.story .sister'))