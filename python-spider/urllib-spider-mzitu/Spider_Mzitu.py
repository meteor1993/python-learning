import urllib.request
import os
from lxml import etree
import time
import random

# 请求头添加 UA

# 保存路径
save_path = 'D:\\spider_file'

def get_ua():
	user_agents = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
		'Opera/8.0 (Windows NT 5.1; U; en)',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	]
	user_agent = random.choice(user_agents) #random.choice(),从列表中随机抽取一个对象
	return user_agent

# 创建文件夹
def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    # 切换路径至上面创建的文件夹
    os.chdir(file_path)

# 抓取外页数据
def get_outer(outer_url):
    ua = get_ua()
    headers = {
        'User-Agent': ua,
        'referer': 'https://www.mzitu.com/'
    }
    req = urllib.request.Request(url=outer_url, headers=headers, method='GET')
    resp = urllib.request.urlopen(req)

    html = etree.HTML(resp.read().decode('utf-8'))
    # 获取文件夹名称列表
    title_list = html.xpath('//*[@id="pins"]/li/a/img/@alt')
    # 获取跳转链接列表
    src_list = html.xpath('//*[@id="pins"]/li/a/@href')

    print('当前页面' + outer_url + ', 共计爬取' + str(len(title_list)) + '个文件夹')

    for i in range(len(title_list)):
        file_path = save_path + '\\' + title_list[i]
        img_url = src_list[i]
        # 创建对应文件夹
        createFile(file_path)
        # 写入对应文件
        flag = get_inner(img_url, file_path)
        if flag == False:
            continue


# 抓取内页数据并写入文件
def get_inner(url, file_path):
    ua = get_ua()
    headers = {
        'User-Agent': ua,
        'referer': 'https://www.mzitu.com/'
    }
    try:
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        resp = urllib.request.urlopen(req)

        html = etree.HTML(resp.read().decode('utf-8'))

        # 获取当前页面最大页数
        max_num = html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
        print('当前页面url：', url, ', 最大页数为', max_num)

        for i in range(1, int(max_num)):
            # 访问过快会被限制，增加睡眠时间
            time.sleep(0.5)

            inner_url = url + '/' + str(i)
            inner_req = urllib.request.Request(url=inner_url, headers=headers, method='GET')
            inner_resp = urllib.request.urlopen(inner_req)

            inner_html = etree.HTML(inner_resp.read().decode('utf-8'))

            # 获取图片 url
            img_src = inner_html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
            file_name = str(img_src).split('/')[-1]
            # 下载图片
            try:
                request = urllib.request.Request(url=img_src, headers=headers, method='GET')
                response = urllib.request.urlopen(request)
                get_img = response.read()
                file_os_path = file_path + '\\' + file_name

                if os.path.isfile(file_os_path):
                    print('图片已存在：', file_os_path)
                    return False
                else:
                    with open(file_os_path, 'wb') as fp:
                        fp.write(get_img)
                        print('图片保存成功：', file_os_path)
                        fp.close()
            except Exception as e:
                print('图片保存失败')
            except:
                continue
    except:
        print('爬取报错')
def main():
    url = 'https://www.mzitu.com/xinggan/page/'
    for i in range(1, 163):
        get_outer(url + str(i))

if __name__ == '__main__':
    main()