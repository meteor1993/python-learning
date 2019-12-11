from lxml import etree
import requests

response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
html = etree.HTML(html_str)

