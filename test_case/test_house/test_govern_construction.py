# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_construction.py
@time: 2019/6/13 10:21
@desc：施工单位接口
"""
import unittest
import random
from conf import Login
from tools.read_yaml import ReadYaml
from source.govern_house import GovernHouse


class TestGovernConstruction(unittest.TestCase):

    house = GovernHouse()
    govern_account = str(ReadYaml("default.yaml").get_account("govern"))
    pass_word = ReadYaml("default.yaml").get_password("govern")

    b_id = []
    name = "api施工单位" + str(random.randint(100, 999))
    phone = "139825556" + str(random.randint(100, 999))

    @Login.govern_login(govern_account, pass_word)
    def test_001_add_construction_business(self):
        """【政府端--适老化】：添加施工单位"""
        param = {
            "account": self.phone,
            "address": "办公地址",
            "annexList": [{
                "name": "1",
                "url": "1.txt"
            }, {
                "name": "2",
                "url": "2.png"
            }
            ],
            "businessLicense": random.randint(1000000, 9999999),
            "certificateList": [{
                "name": "1",
                "url": "1.txt"
            }, {
                "name": "2",
                "url": "2.png"
            }],
            "constructorCount": 100,
            "email": "string@163.com",
            "employeeCount": 30,
            "enable": 1,
            "legalPerson": "法人代表",
            "name": self.name,
            "password": "123456",
            "personInCharge": "测试",
            "personPhone": "15282566260",
            "serviceArea": ["510109"]
        }
        response = self.house.add_construction_business(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_002_get_construction_business_list(self):
        """【政府端--适老化】：分页查询施工单位列表"""
        param = {
            "name": self.name,
            "pageNow": 1,
            "enable": 1
        }
        response = self.house.get_construction_business_list(param=param)
        print(response.json())
        self.b_id.append(response.json()["data"]["records"][0]["id"])
        print(self.b_id[0])
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_003_edit_construction_business(self):
        """【政府端--适老化】：编辑施工单位信息"""
        param = {
            "id": self.b_id[0],
            "account": self.phone,
            "businessLicense": "123456789",
            "address": "办公地址(update)",
            "annex": [{
                "name": "1(update)",
                "url": "1.txt"
            }, {
                "name": "2(update)",
                "url": "2.png"
            }
            ],
            "certificate": [{
                "name": "1",
                "url": "1.txt"
            }, {
                "name": "2",
                "url": "2.png"
            }],
            "constructorCount": 100,
            "email": "string@163.com",
            "employeeCount": 30,
            "enable": 1,
            "legalPerson": "法人代表(update)",
            "name": self.name + "(update)",
            "password": "123456",
            "personInCharge": "测试(update)",
            "serviceArea": ["51010901", "51010902", "51010903"]
        }
        response = self.house.edit_construction_business(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("修改成功", response.json()["message"])

    def test_004_get_business_detail(self):
        """【政府端 - -适老化】：获取施工单位信息"""
        param = {
            "bid": self.b_id[0]
        }
        response = self.house.get_business_detail(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.assertEqual(self.phone, response.json()["data"]["account"])

    def test_005_record_construction_list(self):
        """【政府端--适老化】：施工记录"""
        param = {
            "constructionId": self.b_id[0],
            "pageNow": 1
        }
        response = self.house.record_construction_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_006_stop_or_start_constructor(self):
        """【政府端--适老化】：停启施工单位"""
        param = {
            "bId": self.b_id[0],
            "enable": 0
        }
        response = self.house.stop_or_start_constructor(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])


if __name__ == '__main__':
    unittest.main()