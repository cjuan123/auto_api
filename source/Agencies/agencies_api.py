# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: agencies_api.py
@time: 2019/6/3 9:52
@desc：评估机构api
"""
# agencies_host = DEFAULT.test3
agencies_host = "http://120.76.84.195:8093"
goverment_host = "https://test.chinaylzl.com"

#  政府端--评估
queryUser = goverment_host + "/assessmentManage/queryUser"     # 查询身份证是否存在评估申请
applyAdd = goverment_host + "/assessmentManage/applyAdd"     # 政府端添加评估申请
applyList = goverment_host + "/assessmentManage/applyList"   # 查询评估申请的ID
cancelRecordById = goverment_host + "/assessmentManage/cancelRecordById"     # 取消评估申请
auditList = goverment_host + "/assessmentManage/auditList"    # 待审核页面
update = goverment_host + "/assessmentManage/update"      # 审核


#  政府端--日照
addSunlight = goverment_host + "/sunlight/addSunlight"      # 添加日照中心
sunlightManage = goverment_host + "/sunlight/sunlightManage"    # 根据日照名称查询
sunlightApplyAdd = goverment_host + "/sunlight/sunlightApplyAdd"    # 添加日照评估申请
sunlightApplyList = goverment_host + "/sunlight/sunlightApplyList"    # 查询日照评估ID



#  评估端--app
login = agencies_host + "/api/user/login"  # 评估app登录
querySchemeSubjectList = agencies_host + "/api/evalute/querySchemeSubjectList"  # 下载评估申请
update = agencies_host + "/api/business/update"  # 开始评估申请
calcScore = agencies_host + "/api/evalute/calcScore"  # 计算分数
saveAnswer = agencies_host + "/api/evalute/saveAnswer"  # 上传评估结果

