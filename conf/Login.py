"""
@version: 1.0
@author: chenj
@file: Login.py
@time: 2019/5/19 11:10
@desc：登录类
"""

from conf import DEFAULT
from tools.http_request import Request
from source.Transform import construcotr_web_app_api as c_app

request = Request()
government_host = DEFAULT.test  # 政府端host
pc_host = DEFAULT.test3     # 大配餐host
bus_host = DEFAULT.test1    # 企业host
headers = DEFAULT.HEADERS   # 请求头
construction_login = c_app.login    # 施工app
web_c_login = c_app.web_login       # 施工web端


#   施工web
def get_construction_web(account, password):
    def login(func):
        def inner(*args):
            print(DEFAULT.HEADERS)
            if ("Cookie" in DEFAULT.HEADERS) == True:
                del DEFAULT.HEADERS['Cookie']
            print(DEFAULT.HEADERS)
            print("=========================== 【施工web】登录账号：%s ===========================" % account)
            param = {
                "account": account,
                "password": password
            }
            response = request.get_request(_url=web_c_login, _data=param, _headers=DEFAULT.HEADERS)
            print(response.json())
            headers["token"] = response.json()["data"]
            print(DEFAULT.HEADERS)
            func(*args)
        return inner
    return login


#   施工APP
def get_construction_app(account, password):
    def login(func):
        def inner(*args):
            if ("Cookie" in DEFAULT.HEADERS) == True:
                del dict['Cookie']
            print("=========================== 【施工APP】登录账号：%s ===========================" % account)
            param = {
                "account": account,
                "password": password
            }
            response = request.post_request_data(_url=construction_login, _data=param, _headers=DEFAULT.HEADERS)
            headers["token"] = response.json()["data"]
            print(DEFAULT.HEADERS)
            func(*args)
        return inner
    return login


#   政府端登录
def get_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=============【政府端登录：%s】==================" % account)
            government_url = government_host + "/Gover"
            request.get_request(_url=government_url, _headers=headers)
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


#   大配餐企业端登录
def get_pc_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=============【大配餐企业端登录：%s】==================" % account)
            print(headers)
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


#   大配餐APP登录

def get_app_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=============【大配餐APP登录：%s】==================" % account)
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


#   企业端登录
def get_business_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【企业端】登录账号：%s ===========================" % account)
            _URL_login = bus_host + "/login"  # setting.SAS_HOST + setting.sas_login
            request.get_request(_url=_URL_login, _headers=headers)
            _URL_submit_login = "https://test1.chinaylzl.com/submitLogin"  # setting.SAS_HOST + setting.sas_submit_login
            param = {
                'account': account,
                'password': password
            }
            response = request.post_request_data(_url=_URL_submit_login, _data=param, _headers=headers)
            session = response.cookies.get_dict()["SESSION"]
            ylzlbs = response.cookies.get_dict()["ylzlbs"]
            cookies = "SESSION=" + session + ";ylzlbs=" + ylzlbs
            headers["Cookie"] = cookies
            func(*args)
        return inner
    return login


#   派工助手APP登录
def get_business_app_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【派工APP】登录账号：%s ===========================" % account)
            _URL_login = bus_host + "/user/api/login"
            param = {
                'account': account,
                'password': password
            }
            res = request.post_request_data(_url=_URL_login, _data=param, _headers=None)
            cookies = 'ylzlbs=' + res.cookies.get_dict()['ylzlbs']
            headers["Cookie"] = cookies
            func(*args)
        return inner
    return login


#   评估机构登录
def get_agencies_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【企业端】登录账号：%s ===========================" % account)
            _URL_login = pc_host + "/login"
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


#   评估APP登录
def get_agencies_app_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【评估APP】登录账号：%s ===========================" % account)
            _URL = pc_host + "/api/user/login"
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


#   评估APP登录
def get_transform_account(account, password):
    def login(func):
        def inner(*args):
            headers["Cookie"] = None
            print("=========================== 【评估APP】登录账号：%s ===========================" % account)
            _URL = pc_host + "/api/user/login"
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




