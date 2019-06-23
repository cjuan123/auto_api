# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: yanglao_api.py
@time: 2019/5/29 10:35
@desc：养老模块--api接口
"""

gover_host = "https://test.chinaylzl.com"

loginOut = gover_host + "/loginOut"     # 退出登录
addSurveyUser = gover_host + "/surveyUser/addSurveyUser"    # 添加人员
recharge = gover_host + "/Balance/Recharge"      # 人员批量充值
listUsersNew = gover_host + "/surveyUser/listUsersNew"      # 根据身份证号，查询获取uid
SingleRecharge = gover_host + "/Balance/SingleRecharge"     # 养老积分充值
