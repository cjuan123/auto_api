# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: mysql_helper.py
@time: 2019/5/28 11:03
@desc：连接数据库类
"""

from pymysql import *


class MysqlHelper:
    # host, port, user, password, db, charset='utf8'
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        """连接数据库的基本信息"""
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def open(self):
        """打开数据库连接"""
        self.con = connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db, charset=self.charset)
        self.cursor = self.con.cursor()

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.con.close()

    def cud(self, sql, param=()):
        """增删改"""
        self.open()
        print(sql)
        self.cursor.execute(sql, param)
        self.con.commit()
        print('OK!')
        self.close()

    def find_all(self, sql, param=()):
        """查询数据"""
        self.open()
        self.cursor.execute(sql, param)
        result = self.cursor.fetchall()
        return result

    def find_one(self, sql, param=()):
        self.open()
        self.cursor.execute(sql, param)
        result = self.cursor.fetchone()
        return result
