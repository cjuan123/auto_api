# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: yanglao_api.py
@time: 2019/5/29 10:35
@desc：养老模块--api接口
"""
from conf import DEFAULT

gover_host = DEFAULT.test

addSurveyUser = gover_host + "/surveyUser/addSurveyUser"    # 添加人员
recharge = gover_host + "/Balance/Recharge"      # 人员批量充值
