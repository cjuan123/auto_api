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
from source.Agencies import agencies_api as a_api


class YangLao:

    request = Request()
    headers = DEFAULT.HEADERS

    def login_out(self):
        """退出登录"""
        res = self.request.get_request(url=yl.loginOut, header=self.headers)
        return res

    def add_survey_user(self, param):
        """【政府端养老】：添加人员"""
        response = self.request.post_request_data(_url=yl.addSurveyUser, _data=param, _headers=self.headers)
        return response

    def recharge(self, file):
        """【政府端养老】：批量充值"""
        response = self.request.post_request_files(_url=yl.recharge, _headers=self.headers, _files=file)
        return response

    def list_users_new(self, param):
        """【政府端养老】：根据身份证号，查询获取uid"""
        print(self.headers)
        response = self.request.post_request_data(_url=yl.listUsersNew, _data=param, _headers=self.headers)
        return response

    def single_recharge(self, param):
        """【政府端养老】：单个充值积分"""
        response = self.request.post_request_data(_url=yl.SingleRecharge, _data=param, _headers=self.headers)
        return response

    def query_user(self, param):
        """【政府端--评估】：查询身份证是否存在评估申请"""
        response = self.request.get_request(_url=a_api.queryUser, _data=param, _headers=self.headers)
        return response

    def apply_add(self, param):
        """【政府端--评估】：政府端添加评估申请"""
        response = self.request.post_request_data(_url=a_api.applyAdd, _data=param, _headers=self.headers)
        return response

    def apply_list(self, param):
        """【政府端--评估】：查询评估申请的ID"""
        response = self.request.post_request_data(_url=a_api.applyList, _data=param, _headers=self.headers)
        return response

    def cancel_record_by_id(self, param):
        """【政府端--评估】：取消评估申请"""
        response = self.request.post_request_data(_url=a_api.cancelRecordById, _data=param, _headers=self.headers)
        return response

    def audit_list(self, param):
        """【政府端--评估】：待审核页面"""
        response = self.request.post_request_data(_url=a_api.auditList, _data=param, _headers=self.headers)
        return response

    def update(self, param):
        """【政府端--评估】：审核"""
        response = self.request.post_request_data(_url=a_api.update, _data=param, _headers=self.headers)
        return response

    def add_sunlight(self, param):
        """【政府端--日照评估】：添加日照中心"""
        response = self.request.post_request_data(_url=a_api.addSunlight, _data=param, _headers=self.headers)
        return response

    def sunlight_manage(self, param):
        """【政府端--日照评估】：根据日照名称查询"""
        response = self.request.post_request_data(_url=a_api.sunlightManage, _data=param, _headers=self.headers)
        return response

    def sunlight_apply_add(self, param):
        """【政府端--日照评估】：添加日照评估申请"""
        response = self.request.post_request_data(_url=a_api.sunlightApplyAdd, _data=param, _headers=self.headers)
        return response

    def sunlight_apply_list(self, param):
        """【政府端--日照评估】：查询日照评估ID"""
        response = self.request.post_request_data(_url=a_api.sunlightApplyList, _data=param, _headers=self.headers)
        return response


