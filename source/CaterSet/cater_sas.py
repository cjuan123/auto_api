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
from conf import HEADERS


class CaterSAS:
    request = Request()
    header = HEADERS.headers

    def member_list(self, case_name, param):
        """企业端：根据身份证查询"""
        response = self.request.post_request_data(case_name=case_name, _url=cater.memberList, _data=param, _headers=self.header)
        return response

    def set_recharge(self, case_name, param):
        """企业端：给人员充值"""
        response = self.request.post_request_data(case_name=case_name, _url=cater.setRecharge, _data=param, _headers=self.header)
        return response

    def add_appointment(self, case_name, param):
        """企业端：新增预约"""
        response = self.request.post_request_data(case_name=case_name, _url=cater.addAppointment, _data=param, _headers=self.header)
        return response

    def app_complete_eat(self, case_name, param):
        """APP：就餐扫码"""
        response = self.request.post_request_data(case_name=case_name, _url=cater.completeEat, _data=param, _headers=self.header)
        return response

