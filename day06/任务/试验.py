city = {
    "北京":{
        "昌平":{
            "回龙观":["永辉","永旺"],
            "龙泽":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","五道口切糕"],
            "香山":["香山","植物园"],
            "高校":["清华","北大"]
        },
        "朝阳":{
            "朝阳南北塔":["世纪公园","玉渊潭公园"],
            "双塔":["双塔白醋"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡"]
        }
    },
    "天津":{
        "海淀": {
            "公主坟": ["军事博物馆", "五道口切糕"],
            "香山": ["香山", "植物园"],
            "高校": ["清华", "北大"]},
        "龙庆峡":["龙庆峡"],
        "朝阳":["世纪公园","玉渊潭公园"]
    },# 狗不理不好，麻花，煎饼果子
}

# 展示城市下列的方法
def print_place(data):
    for i in data:
        print(i)

while True:
    print("----------------------欢迎来到Jason全国旅游文化有限公司----------------------")
    print_place(city)
    num1 = input("请输入您要去的城市>>>:")
    if num1 in city: # 北京，天津
        print_place(city[num1])  #num1
        num2 = input("请输入二级城市>>>:")
        if num2 == "Q" or num2 == "q":
            print("欢迎下次光临！！！")
        elif num2 in city[num1]:
            print_place(city[num1][num2])
        elif num2 != []:
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])
                num3 = input("请输入三级城市>>>:")
                print("祝您旅途愉快！！")
            elif num3 == "Q" or num3 == "q":
                print("欢迎下次光临！！！")
            elif num3 != city[num1][num2]:
                print("对不起，输入有误，重新输入！！")
        else:
            print("对不起，输入有误，重新输入！！")




    elif num1 == "Q" or num1 == "q":
        print("欢饮下次光临！！！")
        break
    else:
        print("您输入的城市不存在！别瞎弄！！！！")























