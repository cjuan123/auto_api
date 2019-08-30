# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_business_1_flow.py
@time: 2019/5/29 11:46
@desc：企业订单--普通人员
        人员级别为：1
"""
import unittest
from conf import Login
from tools.logger import Logger
from conf.IDCard import IDCard
from tools.read_yaml import ReadYaml
from source.YangLao.yanglao import YangLao
from source.Business.business import Business


class TestBusiness1(unittest.TestCase):
    read_yaml = ReadYaml("default.yaml")
    pass_word = read_yaml.get_password("govern")

    yang_lao = YangLao()
    business = Business()
    id_card = IDCard().idCard(62, 1)
    uid = []

    @classmethod
    def setUpClass(cls):
        cls.log = Logger()
        Logger().info("------------------------ 普通人员 STA------------------------")
        print("------------------------ 普通人员 STA------------------------")

    @Login.govern_login(read_yaml.get_business_account("shequ"), pass_word)
    def test_001(self):
        """添加人员-级别为：普通老人"""
        print(self.id_card)
        param = {
            "idcard": self.id_card,
            "username": "api" + self.id_card + "_1",
            "nationality": "汉族",
            "maritalstatus": 0,
            "level": 1,
            "contact1": "15212365478",
            "residenceaddress": "9001090201",
            "address": "测试详细地址",
            "emergencycontact1name": "测试",
            "emergencycontact1address": "测试地址",
            "emergencycontact1relationship": 0,
            "emergencycontact1phone": "152133655",
            "epJsonString": "[{'epName':'养老','ephone':'028-1236548','epSex':'','epOtherPhone':'','epIdcard':'',"
                            "'epRelation':'','epAddress':'','epUnits':'','epWorkAddress':''}]",
            'headImage': 'http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png'
        }
        res = self.yang_lao.add_survey_user(case_name="添加普通老人", param=param)
        self.log.info("返回结果：%s" % res.json())
        print("【添加人员-级别为：普通老人】：%s" % res.json())

    @Login.govern_login(read_yaml.get_business_account("jiedao"), pass_word)
    def test_002(self):
        """政府端：根据身份证号查询UID"""
        param = {
            "idCard": self.id_card,
            "pageIndex": 1,
            "isBind": ""
        }
        res = self.yang_lao.list_users_new(case_name="根据身份证号查询UID", param=param)
        u_id = res.json()["pageView"]["records"][0]["id"]
        self.uid.append(u_id)
        self.log.info("返回结果：%s" % res.json())
        print("【根据身份证获取uid】 ：%s" % res.json())
        self.assertEqual("", res.json()["detail"])

    def test_003(self):
        """积分充值"""
        param = {
            "uid": self.uid[0],
            "balance": 100,
            "remark": 0,
            "balanceType": 19287,
            "source": "api"
        }
        res = self.yang_lao.single_recharge(case_name="积分充值", param=param)
        print("【积分充值】：%s" % res.json())
        self.log.info("返回结果：%s" % res.json())
        self.assertEqual("充值成功", res.json()["detail"])

    @Login.business_login(read_yaml.get_business_account("admin"), pass_word)
    def test_004(self):
        """服务订单生成"""
        param = {
            "classification": 1,
            "groupId": 2,
            "idcard": self.id_card
        }
        res = self.business.query_pai_user_info(case_name="服务订单生成", param=param)
        print("【普通人员：服务订单生成】：%s" % res.json())
        print(res.json()["detail"])
        self.log.info("返回结果：%s" % res.json())
        self.assertEqual("该用户不属于服务对象", res.json()["detail"])

    @classmethod
    def tearDownClass(cls):
        Logger().info("------------------------ 普通人员 END------------------------")
        print("------------------------ 普通人员 END------------------------")


if __name__ == "__main__":
    unittest.main()