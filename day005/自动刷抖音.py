from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver  = webdriver.Remote(server,desired_capabilities)
while True:
    time.sleep(5)
    TouchAction(driver).press(x=446, y=1368).move_to(x=463, y=368).release().perform()

# while True:
#     time.sleep(5)
#     x=500
#     y = 1300
#     dis = 1000
#     driver.swipe(x,y,x,y-dis)