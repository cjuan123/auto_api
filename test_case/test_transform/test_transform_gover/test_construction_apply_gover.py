# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_construction_apply_gover.py
@time: 2019/6/6 10:22
@desc：改造施工
"""
import unittest
from conf import Login
from source.Transform.transform_govern import Transform


class TestConstructionApplyGovern(unittest.TestCase):

    transform = Transform()

    @Login.get_account("18981967059", "123qwe")
    def test_001_constructor_apply(self):

        param = {
            "constructionId":  44,
            "id": 36
        }
        response = self.transform.constructor_apply(data=param)
        print(response.json())
