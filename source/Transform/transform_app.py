# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: transform_app.py
@time: 2019/6/5 17:52
@desc：适老化app接口
"""
from conf import DEFAULT
from tools.http_request import Request
from source.Transform import transform_app_api as app_api


class TransformApp:

    headers = DEFAULT.HEADERS
    request = Request()

    def agency_user_edit_submit(self, data):
        """评估机构：添加员工"""
        response = self.request.post_request_data(_url=app_api.agencyUserEditSubmit, _data=data, _headers=self.headers)
        return response

    def agency_user_list_data(self, data):
        """评估机构：查询员工ID"""
        response = self.request.post_request_data(_url=app_api.agencyUserListData, _data=data, _headers=self.headers)
        return response

    def get_tasks(self, data):
        """【适老化--app】：领取任务"""
        response = self.request.post_request_data(_url=app_api.getTasks, _data=data, _headers=self.headers)
        return response

    def list_own_tasks(self, data):
        """【适老化--app】：我的任务列表"""
        response = self.request.post_request_data(_url=app_api.listOwnTasks, _data=data, _headers=self.headers)
        return response

    def save_answer(self, data):
        """"【适老化--app】：上传人员评估结果"""
        response = self.request.post_request_data(_url=app_api.saveAnswer, _data=data, _headers=self.headers)
        return response

    def save_env_answer(self, data):
        """"【适老化--app】：上传环境评估结果"""
        response = self.request.post_request_data(_url=app_api.saveEnvAnswer, _data=data, _headers=self.headers)
        return response

    def save_person_products(self, data):
        """【适老化--app】：保存人员评估结果选择的产品关系"""
        response = self.request.post_request_data(_url=app_api.savePersonProducts, _data=data, _headers=self.headers)
        return response

    def download_subject(self, data):
        response = self.request.post_request_data(_url=app_api.downloadSubject, _data=data, _headers=self.headers)
        return response

