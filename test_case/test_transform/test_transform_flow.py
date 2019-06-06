# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_transform_flow.py
@time: 2019/6/5 19:30
@desc：适老化流程
        1.添加评估机构 2、添加施工单位 3、添加产品 4、申请 5、评估
"""
import unittest
import random
from conf import Login
from conf.IDCard import IDCard
from source.Transform.transform import Transform
from source.Transform.transform_app import TransformApp
from source.Transform.construcotr_app import ConstructionApp


class TestTransformFlow(unittest.TestCase):

    transform = Transform()
    transform_app = TransformApp()
    construction_app = ConstructionApp()
    id_card = IDCard().idCard(66, 1)

    agency_id = []  # 评估机构ID
    agency_name = "api评估机构" + str(random.randint(1000, 9999))
    agency_phone = "1353326" + str(random.randint(1000, 9999))    # 评估机构 登录账号
    construction_id = []    # 施工单位ID
    construction_name = "api施工" + str(random.randint(1000, 9999))
    construction_phone = "1363326" + str(random.randint(1000, 9999))  # 施工单位 登录账号
    product_id = []     # 产品ID
    product_name = "api产品" + str(random.randint(0, 100))
    person_name = "api申请" + str(random.randint(1000, 9999))
    emp_phone = "1373326" + str(random.randint(1000, 9999))
    con_emp_account = "1525621" + str(random.randint(1000, 9999))
    con_emp_name = "api施员工" + str(random.randint(1000, 9999))

    apply_id = []   # 改造申请ID
    verify_id = []  # 改造单ID
    order_id = []   # 订单ID
    emp_id = []     # 评估员ID
    person_record_id = []  # 人员评估记录ID
    env_record_id = []  # 环境评估记录ID
    con_emp_id = []

    @Login.get_account("18981967059", "123qwe")
    def test_001_add_assess_agency(self):
        """1.政府端：添加评估机构"""
        print("评估机构：" + self.agency_name)
        param = {
            "licencesNum": self.agency_phone,
            "password": "123456",
            "loginPhone": self.agency_phone,
            "legal": "测试",
            "contactName": "测试",
            "serviceArea": "51010906",
            "agencyName": self.agency_name,
            "contactMobile": "15285256626",
            "address": "测试",
            "email": "15285256626@123.com",
            "addExist": "",
            "licencesImg": "",
            "agencyCertificate": "",
            "agencyPhoto": "",
            "idcardImgZ": "",
            "idcardImgF": ""
        }
        response = self.transform.add_assess_agency(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("评估添加成功", response.json()["message"])

    def test_002_get_assessment_agencies(self):
        """2.政府端：根据评估名称，获取评估机构ID"""
        param = {
            "agencyName": self.agency_name,
            "pageNow": 1
        }
        response = self.transform.get_assessment_agencies(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.agency_id.append(response.json()["data"]["records"][0]["agencyId"])
        print("评估机构agency_id：%d" % self.agency_id[0])

    def test_003_add_construction_business(self):
        """3.政府端：添加施工单位"""
        print(self.construction_phone)
        param = {
            "account": self.construction_phone,
            "address": "办公地址",
            "annexList": [{
                "name": "1",
                "url": "1.txt"
            },{
                "name": "2",
                "url": "2.png"
            }],
            "businessLicense": self.construction_phone,
            "certificateList": [{
                "name": "1",
                "url": "1.txt"
            }, {
                "name": "2",
                "url": "2.png"
            }],
            "constructorCount": 100,
            "email": "string@163.com",
            "employeeCount": 30,
            "enable": 1,
            "legalPerson": "法人代表",
            "name": self.construction_name,
            "password": "123456",
            "personInCharge": "测试",
            "personPhone": self.construction_phone,
            "serviceArea": ["510109"]
            }
        response = self.transform.add_construction_business(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual("添加成功", response.json()["message"])
        self.assertEqual(0, response.json()["status"])

    def test_004_get_construction_business_list(self):
        """4.政府端：根据施工单位名称，获取施工单位ID"""
        param = {
            "name": self.construction_name,
            "pageNow": 1,
            "enable": 1
        }
        response = self.transform.get_construction_business_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.construction_id.append(response.json()["data"]["records"][0]["id"])
        print("施工单位construction_ID：%d" % self.construction_id[0])

    def test_005_add_product(self):
        """5.政府端：添加产品"""
        param = {
            "name": self.product_name,
            "functionParams": "功能参数",
            "price": 1000,
            "remark": "产品备注",
            "typeIds": [1, 2, 3, 4, 5, 6, 7, 8],
            "imgPath": [{
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }, {
                "name": "38acfc8085c249628beffed54bccb2c7",
                "url": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png"
            }],
            }
        response = self.transform.add_product(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_006_get_product_list(self):
        """6.政府端：根据产品名称获取产品ID"""
        param = {
            "enable": 1,
            "pageNow": 1,
            "name": self.product_name
        }
        response = self.transform.get_product_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.product_id.append(response.json()["data"]["records"][0]["id"])
        print("产品product_id：%d"% self.product_id[0])

    def test_007_get_user_by_id_card(self):
        """7.政府端：根据身份证查询人员信息"""
        param = {
            "idCard": self.id_card
        }
        response = self.transform.get_user_by_id_card(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

        # 政府端：添加改造申请
        print("申请人name:" + self.person_name)
        param = {
            "idCard": self.id_card,
            "userName": self.person_name,
            "phone": "13999999999",
            "addressId": "51010915",
            "addressDetail": "测试地址",
            "transformContents": "测试内容",
            "transformCause": "测试",
            "state": 4,
            "emergencyContact": [{
                "name": "测试",
                "ralative": 1,
                "phone": "13777777777"
            }],
            "certificates": [],
            "annex": []
        }
        response = self.transform.add_transform_apply(param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])

    def test_008_get_transform_apply_list(self):
        """8.政府端：添加改造申请"""
        param = {
            "idCard": self.id_card,
            "addressId": "510109",
            "pageNow": 1
        }
        response = self.transform.get_transform_apply_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.apply_id.append(response.json()["data"]["records"][0]["id"])
        print("改造申请apply_id：%d" % self.apply_id[0])

    def test_009_get_transform_verify_list(self):
        """9.政府端：根据身份证号，查询审核ID"""
        param = {
            "idCard": self.id_card,
            "addressId": "510109"
        }
        response = self.transform.get_transform_apply_list(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.verify_id.append(response.json()["data"]["records"][0]["id"])
        print("审核verify_id：%d" % self.verify_id[0])

    def test_010_verify_transform(self):
        """10.政府端：根据审核ID，审核通过"""
        param = {
            "id": self.verify_id[0],
            "verifyState": 1
        }
        response = self.transform.verify_transform(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("审核成功", response.json()["message"])

    def test_011_business_apply(self):
        """11.政府端：添加改造评估申请"""
        param = {
            "agencyId": self.agency_id,
            "agencyName": self.agency_name,
            "id": self.verify_id[0]
        }
        response = self.transform.business_apply(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("申请成功", response.json()["message"])

    # 15285256626 agency_phone
    @Login.get_agencies_account(agency_phone, "123456")
    def test_012_agency_user_edit_submit(self):
        """13.评估端：添加员工账号"""
        param = {
            "name": "api评估员",
            "sex": 1,
            "idCardNum": "510104199008079959",
            "position": "测试api",
            "account": self.emp_phone
        }
        response = self.transform_app.agency_user_edit_submit(data=param)
        print(response.json())

        # 根据账号获取员工ID
        data = {
            "account": self.emp_phone
        }
        response = self.transform_app.agency_user_list_data(data=data)
        print(response.json())
        self.emp_id.append(response.json()["data"][0]["id"])
        print("员工emp_id: %d" % self.emp_id[0])

    @Login.get_agencies_app_account(emp_phone, "123456")
    def test_013_get_tasks(self):
        """13.评估app：领取任务"""
        param = {
            "orderId": self.verify_id[0],
            "assessmentUserId": self.emp_id[0]
        }
        print(param)
        response = self.transform_app.get_tasks(data=param)
        print(response.json())

    def test_014_list_own_tasks(self):
        """14.评估app：获取record_id"""
        param = {
            "assessmentUserId": self.emp_id[0]
        }
        response = self.transform_app.list_own_tasks(data=param)
        print(response.json())
        self.person_record_id.append(response.json()["data"][0]["personRecordId"])
        self.env_record_id.append(response.json()["data"][0]["envRecordId"])
        print("人员评估申请记录person_record_id：%d" % self.person_record_id[0])
        print("环境评估申请记录env_record_id：%d" % self.env_record_id[0])

    def test_015_save_answer_person(self):
        """15.评估app：人员评估上传评估结果"""
        id = self.person_record_id[0]
        param = {
            'name': 'assess_token',
            'answer': '[{"answerId":1,"parentId":1,"recordId":%d,"subjectId":8},{"answerId":8,"parentId":1,"recordId":%d,"subjectId":11},{"answerId":10,"parentId":1,"recordId":%d,"subjectId":20},{"answerId":12,"parentId":1,"recordId":%d,"subjectId":21},{"answerId":16,"parentId":1,"recordId":%d,"subjectId":22},{"answerId":18,"parentId":1,"recordId":%d,"subjectId":23},{"answerId":22,"parentId":1,"recordId":%d,"subjectId":24},{"answerId":24,"parentId":1,"recordId":%d,"subjectId":25},{"answerId":31,"parentId":1,"recordId":%d,"subjectId":27},{"answerId":36,"parentId":1,"recordId":%d,"subjectId":28},{"answerId":38,"parentId":2,"recordId":%d,"subjectId":32},{"answerId":41,"parentId":2,"recordId":%d,"subjectId":33},{"answerId":44,"parentId":2,"recordId":%d,"subjectId":34},{"answerId":48,"parentId":3,"recordId":%d,"subjectId":39},{"answerId":52,"parentId":3,"recordId":%d,"subjectId":40},{"answerId":57,"parentId":3,"recordId":%d,"subjectId":41},{"answerId":62,"parentId":3,"recordId":%d,"subjectId":42},{"answerId":66,"parentId":4,"recordId":%d,"subjectId":48},{"answerId":70,"parentId":4,"recordId":%d,"subjectId":49},{"answerId":75,"parentId":4,"recordId":%d,"subjectId":50},{"answerId":80,"parentId":4,"recordId":%d,"subjectId":51},{"answerId":85,"parentId":4,"recordId":%d,"subjectId":52},{"answerId":627,"parentId":391,"recordId":%d,"subjectId":393},{"answerId":628,"parentId":391,"recordId":%d,"subjectId":394},{"answerId":625,"parentId":391,"recordId":%d,"subjectId":395}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id),
            'agencyId': self.agency_id[0],
            "conclusion": ""
        }
        response = self.transform_app.save_answer(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)

    def test_016_save_answer_env(self):
        """16.评估app：环境评估上传评估结果"""
        id = self.env_record_id[0]
        param = {
            'name': 'assess_token',
            "answer": '[{"answerId":1129,"parentId":635,"recordId":%d,"subjectId":668},{"answerId":1140,"parentId":635,"recordId":%d,"subjectId":673},{"answerId":1135,"parentId":635,"recordId":%d,"subjectId":671},{"answerId":1124,"parentId":635,"recordId":%d,"subjectId":666},{"answerId":1119,"parentId":635,"recordId":%d,"subjectId":664},{"answerId":1130,"parentId":635,"recordId":%d,"subjectId":669},{"answerId":1141,"parentId":635,"recordId":%d,"subjectId":674},{"answerId":1126,"parentId":635,"recordId":%d,"subjectId":667},{"answerId":1137,"parentId":635,"recordId":%d,"subjectId":672},{"answerId":1121,"parentId":635,"recordId":%d,"subjectId":665},{"answerId":1133,"parentId":635,"recordId":%d,"subjectId":670},{"answerId":1118,"parentId":634,"recordId":%d,"subjectId":652},{"answerId":1113,"parentId":634,"recordId":%d,"subjectId":650},{"answerId":1115,"parentId":634,"recordId":%d,"subjectId":651},{"answerId":1098,"parentId":633,"recordId":%d,"subjectId":642},{"answerId":1105,"parentId":633,"recordId":%d,"subjectId":645},{"answerId":1106,"parentId":633,"recordId":%d,"subjectId":646},{"answerId":1109,"parentId":633,"recordId":%d,"subjectId":644},{"answerId":1156,"parentId":636,"recordId":%d,"subjectId":687},{"answerId":1145,"parentId":636,"recordId":%d,"subjectId":682},{"answerId":1151,"parentId":636,"recordId":%d,"subjectId":685},{"answerId":1157,"parentId":636,"recordId":%d,"subjectId":688},{"answerId":1146,"parentId":636,"recordId":%d,"subjectId":683},{"answerId":1153,"parentId":636,"recordId":%d,"subjectId":686},{"answerId":1149,"parentId":636,"recordId":%d,"subjectId":684},{"answerId":1167,"parentId":637,"recordId":%d,"subjectId":697},{"answerId":1162,"parentId":637,"recordId":%d,"subjectId":695},{"answerId":1169,"parentId":637,"recordId":%d,"subjectId":698},{"answerId":1165,"parentId":637,"recordId":%d,"subjectId":696},{"answerId":1160,"parentId":637,"recordId":%d,"subjectId":694}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id),
            'agencyId': self.agency_id[0],
            "conclusion": ""
        }
        response = self.transform_app.save_answer(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)

    def test_017_save_person_products(self):
        """17.评估app：保存人员评估结果选择的产品关系"""
        param = {
            "recordId": self.person_record_id[0],
            "json": ""
        }
        response = self.transform_app.save_person_products(data=param)
        print(response.json())

    @Login.get_account("18981967059", "123qwe")
    def test_018_constructor_apply(self):
        """18.政府端：施工派单"""
        param = {
            "constructionId": self.construction_id[0],
            "id": self.verify_id[0]
        }
        response = self.transform.constructor_apply(data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("派单成功", response.json()["message"])

    @Login.get_construction_web(construction_phone, "123456")
    def test_019_add_employee(self):
        """19.施工单位添加员工"""
        param = {
            "account": self.con_emp_account,
            "addressDetail": "api测试详细地址",
            "annex": "apiannex",
            "bid": 44,
            "idCard": self.id_card,
            "name": self.con_emp_name,
            "password": "123456",
            "phone": self.con_emp_account,
            "post": 1
        }
        response = self.construction_app.add_employee(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_020_employee_list(self):
        """20.施工单位：获取员工ID"""
        param = {
            "name": self.con_emp_name,
            "pageNow": 1
        }
        response = self.construction_app.employee_list(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        print(len(response.json()["data"]["records"]))
        self.con_emp_id.append(response.json()["data"]["records"][0]["id"])
        print(self.con_emp_id[0])

    @Login.get_construction_app(con_emp_account, "123456")
    def test_021_get_task(self):
        """21.施工app：获取任务"""
        param = {
            "eId": self.con_emp_id[0],
            "recordId": self.verify_id[0]
        }
        response = self.construction_app.get_task(param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取成功", response.json()["message"])


if __name__ == '__main__':
    unittest.main()