# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_assessment_gover.py
@time: 2019/6/5 11:40
@desc：
"""
import unittest
import random
from conf import Login
from source.Transform.transform import Transform


class TestAssessmentGovern(unittest.TestCase):

    transform = Transform()
    agencyId = []
    agencyName = "api评估机构" + str(random.randint(10, 99))

    @Login.get_account("18981967059", "123qwe")
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
        response = self.transform.add_assess_agency(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    @Login.get_account("18981967059", "123qwe")
    def test_002_get_assessment_agencies(self):
        """【政府端--评估机构】：分页查询评估机构列表"""
        param = {
            "agencyName": self.agencyName,
            "pageNow": 1
        }
        response = self.transform.get_assessment_agencies(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.agencyId.append(response.json()["data"]["records"][0]["agencyId"])
        print(self.agencyId[0])

    @Login.get_account("18981967059", "123qwe")
    def test_003_save_assessment_agency(self):
        """【政府端--评估机构】：编辑获取评估机构信息"""
        param = {
            "id": self.agencyId[0],
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
        response = self.transform.save_assessment_agency(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("", response.json()["message"])

    @Login.get_account("18981967059", "123qwe")
    def test_query_agencies_list(self):
        """【政府端--评估机构】：获取选择评估机构列表"""
        response = self.transform.query_agencies_list()
        print(response.json())










