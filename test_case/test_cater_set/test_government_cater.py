"""
@version: 1.0
@author: chenj
@file: test_government_cater.py
@time: 2019/5/19 12:05
"""
from source.CaterSet.cater import government_Cater
import unittest
from conf import Login


class test_government_cater(unittest.TestCase):
    cater = government_Cater()

    def __init__(self, method_name, param, excepted):
        super(test_government_cater, self).__init__(method_name)
        self.param = param
        self.excepted = excepted

    def Ttest_user_list(self):
        response = self.cater.user_list()
        print(response.json())

    def Ttest_get_by_idCard(self):
        param = {
            "idcard": "510104194107186490"
        }
        response = self.cater.get_user_by_idCard(param=param)
        print(response.json())

    def test_add_user(self):
        param = {
            "address": "测试现住地址",
            "applicationCategory": 141,
            "auditState": 1,
            "birthday": "19410718",
            "eatCount": 0,
            "handleWay": "",
            "homeDelivery": 0,
            "homeDeliveryDetail": "",
            "idCard": "510104194107184014",
            "isArea": 1,
            "mealId": 135,
            "name": "测试api01",
            "otherCredentials": [],
            "permanentAddress": "测试户籍地址",
            "phone": "15282566260",
            "residenceAddress": "90010902",
            "sex": "m",
            "useYanglao": 1,
            "userGoverBalance": {}
        }
        response = self.cater.add_user(param=self.param)
        print(response.text)
        self.assertEqual(self.excepted, str(response.json()["message"]).split(":")[0])
        # self.assertEqual("操作异常:用户重复", response.json()["message"])


if __name__ == "__main__":
    unittest.main()
