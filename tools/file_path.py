# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: file_path.py
@time: 2019/6/12 18:32
@desc：获取文件路径工具类
"""
import os


class FilePath:

    def root_path(self):
        """获取项目的根路径"""
        path = os.path.abspath(os.path.dirname(__file__)).split('auto_api')[0]
        root = os.path.join(path, "auto_api")
        return root

    def log_path(self):
        root = self.root_path()
        return os.path.join(root, "logs")

    def reports_path(self):
        root = self.root_path()
        return os.path.join(root, "reports")

    def case_path(self):
        root = self.root_path()
        return os.path.join(root, "test_case")

    def yaml_path(self):
        root = self.root_path()
        return os.path.join(root, "yamls")

    def excel_path(self):
        root = self.root_path()
        return os.path.join(root, "test_data")
