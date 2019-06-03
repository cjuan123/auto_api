"""
@version: 1.0
@author: chenj
@file: demo.py
@time: 2019/5/19 10:43
"""

import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

_url = "https://test.chinaylzl.com/Gover"
requests.get(_url, headers=headers, verify=False)

_check = "https://test.chinaylzl.com/j_spring_security_check"
params = {
    "mobile": "18048054262",
    "password": "123qwe"
          }
res = requests.post(url=_check, data=params, headers=headers, verify=False)

headers["Cookie"] = res.request.headers["Cookie"]
print(headers)

url = "https://test.chinaylzl.com/surveyUser/listUsersNew"      # 人员批量充值
# param = "name=&idCard=510107193303079195&sex=&startAge=&endAge=&address=&sort=&orderby=&pageIndex=1&point=&residenceAddress=51010902&type=0&shinengStr=&cjstate=&cjdj=&level=&personCategory=&liveStatus=&liveType=&startTime=&endTime=&isBind=&isPaging=false"
param = {
    "idCard": "711557195305306788",
    "pageIndex": 1,
    "isBind": ""
}
res = requests.post(url=url, headers=headers, data=param, verify=False)
print(res.status_code)
print(res.json())


# listServiceRecord = "https://test.chinaylzl.com/service/listServiceRecord"
# param = {
#     "userName": "测试0514",
#     "isPaging": "false",
#     "community": "900109"
# }
#
# res = requests.post(url=listServiceRecord, headers=headers, data=param, verify=False)
# print(res.status_code)
# print(res.text)