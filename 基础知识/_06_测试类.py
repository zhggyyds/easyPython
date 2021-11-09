# 我认为测试就是：自己模拟一遍代码执行流程，本来应该是用户输入，我们自行赋予变量值，再让python自动执行测试用例判断是否正确

from _05_Employee import Employee
import unittest


# 1.测试用例↓
class Test(unittest.TestCase):
    # setup方法中变量在所有方法中可以共用，这样不用每次都新建实例
    def setUp(self):
        # 2.测试对象↓
        self.person = Employee('z', 'h', 5000)

    # 3.测试方法↓
    def test_01(self):
        self.person.give_raise()
        self.assertEqual(self.person.salary, 10000)

    def test_02(self):
        self.person.give_raise(10000)
        self.assertEqual(self.person.salary, 15000)


if __name__ == '__main__':
    unittest.main()
