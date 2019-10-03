from urllib import request
from lxml import etree
import re
import pymysql

# 数据库连接
def connect():
    conn = pymysql.connect(host='rm-uf6scm3ghrqkk306w9o.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='root',
                           password='wsy@123456',
                           database='test',
                           charset='utf8mb4')

    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}

connection = connect()
conn, cursor = connection['conn'], connection['cursor']

sql_insert = "insert into spider_data(id, plantform, read_num, fans_num, rank_num, like_num, create_date) values (UUID(), %(plantform)s, %(read_num)s, %(fans_num)s, %(rank_num)s, %(like_num)s, now())"

# csdn

req_csdn = request.Request('https://blog.csdn.net/meteor_93')
req_csdn.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_csdn = request.urlopen(req_csdn).read().decode('utf-8')
read_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[3]/dl[2]/dd/@title')[0]
fans_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="fan"]/text()')[0]
rank_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[3]/dl[4]/@title')[0]
like_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[2]/dl[3]/dd/span/text()')[0]

csdn_data = {
    "plantform": 'csdn',
    "read_num": read_num_csdn,
    "fans_num": fans_num_csdn,
    "rank_num": rank_num_csdn,
    "like_num": like_num_csdn
}

cursor.execute(sql_insert, csdn_data)
conn.commit()

print("---------CSDN 数据写入完成---------")

# juejin

req_juejin = request.Request('https://juejin.im/user/5d1ff49c6fb9a07eb67db07b/posts')
req_juejin.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_juejin = request.urlopen(req_juejin).read().decode('utf-8')
read_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/span/span/text()')[0].replace(",", "")
fans_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[2]/a[2]/div[2]/text()')[0].replace(",", "")
rank_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[3]/span/span/text()')[0].replace(",", "")
like_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[1]/span/span/text()')[0].replace(",", "")

juejin_data = {
    "plantform": 'juejin',
    "read_num": read_num_juejin,
    "fans_num": fans_num_juejin,
    "rank_num": rank_num_juejin,
    "like_num": like_num_juejin
}

cursor.execute(sql_insert, juejin_data)
conn.commit()

print("---------掘金 数据写入完成---------")

# cnblog

# 内容多余1页，在第二页能取到最大多少页
req_cnblog = request.Request('https://www.cnblogs.com/babycomeon/default.html?page=2')
req_cnblog.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_cnblog = request.urlopen(req_cnblog).read().decode('utf-8')

max_page_num = etree.HTML(html_cnblog).xpath('//*[@id="homepage_top_pager"]/div/text()')

# 最大页数
max_page_num = re.findall(r"\d+\.?\d*", str(max_page_num))[0]

page_num_cnblog = 1

read_num_cnblog = 0

while int(page_num_cnblog) <= int(max_page_num):
    req_cnblog = request.Request('https://www.cnblogs.com/babycomeon/default.html?page=' + str(page_num_cnblog))
    req_cnblog.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
    html_cnblog = request.urlopen(req_cnblog).read().decode('utf-8')

    # print(html_cnblog)

    read_url_cnblog_list = etree.HTML(html_cnblog).xpath('//*[@id="mainContent"]/div/div[@class="day"]/div[2]/a/@href')

    # 循环所有文章列表
    for read_url in read_url_cnblog_list:
        postId = read_url[37:60].split(".")[0]
        # cnblog 最神奇的地方是阅读数并不是写在页面上的，而是通过这个 GET 请求来获取的
        req_cnblog_read_num = request.Request('https://www.cnblogs.com/babycomeon/ajax/GetViewCount.aspx?postId=' + str(postId))
        req_cnblog_read_num.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
        html_cnblog_read_num = request.urlopen(req_cnblog_read_num).read().decode('utf-8')
        
        read_num_cnblog += int(html_cnblog_read_num)

    page_num_cnblog += 1

# 获取粉丝、排名信息

req_cnblog = request.Request('https://www.cnblogs.com/babycomeon/ajax/news.aspx')
req_cnblog.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_cnblog = request.urlopen(req_cnblog).read().decode('utf-8')

# 粉丝信息
fans_num_cnblog = int(etree.HTML(html_cnblog).xpath('//*[@id="profile_block"]/a[3]/text()')[0])

# 排名信息
req_cnblog = request.Request('https://www.cnblogs.com/babycomeon/ajax/sidecolumn.aspx')
req_cnblog.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_cnblog = request.urlopen(req_cnblog).read().decode('utf-8')
rank_num_cnblog = int(etree.HTML(html_cnblog).xpath('//*[@id="sidebar_scorerank"]/div/ul/li[2]/text()')[0].replace("排名 -", ""))

cnblog_data = {
    "plantform": 'cnblog',
    "read_num": read_num_cnblog,
    "fans_num": fans_num_cnblog,
    "rank_num": rank_num_cnblog,
    "like_num": 0
}

cursor.execute(sql_insert, cnblog_data)
conn.commit()

print("---------CNBLOG 数据写入完成---------")

# segmentfault 未完成

# 第一页
# req_segmentfault = request.Request('https://segmentfault.com/u/geekdingging/articles?page=1')
# req_segmentfault.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
# html_segmentfault = request.urlopen(req_segmentfault).read().decode('utf-8')
# fans_num_segmentfault = etree.HTML(html_segmentfault).xpath('/html/body/div[3]/div/div/div/div[1]/div[2]/div[2]/a/span[2]/text()')[0].replace("人", "")
# rank_num_segmentfault = etree.HTML(html_segmentfault).xpath('/html/body/div[3]/header/div/div/div[2]/div[1]/a/span[1]/text()')[0]

# # 文章页列表
# page_num_segmentfault_list = etree.HTML(html_segmentfault).xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/ul/li/a/text()')
# # 文章最大页数
# max_page_num_segmentfault = page_num_segmentfault_list[len(page_num_segmentfault_list) - 2]

# page_num = 1

# like_num_segmentfault = 0
# read_num_segmentfault = 0

# while page_num <= int(max_page_num_segmentfault):
#     req_segmentfault = request.Request('https://segmentfault.com/u/geekdingging/articles?page=' + str(page_num))
#     req_segmentfault.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
#     html_segmentfault = request.urlopen(req_segmentfault).read().decode('utf-8')
#     # 获取点赞数列表
#     like_num_segmentfault_list = etree.HTML(html_segmentfault).xpath('/html/body/div[3]/div/div/div/div[2]/ul/li/div/div[1]/span/text()')

#     # 获取当前页点赞总数
#     for like_num in like_num_segmentfault_list:
#         like_num_segmentfault += int(like_num.replace("票", "").replace("\n", ""))

#     # 获取文章内容页列表
#     read_url_segmentfault_list = etree.HTML(html_segmentfault).xpath('/html/body/div[3]/div/div/div/div[2]/ul/li/div/div[2]/a/@href')

#     # 循环访问所有内容页，获取阅读数
#     for read_url in read_url_segmentfault_list:
#         req_segmentfault = request.Request('https://segmentfault.com/' + str(read_url))
#         req_segmentfault.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
#         html_segmentfault = request.urlopen(req_segmentfault).read().decode('utf-8')
#         read_num = etree.HTML(html_segmentfault).xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/span/text()')
#         print(read_num)
#     page_num += 1
# print(like_num_segmentfault)