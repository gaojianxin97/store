class User:
    __age = 0
    __username = ""
    __sex = ""

    def __init__(self,age,username,sex):
        self.__age = age
        self.__username = username
        self.__sex = sex
        print("我今年 ",age,"，我叫",username,"，我是",sex,"性")

    def setAge(self,age):
        self.__age = age
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

u = User(46,"张三","女")
