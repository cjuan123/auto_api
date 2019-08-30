# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: yanglao_api.py
@time: 2019/5/29 10:35
@desc：养老模块--api接口
"""
from tools.read_yaml import ReadYaml
read_yaml = ReadYaml("default.yaml")
govern_host = read_yaml.get_host("govern")

loginOut = govern_host + "/loginOut"     # 退出登录
addSurveyUser = govern_host + "/surveyUser/addSurveyUser"    # 添加人员
recharge = govern_host + "/Balance/Recharge"      # 人员批量充值
listUsersNew = govern_host + "/surveyUser/listUsersNew"      # 根据身份证号，查询获取uid
SingleRecharge = govern_host + "/Balance/SingleRecharge"     # 养老积分充值
