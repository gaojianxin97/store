'''
    __init__(self) 无参构造函数 构造方法：任何类都具有该方法，用于快速进行对象的初始化。
    __init(self,属性1，属性2)有参构造函数
    类标准写法：  set/getxxx +  构造方法
'''
class User:
    __age = 0
    __username = ""
    __sex = ""

    def __init__(self,username,age,sex):
        print("我是构造方法，专门用于初始化对象用的。")
        self.__username = username
        self.__age = age
        self.__sex = sex
    def setAge(self,age):
        self.__age =  age
    def getAge(self):
        return self.__age
    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

u = User("Jason",56,"女")  # 构造方法，调用构造方法完成对象的初始化

print(u.getUsername() , "今年",u.getAge(),"，我是",u.getSex() , "性！")

























