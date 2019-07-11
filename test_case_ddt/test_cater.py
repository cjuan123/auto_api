# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_cater.py
@time: 2019/7/3 17:00
@desc：
"""
import datetime
import ddt, json, unittest
from tools.read_excel import ReadExcel
from source.CaterSet.cater import GovernCater
from conf import Login
from tools.logger import Logger
from db_helper.cater_helper import CaterHelper
from tools.excel_report import ExcelReport


@ddt.ddt
class TestCater(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cater_helper = CaterHelper()
        cls.g_cater = GovernCater()
        cls.log = Logger()
        cls.excel_report = ExcelReport()
        cls.excel_data = []
        cls.start = datetime.datetime.now()
        cls.success_num = []    # 测试用例成功数
        cls.fail_num = []       # 测试用例失败数

        cls.apply_id = []        # 人员申请ID

        print("------------------------------STA------------------------------")
        cls.log.info("------------------------ 大配餐 STA ------------------------")

    def setUp(self):
        self.log.info("------------------ 用例 STA ------------------")

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/getuserbyidcard"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_01_get_user_by_id_card(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """大配餐政府端添加人员:711557193107046197"""

        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            param = json.loads(data)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.get_user_by_id_card(case_name=case_name, param=param)
            result = self.cater_helper.query_user_by_id_card(param["idcard"])   # 查询数据库
            if result != None:
                self.cater_helper.del_cater_user_info(result[0])    # 删除数据库记录
                self.log.info("【身份证：%s】 - 删除成功" % (param["idcard"]))
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/adduser"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_02_add_user(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """大配餐政府端添加人员:711557193107046197"""
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            param = json.loads(data)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.add_user(case_name=case_name, param=param)
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/userlist"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_03_user_list(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            param = json.loads(data)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.user_list(case_name=case_name, param=param)
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/user/userDetail"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_04_user_detail(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            user_id = self.cater_helper.query_user_id()
            param = {
                "id": user_id
            }
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.user_detail(case_name=case_name, param=param)
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/review/queryAllApplyUser"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_05_get_apply_id(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """根据查询条件，获取人员申请ID"""
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            data_list = str(data).split(",")
            param = {
                "parameter": data_list[0],
                "status": 1,
                "type": data_list[1],
                "pageNow": 1
            }
            print(param)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.get_apply_id(case_name=case_name, param=param)
            print(response.json())
            print(len(response.json()["data"]["records"]))
            self.apply_id.append(response.json()["data"]["records"][0]["applyId"])
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/review/reviewUser_1"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_06_review_user(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """人员审核"""
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            data_list = str(data).split(",")
            param = {
                "passed": data_list[0],
                "advice": data_list[1],
                "checkType": data_list[2],
                "applyId": self.apply_id[int(data_list[3])]
            }
            print(param)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.review_user(case_name=case_name, param=param)
            print(response.json())
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    @ddt.data(*ReadExcel("case_data.xlsx", "cater").row_value("/review/reviewUser_2"))
    @ddt.unpack
    @Login.govern_login("13999999992", "123qwe")
    def test_07_review_user(self, moudle, api_name, case_no, case_name, data, except_result, case_desc):
        """人员复审"""
        excel = {}
        excel["t_moudle"] = moudle
        excel["t_id"] = case_no
        excel["t_name"] = case_name
        excel["t_api_name"] = api_name
        excel["t_param"] = data
        excel["t_hope"] = except_result
        try:
            data_list = str(data).split(",")
            param = {
                "passed": data_list[0],
                "advice": data_list[1],
                "checkType": data_list[2],
                "applyId": self.apply_id[int(data_list[3])]
            }
            print(param)
            self.log.info("【%s】 - 用例描述：%s" % (case_name, case_desc))
            response = self.g_cater.review_user(case_name=case_name, param=param)
            print(response.json())
            excel["t_return_data"] = str(response.json())
            self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
            excel["t_actual"] = response.json()["message"]
            self.assertEqual(except_result, response.json()["message"])
            excel["t_result"] = "通过"
            self.success_num.append("通过")
        except Exception as e:
            print("异常：%s" % e)
            excel["t_result"] = "失败"
            self.fail_num.append("失败")
        finally:
            self.excel_data.append(excel)

    def tearDown(self):
        self.log.info("------------------ 用例 END ------------------")

    @classmethod
    def tearDownClass(cls):
        cls.end = datetime.datetime.now()
        print(cls.apply_id)
        cls.profile_data = {}
        cls.profile_data["test_name"] = "大配餐"
        cls.profile_data["test_version"] = "version 2.3"
        cls.profile_data["test_language"] = "python 3"
        cls.profile_data["test_net"] = "test"
        cls.profile_data["test_date"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cls.profile_data["test_sum"] = ReadExcel("case_data.xlsx", "cater").row_num() - 1
        cls.profile_data["test_success"] = len(cls.success_num)
        cls.profile_data["test_failed"] = len(cls.fail_num)
        cls.profile_data["test_time"] = "%s s" % (cls.end - cls.start)
        cls.excel_report.test_profile(data=cls.profile_data)
        cls.excel_report.test_info(cls.excel_data)
        cls.excel_report.close()
        cls.log.info("------------------------ 大配餐 END ------------------------")
        print("------------------------------END------------------------------")


if __name__ == '__main__':
    unittest.main()
