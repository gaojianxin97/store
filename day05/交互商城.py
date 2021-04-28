'''
    商城：
        1、商品
        2、薪资
        3、我的购物车
    逻辑：
        1、初始化您的薪资
        2、展示商城商品
        3、输入商品标号
        4、看钱够不够
            4.1、够了，就添加到我的购物车，薪资减去相对应的金额
            4.2、不够，买其他的。
        继续买东西，一直到输入q或Q，退出
'''
shop =  [
    ["lenovo电脑",7000],  #0
    ["iphone",5000],    #1
    ["华为手表",3000],  #2
    ["华为手机",4000],  #3
    ["卫龙辣条",700],
    ["QQ糖",3],
    ["洗衣液",60],
    ["牛奶",100],
    ["薯片",9]
]
#   随机生成1，2
l = 0
b = 0
import random
for i in range(1):
    num = random.randint(1, 30)
    print(num)
    if num<=10 and num>=1:
        print("恭喜您获得辣条优惠券：满60减30")
        l = 1
    else:
        print("恭喜您获得lenovo电脑优惠券：半折甩卖")
        b = 1
# 2.初始化自己的薪资
salary = input("请输入您的薪资：")
salary = int(salary)
salary1 = salary
# 我的购物车
mycart = []
while True:
    #3.展示商品
    for index,value in enumerate(shop):#将所有的可能都列举出来
        print(index," ",value)
    #4.输入要买的编号：num是商品编号
    num = input("请输入要购买商品的编号：")
    #若输入的是0 1 2 3 4 5 6 7 8 9，成功，若是q或者Q  退出，若是其他，输入非法。
    if num.isdigit(): #num.是不是由数字组成
        num = int(num)
        if num >= len(shop): #商品不存在
            print("商品不存在！！请重新输入！！！")
        else:
            #可以买东西
            if salary >= shop[num][1]:  #某个商品的价格小于等于薪资可以购买
                if l == 1:
                    mycart.append(shop[num])  # 添加购物车


                    print("成功添加购物车！！余额为：", salary - shop[num][1] + 300)
                    salary = salary - shop[num][1]  # 减去金额
                elif b==1:
                    mycart.append(shop[num])    #添加购物车
                    salary  = salary-shop[num][1]   #减去金额
                    print("成功添加购物车！！余额为：",salary+(shop[num][1]*0.5))
                else:
                    mycart.append(shop[num])    #添加购物车
                    salary  = salary-shop[num][1]   #减去金额
                    print("成功添加购物车！！余额为：",salary)
            else:
                print("您的金额不足！！无法购买！！")
    elif num == "q" or num == "Q":
        print("退出成功，欢迎下次光临！！")
        break
    else:
        print("输入非法！！重新输入！！！")
#   打印购物票
print("您本次购物商品如下：")
for index,value in enumerate(mycart):
    print(index,"",value)
print("您的余额为：",salary,"您的积分为：",(salary1-salary)/10)#积分（等于开始薪资-消费金额）/10





