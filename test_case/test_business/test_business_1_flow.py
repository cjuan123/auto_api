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
from conf import DEFAULT
from source.YangLao.yanglao import YangLao
from source.Business.business import Business


class TestBusiness1(unittest.TestCase):
    yang_lao = YangLao()
    business = Business()

    @Login.get_account("13551042646", DEFAULT.PASSWORD_GOVERNMENT)
    def test_001(self):
        """添加人员-级别为：普通老人"""
        print(self.idCard)
        level = 1
        res = self.yang_lao.add_survey_user(idcard=self.idCard, level=level, header=self.header)
        print("【添加人员-级别为：普通老人】：%s" % res.json())

    @Login.get_account("18048054262", DEFAULT.PASSWORD_GOVERNMENT)
    def test_002(self):
        """街道登录，充值积分"""
        param = "name=&idCard=" + self.idCard + "&sex=&startAge=&endAge=&address=&sort=&orderby=&pageIndex=1&point=&residenceAddress=51010902&type=0&shinengStr=&cjstate=&cjdj=&level=&personCategory=&liveStatus=&liveType=&startTime=&endTime=&isBind=&isPaging=false"
        res = self.yang_lao.get_uid(param=param, header=self.header)
        u_id = res.json()["pageView"]["records"][0]["id"]
        self.uid.append(u_id)
        print("【根据身份证获取uid】 ：%s" % res.json())
        assert "" == res.json()["detail"]

    def test_003(self):
        """积分充值"""
        param = {
            "uid": self.uid[0],
            "balance": 100,
            "remark": 0,
            "source": "api"
        }
        res = self.yang_lao.to_recharge(param=param, header=self.header)
        print("【积分充值】：%s" % res.json())
        assert "充值成功" == res.json()["detail"]
        self.yang_lao.login_out(self.header)

    @Login.get_business_account("849001", DEFAULT.PASSWORD_GOVERNMENT)
    def test_004(self):
        """服务订单生成"""
        res = self.business.query_pai_user_info(idCard=self.idCard, header=self.header)
        print("【普通人员：服务订单生成】：%s" % res.json())
        assert "该用户不属于服务对象" == res.json()["detail"]
