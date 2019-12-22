from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.taobao.com/')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')