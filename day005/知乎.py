from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.zhihu.android",
  "appActivity": "com.zhihu.android.app.ui.activity.MainActivity"
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(8)
el1 = driver.find_element_by_id("com.zhihu.android:id/view_guide_info")
el1.click()

el2 = driver.find_element_by_id("com.zhihu.android:id/login_username")
el2.send_keys("908563720@qq.com")
time.sleep(2)
el3 = driver.find_element_by_id("com.zhihu.android:id/login_password")
el3.send_keys("gaojianxin1017.")
time.sleep(10)
el4 = driver.find_element_by_id("com.zhihu.android:id/btn_func")
el4.click()
time.sleep(10)
# el1 = driver.find_element_by_id("com.zhihu.android:id/input")
# el1.click()
el5 = driver.find_element_by_id("com.zhihu.android:id/input")
el5.send_keys("笔记本电脑")

driver.quit()
