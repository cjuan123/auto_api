# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: yanglao.py
@time: 2019/5/29 10:34
@desc：政府端-养老模块
"""
from conf import DEFAULT
from tools.http_request import Request
from source.YangLao import yanglao_api as yl


class YangLao:

    request = Request()
    headers = DEFAULT.HEADERS

    def add_survey_user(self, param):
        """政府端养老：添加人员"""
        response = self.request.post_request_data(_url=yl.addSurveyUser, _data=param, _headers=self.headers)
        return response

    def Recharge(self, file):
        """政府端养老：批量充值"""
        response = self.request.post_request_data(_url=yl.recharge, _headers=self.headers, files=file)
        return response
