"""
@version: 1.0
@author: chenj
@file: runner_cater.py
@time: 2019/5/19 15:07
"""

import unittest
from runner import HTMLTestRunnerNew
from test_case.test_cater_set.test_government_cater import test_government_cater
import os, json
from tools.read_excel import ReadExcel
suite = unittest.TestSuite()

excel_dir = "test_data\\add_user.xls"
read_excel = ReadExcel(excel_dir)
test_data = read_excel.row_value()

for item in test_data:
    j = json.loads(item[1])
    suite.addTest(test_government_cater("test_add_user", param=json.loads(item[1]), excepted=item[2]))

root_path = os.path.dirname(os.path.abspath(".."))
file = open(os.path.join(root_path, "reports\\test_result.html"), "wb+")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
runner.run(suite)
