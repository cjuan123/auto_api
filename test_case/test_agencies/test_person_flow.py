# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_person_flow.py
@time: 2019/6/3 10:19
@desc：评估-人员评估流程
"""
import unittest
from conf import Login
from conf.IDCard import IDCard
from source.Agencies.agencies import Agencies
from source.YangLao.yanglao import YangLao


class TestPersonFlow(unittest.TestCase):

    agencies = Agencies()
    yang_lao = YangLao()
    id_card = IDCard().idCard(69, 1)
    recordID = []

    @Login.govern_login("18048054262", "123qwe")
    def test_001(self):
        """【政府端】：查询身份证是否存在评估申请"""
        param = {
            "idCard": self.id_card
        }
        response = self.yang_lao.query_user(case_name="查询身份证是否存在评估申请", param=param)
        print("【查询身份证是否存在评估申请】接口返回数据：%s" % response.json())
        self.assertEqual("", response.json()["detail"])

    def test_002(self):
        """【政府端】：添加评估申请"""
        param = {
            "idCard": self.id_card,
            "username": "评估数据" + self.id_card,
            "phone": "15282544520",
            "agenciesId": "44",
            "assessmentTypeId": "2",
            "assessmentChildTypeId": "1",
            "schemeId": "19",
            "userAddressDetail": "评估测试数据",
            "userAddressId": "5101090201",
            "userLevel": 2,
            "personType": "PT_CSJZTK,PT_CSFSTK,PT_NCJZTK,PT_NCFSTK,PT_DIBAO,PT_DISHOURU,PT_SHIDU,PT_KONGCHAO,PT_GG,"
                          "PT_DJLR,PT_LSLR,PT_YOUFU,PT_LITUIXIU,PT_GAOLING,PT_DSZNSC,PT_CLJT,PT_XFDX,PT_TEKUNRENYUAN,"
                          "PT_WUBAO,PT_SANWU,PT_LDY,PT_DGB,PT_TSKNJT,PT_JJKNFWBT,PT_QT"
        }
        response = self.yang_lao.apply_add(case_name="添加人员评估申请", param=param)
        print("【添加评估申请】接口返回数据：%s" % response.json())
        self.assertEqual("添加成功", response.json()["detail"])
        print('评估数据：姓名【%s】- 身份证号【%s】' % ("评估数据" + self.id_card, self.id_card))

    def test_003(self):
        """【政府端】：查询评估申请ID"""
        param = {
            "idCard": self.id_card,
        }
        response = self.yang_lao.apply_list(case_name="查询评估申请ID", param=param)
        rid = response.json()['pageView']['records'][0]['id']
        self.recordID.append(rid)
        print("【查询评估申请ID】接口返回数据：%s" % response.json())
        print("评估申请ID：【%s】" % rid)

    @Login.agencies_app_login("18048054260", "123456")
    def test_004(self):
        """【评估app】：下载评估申请"""
        self.assertEqual(1, len(self.recordID))
        param = {
            'name': 'assess_token',
            'schemeId': '19',
            'recordId': self.recordID[0],
            'type': '1',
            'userId': '86'
        }
        response = self.agencies.query_scheme_subject_list(case_name="下载评估申请", param=param)
        print("【app下载评估申请】接口返回数据：%s" % response.json())

    def test_005(self):
        """【评估app】：计算分数"""
        id = self.recordID[0]
        param = {
            'name': 'assess_token',
            'answer': '[{"answerId":1,"parentId":1,"recordId":%d,"subjectId":8},{"answerId":8,"parentId":1,"recordId":%d,"subjectId":11},{"answerId":10,"parentId":1,"recordId":%d,"subjectId":20},{"answerId":12,"parentId":1,"recordId":%d,"subjectId":21},{"answerId":16,"parentId":1,"recordId":%d,"subjectId":22},{"answerId":18,"parentId":1,"recordId":%d,"subjectId":23},{"answerId":22,"parentId":1,"recordId":%d,"subjectId":24},{"answerId":24,"parentId":1,"recordId":%d,"subjectId":25},{"answerId":31,"parentId":1,"recordId":%d,"subjectId":27},{"answerId":36,"parentId":1,"recordId":%d,"subjectId":28},{"answerId":38,"parentId":2,"recordId":%d,"subjectId":32},{"answerId":41,"parentId":2,"recordId":%d,"subjectId":33},{"answerId":44,"parentId":2,"recordId":%d,"subjectId":34},{"answerId":48,"parentId":3,"recordId":%d,"subjectId":39},{"answerId":52,"parentId":3,"recordId":%d,"subjectId":40},{"answerId":57,"parentId":3,"recordId":%d,"subjectId":41},{"answerId":62,"parentId":3,"recordId":%d,"subjectId":42},{"answerId":66,"parentId":4,"recordId":%d,"subjectId":48},{"answerId":70,"parentId":4,"recordId":%d,"subjectId":49},{"answerId":75,"parentId":4,"recordId":%d,"subjectId":50},{"answerId":80,"parentId":4,"recordId":%d,"subjectId":51},{"answerId":85,"parentId":4,"recordId":%d,"subjectId":52},{"answerId":627,"parentId":391,"recordId":%d,"subjectId":393},{"answerId":628,"parentId":391,"recordId":%d,"subjectId":394},{"answerId":625,"parentId":391,"recordId":%d,"subjectId":395}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id),
            'agencyId': '44'
        }
        response = self.agencies.calc_score(case_name="计算分数", param=param)
        print("【计算分数】接口返回数据：%s" % response.json())

    def test_006(self):
        """【评估app】：上传评估结果"""
        id = self.recordID[0]
        param = {
            'name': 'assess_token',
            'answer': '[{"answerId":1,"parentId":1,"recordId":%d,"subjectId":8},{"answerId":8,"parentId":1,"recordId":%d,"subjectId":11},{"answerId":10,"parentId":1,"recordId":%d,"subjectId":20},{"answerId":12,"parentId":1,"recordId":%d,"subjectId":21},{"answerId":16,"parentId":1,"recordId":%d,"subjectId":22},{"answerId":18,"parentId":1,"recordId":%d,"subjectId":23},{"answerId":22,"parentId":1,"recordId":%d,"subjectId":24},{"answerId":24,"parentId":1,"recordId":%d,"subjectId":25},{"answerId":31,"parentId":1,"recordId":%d,"subjectId":27},{"answerId":36,"parentId":1,"recordId":%d,"subjectId":28},{"answerId":38,"parentId":2,"recordId":%d,"subjectId":32},{"answerId":41,"parentId":2,"recordId":%d,"subjectId":33},{"answerId":44,"parentId":2,"recordId":%d,"subjectId":34},{"answerId":48,"parentId":3,"recordId":%d,"subjectId":39},{"answerId":52,"parentId":3,"recordId":%d,"subjectId":40},{"answerId":57,"parentId":3,"recordId":%d,"subjectId":41},{"answerId":62,"parentId":3,"recordId":%d,"subjectId":42},{"answerId":66,"parentId":4,"recordId":%d,"subjectId":48},{"answerId":70,"parentId":4,"recordId":%d,"subjectId":49},{"answerId":75,"parentId":4,"recordId":%d,"subjectId":50},{"answerId":80,"parentId":4,"recordId":%d,"subjectId":51},{"answerId":85,"parentId":4,"recordId":%d,"subjectId":52},{"answerId":627,"parentId":391,"recordId":%d,"subjectId":393},{"answerId":628,"parentId":391,"recordId":%d,"subjectId":394},{"answerId":625,"parentId":391,"recordId":%d,"subjectId":395}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id),
            'conclusion': '测试',
            'userId': '86'
        }
        response = self.agencies.save_answer(case_name="上传评估结果", param=param)
        print("【上传评估结果】接口返回数据：%s" % response.json())


if __name__ == "__main__":
    unittest.main()

