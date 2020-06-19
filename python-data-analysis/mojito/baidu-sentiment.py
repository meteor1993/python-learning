import requests
import time
from pyecharts.charts import Pie
from pyecharts import options as opts
import emoji

grant_type = 'client_credentials'
client_id = 'gL3UmvT6oYprTfVoTlG3HPLY'
client_secret = 'ARyR1GNG3p40r8W4WN8eUvYygeRhMWsG'

# 获取 Baidu API access_token
access_token_url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}&'

res = requests.post(access_token_url)

access_token = res.json()['access_token']

# 通用情感接口
# sentiment_url = f'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={access_token}'
# 定制化情感接口
sentiment_url = f'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify_custom?charset=UTF-8&access_token={access_token}'

with open("dan_mu.txt", encoding="utf-8") as f:
    txt = f.read()
danmu_list = txt.split("\n")

# 情感计数器
optimistic = 0
neutral = 0
pessimistic = 0

for danmu in danmu_list:
    # 因调用 QPS 限制，每次调用间隔 0.5s
    time.sleep(0.5)
    req_data = {
        'text': emoji.demojize(danmu)
    }
    # 调用情感倾向分析接口
    if len(danmu) > 0:
        r = requests.post(sentiment_url, json = req_data)
        print(r.json())
        for item in r.json()['items']:
            if item['sentiment'] == 2:
                # 正向情感
                optimistic += 1
            if item['sentiment'] == 1:
                # 中性情感
                neutral += 1
            if item['sentiment'] == 0:
                # 负向情感
                pessimistic += 1

print('正向情感:', optimistic)
print('中性情感:', neutral)
print('负向情感:', pessimistic)

attr = ['正向情感','中性情感','负向情感']
value = [optimistic, neutral, pessimistic]

c = (
    Pie()
    .add("", [list(attr) for attr in zip(attr, value)])
    .set_global_opts(title_opts=opts.TitleOpts(title="「MOJITO」弹幕情感分析"))
    .render("pie_base.html")
)