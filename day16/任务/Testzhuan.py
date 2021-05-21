import unittest
from User import User
from Address import Address
from Bank import Bank
class Testcun(unittest.TestCase):
    u = None
    a = None
    b = None
    u1 = None
    def setUp(self) -> None:
        self.u = User()
        self.a = Address()
        self.b = Bank()
        self.u1 = User()


    def test_zhuan1(self):
        # 1.准备测试数据
        self.u.setAccount("1")
        self.u1.setAccount("2")
        self.u.setPassword("1")
        self.b.setMoney(10)

        teststart = 1

        start = self.b.bank_transfer(self.u.getAccount(),self.u1.getAccount(),self.u.getPassword(),self.b.getMoney())

        self.assertEqual(teststart, start)