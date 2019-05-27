"""
@version: 1.0
@author: chenj
@file: Login.py
@time: 2019/5/19 11:10
@desc：登录类
"""

from conf import DEFAULT
from tools.http_request import Request

request = Request()
government_host = DEFAULT.test
pc_host = DEFAULT.test3
headers = DEFAULT.HEADERS

def get_account(account, password):
    def login(func):
        def inner(*args):
            government_URL = government_host + "/Gover"
            request.get_request(_url=government_URL, _headers=headers)
            government_check = government_host + "/j_spring_security_check"
            params = {
                "mobile": account,
                "password": password
            }
            print(params)
            response = request.post_request_data(_url=government_check, _data=params, _headers=headers)
            headers["Cookie"] = response.request.headers["Cookie"]
            print("====" + response.request.headers["Cookie"])
            func(*args)
        return inner
    return login

