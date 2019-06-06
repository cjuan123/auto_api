# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: transform_app_api.py
@time: 2019/6/5 17:45
@desc：适老化-app
"""
import conf.DEFAULT as DEFAULT

transform_host = DEFAULT.test3


agencyUserEditSubmit = transform_host + "/user/agencyUserEditSubmit"    # 评估端添加员工
agencyUserListData = transform_host + "/user/agencyUserListData"    # 员工列表查询


getTasks = transform_host + "/api/suitableAging/getTasks"   # 领取任务
listOwnTasks = transform_host + "/api/suitableAging/listOwnTasks"   # 我的任务列表
downloadSubject = transform_host + "/api/suitableAging/downloadSubject"     # 适老化题目下载
saveAnswer = transform_host + "/api/evalute/saveAnswer"  # 上传评估结果
savePersonProducts = transform_host + "/api/suitableAging/savePersonProducts"    # 保存人员评估结果选择的产品关系



