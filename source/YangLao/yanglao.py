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

    def login_out(self):
        """退出登录"""
        res = self.request.get_request(url=yl.loginOut, header=self.headers)
        return res

    def add_survey_user(self, param):
        """政府端养老：添加人员"""
        response = self.request.post_request_data(_url=yl.addSurveyUser, _data=param, _headers=self.headers)
        return response

    def recharge(self, file):
        """政府端养老：批量充值"""
        response = self.request.post_request_files(_url=yl.recharge, _headers=self.headers, _files=file)
        return response

    def list_users_new(self, param):
        """政府端养老：根据身份证号，查询获取uid"""
        print(self.headers)
        response = self.request.post_request_data(_url=yl.listUsersNew, _data=param, _headers=self.headers)
        return response

    def single_recharge(self, param):
        """政府端养老：单个充值积分"""
        response = self.request.post_request_data(_url=yl.SingleRecharge, _data=param, _headers=self.headers)
        return response

