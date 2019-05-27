"""
@version: 1.0
@author: chenj
@file: http_request.py
@time: 2019/5/19 10:32
"""
import requests


class Request:

    def post_request_data(self, _url, _data, _headers):
        response = requests.post(url=_url, data=_data, headers=_headers, verify=False)
        print("【request_URL】：%s" % _url)
        print("【status_code】: %d" % response.status_code)
        return response

    def post_request_json(self, _url, _json, _headers):
        response = requests.post(url=_url, json=_json, headers=_headers)
        print("【request_URL】：%s" % _url)
        print("【status_code】: %d" % response.status_code)
        return response

    def get_request(self, _url, _headers, _data=None):
        response = requests.get(url=_url, params=_data, headers=_headers, verify=False)
        print("【request_URL】：%s" % _url)
        print("【status_code】: %d" % response.status_code)

        return response
