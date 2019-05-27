# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: cater_sas.py
@time: 2019/5/27 16:55
@desc：大配餐企业端
"""
from source.CaterSet import cater_api as cater
from tools.http_request import Request
from conf import DEFAULT


class CaterSAS:
    request = Request()
    header = DEFAULT.HEADERS

    def set_recharge(self, param):
        """企业端：给人员充值"""
        response = self.request.post_request_data(_url=cater.setRecharge, _data=param, _headers=self.header)
        print(self.header)
        return response
