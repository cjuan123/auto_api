"""
@version: 1.0
@author: chenj
@file: cater_api.py
@time: 2019/5/19 11:55
"""
from conf import DEFAULT
goverment_host = DEFAULT.test

userlist = goverment_host + "/cater-server/user/userList"
getUserByIdCard = goverment_host + "/cater-server/user/getUserByIdCard"
adduser = goverment_host + "/cater-server/user/addUser"
