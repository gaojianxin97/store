
import random
num = random.randint(0,5)
jb = 5000
xhcs = 0
while True:
    xhcs =xhcs + 1
    num1 = input("请输入您猜的数字：")
    num1 = int(num1)
    if num1 > num :
        print("大了")
        jb = jb-100
    elif num1 < num :
        print("小了")
        jb = jb-100
    elif num1 == num:
        print("恭喜您猜中了！中奖号码为：",num,"循环次数为：",xhcs,"次")
        print("金币为：",jb)
    else:
        print("您的输入有误")
        break #中断
