import jieba
import pandas as pd
import wordcloud

# 读取弹幕 txt 文件
with open("dan_mu.txt", encoding="utf-8") as f:
    txt = f.read()
danmu_list = txt.split("\n")

# jieba 分词
danmu_cut = [jieba.lcut(item) for item in danmu_list]

# 获取停用词
with open("baidu_stopwords.txt",encoding="utf-8") as f:
    stop = f.read()
stop_words = stop.split()

# 去掉停用词后的最终词
s_data_cut = pd.Series(danmu_cut)
all_words_after = s_data_cut.apply(lambda x:[i for i in x if i not in stop])

# 词频统计
all_words = []
for i in all_words_after:
    all_words.extend(i)
word_count = pd.Series(all_words).value_counts()

wordcloud.WordCloud(
    font_path='msyh.ttc',
    background_color="#fff",
    max_words=1000,
    max_font_size=200,
    random_state=42,
    width=900,
    height=1600
).fit_words(word_count).to_file("wordcloud.png")