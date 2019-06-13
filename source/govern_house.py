# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: govern_house.py
@time: 2019/6/12 21:02
@desc：政府端--适老化改造
"""
from conf import DEFAULT
from tools.read_yaml import ReadYaml
from tools.http_request import Request


class GovernHouse:
    request = Request()
    headers = DEFAULT.HEADERS
    read_default = ReadYaml("default.yaml")
    govern = read_default.get_host("govern") + "/gov-house"
    # govern = "http://192.168.100.151:8084"
    house = ReadYaml("house_api.yaml")

    # 【产品】

    def add_product(self, param):
        """【政府端--适老化】：添加产品"""
        _URL = self.govern + self.house.house_govern("product", "addProduct")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def get_product_list(self, param):
        """【政府端--适老化】：分页查询产品列表"""
        _URL = self.govern + self.house.house_govern("product", "getProductList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_product_type_list(self):
        """【政府端--适老化】：查询产品类型list"""
        _URL = self.govern + self.house.house_govern("product", "getProductTypeList")
        response = self.request.get_request(_url=_URL, _headers=self.headers)
        return response

    def stop_start_product(self, param):
        """【政府端--适老化】：产品停启"""
        _URL = self.govern + self.house.house_govern("product", "stopStartProduct")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def update_product(self, param):
        """【政府端--适老化】：编辑产品信息"""
        _URL = self.govern + self.house.house_govern("product", "updateProduct")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def get_unit_data(self):
        """【政府端--适老化】：获取单位数据"""
        _URL = self.govern + self.house.house_govern("product", "getUnitData")
        response = self.request.get_request(_url=_URL, _headers=self.headers)
        return response

    def get_product_detail(self, param):
        """【政府端--适老化】：查看产品详情"""
        _URL = self.govern + self.house.house_govern("product", "getProductDetail")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response


# 【施工单位】

    def add_construction_business(self, param):
        """【政府端--适老化】：添加施工单位"""
        _URL = self.govern + self.house.house_govern("construction", "addConstructionBusiness")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def get_construction_business_list(self, param):
        """【政府端--适老化】：分页查询施工单位列表"""
        _URL = self.govern + self.house.house_govern("construction", "getConstructionBusinessList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def edit_construction_business(self, param):
        """【政府端--适老化】：编辑施工单位信息"""
        _URL = self.govern + self.house.house_govern("construction", "editConstructionBusiness")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def get_business_detail(self, param):
        """【政府端--适老化】：获取施工单位信息"""
        _URL = self.govern + self.house.house_govern("construction", "getBusinessDetail")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def record_construction_list(self, param):
        """【政府端--适老化】：施工记录"""
        _URL = self.govern + self.house.house_govern("construction", "recordConstructionList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_employee_list(self, param):
        """【政府端--适老化】：通讯名单"""
        _URL = self.govern + self.house.house_govern("construction", "getEmployeeList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def stop_or_start_constructor(self, param):
        """【政府端--适老化】：停启施工单位"""
        _URL = self.govern + self.house.house_govern("construction", "stopOrStartConstructor")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def services_list(self, param):
        """【政府端--适老化】：结算服务"""
        _URL = self.govern + self.house.house_govern("construction", "servicesList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    # 【评估机构】

    def add_assess_agency(self, param):
        """【政府端--评估机构】：添加评估机构"""
        _URL = self.govern + self.house.house_govern("agency", "addAssessAgency")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def assessment_record(self, param):
        """【政府端--评估机构】：机构评估记录"""
        _URL = self.govern + self.house.house_govern("agency", "assessmentRecord")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def edit_assess_agency(self, param):
        """【政府端--评估机构】：编辑获取评估机构信息"""
        _URL = self.govern + self.house.house_govern("agency", "editAssessAgencys")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def get_agency_detail(self, param):
        """【政府端--评估机构】：获取评估机构基本信息"""
        _URL = self.govern + self.house.house_govern("agency", "getAgencyDetail")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_agency_employee_list(self, param):
        """【政府端--评估机构】：通讯名单列表"""
        _URL = self.govern + self.house.house_govern("agency", "getEmployeeList")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_assessment_agencies(self, param):
        """【政府端--评估机构】：分页查询评估机构列表"""
        _URL = self.govern + self.house.house_govern("agency", "getAssessmentAgencies")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_assessment_scheme(self, param):
        """【政府端--评估机构】：查询方案列表"""
        _URL = self.govern + self.house.house_govern("agency", "getAssessmentScheme")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def get_settle_service(self, param):
        """【政府端--评估机构】：结算服务列表"""
        _URL = self.govern + self.house.house_govern("agency", "getSettleService")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def query_agencies_list(self):
        """【政府端--评估机构】：获取选择评估机构列表"""
        _URL = self.govern + self.house.house_govern("agency", "queryAgenciesList")
        response = self.request.get_request(_url=_URL, _headers=self.headers)
        return response

    def save_assessment_agency(self, param):
        """【政府端--评估机构】：保存编辑后评估机构信息"""
        _URL = self.govern + self.house.house_govern("agency", "saveAssessmentAgency")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def settle_agency(self, param):
        """【政府端--评估机构】：结算服务列表"""
        _URL = self.govern + self.house.house_govern("agency", "settleAgency")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def start_or_stop(self, param):
        """【政府端--评估机构】：机构评估停启用"""
        _URL = self.govern + self.house.house_govern("agency", "startOrStop")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

        # 【申请】

    def get_user_by_id_card(self, param):
        """【政府端 - -适老化】：根据身份证查询人员信息"""
        _URL = self.govern + self.house.house_govern("apply", "getUserByIdCard")
        response = self.request.get_request(_url=_URL, _data=param, _headers=self.headers)
        return response

    def add_transform_apply(self, param):
        """【政府端--适老化】：添加改造申请"""
        _URL = self.govern + self.house.house_govern("apply", "addTransformApply")
        response = self.request.post_request_json(_url=_URL, _json=param, _headers=self.headers)
        return response

    def apply_transform(self, data):
        """【政府端--适老化】：改造申请"""
        _URL = self.govern + self.house.house_govern("apply", "applyTransform")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def edit_transform(self, json):
        """【政府端--适老化】：编辑改造单"""
        _URL = self.govern + self.house.house_govern("apply", "editTransform")
        response = self.request.post_request_json(_url=_URL, _json=json, _headers=self.headers)
        return response

    def get_relation_data(self):
        """【政府端--适老化】：获取人员关系数据"""
        _URL = self.govern + self.house.house_govern("apply", "getRelationData")
        response = self.request.get_request(_url=_URL, _headers=self.headers)
        return response

    def get_transform_apply_list(self, data):
        """【政府端--适老化】：分页查询改造申请列表"""
        _URL = self.govern + self.house.house_govern("apply", "getTransformApplyList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_transform_detail(self, data):
        """【政府端--适老化】：获取改造单详情"""
        _URL = self.govern + self.house.house_govern("apply", "getTransformDetail")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

        # 【改造审核】

    def get_transform_verify_list(self, data):
        """【政府端--适老化】：分页查询改造审核列表"""
        _URL = self.govern + self.house.house_govern("verify", "getTransformVerifyList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def verify_transform(self, data):
        """【政府端--适老化】：审核改造单"""
        _URL = self.govern + self.house.house_govern("verify", "verifyTransform")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    # 【改造评估】

    def business_apply(self, data):
        """【政府端--适老化】：申请评估机构"""
        _URL = self.govern + self.house.house_govern("assessment", "businessApply")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def cancel_assessment(self, data):
        """【政府端--适老化】：取消待评估改造"""
        _URL = self.govern + self.house.house_govern("assessment", "cancelAssessment")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_assess_apply_list(self, data):
        """"【政府端--适老化】：评估申请列表分页查询"""
        _URL = self.govern + self.house.house_govern("assessment", "getAssessApplyList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_assessment_list(self, data):
        """【政府端--适老化】：评估中列表分页查询"""
        _URL = self.govern + self.house.house_govern("assessment", "getAssessmentList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_construction_list(self):
        """【政府端--适老化】：选择施工单位列表"""
        _URL = self.govern + self.house.house_govern("assessment", "getConstructionList")
        response = self.request.get_request(_url=_URL, _headers=self.headers)
        return response

# 【改造施工】

    def constructor_apply(self, data):
        """【政府端--适老化】：派单施工方"""
        _URL = self.govern + self.house.house_govern("assessment", "constructorApply")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    # 【项目验收】

    def get_project_inspection_list(self, data):
        """【政府端--适老化】：项目验收列表分页查询"""
        _URL = self.govern + self.house.house_govern("project", "getProjectInspectionList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def check_transform_scheme(self, data):
        """【政府端--适老化】：验收改造方案"""
        _URL = self.govern + self.house.house_govern("project", "checkTransformScheme")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def get_transform_settlement_list(self, data):
        """【政府端--适老化】:项目结算列表分页查询"""
        _URL = self.govern + self.house.house_govern("project", "getTransformSettlementList")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response

    def settlement(self, data):
        """【政府端--适老化】:结算项目"""
        _URL = self.govern + self.house.house_govern("project", "settlement")
        response = self.request.get_request(_url=_URL, _data=data, _headers=self.headers)
        return response
