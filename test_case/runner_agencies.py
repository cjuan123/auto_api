# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: runner_agencies.py
@time: 2019/6/13 20:34
@desc：运行评估流程脚本，并生成测试报告
"""
import unittest
import os, time
from tools.file_path import FilePath
from runner import HTMLTestRunnerNew

# 测试报告存放地址
reports_path = os.path.join(FilePath().reports_path(), "test_reports_agencies_%s.html" % time.strftime('%Y_%m_%d'))

cast_path = os.path.join(FilePath().case_path(), "test_agencies")
# discover = unittest.defaultTestLoader.discover(r"F:\auto_api\test_case\test_agencies", pattern="test_*.py")
discover = unittest.defaultTestLoader.discover(cast_path, pattern="test_*.py")


root_path = os.path.dirname(os.path.abspath(".."))
file = open(os.path.join(root_path, reports_path), "wb+")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
runner.run(discover)