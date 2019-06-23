# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_house_flow.py
@time: 2019/6/13 11:26
@desc：适老化流程脚本
"""
import sys, os
sys.path.append(os.path.dirname(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]))
import unittest, random
from conf import Login
from tools.logger import Logger
from conf.IDCard import IDCard
from source.agencies import Agencies
from source.construction import Construction
from source.govern_house import GovernHouse
from tools.read_yaml import ReadYaml


class TestHouseFlow(unittest.TestCase):
    read_yaml = ReadYaml("default.yaml")
    govern_account = read_yaml.get_account("govern")
    pass_word = read_yaml.get_password("govern")
    community = read_yaml.get_district("community")
    default_pwd = "123456"
    agency_phone = "1353326" + str(random.randint(1000, 9999))  # 评估机构 登录账号
    agency_emp_phone = "1373326" + str(random.randint(1000, 9999))  # 评估员账号
    construction_phone = "1363326" + str(random.randint(1000, 9999))  # 施工单位 登录账号
    con_emp_account = "1383326" + str(random.randint(1000, 9999))  # 施工员账号

    @classmethod
    def setUpClass(cls):
        print("============================ 适老化 STA============================")
        Logger().info("------------------------ 适老化 STA ------------------------")
        cls.id_card = IDCard().idCard(76, 1)
        cls.house = GovernHouse()       # 适老化政府端
        cls.agencies = Agencies()       # 评估机构端
        cls.construction = Construction()   # 施工企业端

        cls.agency_name = "api评估机构" + str(random.randint(1000, 9999))
        # cls.agency_phone = "1353326" + str(random.randint(1000, 9999))  # 评估机构 登录账号
        # cls.agency_emp_phone = "1373326" + str(random.randint(1000, 9999))  # 评估员账号

        cls.construction_name = "api施工单位" + str(random.randint(1000, 9999))
        # cls.construction_phone = "1363326" + str(random.randint(1000, 9999))  # 施工单位 登录账号
        # cls.con_emp_account = "1383326" + str(random.randint(1000, 9999))   # 施工员账号

        cls.product_name = "api产品" + str(random.randint(1000, 9999))
        cls.person_name = "api申请" + str(random.randint(1000, 9999))

        cls.con_emp_name = "api施员工" + str(random.randint(1000, 9999))

        cls.agency_id = []  # 评估机构ID
        cls.construction_id = []  # 施工单位ID
        cls.product_id = []  # 产品ID

        cls.apply_id = []  # 改造申请ID
        cls.verify_id = []  # 改造单ID
        cls.order_id = []  # 订单ID

        cls.agency_emp_id = []  # 评估员ID
        cls.person_record_id = []  # 人员评估记录ID
        cls.env_record_id = []  # 环境评估记录ID

        cls.con_emp_id = []  # 施工单位员工ID
        cls.products = []  # 上传环境评估记录时，上传的产品
        cls.scheme = []  # 产品方案

    @Login.govern_login(govern_account, pass_word)
    def test_001_add_assess_agency(self):
        """1.政府端：添加评估机构"""
        print("评估机构：" + self.agency_name)
        param = {
            "licencesNum": self.agency_phone,
            "password": "123456",
            "loginPhone": self.agency_phone,
            "legal": "测试",
            "contactName": "测试",
            "serviceArea": self.community,
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
        response = self.house.add_assess_agency(case_name="政府端：添加评估机构", param=param)
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
        response = self.house.get_assessment_agencies(case_name="政府端：根据评估名称，获取评估机构ID", param=param)
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
            "serviceAreaList": [{'value': 'shequ', 'id': '5101090201'}]
            }
        response = self.house.add_construction_business(case_name="政府端：添加施工单位", param=param)
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
        print(self.construction_name)
        response = self.house.get_construction_business_list(case_name="政府端：根据施工单位名称，获取施工单位ID", param=param)
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
        response = self.house.add_product(case_name="政府端：添加产品", param=param)
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
        response = self.house.get_product_list(case_name="政府端：根据产品名称获取产品ID", param=param)
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
        response = self.house.get_user_by_id_card(case_name="政府端：根据身份证查询人员信息", param=param)
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
            "addressId": self.community,
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
        response = self.house.add_transform_apply(param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])

    def test_008_get_transform_apply_list(self):
        """8.政府端：添加改造申请"""
        param = {
            "idCard": self.id_card,
            "addressId": self.community,
            "pageNow": 1
        }
        response = self.house.get_transform_apply_list(case_name="政府端：添加改造申请", data=param)
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
            "addressId": self.community
        }
        response = self.house.get_transform_apply_list(case_name="政府端：根据身份证号，查询审核ID", data=param)
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
        response = self.house.verify_transform(case_name="政府端：根据审核ID，审核通过", data=param)
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
        response = self.house.business_apply(case_name="政府端：添加改造评估申请", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("申请成功", response.json()["message"])

    @Login.agencies_login(agency_phone, default_pwd)
    def test_012_agency_user_edit_submit(self):
        """13.评估端：添加员工账号"""
        param = {
            "name": "api评估员",
            "sex": 1,
            "idCardNum": "510104199008079959",
            "position": "测试api",
            "account": self.agency_emp_phone
        }
        response = self.agencies.agency_user_edit_submit(case_name="评估端：添加员工账号", data=param)
        print(response.json())

        # 根据账号获取员工ID
        data = {
            "account": self.agency_emp_phone
        }
        response = self.agencies.agency_user_list_data(data=data)
        print(response.json())
        self.agency_emp_id.append(response.json()["data"][0]["id"])
        print("评估员工emp_id: %d" % self.agency_emp_id[0])

    @Login.agencies_app_login(agency_emp_phone, default_pwd)
    def test_013_get_tasks(self):
        """13.评估app：领取任务"""
        param = {
            "orderId": self.verify_id[0],
            "assessmentUserId": self.agency_emp_id[0]
        }
        print(param)
        response = self.agencies.get_tasks(case_name="评估app：领取任务", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取任务成功", response.json()["detail"])

    def test_014_list_own_tasks(self):
        """14.评估app：获取record_id"""
        param = {
            "assessmentUserId": self.agency_emp_id[0]
        }
        response = self.agencies.list_own_tasks(case_name="评估app：获取record_id", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.person_record_id.append(response.json()["data"][0]["personRecordId"])
        self.env_record_id.append(response.json()["data"][0]["envRecordId"])
        print("人员评估申请记录person_record_id：%d" % self.person_record_id[0])
        print("环境评估申请记录env_record_id：%d" % self.env_record_id[0])

    def test_015_download_subject(self):
        """15.评估app：下载题目，获取产品信息"""
        param = {
            "schemeId": 104
        }
        response = self.agencies.download_subject(case_name="评估app：下载题目，获取产品信息", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        print(len(response.json()["data"][0]["productList"]))
        data = {
            "productId": response.json()["data"][0]["productList"][0]["productId"],
            "selectedCounts": 1,
            "typeId": response.json()["data"][0]["productList"][0]["typeId"],
            "price": response.json()["data"][0]["productList"][0]["price"]
        }
        self.products.append(data)

    def test_016_save_answer_person(self):
        """16.评估app：人员评估上传评估结果"""
        id = self.person_record_id[0]
        param = {
            'name': 'assess_token',
            'answer': '[{"answerId":1,"parentId":1,"recordId":%d,"subjectId":8},{"answerId":8,"parentId":1,"recordId":%d,"subjectId":11},{"answerId":10,"parentId":1,"recordId":%d,"subjectId":20},{"answerId":12,"parentId":1,"recordId":%d,"subjectId":21},{"answerId":16,"parentId":1,"recordId":%d,"subjectId":22},{"answerId":18,"parentId":1,"recordId":%d,"subjectId":23},{"answerId":22,"parentId":1,"recordId":%d,"subjectId":24},{"answerId":24,"parentId":1,"recordId":%d,"subjectId":25},{"answerId":31,"parentId":1,"recordId":%d,"subjectId":27},{"answerId":36,"parentId":1,"recordId":%d,"subjectId":28},{"answerId":38,"parentId":2,"recordId":%d,"subjectId":32},{"answerId":41,"parentId":2,"recordId":%d,"subjectId":33},{"answerId":44,"parentId":2,"recordId":%d,"subjectId":34},{"answerId":48,"parentId":3,"recordId":%d,"subjectId":39},{"answerId":52,"parentId":3,"recordId":%d,"subjectId":40},{"answerId":57,"parentId":3,"recordId":%d,"subjectId":41},{"answerId":62,"parentId":3,"recordId":%d,"subjectId":42},{"answerId":66,"parentId":4,"recordId":%d,"subjectId":48},{"answerId":70,"parentId":4,"recordId":%d,"subjectId":49},{"answerId":75,"parentId":4,"recordId":%d,"subjectId":50},{"answerId":80,"parentId":4,"recordId":%d,"subjectId":51},{"answerId":85,"parentId":4,"recordId":%d,"subjectId":52},{"answerId":627,"parentId":391,"recordId":%d,"subjectId":393},{"answerId":628,"parentId":391,"recordId":%d,"subjectId":394},{"answerId":625,"parentId":391,"recordId":%d,"subjectId":395}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id),
            'agencyId': self.agency_id[0],
            "conclusion": ""
        }
        response = self.agencies.save_answer(case_name="评估app：人员评估上传评估结果", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])

    def test_017_save_answer_env(self):
        """17.评估app：环境评估上传评估结果"""
        id = self.env_record_id[0]
        param = {
            'recordId': id,
            "answers": '[{"answerId":1129,"parentId":635,"recordId":%d,"subjectId":668},{"answerId":1140,"parentId":635,"recordId":%d,"subjectId":673},{"answerId":1135,"parentId":635,"recordId":%d,"subjectId":671},{"answerId":1124,"parentId":635,"recordId":%d,"subjectId":666},{"answerId":1119,"parentId":635,"recordId":%d,"subjectId":664},{"answerId":1130,"parentId":635,"recordId":%d,"subjectId":669},{"answerId":1141,"parentId":635,"recordId":%d,"subjectId":674},{"answerId":1126,"parentId":635,"recordId":%d,"subjectId":667},{"answerId":1137,"parentId":635,"recordId":%d,"subjectId":672},{"answerId":1121,"parentId":635,"recordId":%d,"subjectId":665},{"answerId":1133,"parentId":635,"recordId":%d,"subjectId":670},{"answerId":1118,"parentId":634,"recordId":%d,"subjectId":652},{"answerId":1113,"parentId":634,"recordId":%d,"subjectId":650},{"answerId":1115,"parentId":634,"recordId":%d,"subjectId":651},{"answerId":1098,"parentId":633,"recordId":%d,"subjectId":642},{"answerId":1105,"parentId":633,"recordId":%d,"subjectId":645},{"answerId":1106,"parentId":633,"recordId":%d,"subjectId":646},{"answerId":1109,"parentId":633,"recordId":%d,"subjectId":644},{"answerId":1156,"parentId":636,"recordId":%d,"subjectId":687},{"answerId":1145,"parentId":636,"recordId":%d,"subjectId":682},{"answerId":1151,"parentId":636,"recordId":%d,"subjectId":685},{"answerId":1157,"parentId":636,"recordId":%d,"subjectId":688},{"answerId":1146,"parentId":636,"recordId":%d,"subjectId":683},{"answerId":1153,"parentId":636,"recordId":%d,"subjectId":686},{"answerId":1149,"parentId":636,"recordId":%d,"subjectId":684},{"answerId":1167,"parentId":637,"recordId":%d,"subjectId":697},{"answerId":1162,"parentId":637,"recordId":%d,"subjectId":695},{"answerId":1169,"parentId":637,"recordId":%d,"subjectId":698},{"answerId":1165,"parentId":637,"recordId":%d,"subjectId":696},{"answerId":1160,"parentId":637,"recordId":%d,"subjectId":694}]'
                       % (
                       id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                       id, id, id, id, id, id),
            "products": str(self.products)

        }
        print(param)
        response = self.agencies.save_env_answer(case_name="评估app：环境评估上传评估结果", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])

    def test_018_save_person_products(self):
        """18.评估app：保存人员评估结果选择的产品关系"""
        param = {
            "recordId": self.person_record_id[0],
            "json": ""
        }
        response = self.agencies.save_person_products(case_name="评估app：保存人员评估结果选择的产品关系", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])

    @Login.govern_login(govern_account, pass_word)
    def test_019_constructor_apply(self):
        """19.政府端：施工派单"""
        param = {
            "constructionId": self.construction_id[0],
            "id": self.verify_id[0]
        }
        response = self.house.constructor_apply(case_name="政府端：施工派单", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("派单成功", response.json()["message"])

    @Login.construction_login(construction_phone, default_pwd)
    def test_020_add_employee(self):
        """20.施工单位添加员工"""
        param = {
            "account": self.con_emp_account,
            "addressDetail": "api测试详细地址",
            "annex": [{
                "name": "1",
                "url": "1.txt"
            }, {
                "name": "2",
                "url": "2.png"
            }],
            "idCard": self.id_card,
            "name": self.con_emp_name,
            "password": "123456",
            "phone": self.con_emp_account,
            "post": 1
        }
        response = self.construction.add_employee(case_name="施工单位添加员工", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("添加成功", response.json()["message"])

    def test_021_employee_list(self):
        """21.施工单位：获取员工ID"""
        param = {
            "name": self.con_emp_name,
            "pageNow": 1
        }
        response = self.construction.employee_list(case_name="施工单位：获取员工ID", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])
        self.con_emp_id.append(response.json()["data"]["records"][0]["id"])
        print("施工员工ID：%s" % self.con_emp_id[0])

    @Login.construction_app_login(con_emp_account, default_pwd)
    def test_022_get_task(self):
        """22.施工app：获取任务"""
        param = {
            "recordId": self.verify_id[0]
        }
        print(param)
        response = self.construction.get_task(case_name="施工app：获取任务D", param=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("领取成功", response.json()["message"])

    def test_023_construction_details(self):
        """23.施工app：查询任务详情"""
        param = {
            "id": self.verify_id
        }
        response = self.construction.construction_details(case_name="施工app：查询任务详情", param=param)
        print(response.json())
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["id"])
        self.scheme.append(response.json()["data"]["transformSchemesType"][0]["transformSchemes"][0]["productImg"])

    def test_024_commit_scheme(self):
        """24.施工app：提交施工产品方案"""
        param = {
            "recordId": self.verify_id,
            "scheme": str({
                "id": self.scheme[0],
                "transformBefore": self.scheme[1],
                "transformMiddle": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png",
                "transformAfter": "http://file.chinaylzl.com/test/userHead/2018/11/16/38acfc8085c249628beffed54bccb2c7.png",
                "remark": "api施工小程序产品备注"
            })
        }
        print(param)
        response = self.construction.commit_scheme(case_name="施工app：提交施工产品方案", data=param)
        print(response.json())

    @Login.govern_login(govern_account, pass_word)
    def test_025_govern_get_project_inspection_list(self):
        """25.政府端：项目验收列表分页查询"""
        param = {
            "pageNow": 1
        }
        response = self.house.get_project_inspection_list(case_name="政府端：项目验收列表分页查询", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_026_govern_check_transform_scheme(self):
        """26.政府端：验收改造方案"""
        param = {
            "schemeId": self.scheme[0],
            "recordId": self.verify_id,
            "qualified": 1
        }
        response = self.house.check_transform_scheme(case_name="政府端：验收改造方案", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("验收成功", response.json()["message"])

    def test_027_get_transform_settlement_list(self):
        """27.政府端：项目结算列表分页查询"""
        param = {
            "pageNow": 1
        }
        response = self.house.get_transform_settlement_list(case_name="政府端：项目结算列表分页查询", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("操作成功", response.json()["message"])

    def test_028_settlement(self):
        """28.政府端：结算项目"""
        param = {
            "id": self.verify_id
        }
        response = self.house.settlement(case_name="政府端：结算项目", data=param)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()["status"])
        self.assertEqual("结算成功", response.json()["message"])

    def test_029_info(self):
        print("评估机构名称：%s ；账号: %s ；ID：%d" % (self.agency_name, self.agency_phone, self.agency_id[0]))
        print("施工单位名称：%s ；账号: %s ；ID：%d" % (self.construction_name, self.construction_phone, self.construction_id[0]))
        print("产品名称：%s ；ID：%d" % (self.product_name, self.product_id[0]))
        print("人员名称：%s ；id_card: %s ；ID：%d" % (self.person_name, self.id_card, self.apply_id[0]))
        print("改造申请ID：%s ；改造审核ID: %s " % (self.apply_id[0], self.verify_id[0]))
        print("评估员账号：%s ；ID: %s " % (self.agency_emp_phone, self.agency_emp_id[0]))
        print("人员记录person_record_id：%d ; 环境记录env_record_id：%d" % (self.person_record_id[0], self.env_record_id[0]))

    @classmethod
    def tearDownClass(cls):
        Logger().info("------------------------ 适老化 END ------------------------")
        print("============================ 适老化 END============================")


if __name__ == '__main__':
    unittest.main()