# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_construction_app.py
@time: 2019/6/6 14:15
@desc：施工app
"""
import unittest
from conf.IDCard import IDCard
import random
from conf import Login
from source.Transform.construcotr_app import ConstructionApp


class TestConstructionApp(unittest.TestCase):
    construction_app = ConstructionApp()
    id_card = IDCard().idCard(75, 2)
    con_emp_account = "1525621" + str(random.randint(1000, 9999))
    con_emp_name = "api施员工" + str(random.randint(1000, 9999))

    @Login.get_construction_web("13633269651", "123456")
    def test_add_employee(self):
        param = {
            "account": self.con_emp_account,
            "addressDetail": "api测试详细地址",
            "annex": "apiannex",
            "bid": 45,
            "idCard": self.id_card,
            "name": self.con_emp_name,
            "password": "123456",
            "phone": self.con_emp_account,
            "post": 1
            }
        response = self.construction_app.add_employee(param=param)
        print(response.json())

    def test_get_task(self):
        """施工app：获取任务"""
        param = {
            "eId": "",
            "recordId": ""
        }
        response = self.construction_app.get_task(param=param)
        print(response.json())
