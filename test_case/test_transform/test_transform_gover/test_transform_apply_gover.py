# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_transform_product_gover.py
@time: 2019/6/3 17:42
@desc：适老化政府端:添加评估申请
"""
import unittest
import random
from conf import Login
from conf.IDCard import IDCard
from source.Transform.transform import Transform


class TestTransformGovern(unittest.TestCase):

    transform = Transform()
    id_card = IDCard().idCard(85, 1)
    name = "api申请" + str(random.randint(0, 100))
    apply_id = []
    v_id = []     # 改造单ID

    @Login.get_account("18981967059", "123qwe")
    def test_001_get_user_by_id_card(self):
        """【政府端 - -适老化】：根据身份证查询人员信息"""
        param = {
            "idCard": self.id_card
        }
        response = self.transform.get_user_by_id_card(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_002_add_apply(self):
        """【政府端--适老化】：添加改造申请"""
        print("申请人name:" + self.name)
        param = {
            "idCard": self.id_card,
            "userName": self.name,
            "phone": "13999999999",
            "addressId": "51010915",
            "addressDetail": "测试地址",
            "transformContents": "测试内容",
            "transformCause": "测试",
            "state": 4,
            "emergencyContact": [{
                "name": "测试",
                "ralative": 1,
                "phone": "13777777777"
            }],
            "certificates": [],
            "annex": []
            }
        response = self.transform.add_transform_apply(param)
        print(response.json())

    def test_003_get_transform_apply_list(self):
        param = {
            "idCard": self.id_card,
            "addressId": "510109",
            "pageNow": 1
        }
        response = self.transform.get_transform_apply_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.apply_id.append(response.json()["data"]["records"][0]["id"])

    def test_004_edit_transform(self):
        param = {
            "id": self.apply_id[0],
            "idCard": self.id_card,
            "userName": self.name + "(edit)",
            "phone": "13999999999",
            "addressDetail": "测试地址(edit)",
            "transformContents": "测试内容(edit)",
            "transformCause": "测试(edit)",
            "emergencyContact": [{
                "ralative": 1,
                "phone": "13777777787",
                "name": "测试(edit)"
            }],
            "certificates": [{
                "name": "timg.gif",
                "url": "blob:https://test.chinaylzl.com/df5e890d-d6e3-454a-8d28-1786b9230e31"
            }],
            "state": 1,
            "version": 1
            }
        response = self.transform.edit_transform(json=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("编辑成功", response.json()["message"])

    def test_005_get_transform_verify_list(self):
        """【政府端--适老化】：分页查询改造审核列表"""
        param = {
            "idCard": self.id_card,
            "addressId": "510109"
        }
        response = self.transform.get_transform_apply_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.v_id.append(response.json()["data"]["records"][0]["id"])
        print(self.v_id)

    def test_006_verify_transform(self):
        """【政府端--适老化】：审核改造单"""
        param = {
            "id": self.v_id[0],
            "verifyState": 1
        }
        response = self.transform.verify_transform(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("审核成功", response.json()["message"])

    def test_007_business_apply(self):
        """【政府端--适老化】：评估中列表分页查询"""
        param = {
            "agencyId": 125,
            "agencyName": "api评估机构6872",
            "id": self.v_id[0]
        }
        response = self.transform.business_apply(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("申请成功", response.json()["message"])

    def test_008_get_assessment_list(self):
        """【政府端--适老化】：评估中列表分页查询"""
        param = {
            "idCard": self.id_card,
            "addressId": "510109",
            "pageNow": 1
        }
        response = self.transform.get_assessment_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.assertEqual(125, response.json()["data"]["records"][0]["agencyId"])
        self.assertEqual("api评估机构53", response.json()["data"]["records"][0]["agencyName"])


if __name__ == '__main__':
    unittest.main()