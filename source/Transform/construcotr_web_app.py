# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: construcotr_web_app.py
@time: 2019/6/6 14:10
@desc：施工企业app
"""
from conf import DEFAULT
from tools.http_request import Request
from source.Transform import construcotr_web_app_api as c_app_api


class ConstructionApp:

    request = Request()
    headers = DEFAULT.HEADERS

    def add_employee(self, param):
        """【施工web：添加员工】"""
        response = self.request.post_request_json(_url=c_app_api.addEmployee, _json=param, _headers=self.headers)
        return response

    def update_employee(self, param):
        """【施工web：添加员工】"""
        response = self.request.post_request_json(_url=c_app_api.updateEmployee, _json=param, _headers=self.headers)
        return response

    def employee_list(self, param):
        """【施工web：查询列表】"""
        response = self.request.get_request(_url=c_app_api.employeeList, _data=param, _headers=self.headers)
        return response

    def get_task(self, param):
        """【施工app：领取任务】"""
        response = self.request.post_request_data(_url=c_app_api.getTask, _data=param, _headers=self.headers)
        return response

    def get_transform_scheme_detail(self, param):
        """【施工app: 查看改造方案详情】"""
        response = self.request.get_request(_url=c_app_api.getTransFormSchemeDetail, _data=param, _headers=self.headers)
        return response

    def my_task_list(self, param):
        """【施工app：我的任务列表】"""
        response = self.request.get_request(_url=c_app_api.myTaskList, _data=param, _headers=self.headers)
        return response

    def construction_details(self, param):
        """【施工app：查询任务详情】"""
        response = self.request.get_request(_url=c_app_api.constructionDetails, _data=param, _headers=self.headers)
        return response

    def commit_scheme(self, data):
        """【施工app：提交施工产品方案】"""
        response = self.request.post_request_data(_url=c_app_api.commitScheme, _data=data, _headers=self.headers)
        return response

    def complete_scheme(self, data):
        """"【施工app：施工完成】"""
        response = self.request.post_request_data(_url=c_app_api.commitScheme, _data=data, _headers=self.headers)
        return response

    def complete_task_list(self, data):
        """"【施工app：已完成列表】"""
        response = self.request.get_request(_url=c_app_api.completeTaskList, _data=data, _headers=self.headers)
        return response

