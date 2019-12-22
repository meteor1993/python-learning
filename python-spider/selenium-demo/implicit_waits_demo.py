from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10) # seconds
driver.get("https://www.jd.com/")
key = driver.find_element_by_id("key")

print(key)