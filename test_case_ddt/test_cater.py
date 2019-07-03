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


@ddt.ddt
class TestCater(unittest.TestCase):
    g_cater = GovernCater()
    log = Logger()
    test_data = ReadExcel("case_data.xlsx", "cater").row_value()

    @classmethod
    def setUpClass(cls):
        print("------------------------------STA------------------------------")
        cls.log.info("------------------------ 大配餐 STA ------------------------")

    @ddt.data(*test_data)
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_add_user(self, moudle, api_name, case_no, case_detail, param, except_result, case_desc):
        """大配餐政府端添加人员"""
        if api_name == "add_user":
            response = self.g_cater.add_user(case_name=case_detail, param=json.loads(param))
            self.log.info("【%s】 - 返回结果：%s" % (case_detail, response.json()))
            self.log.info("【%s】 - 用例描述：%s" % (case_detail, case_desc))
            self.assertEqual(except_result, response.json()["message"])

    @classmethod
    def tearDownClass(cls):
        cls.log.info("------------------------ 大配餐 END ------------------------")
        print("------------------------------END------------------------------")


if __name__ == '__main__':
    unittest.main()
