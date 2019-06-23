# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: business.py
@time: 2019/5/29 11:22
@desc：企业类
"""
from tools.http_request import Request
from conf import HEADERS
from source.Business import business_api as b_api


class Business:

    request = Request()
    headers = HEADERS.headers

    def add_or_update_branch(self, case_name, param):
        """企业端：添加|更新分支机构"""
        res = self.request.post_request_data(case_name=case_name, _url=b_api.addOrUpdateBranch, _data=param, _headers=self.headers)
        return res

    def branch_info(self, case_name, param):
        """企业端：查询分支机构，获取id"""
        pass

    def query_pai_user_info(self, case_name, param):
        """企业端：服务订单生成"""
        response = self.request.get_request(case_name=case_name, _url=b_api.queryPaiUserInfo, _data=param, _headers=self.headers)
        return response

    def create_orders(self, case_name, param):
        """企业端：创建订单"""
        response = self.request.post_request_data(case_name=case_name, _url=b_api.createOrders, _data=param, _headers=self.headers)
        return response

    def query_pai_order_send(self, case_name, param):
        """企业端：订单派工页面，获取订单ID"""
        response = self.request.post_request_data(case_name=case_name, _url=b_api.queryPaiOrderSend, _data=param, _headers=self.headers)
        return response

    def save_service_record(self, case_name, param):
        """企业端：派工"""
        response = self.request.post_request_data(_url=b_api.saveServiceRecord, _data=param, _headers=self.headers)
        return response

    def start_service(self, case_name, param):
        """派工助手APP：开始服务"""
        response = self.request.post_request_data(case_name=case_name, _url=b_api.startService, _data=param, _headers=self.headers)
        return response

    def complete_service(self, case_name, param):
        """派工助手APP：完成服务"""
        response = self.request.post_request_data(case_name=case_name, _url=b_api.completeService, _data=param, _headers=self.headers)
        return response

    def update_service_degree(self, case_name, param):
        """派工助手APP：评价订单"""
        response = self.request.post_request_data(case_name=case_name, _url=b_api.updateServiceDegree, _data=param, _headers=self.headers)
        return response
