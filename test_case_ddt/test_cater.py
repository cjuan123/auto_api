# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_cater.py
@time: 2019/7/3 17:00
@desc：
"""
import ddt, json, unittest
from tools.read_excel import ReadExcel
from source.CaterSet.cater import GovernCater
from conf import Login
from tools.logger import Logger
from db_helper.cater_helper import CaterHelper


@ddt.ddt
class TestCater(unittest.TestCase):
    g_cater = GovernCater()
    log = Logger()
    # test_data = ReadExcel("case_data.xlsx", "cater").row_value()

    @classmethod
    def setUpClass(cls):
        print("------------------------------STA------------------------------")
        cls.log.info("------------------------ 大配餐 STA ------------------------")
        cls.cater_helper = CaterHelper()

    def setUp(self):
        self.log.info("------------------ 用例 STA ------------------")

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("get_user_by_id_card"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_get_user_by_id_card(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """大配餐政府端添加人员:711557193107046197"""
        param = json.loads(data)
        self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
        response = self.g_cater.get_user_by_id_card(case_name=case_name, param=param)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(except_result, response.json()["message"])

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("add_user"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def _test_add_user(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """大配餐政府端添加人员:711557193107046197"""
        param = json.loads(data)
        self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
        response = self.g_cater.add_user(case_name=case_name, param=param)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(except_result, response.json()["message"])

    def tearDown(self):
        self.log.info("------------------ 用例 END ------------------")

    @classmethod
    def tearDownClass(cls):
        cls.log.info("------------------------ 大配餐 END ------------------------")
        print("------------------------------END------------------------------")


if __name__ == '__main__':
    unittest.main()
