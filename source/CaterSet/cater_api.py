"""
@version: 1.0
@author: chenj
@file: cater_api.py
@time: 2019/5/19 11:55
"""
from conf import DEFAULT
goverment_host = "https://test.chinaylzl.com"
pc_host = "https://test3.chinaylzl.com"

#   【大配餐政府端api】
userlist = goverment_host + "/cater-server/user/userList"   # 人员列表
getUserByIdCard = goverment_host + "/cater-server/user/getUserByIdCard"     # 添加人员更加身份证查询是否存在
adduser = goverment_host + "/cater-server/user/addUser"     # 添加人员
reviewUser = goverment_host + "/cater-server/review/reviewUser"     # 人员审核：checkType  1.审核    2.复审
queryAllApplyUser = goverment_host + "/cater-server/review/queryAllApplyUser"   # 人员审核：查询人员申请，获取applyID

#   【大配餐企业端api】
setRecharge = pc_host + "/recharge/setRecharge"   # 人员充值
memberList = pc_host + "/member/memberList"     # 人员列表 根据身份查询，获取userid
addAppointment = pc_host + "/appointment/addAppointment"    # 新增预约

#   【大配餐APP api】
completeEat = pc_host + "/api/completeEat"  # 大配餐app 就餐扫码


