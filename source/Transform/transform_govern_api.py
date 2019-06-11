# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: transform_govern_api.py
@time: 2019/6/3 17:37
@desc：适老化改造api
"""
from conf import DEFAULT


# government_host = DEFAULT.test + "/gov-house"
government_host = "http://192.168.100.151:8084"

# 【产品】
addProduct = government_host + "/product/addProduct"    # 添加产品
getProductList = government_host + "/product/getProductList"    # 分页查询产品列表
getProductTypeList = government_host + "/product/getProductTypeList"    # 查询产品类型list
stopStartProduct = government_host + "/product/stopStartProduct"    # 产品停启
updateProduct = government_host + "/product/updateProduct"      # 编辑产品信息
getUnitData = government_host + "/product/getUnitData"      # 获取单位数据
getProductDetail = government_host + "/product/getProductDetail"    # 查看产品详情

# 【施工单位】
addConstructionBusiness = government_host + "/business/addConstructionBusiness"     # 添加施工单位
getConstructionBusinessList = government_host + "/business/getConstructionBusinessList"     # 分页查询施工单位列表
editConstructionBusiness = government_host + "/business/editConstructionBusiness"   # 编辑施工单位信息
getBusinessDetail = government_host + "/business/getBusinessDetail"     # 获取施工单位信息
recordConstructionList = government_host + "/business/recordConstructionList"   # 施工记录
getEmployeeList = government_host + "/business/getEmployeeList"     # 通讯名单
stopOrStartConstructor = government_host + "/business/stopOrStartConstructor"   # 停启施工单位
servicesList = government_host + "/business/servicesList"   # 结算服务

# 【评估机构】
addAssessAgency = government_host + "/assessment/addAssessAgency"   # 添加评估机构
assessmentRecord = government_host + "/assessment/assessmentRecord"     # 机构评估记录
editAssessAgency = government_host + "/assessment/editAssessAgency"     # 编辑获取评估机构信息
getAgencyDetail = government_host + "/assessment/getAgencyDetail"       # 获取评估机构基本信息
getAgencyEmployeeList = government_host + "/assessment/getAgencyEmployeeList"   # 通讯名单列表
getAssessmentAgencies = government_host + "/assessment/getAssessmentAgencies"   # 分页查询评估机构列表
getAssessmentScheme = government_host + "/assessment/getAssessmentScheme"   # 查询方案列表
getSettleService = government_host + "/assessment/getSettleService"     # 结算服务列表
queryAgenciesList = government_host + "/assessment/queryAgenciesList"   # 获取选择评估机构列表
saveAssessmentAgency = government_host + "/assessment/saveAssessmentAgency"     # 保存编辑后评估机构信息
settleAgency = government_host + "/assessment/settleAgency"     # 结算服务列表
startOrStop = government_host + "/assessment/startOrStop"       # 机构评估停启用

# 【改造申请】
getUserByIdCard = government_host + "/transformApply/getUserByIdCard"       # 根据身份证查询人员信息
addTransformApply = government_host + "/transformApply/addTransformApply"   # 添加改造申请
applyTransform = government_host + "/transformApply/applyTransform"     # 改造申请
editTransform = government_host + "/transformApply/editTransform"       # 编辑改造单
getRelationData = government_host + "/transformApply/getRelationData"   # 获取人员关系数据
getTransformApplyList = government_host + "/transformApply/getTransformApplyList"   # 分页查询改造申请列表
getTransformDetail = government_host + "/transformApply/getTransformDetail"     # 获取改造单详情

# 【改造审核】
getTransformVerifyList = government_host + "/transformVerify/getTransformVerifyList"    # 分页查询改造审核列表
verifyTransform = government_host + "/transformVerify/verifyTransform"      # 审核改造单

# 【改造评估】
businessApply = government_host + "/transformAssess/businessApply"      # 申请评估机构
cancelAssessment = government_host + "/transformAssess/cancelAssessment"    # 取消待评估改造
getAssessApplyList = government_host + "/transformAssess/getAssessApplyList"    # 评估申请列表分页查询
getAssessmentList = government_host + "/transformAssess/getAssessmentList"      # 评估中列表分页查询
getConstructionList = government_host + "/transformAssess/getConstructionList"      # 选择施工单位列表

# 【改造施工】
constructorApply = government_host + "/transformConstruction/constructorApply"  # 派单施工方

# 【项目验收】
getProjectInspectionList = government_host + "/transformCheck/getProjectInspectionList"     # 项目验收列表分页查询
checkTransformScheme = government_host + "/transformCheck/checkTransformScheme"     # 验收改造方案

# 【项目结算】
getTransformSettlementList = government_host + "/transformSettlement/getTransformSettlementList"    # 项目结算列表分页查询
settlement = government_host + "/transformSettlement/settlement"    # 结算项目









