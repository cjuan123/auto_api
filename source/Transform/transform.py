# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: transform.py
@time: 2019/6/3 17:39
@desc：适老化政府端接口
"""
from conf import DEFAULT
from tools.http_request import Request
from source.Transform import transform_api as t_api


class Transform:
    headers = DEFAULT.HEADERS
    request = Request()

    # 【产品】

    def add_product(self, param):
        """【政府端--适老化】：添加产品"""
        response = self.request.post_request_json(_url=t_api.addProduct, _json=param, _headers=self.headers)
        return response

    def get_product_list(self, param):
        """【政府端--适老化】：分页查询产品列表"""
        response = self.request.get_request(_url=t_api.getProductList, _data=param, _headers=self.headers)
        return response

    def get_product_type_list(self):
        """【政府端--适老化】：查询产品类型list"""
        response = self.request.get_request(_url=t_api.getProductTypeList, _headers=self.headers)
        return response

    def stop_start_product(self, param):
        """【政府端--适老化】：产品停启"""
        response = self.request.get_request(_url=t_api.stopStartProduct, _data=param, _headers=self.headers)
        return response

    def update_product(self, param):
        """【政府端--适老化】：编辑产品信息"""
        response = self.request.post_request_json(_url=t_api.updateProduct, _json=param, _headers=self.headers)
        return response

    def get_unit_data(self):
        """【政府端--适老化】：获取单位数据"""
        response = self.request.get_request(_url=t_api.getUnitData, _headers=self.headers)
        return response

    def get_product_detail(self, param):
        """【政府端--适老化】：查看产品详情"""
        response = self.request.get_request(_url=t_api.getProductDetail, _data=param, _headers=self.headers)
        return response

    # 【施工单位】

    def add_construction_business(self, param):
        """【政府端--适老化】：添加施工单位"""
        response = self.request.post_request_json(_url=t_api.addConstructionBusiness, _json=param, _headers=self.headers)
        return response

    def get_construction_business_list(self, param):
        """【政府端--适老化】：分页查询施工单位列表"""
        response = self.request.get_request(_url=t_api.getConstructionBusinessList, _data=param, _headers=self.headers)
        return response

    def edit_construction_business(self, param):
        """【政府端--适老化】：编辑施工单位信息"""
        response = self.request.post_request_json(_url=t_api.editConstructionBusiness, _json=param, _headers=self.headers)
        return response

    def get_business_detail(self, param):
        """【政府端--适老化】：获取施工单位信息"""
        response = self.request.get_request(_url=t_api.getBusinessDetail, _data=param, _headers=self.headers)
        return response

    def record_construction_list(self, param):
        """【政府端--适老化】：施工记录"""
        response = self.request.get_request(_url=t_api.recordConstructionList, _data=param, _headers=self.headers)
        return response

    def get_employee_list(self, param):
        """【政府端--适老化】：通讯名单"""
        response = self.request.get_request(_url=t_api.getEmployeeList, _data=param, _headers=self.headers)
        return response

    def stop_or_start_constructor(self, param):
        """【政府端--适老化】：停启施工单位"""
        response = self.request.get_request(_url=t_api.stopOrStartConstructor, _data=param, _headers=self.headers)
        return response

    def services_list(self, param):
        """【政府端--适老化】：结算服务"""
        response = self.request.get_request(_url=t_api.servicesList, _data=param, _headers=self.headers)
        return response

    # 【评估机构】

    def add_assess_agency(self, param):
        """【政府端--评估机构】：添加评估机构"""
        response = self.request.post_request_json(_url=t_api.addAssessAgency, _json=param, _headers=self.headers)
        return response

    def assessment_record(self, param):
        """【政府端--评估机构】：机构评估记录"""
        response = self.request.get_request(_url=t_api.assessmentRecord, _data=param, _headers=self.headers)
        return response

    def edit_assess_agency(self, param):
        """【政府端--评估机构】：编辑获取评估机构信息"""
        response = self.request.post_request_json(_url=t_api.editAssessAgency, _json=param, _headers=self.headers)
        return response

    def get_agency_detail(self, param):
        """【政府端--评估机构】：获取评估机构基本信息"""
        response = self.request.get_request(_url=t_api.getAgencyDetail, _data=param, _headers=self.headers)
        return response

    def get_agency_employee_list(self, param):
        """【政府端--评估机构】：通讯名单列表"""
        response = self.request.get_request(_url=t_api.getEmployeeList, _data=param, _headers=self.headers)
        return response

    def get_assessment_agencies(self, param):
        """【政府端--评估机构】：分页查询评估机构列表"""
        response = self.request.get_request(_url=t_api.getAssessmentAgencies, _data=param, _headers=self.headers)
        return response

    def get_assessment_scheme(self, param):
        """【政府端--评估机构】：查询方案列表"""
        response = self.request.get_request(_url=t_api.getAssessmentScheme, _data=param, _headers=self.headers)
        return response

    def get_settle_service(self, param):
        """【政府端--评估机构】：结算服务列表"""
        response = self.request.get_request(_url=t_api.getSettleService, _data=param, _headers=self.headers)
        return response

    def query_agencies_list(self):
        """【政府端--评估机构】：获取选择评估机构列表"""
        response = self.request.get_request(_url=t_api.queryAgenciesList, _headers=self.headers)
        return response

    def save_assessment_agency(self, param):
        """【政府端--评估机构】：保存编辑后评估机构信息"""
        response = self.request.post_request_json(_url=t_api.saveAssessmentAgency, _json=param, _headers=self.headers)
        return response

    def settle_agency(self, param):
        """【政府端--评估机构】：结算服务列表"""
        response = self.request.get_request(_url=t_api.settleAgency, _data=param, _headers=self.headers)
        return response

    def start_or_stop(self, param):
        """【政府端--评估机构】：机构评估停启用"""
        response = self.request.get_request(_url=t_api.startOrStop, _data=param, _headers=self.headers)
        return response

    # 【申请】

    def get_user_by_id_card(self, param):
        """【政府端 - -适老化】：根据身份证查询人员信息"""
        response = self.request.get_request(_url=t_api.getUserByIdCard, _data=param, _headers=self.headers)
        return response

    def add_transform_apply(self, param):
        """【政府端--适老化】：添加改造申请"""
        response = self.request.post_request_json(_url=t_api.addTransformApply, _json=param, _headers=self.headers)
        return response

    def apply_transform(self, data):
        """【政府端--适老化】：改造申请"""
        response = self.request.get_request(_url=t_api.applyTransform,_data=data, _headers=self.headers)
        return response

    def edit_transform(self, json):
        """【政府端--适老化】：编辑改造单"""
        response = self.request.post_request_json(_url=t_api.editTransform, _json=json, _headers=self.headers)
        return response

    def get_relation_data(self):
        """【政府端--适老化】：获取人员关系数据"""
        response = self.request.get_request(_url=t_api.getRelationData, _headers=self.headers)
        return response

    def get_transform_apply_list(self, data):
        """【政府端--适老化】：分页查询改造申请列表"""
        response = self.request.get_request(_url=t_api.getTransformApplyList, _data=data, _headers=self.headers)
        return response

    def get_transform_detail(self, data):
        """【政府端--适老化】：获取改造单详情"""
        response = self.request.get_request(_url=t_api.getTransformDetail, _data=data, _headers=self.headers)
        return response

    # 【改造审核】

    def get_transform_verify_list(self, data):
        """【政府端--适老化】：分页查询改造审核列表"""
        response = self.request.get_request(_url=t_api.getTransformVerifyList, _data=data, _headers=self.headers)
        return response

    def verify_transform(self, data):
        """【政府端--适老化】：审核改造单"""
        response = self.request.get_request(_url=t_api.verifyTransform, _data=data, _headers=self.headers)
        return response

    # 【改造评估】

    def business_apply(self, data):
        """【政府端--适老化】：申请评估机构"""
        response = self.request.get_request(_url=t_api.businessApply, _data=data, _headers=self.headers)
        return response

    def cancel_assessment(self, data):
        """【政府端--适老化】：取消待评估改造"""
        response = self.request.get_request(_url=t_api.cancelAssessment, _data=data, _headers=self.headers)
        return response

    def get_assess_apply_list(self, data):
        """"【政府端--适老化】：评估申请列表分页查询"""
        response = self.request.get_request(_url=t_api.getAssessApplyList, _data=data, _headers=self.headers)
        return response

    def get_assessment_list(self, data):
        """【政府端--适老化】：评估中列表分页查询"""
        response = self.request.get_request(_url=t_api.getAssessmentList, _data=data, _headers=self.headers)
        return response

    def get_construction_list(self):
        """【政府端--适老化】：选择施工单位列表"""
        response = self.request.get_request(_url=t_api.getConstructionList, _headers=self.headers)
        return response

    # 【改造施工】

    def constructor_apply(self, data):
        response = self.request.get_request(_url=t_api.constructorApply, _data=data, _headers=self.headers)
        return response

