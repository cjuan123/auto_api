# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_product.py
@time: 2019/6/12 21:30
@desc：适老化：产品
"""
import unittest
import random
from conf import Login
from tools.read_yaml import ReadYaml
from source.govern_house import GovernHouse


class TestGovernProduct(unittest.TestCase):

    house = GovernHouse()
    govern_account = str(ReadYaml("default.yaml").get_account("govern"))
    pass_word = ReadYaml("default.yaml").get_password("govern")
    name = "api产品" + str(random.randint(100, 999))
    product_id = []     # 产品ID

    @Login.govern_login(govern_account, pass_word)
    def test_1_add_product(self):
        """【适老化】：添加产品"""
        param = {
            "imgPath": [{
                "name": "123",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "456",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "789",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }],
            "enable": 1,
            "enableText": "启用",
            "functionParams": "功能参数",
            "name": self.name,
            "price": 100,
            "remark": "产品备注",
            "typeIds": [1, 2, 3, 4, 5, 6, 7, 8]
        }
        response = self.house.add_product(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_2_get_product_list(self):
        """【适老化】：分页查询产品列表"""
        param = {
            "enable": 1,
            "pageNow": 1,
            "name": self.name
        }
        response = self.house.get_product_list(param=param)
        print(response.json())
        self.product_id.append(response.json()["data"]["records"][0]["id"])
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_3_update_product(self):
        """【适老化】：编辑产品信息"""
        param = {
            "id": self.product_id[0],
            "functionParams": "功能参数(update)",
            "name": self.name + "(update)",
            "price": 156.36,
            "remark": "产品备注(update)",
            "typeIds": [1, 7, 5, 3],
            "imgPath": [{
                "name": "1",
                "url": "1.png"
            }, {
                "name": "3",
                "url": "3.png"
            }, {
                "name": "5",
                "url": "5.png"
            }]
            }
        response = self.house.update_product(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("编辑成功", response.json()["message"])

    def test_4_stop_start_product(self):
        """【适老化】：产品停启"""
        param = {
            "enable": 0,
            "pId": self.product_id[0]
        }
        response = self.house.stop_start_product(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_5_get_product_detail(self):
        """【适老化】：查看产品详情"""
        param = {
            "id": self.product_id[0]
        }
        response = self.house.get_product_detail(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.assertEqual(self.name + "(update)", response.json()["data"]["name"])


if __name__ == '__main__':
    unittest.main()
