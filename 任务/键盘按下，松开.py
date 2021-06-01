from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
a = ActionChains(driver)
#寻找搜索输入框
driver.find_element_by_id("kw")
time.sleep(5)
a.key_down("a").key_up("a").perform()
driver.quit()