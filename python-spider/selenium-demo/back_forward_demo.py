import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.jd.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.geekdigging.com/')
browser.back()
time.sleep(1)
browser.forward()