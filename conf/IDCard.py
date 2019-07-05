# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: IDCard.py
@time: 2019/5/27 16:21
@desc：
"""
import datetime
import random


class IDCard(object):

    addressID = "711557"

    def getYear(self, age):
        """获取年份"""
        year = int(datetime.datetime.now().year) - age
        return year

    def getMouth(self):
        """获取月份"""
        mouth = datetime.datetime.now().month
        if mouth < 10:
            mouth = "0" + str(mouth)
            return mouth
        else:
            return mouth

    def getDay(self):
        """获取日"""
        day = datetime.datetime.now().day
        if day < 10:
            day = "0" + str(day)
            return day
        else:
            return day

    def getOrder(self, sex=1):
        num = ""
        for i in range(2):
            s = random.randint(0, 9)
            num = str(num) + str(s)
        s = random.randrange(sex, 10, step=2)
        num = str(num) + str(s)
        return num

    def vilable(self, id17):
        """最后一位校验"""
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        result = 0
        for i in range(0, len(id17)):
            result += int(id17[i]) * weight[i]
        num = checkcode[str(result % 11)]
        return num

    def idCard(self, age, sex):
        num = str(self.addressID) + str(self.getYear(age)) + str(self.getMouth()) + str(self.getDay()) + str(self.getOrder(sex))
        idCard = str(num) + str(self.vilable(num))
        return idCard


# id = IDCard()
# print(id.idCard(40, 1))
# print(id.idCard(88, 1))
# print(id.idCard(88, 1))
# print(id.idCard(88, 1))
# print(id.idCard(88, 1))