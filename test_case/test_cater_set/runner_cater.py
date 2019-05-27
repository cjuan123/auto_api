"""
@version: 1.0
@author: chenj
@file: runner_cater.py
@time: 2019/5/19 15:07
"""

import unittest
from runner import HTMLTestRunnerNew
from test_case.test_cater_set.test_government_cater import test_government_cater
import os
from tools.read_excel import ReadExcel
suite = unittest.TestSuite()
# test_data = [[{
#             "address": "测试现住地址api",
#             "applicationCategory": "200",
#             "auditState": 1,
#             "birthday": "19410718",
#             "eatCount": 0,
#             "homeDelivery": 0,
#             "idCard": "510104194107189317",
#             "isArea": 1,
#             "mealId": 307,
#             "name": "测试数据api1",
#             "permanentAddress": "测试户籍地址api",
#             "phone": "15282566260",
#             "residenceAddress": "51010613",
#             "sex": "m",
#             "useYanglao": 1
#         }, "操作异常:用户重复"], [{
#             "address": "测试现住地址api",
#             "applicationCategory": "200",
#             "auditState": 1,
#             "birthday": "19410718",
#             "eatCount": 0,
#             "homeDelivery": 0,
#             "idCard": "510104194107180232",
#             "isArea": 1,
#             "mealId": 307,
#             "name": "测试数据api2",
#             "permanentAddress": "测试户籍地址api",
#             "phone": "15282566260",
#             "residenceAddress": "51010613",
#             "sex": "m",
#             "useYanglao": 1
#         }, "添加成功"]]
excel_dir = "test_data\\add_user.xls"
read_excel = ReadExcel(excel_dir)
test_data = read_excel.row_value()
for item in test_data:
    suite.addTest(test_government_cater("test_add_user", param=item[1], excepted=item[2]))

root_path = os.path.dirname(os.path.abspath(".."))
file = open(os.path.join(root_path, "reports\\test_result.html"), "wb+")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
runner.run(suite)
