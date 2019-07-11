"""
@version: 1.0
@author: chenj
@file: cater.py
@time: 2019/5/19 11:57
"""
from tools.http_request import Request
from conf import HEADERS
from source.CaterSet import cater_api as cater


class GovernCater(object):

    request = Request()
    headers = HEADERS.headers

    def user_list(self, case_name, param):
        """人员列表"""
        response = self.request.get_request(case_name=case_name, _url=cater.userlist, _data=param, _headers=self.headers)
        return response

    def user_detail(self, case_name, param):
        """人员详情"""
        response = self.request.get_request(case_name=case_name, _url=cater.userDetail, _data=param, _headers=self.headers)
        return response

    def get_user_by_id_card(self, case_name, param):
        """根据身份证号码是否存在"""
        response = self.request.get_request(case_name=case_name, _url=cater.getUserByIdCard, _data=param, _headers=self.headers)
        return response

    def add_user(self, case_name, param):
        """添加人员申请"""
        response = self.request.post_request_json(case_name=case_name, _url=cater.adduser, _json=param, _headers=self.headers)
        return response

    def get_apply_id(self, case_name, param):
        """根据身份证获取applyID"""
        response = self.request.get_request(case_name=case_name, _url=cater.queryAllApplyUser, _data=param, _headers=self.headers)
        return response

    def review_user(self, case_name, param):
        """人员审核checkType  1.审核    2.复审"""
        response = self.request.post_request_json(case_name=case_name, _url=cater.reviewUser, _json=param, _headers=self.headers)
        return response


