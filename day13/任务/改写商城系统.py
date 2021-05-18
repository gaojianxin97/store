#
# import xlwt
# wt = xlwt.Workbook()
# sheet = wt.add_sheet("商品信息")
# sheet.write(0,0,"Lenovo电脑")
# sheet.write(0,1,7000)
# sheet.write(1,0,"iphone")
# sheet.write(1,1,6000)
# sheet.write(2,0,"华为手机")
# sheet.write(2,1,4000)
# sheet.write(3,0,"华为手表")
# sheet.write(3,1,2000)
# sheet.write(4,0,"卫龙辣条")
# sheet.write(4,1,7)
# sheet.write(5,0,"QQ糖")
# sheet.write(5,1,5999)
# sheet.write(6,0,"卡西欧")
# sheet.write(6,1,3)
# sheet.write(7,0,"洗衣液")
# sheet.write(7,1,60)
# sheet.write(8,0,"牛奶")
# sheet.write(8,1,100)
# wt.save("F:\Pythonwenjian\day13\上课\商城.xls")
# import xlrd
# rb = xlrd.open_workbook(filename="F:\Pythonwenjian\day13\上课\商城.xls",encoding_override=True)
# sheet = rb.sheet_by_name("商品信息")
# rows = sheet.nrows #多少行
# for i in range(rows):
#     print(sheet.row_values(i))




'''
    商城：
        1.商品
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1够了，就添加我的购物车，薪资减去相对应的金额
            4.2不够，买其他的。
        继续买东西，一直到输入Q获取q，退出
'''
import xlwt
shop = [
    ["lenovo thinkpad e580",5000],  # 0
    ["ipad 2021",3000],   # 1
    ["华为手表",3000], #
    ["辣条",3.5],
    ["大米",50],
    ["旺财QQ糖",50]
]
wb = xlwt.Workbook(encoding='utf-8')
sheet = wb.add_sheet("商品信息")
sheet.write(0,0,"商品")
sheet.write(0,1,"价格")
sheet.write(1,0,"lenovo thinkpad e580")
sheet.write(1,1,5000)
sheet.write(2,0,"ipad 2021")
sheet.write(2,1,3000)
sheet.write(3,0,"华为手表")
sheet.write(3,1,1500)
sheet.write(4,0,"辣条")
sheet.write(4,1,5)
sheet.write(5,0,"大米")
sheet.write(5,1,50)
sheet.write(6,0,"旺财QQ糖")
sheet.write(6,1,5)
wb.save("商城改造.xls")

wb.save("F:\Pythonwenjian\day13\上课\商品信息表.xls")
#初始化自己的薪资
salary = input("请输入您的薪资：")
salary = int(salary)
# 我的购物车
mycart = []

while True:
    # 3.展示商品
    for index,value in enumerate(shop): #enumerate()枚举：将所有的可能都列举出来
        print(index,"  ",value)

    # 4.输入要买的编号:num 是商品编号
    num = input("请输入您要买的商品编号：")

    # 若是 0 1 2 3 4 5 6 7 8 9 ，  若是  Q或者q  ,  输入非法
    if num.isdigit():
        num = int(num) # 转换成数字
        # 判断是否有这个商品
        if num >= len(shop):  # 不存在
            print("商品不存在！！！请重新输入！！！")
        else:
            # 可以买东西
            if salary >= shop[num][1]:  # 某个商品的价格:正常买
                # 添加到购物车
                mycart.append(shop[num])  # 添加购物车
                salary = salary - shop[num][1]  # 减去金额
                print("成功添加到购物车！！！余额为：",salary)
            else:
                print("对不起，穷鬼，您的金额不足！！！！！")
    elif num == "Q" or num == "q":
        print("------------欢迎下次光临！！！！----------")
        break
    else:
        print("输入非法！！！！请重新输入！！！")

# 打印购物小条：
print("您本次购物商品如下：")
for index,value in enumerate(mycart):
    print(index,"  ",value)
print("您的余额为：",salary)
