# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: runner_agencies.py
@time: 2019/6/13 20:34
@desc：执行大配餐所有测试用例，并生成测试报告
"""
import sys, os, unittest, time
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)).split('auto_api')[0], "auto_api"))

from tools.file_path import FilePath
from runner import HTMLTestRunnerNew

# 测试报告存放地址
reports_path = os.path.join(FilePath().reports_path(), "test_reports_cater_%s.html" % time.strftime('%Y_%m_%d'))

cast_path = FilePath().case_ddt_path()
discover = unittest.defaultTestLoader.discover(cast_path, pattern="test_*.py")


root_path = os.path.dirname(os.path.abspath(".."))
file = open(os.path.join(root_path, reports_path), "wb+")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
runner.run(discover)

print("【测试报告地址】：%s" % reports_path)