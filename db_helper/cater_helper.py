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
        result = self.db.find_one(sql)
        return result

    def del_cater_user_info(self, user_id):
        """根据用户id，删除人员相关信息"""
        user = "DELETE FROM `user` WHERE id = '%s';" % user_id

        user_balance = "DELETE FROM `user_balance` WHERE uid = '%s';" % user_id

        user_gover_balance = "DELETE FROM `user_gover_balance` WHERE uid = '%s';" % user_id

        user_review = "DELETE FROM `user_review` WHERE user_id = '%s';" % user_id

        appointment = "DELETE FROM `appointment` WHERE user_id = '%s';" % user_id

        service_order = "DELETE FROM `service_order` WHERE uid = '%s';" % user_id

        service_order_detail = "DELETE FROM `service_order_detail` WHERE order_id = (SELECT id FROM `service_order` " \
                               "WHERE uid = '%s');" % user_id
        try:
            self.db.cud(user)
            self.db.cud(user_balance)
            self.db.cud(user_gover_balance)
            self.db.cud(user_review)
            self.db.cud(appointment)
            self.db.cud(service_order)
            self.db.cud(service_order_detail)
        except Exception as e:
            self.db.con.rollback()
            print("事务处理失败", e)
        else:
            self.db.con.commit()
            print("事务处理成功")     # self.db.cursor.rowcount
            """
                pymysql.err.InterfaceError: (0, '')错误原因：执行完sql语句后，没有关闭连接
            """
            self.db.close()

    def query_user(self, name, value):
        """人员管理：高级筛选"""
        address = "900109" + "%"
        sql = "SELECT * FROM user WHERE {} = '{}' AND residence_address LIKE '{}%'".format(name, value, address)
        print(sql)
        result = self.db.find_all(sql)
        return result

    # 随机获取一个user id
    def query_user_id(self):
        sql = "SELECT id FROM `user`  ORDER BY id DESC LIMIT 1;"
        result = self.db.find_one(sql=sql)
        return result[0]

#
# if __name__ == '__main__':
#     cater = CaterHelper()
#     result = cater.query_user_id()
#     print(result)
