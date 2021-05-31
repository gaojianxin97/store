from selenium import webdriver
import time
c = webdriver.Chrome()
c.get(r"F:/Python自动化测试技术/Python/功能自动化测试/day01/资料/练习的html/上传文件和下拉列表/autotest.html")
c.maximize_window()
time.sleep(2)
c.find_element_by_xpath("//*[@id='accountID']").send_keys("爱国")
time.sleep(2)
c.find_element_by_xpath("//*[@id = 'passwordID']").send_keys("123456")
time.sleep(2)
c.find_element_by_xpath("//*[@id = 'areaID']").send_keys("北京市")
time.sleep(2)
c.find_element_by_xpath("//*[@id = 'sexID2']").click()
time.sleep(2)
c.find_element_by_xpath("//*[@value='Auterm']").click()
time.sleep(2)
c.find_element_by_xpath("//input[@name='file' and @type ='file']").send_keys(r"C:\Users\高建新\Pictures\新建文件夹\11.jpg")
time.sleep(2)
c.find_element_by_xpath("//*[@id='buttonID']").click()
c.switch_to.alert.accept()
time.sleep(2)
c.quit()



