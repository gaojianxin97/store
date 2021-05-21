import unittest
from Cal import Calc
class TestCalc(unittest.TestCase):#类就是单元测试的子类
    def test_Add1(self):
        #1.准备测试是数据
        a = 6
        b = 6
        s = 12

        #调用被测方法
        calc = Calc()
        sum = calc.jia(a,b)

        #断言
        self.assertEquals(s,sum)
