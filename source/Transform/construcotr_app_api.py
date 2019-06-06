# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: construcotr_app_api.py
@time: 2019/6/6 10:58
@desc：适老化：施工方app api接口
"""
from conf import DEFAULT

host = DEFAULT.host_8094

login = host + "/app/login"         # 施工app登录
web_login = host + "/web/login"     # web管理后台系统登录

#   【施工web】
addEmployee = host + "/web/staff/addEmployee"      # 添加员工
updateEmployee = host + "/web/staff/updateEmployee"     # 编辑员工
employeeList = host + "/web/staff/employeeList"     # 查询员工列表

# 【施工APP】

getTask = host + "/app/getTask"     # 领取任务
