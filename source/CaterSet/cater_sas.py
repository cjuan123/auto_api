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

    def member_list(self, param):
        """企业端：根据身份证查询"""
        response = self.request.post_request_data(_url=cater.memberList, _data=param, _headers=self.header)
        return response

    def set_recharge(self, param):
        """企业端：给人员充值"""
        response = self.request.post_request_data(_url=cater.setRecharge, _data=param, _headers=self.header)
        return response

    def add_appointment(self, param):
        """企业端：新增预约"""
        response = self.request.post_request_data(_url=cater.addAppointment, _data=param, _headers=self.header)
        return response

    def app_complete_eat(self, param):
        """APP：就餐扫码"""
        response = self.request.post_request_data(_url=cater.completeEat, _data=param, _headers=self.header)
        return response

