'''

6个厨师正在造面包，造完后扔到面包篮子里，
窗外有5个人，抢买面包。
面包篮子 只能存300个面包，厨师如果发现篮子慢了 暂停3秒，然后继续放
跑5分钟时间，统计厨师共造了多少个面包，，顾客买了多少个，
每个顾客付了多少钱 （10块/个）

'''
from threading import Thread
import time
shijian = 0
s = 0
a = 0
class clock(Thread):
    def run(self) -> None:
        global shijian
        while shijian<30:
            shijian.sleep(1)
            shijian =shijian+1

class cook(Thread):
    username = ""
    def run(self) -> None:
        global s
        global a
        while shijian<30:
            if s <= 300:
                s = s+1
                a = a+1
                # print(self.username,"造了",s,"面包")
            else:
                print("篮子满了，停3秒")
                time.sleep(3)
        else:
            print("时间到.",self.username,"做了",s,"六个人一个做了",a)
            time.sleep(3)

class people(Thread):
    nam = ""
    ge = 0
    def run(self) -> None:
        global s
        while shijian<30:
            if s > 0 :
                s = s-1
                self.ge = self.ge+1
            else:
                print("厨师共造了",a,self.nam,"买了",self.ge,"个","付了",self.ge*10,"钱")
                time.sleep(3)
c = clock()
c1 = cook()
c2 = cook()
c3 = cook()
c4 = cook()
c5 = cook()
c6 = cook()
c1.username = "张家辉"
c2.username = "杜旱情"
c3.username = "旺财"
c4.username = "手动阀"
c5.username = "斯拉克"
c6.username = "账上"
p=people()
p1=people()
p2=people()
p3=people()
p4=people()
p.nam = "张三"
p1.nam = "张四"
p2.nam = "张五"
p3.nam = "张六"
p4.nam = "张七"

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()

p.start()
p1.start()
p2.start()
p3.start()
p4.start()
