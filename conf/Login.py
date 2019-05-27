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

# government_URL = government_host + "/Gover"
# request.get_request(_url=government_URL, _headers=headers)
# government_check = government_host + "/j_spring_security_check"
# params = {
#             "mobile": "15184448326",
#             "password": "123qwe"
#         }
# print(params)
# response = request.post_request(_url=government_check, _data=params, _headers=headers)
# print(response.request.headers["Cookie"])


def get_account(mobile, password):
    def login(func):
        func()
        government_URL = government_host + "/Gover"
        request.get_request(_url=government_URL, _headers=headers)
        government_check = government_host + "/j_spring_security_check"
        params = {
                    "mobile": mobile,
                    "password": password
                }
        print(params)
        response = request.post_request_data(_url=government_check, _data=params, _headers=headers)
        headers["Cookie"] = response.request.headers["Cookie"]
        print("====" + response.request.headers["Cookie"])
    return login


@get_account("13999999992", "123qwe")
def government_login():
    print("13")

