import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.taobao.com/robots.txt")
rp.read()

print(rp.can_fetch('Googlebot', 'https://www.taobao.com/article'))
print(rp.can_fetch('Googlebot', "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=iphone&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest"))