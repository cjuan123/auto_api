# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: agencies.py
@time: 2019/6/13 10:56
@desc：评估端相关接口方法
"""
from conf import HEADERS
from tools.read_yaml import ReadYaml
from tools.http_request import Request


class Agencies:
    headers = HEADERS.headers
    host_8093 = ReadYaml("default.yaml").get_host("host_8093")
    read_agencies = ReadYaml("agencies_api.yaml")
    request = Request()

    def agency_user_edit_submit(self, data):
        """评估机构：添加员工"""
        _URL = self.host_8093 + self.read_agencies.agencies("web", "agencyUserEditSubmit")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def agency_user_list_data(self, data):
        """评估机构：查询员工ID"""
        _URL = self.host_8093 + self.read_agencies.agencies("web", "agencyUserListData")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_tasks(self, data):
        """【适老化--app】：领取任务"""
        _URL = self.host_8093 + self.read_agencies.agencies("app", "getTasks")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def list_own_tasks(self, data):
        """【适老化--app】：我的任务列表"""
        _URL = self.host_8093 + self.read_agencies.agencies("app", "listOwnTasks")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def save_answer(self, data):
        """"【适老化--app】：上传人员评估结果"""
        _URL = self.host_8093 + self.read_agencies.agencies("app", "saveAnswer")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def save_env_answer(self, data):
        """"【适老化--app】：上传环境评估结果"""
        _URL = self.host_8093 + self.read_agencies.agencies("app", "saveEnvAnswer")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def save_person_products(self, data):
        """【适老化--app】：保存人员评估结果选择的产品关系"""
        _URL = self.host_8093 + self.read_agencies.agencies("app", "savePersonProducts")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response

    def download_subject(self, data):
        _URL = self.host_8093 + self.read_agencies.agencies("app", "downloadSubject")
        response = self.request.post_request_data(_url=_URL, _data=data, _headers=self.headers)
        return response
