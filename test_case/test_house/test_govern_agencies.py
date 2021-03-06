# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_agencies.py
@time: 2019/6/12 22:22
@desc：适老化：评估机构
"""
import sys, os
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]))
import unittest
import random
from conf import Login
from tools.read_yaml import ReadYaml
from source.govern_house import GovernHouse


class TestGovernAgencies(unittest.TestCase):
    house = GovernHouse()
    govern_account = str(ReadYaml("default.yaml").get_account("govern"))
    pass_word = ReadYaml("default.yaml").get_password("govern")

    agencyId = []
    agencyName = "api评估机构" + str(random.randint(10, 99))

    @Login.govern_login(govern_account, pass_word)
    def test_001_add_assess_agency(self):
        """【政府端-适老化-评估机构】：添加评估机构"""
        param = {
            "licencesNum": str(random.randint(100000, 99999999)),
            "password": "123456",
            "loginPhone": "152852566" + str(random.randint(10, 99)),
            "legal": "测试",
            "contactName": "测试",
            "serviceArea": "51010906",
            "agencyName": self.agencyName,
            "contactMobile": "15285256626",
            "address": "测试",
            "email": "15285256626@123.com",
            "addExist": "",
            "licencesImg": "",
            "agencyCertificate": "",
            "agencyPhoto": "",
            "idcardImgZ": "",
            "idcardImgF": ""
        }
        response = self.house.add_assess_agency(case_name="适老化：添加评估机构", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("评估添加成功", response.json()["message"])

    def test_002_get_assessment_agencies(self):
        """【政府端--评估机构】：分页查询评估机构列表"""
        param = {
            "agencyName": self.agencyName,
            "pageNow": 1
        }
        response = self.house.get_assessment_agencies(case_name="分页查询评估机构列表", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.agencyId.append(response.json()["data"]["records"][0]["agencyId"])
        print(self.agencyId[0])

    def test_003_save_assessment_agency(self):
        """【政府端--评估机构】：编辑获取评估机构信息"""
        param = {
            "agencyId": self.agencyId[0],
            "password": "123456",
            "legal": "测试(update)",
            "contactName": "测试(update)",
            "serviceArea": "51010906",
            "agencyName": self.agencyName + "(update)",
            "contactMobile": "15285256626",
            "address": "测试(update)",
            "email": "15285256626@123.com",
            "addExist": 0,
            "licencesImg": "https://file.chinaylzl.com/test/house/gover/img/2019/06/05/"
                           "timg_884ce9dd38e848129cf7c86e914f4bdd.gif",
            "agencyCertificate": "https://file.chinaylzl.com/test/house/gover/img/2019/06/05/"
                                 "timg_884ce9dd38e848129cf7c86e914f4bdd.gif",
            "agencyPhoto": "https://file.chinaylzl.com/test/house/gover/img/2019/06/05/"
                           "timg_884ce9dd38e848129cf7c86e914f4bdd.gif",
            "idcardImgZ": "https://file.chinaylzl.com/test/house/gover/img/2019/06/05/"
                          "timg_884ce9dd38e848129cf7c86e914f4bdd.gif",
            "idcardImgF": "https://file.chinaylzl.com/test/house/gover/img/2019/06/05/"
                          "timg_884ce9dd38e848129cf7c86e914f4bdd.gif"
        }
        print(param)
        response = self.house.save_assessment_agency(case_name="编辑获取评估机构信息", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("评估保存成功", response.json()["message"])

    def test_query_agencies_list(self):
        """【政府端--评估机构】：获取选择评估机构列表"""
        response = self.house.query_agencies_list(case_name="获取选择评估机构列表")
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])


if __name__ == '__main__':
    unittest.main()