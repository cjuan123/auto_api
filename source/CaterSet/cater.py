"""
@version: 1.0
@author: chenj
@file: cater.py
@time: 2019/5/19 11:57
"""
from tools.http_request import Request
from conf import DEFAULT
from source.CaterSet import cater_api as cater

class government_Cater(object):

    request = Request()
    headers = DEFAULT.HEADERS

    def user_list(self):
        response = self.request.get_request(_url=cater.userlist, _headers=self.headers)
        return response

    def get_user_by_idCard(self, param):
        """根据身份证号码是否存在"""
        response = self.request.get_request(_url=cater.getUserByIdCard, _data=param, _headers=self.headers)
        return response

    def add_user(self, param):
        """添加人员申请"""
        response = self.request.post_request(_url=cater.adduser, _data=param, _headers=self.headers)
        return response

