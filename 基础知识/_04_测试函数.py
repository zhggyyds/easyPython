# 测试不用自己调用方法，Python会自己调用
# 1.测试需要引入需要的函数和unittest
from _03_country import get_country_city as gcc
import unittest


# 2.创建一个继承unittest.TestCase的类,python才知道怎么运行你的测试
class TestGcc(unittest.TestCase):
    """"测试"""
    # 这个类包含测试成员函数，以test打头，python只运行test打头的方法
    def test_01(self):
        res = gcc('China', 'Beijing')
        # 3.断言方法↓，检查是否确实如此
        self.assertEqual(res, 'Beijing,China')

    def test_02(self):
        res = gcc('China', 'Beijing', 5_0000_0000)
        # 断言方法↓，检查是否确实如此
        self.assertEqual(res, 'Beijing,China - population 500000000')


if __name__ == '__main__':
    # 4.下面是测试开始
    unittest.main()
