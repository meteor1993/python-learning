from selenium import webdriver

proxy = '222.95.241.6:3000'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=https://' + proxy)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://httpbin.org/get')