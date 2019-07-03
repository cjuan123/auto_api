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
        self.path = os.path.join(FilePath().yaml_path(), path)
        self.fo = None

    def open_yaml(self):
        """打开yaml文件"""
        try:
            with open(self.path, 'r', encoding='utf-8') as u:
                url_data = yaml.load(u)
            return url_data
        except Exception as e:
            print('yaml读取失败，原因为：%s' % e)
        return url_data

    def house_govern(self, type, api_name):
        """适老化政府端接口地址"""
        data = self.open_yaml()
        return data["house_govern"][type][api_name]

    def house_constructor(self, type, api_name):
        """适老化施工单位接口地址"""
        data = self.open_yaml()
        return data["house_constructor"][type][api_name]

    def business(self, type, api_name):
        """服务企业端接口地址"""
        data = self.open_yaml()
        return data["business"][type][api_name]

    def agencies(self, type, api_name):
        """评估机构接口地址"""
        data = self.open_yaml()
        return data["agencies"][type][api_name]

    def govern_agencies(self, type, api_name):
        """政府端评估机构接口地址"""
        data = self.open_yaml()
        return data["govern_agencies"][type][api_name]

    def govern_cater(self, api_name):
        """大配餐政府端接口地址"""
        data = self.open_yaml()
        return data["govern_cater"][api_name]

    def cater(self, api_name):
        """大配餐企业端接口地址"""
        data = self.open_yaml()
        return data["cater"][api_name]

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

    def get_district(self, type):
        data = self.open_yaml()
        return data["district"][type]

    def close_yaml(self):
        """关闭文件"""
        self.fo.close()


# read = ReadYaml("default.yaml")

