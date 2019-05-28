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
requests.get(_url, headers=headers)

_check = "https://test.chinaylzl.com/j_spring_security_check"
params = {
    "mobile": "15184448326",
    "password": "123qwe"
          }
res = requests.post(url=_check, data=params, headers=headers)
print(res.request.headers["Cookie"])