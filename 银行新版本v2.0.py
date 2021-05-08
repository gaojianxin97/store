import random

from DBUtils import update
from DBUtils import select

# 1. 空的银行的库 ： 100个

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    sql = "select count(*) from blank"
    data = select(sql,[])
    if data[0][0] >= 100:
        return 3

    # 判断是否存在
    sql1 = "select * from blank where account = %s"
    data1 = select(sql1,account)
    if len(data1) != 0:
        return 2

    #正常开户
    #数据存到数据库中
    sql2 = "insert into blank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,0,bank_name]
    update(sql2,param2)
    return 1

# 用户开户方法
def addUser():
    # 随机获取账号
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")


# 用户存钱方法    zh ：账号
def cun():
    zh = input("请输入您的账号：")
    sql = "select * from blank where account = %s"
    param = [zh]
    data = select(sql,param)
    if len(data) != 0:
        jine = int(input("请输入存钱金额："))
        sql1 = "update blank set money = money + %s where account = %s"
        param1 = [jine,zh]
        update(sql1,param1)
        print("存钱成功!!")
    else:
            print("不存在该用户，请重新输入！！")


# 用户取钱    mm ：密码
def qu():
    zh = input("请输入您的账号：")
    sql = "select * from blank where account = %s"
    param = [zh]
    data = select(sql,param)
    if len(data) != 0:
        print("账户存在！")
        password = input("请输入您的密码：")
        sql1 = "SELECT passwords FROM blank WHERE account =  %s"
        data1 = select(sql1,param)
        print(data1[0][0])
        if data1[0][0] == password:
            quqian = int(input("请输入取钱金额："))
            sql3 = "SELECT money FROM blank WHERE account =  %s"
            data3 = select(sql3,param)
            print(data3)
            if quqian <= data3[0][0] :
                sql2 = "update blank set money = money - %s where account = %s"
                param1 = [quqian,zh]
                update(sql2, param1)
                print("取钱成功！！")
            else:
                print("取钱失败，金额不足！")

        else:
            print("请输入正确的密码！！！")
            return 2
    else:
        print("请输入用户账号不存在！！！")
        return 1


# 转账        zcje : 转出金额
def zhuan():
    zhuanchu = input("请输入转出账号：")
    sql = "select * from blank where account = %s"
    param = [zhuanchu]
    data = select(sql,param)
    if len(data) != 0:
        zhuanru = input("请输入转入账号：")
        sql1 = "select * from blank where account = %s"
        param1 = [zhuanru]
        data1 = select(sql1, param1)
        if len(data1) != 0:
            password = input("请输入您的密码：")
            sql2 = "SELECT passwords FROM blank WHERE account =  %s"
            data2 = select(sql2, param)
            print(data2[0][0])
            if data2[0][0] == password:
                print("密码正确！")
                zcje= int(input("请输入转出金额："))
                sql3 = "SELECT money FROM blank WHERE account =  %s"
                data3 = select(sql3, param)
                print(data3)
                if zcje <= data3[0][0]:
                    sql2 = "update blank set money = money - %s where account = %s"
                    param1 = [zcje, zhuanchu]
                    update(sql2, param1)
                    sql2 = "update blank set money = money + %s where account = %s"
                    param1 = [zcje, zhuanru]
                    update(sql2, param1)
                    print("转账成功！！")
                else:
                    print("金额不足，转账失败！！")
                    return 3
            else:
                print("您输入的转出账号密码不正确！！")
                return 2
        else:
            print("转入账号不存在！！")
            return 1
    else:
        print("转出账号不存在！！")
        return 1


# 查询        cxzh : 查询账号   cxmm ：查询密码
def cha():
    cxzh = input("请输入要查询的账号：")
    sql = "select * from blank where account = %s"
    param = [cxzh]
    data = select(sql,param)
    if len(data) != 0:
        cxmm = input("请输入要查询账号的密码：")
        sql1 = "SELECT passwords FROM blank WHERE account =  %s"
        data1 = select(sql1,cxzh)
        if cxmm == data1[0][0]:
            info = '''
                        ------------个人信息----------------
                        账号：%s,
                        用户名：%s,
                        取款密码：%s,
                        地址信息：
                            国家：%s,
                            省份：%s,
                            街道：%s,
                            门牌号：%s,
                        余额：%s,
                        开户行：%s
                        -----------------------------------
                    '''
            print(info % (data[0][0],data[0][1], data[0][2],data[0][3],
                          data[0][4],data[0][5], data[0][6],data[0][7],
                          bank_name))
        else:
            print("您输入的密码不正确，请重新输入！！")

    else:
        print("该用户不存在，请重新输入！！")


while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            cun()
        elif num == 3:
            qu()
        elif num == 4:
            zhuan()
        elif num == 5:
            cha()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")




