# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_cater_flow.py
@time: 2019/5/27 16:13
@desc：大配餐流程 政府端、企业端、app
        人员无养老积分
"""
import unittest, datetime
from tools.logger import Logger
from source.CaterSet.cater import GovernCater
from source.CaterSet.cater_sas import CaterSAS
from source.CaterSet.cater_helper import CaterHelper
from conf.IDCard import IDCard
from conf import Login


class TestCaterFlow(unittest.TestCase):
    g_cater = GovernCater()
    s_cater = CaterSAS()
    cater_helper = CaterHelper()
    id_card = IDCard().idCard(65, 1)
    PASSWORD_GOVERNMENT = "123qwe"
    PASSWORD_PG = "123456"
    user_info = []
    applyId = []

    @classmethod
    def setUpClass(cls):
        Logger().info("------------------------ 大配餐 STA ------------------------")
        print("------------------------ 大配餐 STA ------------------------")

    @Login.govern_login("13999999992", PASSWORD_GOVERNMENT)
    def test_001(self):
        """添加人员"""
        param = {
            "idcard": self.id_card
        }
        response = self.g_cater.get_user_by_id_card(case_name="添加人员", param=param)
        print(response.json())
        self.assertEqual("操作成功", response.json()["message"])
        print("人员身份证号：%s" % self.id_card)
        param = {
            "address": "测试现住地址",
            "applicationCategory": 141,
            "auditState": 1,
            "birthday": self.id_card[6:14],
            "eatCount": 0,
            "handleWay": "",
            "homeDelivery": 0,
            "homeDeliveryDetail": "",
            "idCard": self.id_card,
            "isArea": 1,
            "mealId": 135,
            "name": "api" + datetime.datetime.now().strftime('%m%d%H'),
            "otherCredentials": [],
            "permanentAddress": "测试户籍地址",
            "phone": "15282566260",
            "residenceAddress": "90010902",
            "sex": "m",
            "useYanglao": 1,
            "userGoverBalance": {}
        }
        print(param)
        response = self.g_cater.add_user(case_name="添加人员", param=param)
        print(response.json())

    def test_002(self):
        """根据身份证获取applyid"""
        param = {
            "parameter": self.id_card,
            "status": 1
        }
        response = self.g_cater.get_apply_id(param)
        self.applyId.append(response.json()["data"]["records"][0]["applyId"])
        print(response.json())

    def test_003(self):
        """人员审核、复审"""
        #   1.人员审核
        param_1 = {
            "passed":  1,
            "advice": "",
            "checkType": 1,
            "applyId": self.applyId[0]
        }
        response_1 = self.g_cater.review_user(param=param_1)
        print(response_1.json())
        self.assertEqual("操作成功", response_1.json()["message"])

        #   2.人员复审
        param_2 = {
            "passed": 1,
            "advice": "",
            "checkType": 2,
            "applyId": self.applyId[0]
        }
        response_2 = self.g_cater.review_user(param=param_2)
        print(response_2.json())
        self.assertEqual("操作成功", response_2.json()["message"])

    @Login.cater_login("13999999993", PASSWORD_PG)
    def test_004(self):
        """企业端：根据身份证查询人员信息"""
        param = {
            "idCard": self.id_card
        }
        response = self.s_cater.member_list(param=param)
        self.user_info.append(response.json()["pageView"]["records"][0]["id"])
        self.user_info.append(response.json()["pageView"]["records"][0]["name"])
        self.user_info.append(response.json()["pageView"]["records"][0]["phone"])
        self.user_info.append(response.json()["pageView"]["records"][0]["idCard"])
        self.user_info.append(response.json()["pageView"]["records"][0]["userCode"])
        self.user_info.append(response.json()["pageView"]["records"][0]["cid"])
        print(response.json())
        self.assertEqual(200, response.status_code)

    def test_005(self):
        """企业端：给人员充值积分"""
        param = {
            "userId": self.user_info[0],
            "money": "100"
        }
        response = self.s_cater.set_recharge(param=param)
        print(response.json())

    def test_006(self):
        """企业端：给人员新增预约"""
        param = {
            "id": self.user_info[0],
            "name": self.user_info[1],
            "phone": self.user_info[2],
            "idCard": self.user_info[3],
            "userCode": self.user_info[4],
            "mealId": self.user_info[5],
            "packageId": "39"
        }
        response = self.s_cater.add_appointment(param=param)
        print(response.json())
        self.assertEqual("预约成功", response.json()["detail"])
        """预约成功：修改预约、就餐时间"""
        self.cater_helper.update_appointment_time(self.user_info[0])
        self.cater_helper.update_server_order_time(self.user_info[0])

    @Login.cater_app_login("13999999993", PASSWORD_PG)
    def test_007(self):
        """APP：就餐扫码"""
        param = {
            "userCode": self.user_info[4],
            "packageId": "39",
            "payType": 1,       # 支付方式: 1 积分 2 现金 3 其他
            "isAppointment": 0,     # 是否预约明日:  1是  0否
            "appointmentPackageId": "",
            "eid": 158
        }
        response = self.s_cater.app_complete_eat(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user_info[1], response.json()["data"]["userName"])

    @classmethod
    def tearDownClass(cls):
        Logger().info("------------------------ 大配餐 END ------------------------")
        print("------------------------ 大配餐 END ------------------------")


if __name__ == "__main__":
    unittest.main()
