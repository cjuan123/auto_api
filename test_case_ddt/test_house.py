# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_product.py
@time: 2019/6/12 21:30
@desc：适老化：产品
"""
import unittest
import random, ddt
from conf import Login
from tools import ddt_tool
from tools.read_yaml import ReadYaml
from source.govern_house import GovernHouse

@ddt.ddt
class TestGovernProduct(unittest.TestCase):

    house = GovernHouse()
    govern_account = str(ReadYaml("default.yaml").get_account("govern"))
    pass_word = ReadYaml("default.yaml").get_password("govern")
    name = "api产品" + str(random.randint(100, 999))
    product_id = []     # 产品ID

    @ddt.data(*ddt_tool.excel_data())
    @Login.govern_login(govern_account, pass_word)
    def test_1_add_product(self, param):
        """【适老化】：添加产品"""
        response = self.house.add_product(param=param[4])
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual(param[5], response.json()["message"])


if __name__ == '__main__':
    unittest.main()
