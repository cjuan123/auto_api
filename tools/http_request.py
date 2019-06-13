"""
@version: 1.0
@author: chenj
@file: http_request.py
@time: 2019/5/19 10:32
"""
import requests
import urllib3
import warnings
from tools.logger import Logger


class Request:
    def __init__(self):
        self.log = Logger()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        warnings.simplefilter("ignore", ResourceWarning)

        # 禁用安全请求警告
        requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def post_request_data(self, _url, _data, _headers):
        response = requests.post(url=_url, data=_data, headers=_headers, verify=False)
        self.log.info("【request_URL】：%s" % _url)
        self.log.info("【param_data】: %s" % _data)
        self.log.info("【status_code】: %d" % response.status_code)
        return response

    def post_request_json(self, _url, _json, _headers):
        response = requests.post(url=_url, json=_json, headers=_headers, verify=False)
        self.log.info("【request_URL】：%s" % _url)
        self.log.info("【param_data】: %s" % _json)
        self.log.info("【status_code】: %d" % response.status_code)
        return response

    def post_request_files(self, _url, _files, _headers):
        response = requests.post(url=_url, files=_files, headers=_headers, verify=False)

        self.log.info("【request_URL】：%s" % _url)
        self.log.info("【param_data】: %s" % _files)
        self.log.info("【status_code】: %d" % response.status_code)

        return response

    def get_request(self, _url, _headers, _data=None):
        response = requests.get(url=_url, params=_data, headers=_headers, verify=False)
        self.log.info("【request_URL】：%s" % _url)
        self.log.info("【param_data】: %s" % _data)
        self.log.info("【status_code】: %d" % response.status_code)
        return response
