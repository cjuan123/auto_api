# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: run_govern_house.py
@time: 2019/6/13 14:49
@desc：运行适老化改造流程脚本，并生成测试报告
"""
import unittest
import os, time
from tools.file_path import FilePath
from runner import HTMLTestRunnerNew

reports_path = os.path.join(FilePath().reports_path(), "test_reports_%s.html" % time.strftime('%Y_%m_%d'))


discover = unittest.defaultTestLoader.discover(r"F:\auto_api\test_case\test_house", pattern="test_house_flow.py")

root_path = os.path.dirname(os.path.abspath(".."))
file = open(os.path.join(root_path, reports_path), "wb+")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
runner.run(discover)
