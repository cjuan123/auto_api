# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: construction.py
@time: 2019/6/12 20:32
@desc：施工单位web端、app端相关接口方法

"""
from conf import HEADERS
from tools.http_request import Request
from tools.read_yaml import ReadYaml


class Construction:

    request = Request()
    headers = HEADERS.headers
    read_default = ReadYaml("default.yaml")
    host_8094 = read_default.get_host("host_8094")
    house = ReadYaml("house_api.yaml")

    def add_employee(self, case_name, param):
        """【施工web：添加员工】"""
        _URL = self.host_8094 + self.house.house_constructor("web", "addEmployee")
        response = self.request.post_request_json(case_name=case_name, _url=_URL, _json=param, _headers=self.headers)
        return response

    def update_employee(self, case_name, param):
        """【施工web：添加员工】"""
        _URL = self.host_8094 + self.house.house_constructor("web", "updateEmployee")
        response = self.request.post_request_json(case_name=case_name, _url=_URL, _json=param, _headers=self.headers)
        return response

    def employee_list(self, case_name, param):
        """【施工web：查询列表】"""
        _URL = self.host_8094 + self.house.house_constructor("web", "employeeList")
        response = self.request.get_request(case_name=case_name, _url=_URL, _data=param, _headers=self.headers)
        return response

    def get_task(self, case_name, param):
        """【施工app：领取任务】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "getTask")
        response = self.request.post_request_data(case_name=case_name, _url=_URL, _data=param, _headers=self.headers)
        return response

    def get_transform_scheme_detail(self, case_name, param):
        """【施工app: 查看改造方案详情】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "getTransFormSchemeDetail")
        response = self.request.get_request(case_name=case_name, _url=_URL, _data=param, _headers=self.headers)
        return response

    def my_task_list(self, case_name, param):
        """【施工app：我的任务列表】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "myTaskList")
        response = self.request.get_request(case_name=case_name, _url=_URL, _data=param, _headers=self.headers)
        return response

    def construction_details(self, case_name, param):
        """【施工app：查询任务详情】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "constructionDetails")
        response = self.request.get_request(case_name=case_name, _url=_URL, _data=param, _headers=self.headers)
        return response

    def commit_scheme(self, case_name, data):
        """【施工app：提交施工产品方案】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "commitScheme")
        response = self.request.post_request_data(case_name=case_name, _url=_URL, _data=data, _headers=self.headers)
        return response

    def complete_scheme(self, case_name, data):
        """"【施工app：施工完成】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "commitScheme")
        response = self.request.post_request_data(case_name=case_name, _url=_URL, _data=data, _headers=self.headers)
        return response

    def complete_task_list(self, case_name, data):
        """"【施工app：已完成列表】"""
        _URL = self.host_8094 + self.house.house_constructor("app", "completeTaskList")
        response = self.request.get_request(case_name=case_name, _url=_URL, _data=data, _headers=self.headers)
        return response
