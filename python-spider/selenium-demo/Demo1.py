from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('极客挖掘机')
input.send_keys(Keys.ENTER)
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
# 关闭浏览器
browser.close()

# 声明浏览器对象，需对应的驱动程序方可使用
# browser = webdriver.android()
# browser = webdriver.blackberry()
# browser = webdriver.chrome()
# browser = webdriver.edge()
# browser = webdriver.firefox()
# browser = webdriver.ie()
# browser = webdriver.opera()
# browser = webdriver.phantomjs()
# browser = webdriver.safari()