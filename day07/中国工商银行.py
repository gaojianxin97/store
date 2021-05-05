import random
# 1. 空的银行的库 ： 100个
users = {}

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
    if len(users) >= 100:
        return 3

    # 判断是否存在
    if account in users:
        return 2

    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1


# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
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
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")



# 用户存钱方法    zh ：账号
def cun():
    zh = input("请输入您的账号：")
    if zh in users:
        jine = int(input("请输入存钱金额："))
        users[zh]["money"] =0+jine
        print("存钱成功，当前账户余额为：",users[zh]["money"],"元")
    else:
        print("不存在该用户，请重新输入！！")

# 用户取钱    mm ：密码
def qu():
    zh = input("请输入您的账号：")
    if zh in users.keys():
        print("账户存在！")
        password = input("请输入您的密码：")
        if password == users[zh]["password"]:
            print("密码正确！")
            quqian = int(input("请输入取钱金额："))
            if quqian <= users[zh]["money"] :
                users[zh]["money"] = users[zh]["money"]-quqian
                print("取钱成功！","您的余额为：",users[zh]["money"])
            else:
                print("取钱失败，没有这么多钱！！")
                return 3
        else:
            print("请输入正确的密码！！！")
            return 2
    else:
        print("请输入用户账号不存在！！！")
        return 1

# 转账        zcje : 转出金额
def zhuan():
    zhuanchu = input("请输入转出账号：")
    if zhuanchu in users.keys():
        zhuanru = input("请输入转入账号：")
        if zhuanru in users.keys():
            password = input("请输入您的密码：")
            if password == users[zhuanchu]["password"]:
                print("密码正确！")
                zcje= int(input("请输入转出金额："))
                if zcje<=users[zhuanchu]["money"]:
                    users[zhuanru]["money"]=zcje
                    users[zhuanchu]["money"] = users[zhuanchu]["money"]-zcje
                    print("转出账号余额：",users[zhuanchu]["money"],
                          "转入账号余额：",users[zhuanru]["money"])
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
    if cxzh in users.keys():
        cxmm = input("请输入要查询账号的密码：")
        if cxmm  ==  users[cxzh]["password"]:
            print("当前账号：",users[cxzh]["username"],"密码：",users[cxzh]["password"],
                  "余额：",users[cxzh]["money"],"用户居住地址：",users[cxzh]["country"],
                  users[cxzh]["province"],users[cxzh]["street"],users[cxzh]["door"],
                  "账户开户行：",bank_name)
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




