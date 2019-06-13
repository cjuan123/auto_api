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
        self.file_path = FilePath().root_path()
        self.path = os.path.join(os.path.join(self.file_path, "yamls"), path)
        self.fo = None

    def open_yaml(self):
        """打开yaml文件"""
        try:
            with open(self.path, 'r', encoding='utf-8') as url:
                url_data = yaml.load(url)
            return url_data
        except Exception as e:
            print('yaml读取失败，原因为：%s' % e)
        return url_data

    def house_govern(self, type, api_name):
        data = self.open_yaml()
        return data["house_govern"][type][api_name]

    def house_constructor(self, type, api_name):
        data = self.open_yaml()
        return data["house_constructor"][type][api_name]

    def business(self, type, api_name):
        data = self.open_yaml()
        return data["business"][type][api_name]

    def agencies(self, type, api_name):
        data = self.open_yaml()
        return data["agencies"][type][api_name]

    def govern_agencies(self, type, api_name):
        data = self.open_yaml()
        return data["govern_agencies"][type][api_name]

    def get_header(self):
        data = self.open_yaml()
        return data["HEADER"]

    def get_host(self, type):
        data = self.open_yaml()
        return data["host"][type]

    def get_account(self, type):
        data = self.open_yaml()
        return data["account"][type]

    def get_password(self, type):
        data = self.open_yaml()
        return data["password"][type]

    def close_yaml(self):
        """关闭文件"""
        self.fo.close()


# read = ReadYaml("default.yaml")

