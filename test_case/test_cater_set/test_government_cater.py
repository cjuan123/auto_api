"""
@version: 1.0
@author: chenj
@file: test_government_cater.py
@time: 2019/5/19 12:05
"""
from source.CaterSet.cater import government_Cater
import unittest
from conf import Login


class test_government_cater(unittest.TestCase):
    cater = government_Cater()

    def __init__(self, method_name, param, excepted):
        super(test_government_cater, self).__init__(method_name)
        self.param = param
        self.excepted = excepted

    @Login.get_account("13999999992", "123qwe")
    def test_get_by_idCard(self):
        param = {
            "idcard": self.param
        }

        response = self.cater.get_user_by_idCard(param=param)
        print(response.json())
        self.assertEqual(self.excepted, response.json()["message"])

    @Login.get_account("13999999992", "123qwe")
    def test_add_user(self):
        response = self.cater.add_user(param=self.param)
        print(response.text)
        self.assertEqual(self.excepted, response.json()["message"])


if __name__ == "__main__":
    # unittest.main()
    pass