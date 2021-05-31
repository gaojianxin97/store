from selenium import webdriver
import time
#创建谷歌浏览器对象
c = webdriver.Chrome()
#打开网址
c.get(r"F:/Python自动化测试技术/Python/功能自动化测试/day01/资料/练习的html/main.html")
#窗口最大化
c.maximize_window()
#切换到ID = frame这个框架页里
c.switch_to.frame("frame")

c.find_element_by_id("input1").send_keys("123456465465")
time.sleep(3)
c.quit()




