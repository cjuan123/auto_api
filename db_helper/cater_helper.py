# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: cater_helper.py
@time: 2019/7/4 14:34
@desc：大配餐数据库操作
"""
from tools.read_yaml import ReadYaml
from tools.mysql_helper import MysqlHelper


class CaterHelper:

    def __init__(self):
        self.db_info = ReadYaml("default.yaml").get_msyql()
        self.db = MysqlHelper(host=self.db_info["host"], user=self.db_info["user"],
                         password=self.db_info["password"], db='assist_catering')

    def query_user_by_id_card(self, id_card):
        """通过身份证号查询，该身份证号是否存在"""
        sql = "SELECT * FROM `user` WHERE idCard = '%s';" % id_card
        result = self.db.find_all(sql)
        return result


# if __name__ == '__main__':
# #     cater = CaterHelper()
# #     cater.query_user_by_id_card("711557195407037815")