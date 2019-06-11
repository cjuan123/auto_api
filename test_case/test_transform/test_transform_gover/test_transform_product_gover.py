# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_transform_product_gover.py
@time: 2019/6/3 17:42
@desc：政府端--适老化改造
        添加产品、编辑产品等产品相关操作
"""
import unittest
import random
from conf import Login
from source.Transform.transform_govern import Transform


class TestTransformGovern(unittest.TestCase):

    transform = Transform()
    name = "api产品" + str(random.randint(0, 100))
    product_id = []

    @Login.get_account("18981967059", "123qwe")
    def test_001_add_product(self):
        """【政府端--适老化】：添加产品"""
        param = {
            "imgPath": [{
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }],
            "enable": 1,
            "enableText": "启用",
            "functionParams": "功能参数",
            "name": self.name,
            "price": 1000,
            "remark": "产品备注",
            "typeIds": [1, 2, 3, 4, 5, 6, 7, 8]
            }
        response = self.transform.add_product(param=param)
        print(response.json())
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_002_get_product_list(self):
        """【政府端--适老化】：分页查询产品列表"""
        param = {
            "enable": 1,
            "pageNow": 1,
            "name": self.name
        }
        response = self.transform.get_product_list(param=param)
        print(response.json())
        self.product_id.append(response.json()["data"]["records"][0]["id"])
        print(self.product_id[0])

    def test_003_update_product(self):
        """【政府端--适老化】：编辑产品信息"""
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
        response = self.transform.update_product(param=param)
        print(response.json())

    def test_004_stop_start_product(self):
        """【政府端--适老化】：产品停启"""
        param = {
            "enable": 0,
            "pId": self.product_id[0]
        }
        response = self.transform.stop_start_product(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_get_product_detail(self):
        """【政府端--适老化】：查看产品详情"""
        param = {
            "id": self.product_id[0]
        }
        response = self.transform.get_product_detail(param=param)
        print(response.json())
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.assertEqual(self.name + "(update)", response.json()["data"]["name"])


if __name__ == "__main__":
    unittest.main()