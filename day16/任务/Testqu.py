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


    def test_qu1(self):
        # 1.准备测试数据
        self.u.setAccount("1")
        self.u.setPassword("1")
        self.b.setMoney(10)
        #2.期望结果
        teststart = 0

        start = self.b.bank_withdrawal(self.u.getAccount(),self.u.getPassword(),self.b.getMoney())

        self.assertEqual(teststart, start)