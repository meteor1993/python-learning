from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.jd.com/')
input_key = browser.find_element_by_id('key')
input_key1 = browser.find_element(By.ID, 'key')
print(input_key)
print(input_key1)

lis = browser.find_elements_by_css_selector('.cate_menu li')
print(lis)
browser.close()