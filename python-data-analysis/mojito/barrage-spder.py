import requests
import re

# 获取 cid
res = requests.get("https://api.bilibili.com/x/player/pagelist?bvid=BV1PK4y1b7dt&jsonp=jsonp")
cid = res.json()['data'][0]['cid']

# 将弹幕 xml 通过正则取出，生成 list
danmu_url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
result = requests.get(danmu_url).content.decode('utf-8')
pattern = re.compile('<d.*?>(.*?)</d>')
danmu_list = pattern.findall(result)

# 将弹幕 list 保存至 txt 文件
with open("dan_mu.txt", mode="w", encoding="utf-8") as f:
    for item in danmu_list:
        f.write(item)
        f.write("\n")