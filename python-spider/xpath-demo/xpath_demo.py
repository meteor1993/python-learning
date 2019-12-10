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

result_3 = html.xpath('//main/article')
print(result_3)

result_4 = html.xpath('//main//div')
print(result_4)

result_5 = html.xpath('//img[@alt="小白学 Python 爬虫（16）：urllib 实战之爬取妹子图"]/../@href')
print(result_5)

result_6 = html.xpath('//img[@alt="小白学 Python 爬虫（16）：urllib 实战之爬取妹子图"]/parent::*/@href')
print(result_6)

result_7 = html.xpath('//section/div[@class="container"]')
print(result_7)