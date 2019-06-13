"""
@version: 1.0
@author: chenj
@file: demo.py
@time: 2019/5/19 10:43
"""
from conf import Login_s


@Login_s.construction_login("1", "123456")
def test_01():
    print(123455)

test_01()

