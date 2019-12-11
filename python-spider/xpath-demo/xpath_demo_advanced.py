from lxml import etree
import requests

response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
html = etree.HTML(html_str)

result_1 = html.xpath('/html/body/section/div/div/main/article[1]/div[2]/div/h3/a/text()')
print(result_1)

result_2 = html.xpath('/html/body/section/div/div/main/article[1]/div[2]/div/h3/a/@href')
print(result_2)

result_3 = html.xpath('//div[contains(@class, "post-head")]')
print(result_3)

result_4 = html.xpath('//img[@class="img-ajax" and @alt="小白学 Python 爬虫（18）：Requests 进阶操作"]')
print(result_4)

result_5 = html.xpath('//article/div/div/h3[@class="post-title"]/a/text()')
print(result_5)
result_6 = html.xpath('//article[1]/div/div/h3[@class="post-title"]/a/text()')
print(result_6)
result_7 = html.xpath('//article[last()]/div/div/h3[@class="post-title"]/a/text()')
print(result_7)
result_8 = html.xpath('//article[position() < 5]/div/div/h3[@class="post-title"]/a/text()')
print(result_8)

# 节点轴示例
# 获取所有祖先节点
result_9 = html.xpath('//article/ancestor::*')
print(result_9)
# 获取祖先节点 main 节点
result_10 = html.xpath('//article/ancestor::main')
print(result_10)