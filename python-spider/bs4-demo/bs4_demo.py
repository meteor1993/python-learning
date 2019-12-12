import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geekdigging.com/')
soup = BeautifulSoup(response.content, "html5lib")
# 打印内容过长，先注释
# print(soup.prettify())

print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.a)

tag = soup.section
print(tag.name)

print(tag['class'])
print(tag.attrs)

print(soup.title.string)

print(soup.a.img)
print(type(soup.a.img))
print(soup.a.img.attrs)

# 获取子节点
print(soup.article.contents)

for i, child in enumerate(soup.article.children):
    print(i, child)

# 获取所有子孙节点
for i, child in enumerate(soup.article.descendants):
    print(i, child)
# 父节点
print(soup.title.parent)

# 兄弟节点
print('next_sibling：', soup.title.next_sibling)
print('previous_sibling：', soup.title.previous_sibling)
print('next_siblings：', soup.title.next_siblings)
print('previous_siblings：', soup.title.previous_siblings)