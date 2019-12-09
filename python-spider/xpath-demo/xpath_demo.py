from lxml import etree
import requests

response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
html = etree.HTML(html_str)
result = etree.tostring(html, encoding = 'UTF-8').decode('UTF-8')
# 输出太长，先注释
# print(result)

result_1 = html.xpath('//*')
print(result_1)

result_2 = html.xpath('//meta')
print(result_2)