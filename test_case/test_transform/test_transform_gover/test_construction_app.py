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
    con_emp_id = []
    con_emp_account = "1525621" + str(random.randint(1000, 9999))
    con_emp_name = "api施员工" + str(random.randint(1000, 9999))

    @Login.get_construction_web("13633268550", "123456")
    def test_add_employee(self):
        print(self.con_emp_name)
        param = {
            "account": self.con_emp_account,
            "addressDetail": "api测试详细地址",
            "annex": "apiannex",
            "bid": 44,
            "idCard": self.id_card,
            "name": self.con_emp_name,
            "password": "123456",
            "phone": self.con_emp_account,
            "post": 1
            }
        response = self.construction_app.add_employee(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    @Login.get_construction_web("13633261866", "123456")
    def test_employee_list(self):
        """施工单位：查询员工列表"""
        param = {
            "name": self.con_emp_name,
            "pageNow": 1
        }

        response = self.construction_app.employee_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        print(len(response.json()["data"]["records"]))
        self.con_emp_id.append(response.json()["data"]["records"][0]["id"])
        print(self.con_emp_id[0])

    @Login.get_construction_app("13633269651", "123456")
    def test_get_task(self):
        """施工app：获取任务"""
        param = {
            # self.con_emp_id[0],
            "recordId": 63
        }
        response = self.construction_app.get_task(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取成功", response.json()["message"])

    @Login.get_construction_app("15256216643", "123456")
    def test_my_task_list(self):
        param = {
            "pageNow": 1
        }
        response = self.construction_app.my_task_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_construction_details(self):
        param = {
            "id": 63
        }
        # response = self.construction_app.


if __name__ == '__main__':
    unittest.main()