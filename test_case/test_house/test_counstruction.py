# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_counstruction.py
@time: 2019/6/13 11:16
@desc：施工
"""
import sys, os
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]))
import unittest
import random
from conf import Login
from conf.IDCard import IDCard
from tools.read_yaml import ReadYaml
from source.construction import Construction
from source.govern_house import GovernHouse


class Agencies(unittest.TestCase):

    construction = Construction()
    house = GovernHouse()

    govern_account = str(ReadYaml("default.yaml").get_account("govern"))
    pass_word = ReadYaml("default.yaml").get_password("govern")

    id_card = IDCard().idCard(75, 2)
    con_emp_id = []
    con_emp_account = "1525621" + str(random.randint(1000, 9999))
    con_emp_name = "api施员工" + str(random.randint(1000, 9999))
    scheme = []

    @Login.construction_login("13633262703", "123456")
    def test_add_employee(self):
        """【施工web：添加员工】"""
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
        response = self.construction.add_employee(case_name="添加员工", param=param)
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

        response = self.construction.employee_list(case_name="查询员工列表", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        print(len(response.json()["data"]["records"]))
        self.con_emp_id.append(response.json()["data"]["records"][0]["id"])
        print(self.con_emp_id[0])

    @Login.construction_app_login("13633269651", "123456")
    def test_get_task(self):
        """施工app：获取任务"""
        param = {
            # self.con_emp_id[0],
            "recordId": 63
        }
        response = self.construction.get_task(case_name="获取任务", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取成功", response.json()["message"])

    def test_my_task_list(self):
        """【施工app：我的任务列表】"""
        param = {
            "pageNow": 1
        }
        response = self.construction.my_task_list(case_name="我的任务列表", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_construction_details(self):
        """【施工app：查询任务详情】"""
        param = {
            "id": 91
        }
        response = self.construction.construction_details(case_name="查询任务详情", param=param)
        print(response.json())
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["id"])
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["productImg"])

    def test_commit_scheme(self):
        """【施工app：提交施工产品方案】"""
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
        response = self.construction.commit_scheme(case_name="提交施工产品方案", data=param)
        print(response.json())

    @Login.govern_login(govern_account, pass_word)
    def test_03_govern_get_project_inspection_list(self):
        """【政府端--适老化】：项目验收列表分页查询"""
        param = {
            "pageNow": 1
        }
        response = self.house.get_project_inspection_list(case_name="项目验收列表分页查询", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_04_govern_check_transform_scheme(self):
        """【政府端--适老化】：验收改造方案"""
        param = {
            "schemeId": 83,
            "recordId": 91,
            "qualified": 1
        }
        response = self.house.check_transform_scheme(case_name="验收改造方案", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("验收成功", response.json()["message"])

    def test_05_get_transform_settlement_list(self):
        """项目结算"""
        param = {
            "pageNow": 1
        }
        response = self.house.get_transform_settlement_list(case_name="项目结算", data=param)
        print(response.json())

    def test_06_settlement(self):
        """【政府端--适老化】:结算项目"""
        param = {
            "id": 91
        }
        response = self.house.settlement(case_name="适老化：结算项目", data=param)
        print(response.json())


if __name__ == '__main__':
    unittest.main()



