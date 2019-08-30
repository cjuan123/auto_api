# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: business_api.py
@time: 2019/5/29 11:25
@desc：企业接口文件
"""



from tools.read_yaml import ReadYaml
read_yaml = ReadYaml("default.yaml")
business_host = read_yaml.get_host("business")

#   【企业端】
addOrUpdateBranch = business_host + "/business/addOrUpdateBranch"       # 添加|更新分支机构
branchInfo = business_host + "/managementBusiness/branchInfo"    # 查询分支机构，获取id"
queryPaiUserInfo = business_host + "/service/queryPaiUserInfo"   # 服务订单生成
createOrders = business_host + "/service/createOrders"   # 创建订单
queryPaiOrderSend = business_host + "/paiOrder/queryPaiOrderSend"    # 订单派工页面，获取订单ID
saveServiceRecord = business_host + "/serviceRecord/saveServiceRecord"   # 派工

#   【APP】
startService = business_host + "/user/api/startService"  # 派工助手APP：开始服务
completeService = business_host + "/user/api/completeService"    # 派工助手APP：完成服务
updateServiceDegree = business_host + "/user/api/updateServiceDegree"    # 派工助手APP：评价订单
