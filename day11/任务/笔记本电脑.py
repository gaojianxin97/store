class computer:
    __size = 0   #屏幕大小
    __cpu = ""    #cpu型号
    __memory = 0  #内存大小
    __standby = 0 #待机时长

    def setsize(self,size):
        self.__size = size
    def getsize(self):
        return self.__size


    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu


    def setmemory(self,memory):
        self.__memory = memory
    def getmemory(self):
        return self.__memory


    def setstandby(self,standby):
        self.__standby = standby
    def getstandby(self):
        return self.__standby


    def show(self):       #打字
        print("用",self.__cpu,"打字不死机！！！")
    def playgames(self):    #打游戏
        print("用",self.__cpu,"玩游戏不卡！！")
    def watch(self):    #看电视
        print("用",self.__size,"屏看电视屏幕大！！")


c = computer()
c.setsize (15.6)
c.setcpu ("Intel 酷睿i9 11900k")
c.setmemory (500)
c.setstandby (8)

c.show()
c.playgames()
c.watch()
