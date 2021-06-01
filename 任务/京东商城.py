from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
#打开浏览器
driver.get(r"https://www.jd.com")
#放大窗口
driver.maximize_window()
#点击登录
driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
time.sleep(2)
#点击账户登录
driver.find_element_by_link_text("账户登录").click()
time.sleep(2)
#输入账号 密码
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("17336341612")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("12345685209.")
time.sleep(2)
#点击登录按钮
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(10)
#将鼠标放在手机上
ele = driver.find_element_by_xpath("//*[@id='J_cate']/ul/li[2]/a[1]")
ac = ActionChains(driver)
ac.move_to_element(ele).perform()
time.sleep(2)
#点击微单相机
driver.find_element_by_xpath("//*[@id='cate_item2']/div[1]/div[2]/dl[4]/dd/a[2]").click()
#获取所有打开窗口
wins = driver.window_handles
driver.switch_to.window(wins[1])
time.sleep(2)
#选择相机
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[4]/div/div[3]/a/em").click()
time.sleep(2)
#获取所有打开窗口
wins = driver.window_handles
driver.switch_to.window(wins[2])
time.sleep(2)
#点击加入购物车
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(3)
#退出
driver.quit()

