# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_business_5_flow.py
@time: 2019/5/30 12:48
@desc：企业订单--
        人员级别为：5
"""
import unittest
import datetime
from conf import Login, IDCard
from source.Business.business import Business
from source.YangLao.yanglao import YangLao
from tools.read_yaml import ReadYaml


class TestBusiness2(unittest.TestCase):
    business = Business()
    yang_lao = YangLao()
    id_card = IDCard.IDCard().idCard(66, 2)
    uid = []
    order_id = []
    read_yaml = ReadYaml("default.yaml")
    pwd = read_yaml.get_password("govern")

    @Login.govern_login("13551042646", pwd)
    def test_001(self):
        """添加人员-级别为：居家养老服务补贴"""
        print("添加人员身份证号：%s" % self.id_card)
        param = {
            "idcard": self.id_card,
            "username": "api" + self.id_card + "_5",
            "nationality": "汉族",
            "maritalstatus": 0,
            "level": 5,
            "contact1": "15212365478",
            "residenceaddress": "5101090201",
            "address": "测试详细地址",
            "emergencycontact1name": "测试",
            "emergencycontact1address": "测试地址",
            "emergencycontact1relationship": 0,
            "emergencycontact1phone": "152133655",
            "epJsonString": "[{'epName':'养老','ephone':'028-1236548','epSex':'','epOtherPhone':'','epIdcard':'',"
                            "'epRelation':'','epAddress':'','epUnits':'','epWorkAddress':''}]",
            'headImage': 'http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png'
        }
        res = self.yang_lao.add_survey_user(param=param)
        print("【添加人员-级别为：居家养老服务补贴】：%s" % res.json())

    @Login.govern_login("18048054262", pwd)
    def test_002(self):
        """政府端：根据身份证号查询UID"""
        param = {
            "idCard": self.id_card,
            "pageIndex": 1,
            "isBind": ""
        }
        res = self.yang_lao.list_users_new(param=param)
        u_id = res.json()["pageView"]["records"][0]["id"]
        self.uid.append(u_id)
        print("【根据身份证获取uid】 ：%s" % res.json())
        self.assertEqual("", res.json()["detail"])

    def test_003(self):
        """积分充值"""
        param = {
            "uid": self.uid[0],
            "balance": 100,
            "remark": 0,
            "source": "api"
        }
        res = self.yang_lao.single_recharge(param=param)
        # print("【积分充值】：%s" % res.json())
        # assert "充值成功" == res.json()["detail"]

    @Login.business_login("849001", pwd)
    def test_004(self):
        """服务订单生成--查询信息"""
        param = {
            "classification": 1,
            "groupId": 2,
            "idcard": self.id_card
        }
        res = self.business.query_pai_user_info(param=param)
        print("【普通人员：服务订单生成】：%s" % res.json())

    def test_005(self):
        """创建服务订单"""
        endDate = str(datetime.datetime.now().strftime('%Y-%m-%d')) + " 23:59:59"
        param = {
            "classification": 1,
            "groupId": 2,
            "idcard": self.id_card,
            "uid": self.uid[0],
            "mark": "api",
            "itemsId": "310",
            "number": 1,
            "endDate": str(endDate)
        }
        res = self.business.create_orders(param=param)
        print("【创建服务订单】: %s" % res.json())

    def test_006(self):
        """获取订单ID"""
        param = {
            "idCard": self.id_card
        }
        res = self.business.query_pai_order_send(param=param)
        print("【获取订单ID】：%s" % res.json())
        self.order_id.append(res.json()['pageView']['records'][0]['orderId'])
        self.assertEqual("获取成功", res.json()["detail"])

    def test_007(self):
        """订单派工"""
        param = {
            "buid": "1182",
            "orderId": self.order_id[0]
        }
        res = self.business.save_service_record(param=param)
        print("【订单派工】: %s" % res.json())

    @Login.business_app_login("626753", pwd)
    def test_008(self):
        """派工助手--开始服务"""
        param = {
            'orderId': self.order_id[0],
            'startPosition': '104.081859,30.546299'
        }
        res = self.business.start_service(param=param)
        print("【派工助手--开始服务】: %s" % res.json())

    def test_009(self):
        """派工助手--完成服务"""
        param = {
            'type': '2',
            'endPosition': '104.081849,30.54631',
            'orderId': self.order_id[0],
            'images': 'https://file.chinaylzl.com/test/serviceImages/2018/11/15/4a6f2a0ffff54ca88aed5132f482a4aa.jpg,'
        }
        res = self.business.complete_service(param=param)
        print("【派工助手--完成服务】: %s" % res.json())

    def test_010(self):
        """派工助手--评价订单"""
        param = {
            'orderId': self.order_id[0],
            'degree': '100'
        }
        res = self.business.update_service_degree(param=param)
        print("【派工助手--评价订单】: %s" % res.json())


if __name__ == "__main__":
    unittest.main()