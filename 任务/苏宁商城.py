from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.suning.com")
driver.maximize_window()

#在搜索框输入辣条
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")
time.sleep(2)
#点击搜索按钮
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)
#点击关闭悬浮广告
driver.find_element_by_xpath("//*[@id='pop418']/a").click()
#选择电脑品牌
driver.find_element_by_xpath("//*[@id='联想Lenovo']/a/img").click()
#选择列表中其中一个电脑
driver.find_element_by_xpath("//*[@id='0000000000-12110004127']/div/div/div[2]/div[2]/a").click()
time.sleep(3)
#获取所有打开的窗口
wins = driver.window_handles
driver.switch_to.window(wins[1])
time.sleep(2)
#选择电脑型号
driver.find_element_by_xpath("//*[@id='versionItemList']/dd/ul/li[2]/a").click()
time.sleep(2)
#加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(3)
#去购物车查看
driver.find_element_by_xpath("/html/body/div[39]/div/div[2]/div/div[1]/a").click()
time.sleep(3)
# 退出
driver.quit()


