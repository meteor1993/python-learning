import requests
import re
import wordcloud

res = requests.get("https://api.bilibili.com/x/player/pagelist?bvid=BV1FV411d7u7&jsonp=jsonp")
cid = res.json()['data'][0]['cid']
print(cid)

danmu_url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
result = requests.get(danmu_url).content.decode('utf-8')
pattern = re.compile('<d.*?>(.*?)</d>')
danmu_list = pattern.findall(result)

wordcloud = wordcloud.WordCloud(font_path='msyh.ttc', width=900, height=1600).generate("".join(danmu_list))
wordcloud.to_file('wordcloud.png')