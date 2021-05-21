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
        self.u.setAccount("sdfas12")
        self.u.setUsername("123")
        self.u.setPassword("1")
        self.a.setCounrry("中国")
        self.a.setProvince("河北")
        self.a.setStreet("承德")
        self.a.setDoor("1003")

        teststart = 2

        start = self.b.bank_addUser(self.u.getAccount(), self.u.getUsername(), self.u.getPassword(), self.a.getCounrry(),
                                  self.a.getProvicne(), self.a.getStreet(),self.a.getDoor())

        self.assertEqual(teststart, start)