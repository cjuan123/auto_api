# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: cater_helper.py
@time: 2019/5/28 11:31
@desc：大配餐数据库
"""
from datetime import datetime, date, timedelta
import time
from tools.mysql_helper import MysqlHelper


class CaterHelper:

   

    def query_appointment(self, user_id):
        """查询预约记录"""
        sql = "SELECT * FROM `appointment` where user_id = %s and enabled = 1;" % user_id
        result = self.my_sql.find_all(sql)
        print(result)

    def update_appointment_time(self, user_id):
        """修改预约时间"""
        create_time = datetime.strptime(str(self.get_yesterday()) + " " + datetime.now().strftime('%H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        time = datetime.strptime(str(date.today()) + " " + datetime.now().strftime('%H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        print(type(create_time))
        print(type(time))
        sql = "UPDATE `appointment` SET create_time = '%s' , `time` = '%s' WHERE user_id = %s AND enabled = 1;" % (create_time, time, user_id)
        self.my_sql.cud(sql=sql)

    def update_server_order_time(self, user_id):
        """修改就餐时间"""
        create_time = datetime.strptime(str(self.get_yesterday()) + " " + datetime.now().strftime('%H:%M:%S'),
                                        '%Y-%m-%d %H:%M:%S')
        eat_time = datetime.strptime(str(date.today()) + " " + datetime.now().strftime('%H:%M:%S'), '%Y-%m-%d %H:%M:%S')

        sql = "UPDATE `service_order` SET create_time = '%s' , `eat_time` = '%s'" \
              " WHERE uid = %s AND enabled = 1;" % (self.get_yesterday(), date.today(), user_id)
        self.my_sql.cud(sql=sql)

    def get_yesterday(self):
        """获取昨天日期"""
        today = date.today()  # datetime类型当前日期
        yesterday = today + timedelta(days=-1)  # 减去一天
        return yesterday


# cater = CaterHelper()
# cater.update_server_order_time("1541")
# cater.update_appointment_time("1359")
# print(cater.get_yesterday())

print()