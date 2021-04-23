name = ["高建新","叶浩宇","冯文泽","杜汗卿","李文聪","任明帅"]
import random
while True:
    print("1:随机点名       2:随机处罚》》》：")
    num = input("请输入编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            A = random.randint(0,len(name)-1)
            print(name[A])
        elif num== 2:
            B = random.randint(0,100)
            print("恭喜您处罚",B,"遍！！")
    elif num == "q" or num == "Q":
        print("系统退出！")
        break
    else:
        print("输入非法！！")





