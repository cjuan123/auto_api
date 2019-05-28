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
    """政府端登录"""
    def login(func):
        def inner(*args):
            print("=============【政府端登录：%s】==================" % account)
            government_URL = government_host + "/Gover"
            request.get_request(_url=government_URL, _headers=headers)
            government_check = government_host + "/j_spring_security_check"
            params = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=government_check, _data=params, _headers=headers)
            headers["Cookie"] = response.request.headers["Cookie"]
            func(*args)
        return inner
    return login


def get_pc_account(account, password):
    """大配餐企业端登录"""
    def login(func):
        def inner(*args):
            print("=============【大配餐企业端登录：%s】==================" % account)
            pc_URL = pc_host + "/login"
            request.get_request(_url=pc_URL, _headers=headers)
            pc_check = pc_host + "/checkUser"
            param = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=pc_check, _data=param, _headers=headers)
            headers["Cookie"] = "JSESSIONID=" + response.cookies.get_dict()["JSESSIONID"] + \
                                ";USER_COOKIE_ID_meal=" + response.cookies.get_dict()["USER_COOKIE_ID_meal"]
            func(*args)
        return inner
    return login


def get_app_account(account, password):
    def login(func):
        def inner(*args):
            _url = pc_host + "/api/login"
            param = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=_url, _data=param, _headers=headers)
            headers["Cookie"] = "USER_COOKIE_ID_meal=" + response.cookies.get_dict()["USER_COOKIE_ID_meal"]
            func(*args)
        return inner
    return login

