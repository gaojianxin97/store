
class OldPhone():
    __brand = ""
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand
    def call(self,name):
        print("正在给",name,"打电话")
class NewPhone(OldPhone):
    def call(self,name):
        print("语音拨号中。。")
        super().call(name)
    def jieshao(self):
        print("品牌为：",self.getBrand(),"的手机很好用")

newphone = NewPhone()
newphone.setBrand("华为")
newphone.call("张三")
newphone.jieshao()
