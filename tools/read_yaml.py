# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: read_yaml.py
@time: 2019/6/12 18:34
@desc：读取yaml文件
"""
import yaml, os
from tools.file_path import FilePath


class ReadYaml:

    def __init__(self, path):
        self.path = path
        self.file_path = FilePath()
        self.fo = None

    def open_yaml(self):
        """打开yaml文件"""
        path = os.path.join(self.file_path.root_path(), self.path)
        self.fo = open(path, encoding='utf-8')
        data = yaml.load(self.fo)
        return data

    def close_yaml(self):
        """关闭文件"""
        self.fo.close()

