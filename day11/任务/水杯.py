class glass:
    __height = 0
    __volume = 0
    __color = ""
    __material = ""

    def setheight(self,height):
        self.__height = height
    def getheight(self):
        return self.__height


    def setvolume(self,volume):
        self.__volume = volume
    def getvolume(self):
        return self.__volume


    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color


    def setmaterial(self,material):
        self.__material = material
    def getmaterial(self):
        return self.__material

    def shou(self):
        print("这个",self.__color,"的",self.__material,"水杯高度为：",self.__height,
        "容积为：" ,self.__volume)

c = glass()
c.setheight ("20cm")
c.setvolume ("500ml")
c.setcolor ("透明")
c.setmaterial  ("玻璃")
c.shou()