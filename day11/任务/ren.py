class people:
    name = ""
    gender = ""
    age = 0
    address = ""
    id = "0"
    def information(self):
        print("--------------个人信息---------------")
        print(self.name,"\n",self.gender,"\n",
              self.age,"\n",self.address,"\n",
              self.id
            )

c = people()
c.name = "张三"
c.gender = "男"
c.age = "20"
c.address = "河北省北京市"
c.id = "130823166655414"
c.information()