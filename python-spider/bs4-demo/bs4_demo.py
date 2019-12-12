import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
soup = BeautifulSoup(html_str, 'html.parser')
print(soup)