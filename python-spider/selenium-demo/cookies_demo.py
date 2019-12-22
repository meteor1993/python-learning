from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.geekdigging.com/')
# 获取 cookies
print(browser.get_cookies())
# 添加一个 cookie
browser.add_cookie({'name': 'name', 'domain': 'www.geekdigging.com', 'value': 'geekdigging'})
print(browser.get_cookies())
# 删除所有 cookie
browser.delete_all_cookies()
print(browser.get_cookies())