# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: business.py
@time: 2019/5/29 11:22
@desc：企业类
"""
from tools.http_request import Request
import datetime
from source.Business import business_api as b_api


class Business:

    request = Request()

    def add_or_update_branch(self, param, header):
        """添加|更新分支机构"""
        res = self.request.post_request(url=b_api.addOrUpdateBranch, data=param, header=header)
        return res

    def branch_info(self, param, header):
        """查询分支机构，获取id"""
        pass

    def query_pai_user_info(self, idCard, header):
        """服务订单生成"""
        param = {
            "classification": 1,
            "groupId": 2,
            "idcard": idCard
        }
        response = self.request.get_request(url=b_api.queryPaiUserInfo, data=param, header=header)
        return response

    def create_orders(self, idCard, user_id, header):
        """创建订单"""
        endDate = str(datetime.datetime.now().strftime('%Y-%m-%d')) + " 23:59:59"
        param = 'classification=1&groupId=2&idcard='+idCard+'&uid='+str(user_id)+'&memberId=&mark=%E6%B5%8B%E8%AF%95&itemsId=310&number=1&endDate='+endDate+'&daycareId='
        # param = {
        #     "classification": 1,
        #     "groupId": 2,
        #     "idcard": idCard,
        #     "uid": user_id,
        #     "mark": "api备注",
        #     "itemsId": "310",
        #     "number": "1",
        #     "endDate": endDate
        # }
        response = self.request.post_request(url=b_api.createOrders, data=param, header=header)
        return response

    def query_pai_order_send(self, idcard, header):
        """订单派工页面，获取订单ID"""
        param = {
            "idCard": idcard
        }
        response = self.request.post_request(url=b_api.queryPaiOrderSend, data=param, header=header)
        return response

    def save_service_record(self, orderId, header):
        """派工"""
        param = {
            "buid": "1182",
            "orderId": orderId
        }
        response = self.request.post_request(url=b_api.saveServiceRecord, data=param, header=header)
        return response

    def start_service(self, order_id, header):
        """派工助手APP：开始服务"""
        param = {
            'orderId': order_id,
            'startPosition': '104.081859,30.546299'
        }
        response = self.request.post_request(url=b_api.startService, data=param, header=header)
        return response

    def complete_service(self, order_id, header):
        """派工助手APP：完成服务"""
        param = {
            'type': '2',
            'endPosition': '104.081849,30.54631',
            'orderId': order_id,
            'images': 'https://file.chinaylzl.com/test/serviceImages/2018/11/15/4a6f2a0ffff54ca88aed5132f482a4aa.jpg,'
        }
        response = self.request.post_request(url=b_api.completeService, data=param, header=header)
        return response

    def update_service_degreeb(self, order_id, header):
        """派工助手APP：评价订单"""
        param = {
            'orderId': order_id,
            'degree': '100'
        }
        response = self.request.post_request(url=b_api.updateServiceDegree, data=param, header=header)
        return response
