#
# class car:# 用 class 描述一辆车
#     #属性与行为
#     num = ""
#     color = ""
#     paizi = ""
#     chelun = ""
#     weight = 0
#     def run(self):
#         print("一辆",self.paizi,"正在马路上跑！！！")
# c = car()
# #给车赋值
# c.num = "6"
# c.color = "yellow"
# c.paizi = "奔驰s"
# c.chelun = "8"
# c.weight = "2kg"
# #调用车的方法
# c.run()
#

class people:
    name = ""
    gender = ""
    age = 0
    address = ""
    id = 0
    def information(self):
        print("--------------个人信息---------------")
        print(self.name,"\n",self.gender,"\n",
              self.age,"\n",self.address,"\n",
              self.id
            )

c = people()
c.name = "张三"
c.gender = "男"
c.age = 20
c.address = "河北省北京市"
c.id = 130823166655414