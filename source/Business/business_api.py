# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: business_api.py
@time: 2019/5/29 11:25
@desc：企业接口文件
"""



business = "https://test1.chinaylzl.com"

#   【企业端】
addOrUpdateBranch = business + "/business/addOrUpdateBranch"       # 添加|更新分支机构
branchInfo = business + "/managementBusiness/branchInfo"    # 查询分支机构，获取id"
queryPaiUserInfo = business + "/service/queryPaiUserInfo"   # 服务订单生成
createOrders = business + "/service/createOrders"   # 创建订单
queryPaiOrderSend = business + "/paiOrder/queryPaiOrderSend"    # 订单派工页面，获取订单ID
saveServiceRecord = business + "/serviceRecord/saveServiceRecord"   # 派工

#   【APP】
startService = business + "/user/api/startService"  # 派工助手APP：开始服务
completeService = business + "/user/api/completeService"    # 派工助手APP：完成服务
updateServiceDegree = business + "/user/api/updateServiceDegree"    # 派工助手APP：评价订单
