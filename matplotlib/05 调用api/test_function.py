"""function文件中函数的单元测试"""

import unittest
from function import get_response_status


class StatusTestCase(unittest.TestCase):

    def test_status(self):
        url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
        resp = get_response_status(url)
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()