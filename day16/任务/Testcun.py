import unittest
from User import User
from Address import Address
from Bank import Bank
class Testcun(unittest.TestCase):
    u = None
    a = None
    b = None
    def setUp(self) -> None:
        self.u = User()
        self.a = Address()
        self.b = Bank()


    def test_cun1(self):
        # 1.准备测试数据
        self.u.setAccount("1")
        self.b.setMoney(1000)
        # 期望结果
        teststart = 1
        # 调用被测方法
        start = self.b.bank_addMoney(self.u.getAccount(), self.b.getMoney())# start 是实际结果
        # 断言
        self.assertEqual(teststart, start)