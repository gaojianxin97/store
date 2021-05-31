from selenium import webdriver
import time
c = webdriver.Chrome()
c.get(r"F:/Python自动化测试技术/Python/功能自动化测试/day01/资料/练习的html/弹框的验证/dialogs.html")
c.maximize_window()
c.find_element_by_id("alert").click()
time.sleep(3)
c.switch_to.alert.accept()  #   .accept 点击确认   .dismiss 点击取消
time.sleep(2)
c.quit()

