import emoji

with open("dan_mu.txt", encoding="utf-8") as f:
    txt = f.read()
danmu_list = txt.split("\n")

for item in danmu_list:
    print(emoji.demojize(item))
