# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_apply_aging.py
@time: 2019/6/13 10:53
@desc：评估APP、完成评估
"""
import sys, os
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]))
import unittest
from conf import Login
from source.agencies import Agencies


class TestGovernApplyAging(unittest.TestCase):

    agencies = Agencies()
    order_id = [21]
    person_record_id = []  # 人员评估记录ID
    evn_record_id = []  # 环境评估记录ID
    products = []
    agency_id = []

    @Login.agencies_app_login("13733263135", "123456")
    def test_001_get_tasks(self):
        """【适老化--app】：领取任务"""
        param = {
            "orderId": 77,
            "assessmentUserId": 498
        }
        print(param)
        response = self.agencies.get_tasks(case_name="领取任务", data=param)
        print(response.json())

    @Login.agencies_app_login("15982566561", "123456")
    def test_002_list_own_tasks(self):
        """【适老化--app】：我的任务列表"""
        param = {
            "assessmentUserId": 465
        }
        response = self.agencies.list_own_tasks(case_name="我的任务列表", data=param)
        print(response.json())
        self.person_record_id.append(response.json()["data"][0]["personRecordId"])
        self.evn_record_id.append(response.json()["data"][0]["personRecordId"])

    @Login.agencies_app_login("15982566561", "123456")
    def test_003_save_answer_person(self):
        """"【适老化--app】：上传人员评估结果"""
        id = 1009335
        param = {
            'name': 'assess_token',
            'answer': '[{"answerId":1,"parentId":1,"recordId":%d,"subjectId":8},{"answerId":8,"parentId":1,"recordId":%d,"subjectId":11},{"answerId":10,"parentId":1,"recordId":%d,"subjectId":20},{"answerId":12,"parentId":1,"recordId":%d,"subjectId":21},{"answerId":16,"parentId":1,"recordId":%d,"subjectId":22},{"answerId":18,"parentId":1,"recordId":%d,"subjectId":23},{"answerId":22,"parentId":1,"recordId":%d,"subjectId":24},{"answerId":24,"parentId":1,"recordId":%d,"subjectId":25},{"answerId":31,"parentId":1,"recordId":%d,"subjectId":27},{"answerId":36,"parentId":1,"recordId":%d,"subjectId":28},{"answerId":38,"parentId":2,"recordId":%d,"subjectId":32},{"answerId":41,"parentId":2,"recordId":%d,"subjectId":33},{"answerId":44,"parentId":2,"recordId":%d,"subjectId":34},{"answerId":48,"parentId":3,"recordId":%d,"subjectId":39},{"answerId":52,"parentId":3,"recordId":%d,"subjectId":40},{"answerId":57,"parentId":3,"recordId":%d,"subjectId":41},{"answerId":62,"parentId":3,"recordId":%d,"subjectId":42},{"answerId":66,"parentId":4,"recordId":%d,"subjectId":48},{"answerId":70,"parentId":4,"recordId":%d,"subjectId":49},{"answerId":75,"parentId":4,"recordId":%d,"subjectId":50},{"answerId":80,"parentId":4,"recordId":%d,"subjectId":51},{"answerId":85,"parentId":4,"recordId":%d,"subjectId":52},{"answerId":627,"parentId":391,"recordId":%d,"subjectId":393},{"answerId":628,"parentId":391,"recordId":%d,"subjectId":394},{"answerId":625,"parentId":391,"recordId":%d,"subjectId":395}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id),
            'agencyId': '110',
            "conclusion": ""
        }
        response = self.agencies.save_answer(case_name="上传人员评估结果", data=param)
        print(response.json())

    @Login.agencies_app_login("13733263394", "123456")
    def test_004_save_answer_product(self):
        """"【适老化--app】：上传环境评估结果"""
        id = 1009438
        param = {
            'recordId': id,
            "answers": '[{"answerId":1129,"parentId":635,"recordId":%d,"subjectId":668},{"answerId":1140,"parentId":635,"recordId":%d,"subjectId":673},{"answerId":1135,"parentId":635,"recordId":%d,"subjectId":671},{"answerId":1124,"parentId":635,"recordId":%d,"subjectId":666},{"answerId":1119,"parentId":635,"recordId":%d,"subjectId":664},{"answerId":1130,"parentId":635,"recordId":%d,"subjectId":669},{"answerId":1141,"parentId":635,"recordId":%d,"subjectId":674},{"answerId":1126,"parentId":635,"recordId":%d,"subjectId":667},{"answerId":1137,"parentId":635,"recordId":%d,"subjectId":672},{"answerId":1121,"parentId":635,"recordId":%d,"subjectId":665},{"answerId":1133,"parentId":635,"recordId":%d,"subjectId":670},{"answerId":1118,"parentId":634,"recordId":%d,"subjectId":652},{"answerId":1113,"parentId":634,"recordId":%d,"subjectId":650},{"answerId":1115,"parentId":634,"recordId":%d,"subjectId":651},{"answerId":1098,"parentId":633,"recordId":%d,"subjectId":642},{"answerId":1105,"parentId":633,"recordId":%d,"subjectId":645},{"answerId":1106,"parentId":633,"recordId":%d,"subjectId":646},{"answerId":1109,"parentId":633,"recordId":%d,"subjectId":644},{"answerId":1156,"parentId":636,"recordId":%d,"subjectId":687},{"answerId":1145,"parentId":636,"recordId":%d,"subjectId":682},{"answerId":1151,"parentId":636,"recordId":%d,"subjectId":685},{"answerId":1157,"parentId":636,"recordId":%d,"subjectId":688},{"answerId":1146,"parentId":636,"recordId":%d,"subjectId":683},{"answerId":1153,"parentId":636,"recordId":%d,"subjectId":686},{"answerId":1149,"parentId":636,"recordId":%d,"subjectId":684},{"answerId":1167,"parentId":637,"recordId":%d,"subjectId":697},{"answerId":1162,"parentId":637,"recordId":%d,"subjectId":695},{"answerId":1169,"parentId":637,"recordId":%d,"subjectId":698},{"answerId":1165,"parentId":637,"recordId":%d,"subjectId":696},{"answerId":1160,"parentId":637,"recordId":%d,"subjectId":694}]'
                       % (
                           id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                           id,
                           id, id, id, id, id, id),
            'agencyId': self.agency_id[0],
            "products": self.products
        }
        print(param)
        response = self.agencies.save_env_answer(case_name="上传环境评估结果", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)

    @Login.agencies_app_login("13733263135", "123456")
    def test_download_subject(self):
        """【适老化--app】：适老化题目下载"""
        param = {
            "schemeId": 104
        }
        response = self.agencies.download_subject(case_name="适老化题目下载", data=param)
        print(response.json())
        print(len(response.json()["data"][0]["productList"]))
        data = {
            "productId": response.json()["data"][0]["productList"][0]["productId"],
            "selectedCounts": 1,
            "typeId": response.json()["data"][0]["productList"][0]["typeId"],
            "price": response.json()["data"][0]["productList"][0]["price"]
        }
        self.products.append(data)
        print(self.products)


if __name__ == '__main__':
    unittest.main()