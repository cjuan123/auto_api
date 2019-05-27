# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_cater_flow.py
@time: 2019/5/27 16:13
@desc：大配餐流程 政府端、企业端、app
"""
import unittest, datetime
from source.CaterSet.cater import government_Cater
from source.CaterSet.cater_sas import CaterSAS
from conf.IDCard import IDCard
from conf import Login



class TestCaterFlow(unittest.TestCase):
    g_cater = government_Cater()
    s_cater = CaterSAS()
    id_card = IDCard().idCard(65, 1)
    applyId = []

    # @Login.get_account("13999999992", "123qwe")
    # def test_001(self):
    #     """添加人员"""
    #     param = {
    #         "idcard": self.id_card
    #     }
    #     # response = self.g_cater.get_user_by_idCard(param)
    #     # print(response.json())
    #     # self.assertEqual("操作成功", response.json()["message"])
    #     #
    #     # param = {
    #     #     "address": "测试现住地址",
    #     #     "applicationCategory": 141,
    #     #     "auditState": 1,
    #     #     "birthday": self.id_card[6:14],
    #     #     "eatCount": 0,
    #     #     "handleWay": "",
    #     #     "homeDelivery": 0,
    #     #     "homeDeliveryDetail": "",
    #     #     "idCard": self.id_card,
    #     #     "isArea": 1,
    #     #     "mealId": 135,
    #     #     "name": "api" + datetime.date.today().strftime("%y%m%d"),
    #     #     "otherCredentials": [],
    #     #     "permanentAddress": "测试户籍地址",
    #     #     "phone": "15282566260",
    #     #     "residenceAddress": "90010902",
    #     #     "sex": "m",
    #     #     "useYanglao": 1,
    #     #     "userGoverBalance": {}
    #     # }
    #     # response = self.g_cater.add_user(param=param)
    #     # print(response.json())

    # def test_002(self):
    #     """根据身份证获取applyid"""
    #     param = {
    #         "parameter": "711557195405275675",
    #         "status": 1
    #     }
    #     response = self.g_cater.get_apply_id(param)
    #     self.applyId.append(response.json()["data"]["records"][0]["applyId"])
    #     print(response.json())
    #
    # def test_003(self):
    #     """人员审核"""
    #     param_1 = {
    #         "passed":  1,
    #         "advice": "",
    #         "checkType": 1,
    #         "applyId": self.applyId[0]
    #     }
    #     response_1 = self.g_cater.review_user(param=param_1)
    #     print(response_1.json())
    #     self.assertEqual("操作成功", response_1.json()["message"])
    #
    #     """人员复审"""
    #     param_2 = {
    #         "passed": 1,
    #         "advice": "",
    #         "checkType": 2,
    #         "applyId": self.applyId[0]
    #     }
    #     response_2 = self.g_cater.review_user(param=param_2)
    #     print(response_2.json())
    #     self.assertEqual("操作成功", response_2.json()["message"])

    @Login.get_pc_account("13999999993", "Qsheal502")
    def test_004(self):
        param = {
            "userId": "1357",
            "money": 10
        }
        response = self.s_cater.set_recharge(param=param)
        # print(response.text)


if __name__ == "__main__":
    unittest.main()
