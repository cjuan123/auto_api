# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: agencies.py
@time: 2019/6/3 9:57
@desc：评估
"""
from conf import DEFAULT
from tools.http_request import Request
from source.Agencies import agencies_api as a_api


class Agencies:

    request = Request()
    headers = DEFAULT.HEADERS

    def query_scheme_subject_list(self, param):
        """【评估-APP】：下载评估申请"""
        response = self.request.post_request_data(_url=a_api.querySchemeSubjectList, _data=param, _headers=self.headers)
        return response

    def update(self, param):
        """【评估-APP】：开始评估申请"""
        response = self.request.post_request_data(_url=a_api.update, _data=param, _headers=self.headers)
        return response

    def calc_score(self, param):
        """【评估-APP】：计算分数"""
        response = self.request.post_request_data(_url=a_api.calcScore, _data=param, _headers=self.headers)
        return response

    def save_answer(self, param):
        """【评估-APP】：上传评估结果"""
        response = self.request.post_request_data(_url=a_api.saveAnswer, _data=param, _headers=self.headers)
        return response




