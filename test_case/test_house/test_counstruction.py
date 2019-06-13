# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_counstruction.py
@time: 2019/6/13 11:16
@desc：施工
"""
import unittest
import random
from conf import Login
from conf.IDCard import IDCard
from source.construction import Construction
from source.govern_house import GovernHouse


class Agencies(unittest.TestCase):

    construction = Construction()
    house = GovernHouse()

    id_card = IDCard().idCard(75, 2)
    con_emp_id = []
    con_emp_account = "1525621" + str(random.randint(1000, 9999))
    con_emp_name = "api施员工" + str(random.randint(1000, 9999))
    scheme = []

    @Login.get_construction_web("13633262703", "123456")
    def test_add_employee(self):
        print(self.con_emp_name)
        param = {
            "account": self.con_emp_account,
            "addressDetail": "api测试详细地址",
            "annex": "apiannex",
            "bid": 99,
            "idCard": self.id_card,
            "name": self.con_emp_name,
            "password": "123456",
            "phone": self.con_emp_account,
            "post": 1
            }
        response = self.construction.add_employee(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_employee_list(self):
        """施工单位：查询员工列表"""
        param = {
            "name": self.con_emp_name,
            "pageNow": 1
        }

        response = self.construction.employee_list(param=param)
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
        response = self.construction.get_task(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取成功", response.json()["message"])

    @Login.get_construction_app("15256218834", "123456")
    def test_my_task_list(self):
        param = {
            "pageNow": 1
        }
        response = self.construction.my_task_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    @Login.get_construction_app("15256218834", "123456")
    def test_01_construction_details(self):
        param = {
            "id": 91
        }
        response = self.construction.construction_details(param=param)
        print(response.json())
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["id"])
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["productImg"])

    def test_02_commit_scheme(self):
        param = {
            "recordId": 91,
            "scheme": str({
                "id": self.scheme[0],
                "transformBefore": self.scheme[1],
                "transformMiddle": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png",
                "transformAfter": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png",
                "remark": "api施工小程序产品备注"
            })
        }
        print(param)
        response = self.construction.commit_scheme(data=param)
        print(response.json())

    @Login.get_account("18981967059", "123qwe")
    def test_03_govern_get_project_inspection_list(self):
        param = {
            "pageNow": 1
        }
        response = self.house.get_project_inspection_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    @Login.get_account("18981967059", "123qwe")
    def test_04_govern_check_transform_scheme(self):
        param = {
            "schemeId": 83,
            "recordId": 91,
            "qualified": 1
        }
        response = self.house.check_transform_scheme(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("验收成功", response.json()["message"])

    # @Login.get_account("18981967059", "123qwe")
    def test_05_get_transform_settlement_list(self):
        """项目结算"""
        param = {
            "pageNow": 1
        }
        response = self.house.get_transform_settlement_list(data=param)
        print(response.json())

    def test_06_settlement(self):
        param = {
            "id": 91
        }
        response = self.house.settlement(data=param)
        print(response.json())


if __name__ == '__main__':
    unittest.main()



