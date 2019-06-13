# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: Login_s.py
@time: 2019/6/13 13:32
@desc：
"""
from conf import HEADERS
from tools.read_yaml import ReadYaml
from tools.http_request import Request

headers = HEADERS.headers

request = Request()

read_yaml = ReadYaml("default.yaml")
govern_host = read_yaml.get_host("govern")      # 政府端
business = read_yaml.get_host("business")       # 企业端
agencies = read_yaml.get_host("host_8093")      # 评估端
host_8094 = read_yaml.get_host("host_8094")     # 施工端
cater = read_yaml.get_host("agencies")          # 配餐企业端


def construction_app_login(account, password):
    """施工app登录"""
    def login(func):
        def inner(*args):
            print("=========================== 【施工web】登录账号：%s ===========================" % account)
            _URL = host_8094 + "/app/login"
            param = {
                "account": account,
                "password": password
            }
            response = request.post_request_data(_url=_URL, _data=param, _headers=headers)

            headers["token"] = response.json()["data"]
            func(*args)
        return inner
    return login


def construction_login(account, password):
    """施工端登录"""
    def login(func):
        def inner(*args):
            print("=========================== 【施工web】登录账号：%s ===========================" % account)
            _URL = host_8094 + "/web/login"
            param = {
                "account": account,
                "password": password
            }
            response = request.get_request(_url=_URL, _data=param, _headers=headers)
            headers["token"] = response.json()["data"]
            func(*args)
        return inner
    return login


def agencies_login(account, password):
    """评估端登录"""
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【企业端】登录账号：%s ===========================" % account)
            _URL_login = agencies + "/login"
            param = {
                'phone': account,
                'password': password
            }
            response = request.post_request_data(_url=_URL_login, _data=param, _headers=headers)
            session = response.cookies.get_dict()["SESSION"]
            user = response.cookies.get_dict()["user"]
            cookies = "SESSION=" + session + ";user=" + user
            headers["Cookie"] = cookies
            func(*args)
        return inner
    return login


def govern_login(account, password):
    """政府端登录"""
    def login(func):
        def inner(*args):
            print("=============【政府端登录：%s】==================" % account)
            headers["token"] = None
            headers["Cookie"] = None
            government_url = govern_host + "/Gover"
            request.get_request(_url=government_url, _headers=headers)
            government_check = govern_host + "/j_spring_security_check"
            params = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=government_check, _data=params, _headers=headers)
            headers["Cookie"] = response.request.headers["Cookie"]
            func(*args)
        return inner
    return login


def agencies_app_login(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【评估APP】登录账号：%s ===========================" % account)
            _URL = agencies + "/api/user/login"
            param = {
                'phone': account,
                'password': password
            }
            res = request.post_request_data(_url=_URL, _data=param, _headers=headers)
            print(res.cookies.get_dict()['assess_token'])
            headers["Cookie"] = 'assess_token=' + res.cookies.get_dict()['assess_token']
            print(res.json()['detail'])
            print(res.json()['data']['agencyId'])
            func(*args)
        return inner
    return login


def cater_login(account, password):
    """配餐企业端登录"""
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=============【大配餐企业端登录：%s】==================" % account)
            print(headers)
            _URL = cater + "/login"
            request.get_request(_url=_URL, _headers=headers)
            _check = cater + "/checkUser"
            param = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=_check, _data=param, _headers=headers)
            headers["Cookie"] = "JSESSIONID=" + response.cookies.get_dict()["JSESSIONID"] + \
                                ";USER_COOKIE_ID_meal=" + response.cookies.get_dict()["USER_COOKIE_ID_meal"]
            func(*args)
        return inner
    return login


def cater_app_login(account, password):
    """配餐APP登录"""
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("==================【大配餐APP登录：%s】==================" % account)
            _URL = cater + "/api/login"
            param = {
                "mobile": account,
                "password": password
            }
            response = request.post_request_data(_url=_URL, _data=param, _headers=headers)
            headers["Cookie"] = "USER_COOKIE_ID_meal=" + response.cookies.get_dict()["USER_COOKIE_ID_meal"]
            func(*args)
        return inner
    return login


def business_login(account, password):
    """企业端登录"""
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【企业端】登录账号：%s ===========================" % account)
            _URL = business + "/login"
            request.get_request(_url=_URL, _headers=headers)
            _submit_login = business + "/submitLogin"
            param = {
                'account': account,
                'password': password
            }
            response = request.post_request_data(_url=_submit_login, _data=param, _headers=headers)
            session = response.cookies.get_dict()["SESSION"]
            ylzlbs = response.cookies.get_dict()["ylzlbs"]
            cookies = "SESSION=" + session + ";ylzlbs=" + ylzlbs
            headers["Cookie"] = cookies
            func(*args)
        return inner
    return login


def business_app_login(account, password):
    """派工助手APP登录"""
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【派工APP】登录账号：%s ===========================" % account)
            _URL = business + "/user/api/login"
            param = {
                'account': account,
                'password': password
            }
            res = request.post_request_data(_url=_URL, _data=param, _headers=None)
            cookies = 'ylzlbs=' + res.cookies.get_dict()['ylzlbs']
            headers["Cookie"] = cookies
            func(*args)
        return inner
    return login
