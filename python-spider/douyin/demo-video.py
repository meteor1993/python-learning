import requests
import re

# 创建一个请求头
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

# 分享路径
share_url = "https://v.douyin.com/JefvNdx/"

session = requests.Session()
res = session.get(share_url, headers = headers)

# 获取视频 id
item_ids = re.compile(r'itemId: "([0-9]+)"').findall(res.text)[0]

# 拼接请求
item_info_url = f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_ids}"
res_json = session.get(item_info_url, headers = headers).json()

# 获取视频源路径
vedio_url = res_json['item_list'][0]['video']['play_addr']['url_list'][0]

res = requests.get(vedio_url, headers = headers)
with open('demo.mp4', 'wb') as fb:
    fb.write(res.content)

print("视频下载完成~~~")