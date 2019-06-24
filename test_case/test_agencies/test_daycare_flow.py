# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_daycare_flow.py
@time: 2019/6/3 11:28
@desc：评估--日照评估
"""
import unittest
import random
from conf import Login
from tools.logger import Logger
from tools.read_yaml import ReadYaml
from source.Agencies.agencies import Agencies
from source.YangLao.yanglao import YangLao
from tools.http_request import Request


class TestDaycareFlow(unittest.TestCase):

    read_yaml = ReadYaml("default.yaml")
    govern = read_yaml.get_password("govern")
    agencies_pwd = read_yaml.get_password("agencies_app")

    yang_lao = YangLao()
    request = Request()
    agencies = Agencies()
    num = random.randint(000000, 999999)
    sunlightName = "api日照" + str(num)
    bid = []  # 日照中心ID
    record_id = []

    @classmethod
    def setUpClass(cls):
        print("------------------------ 日照评估 STA------------------------")
        Logger().info("------------------------ 日照评估 STA------------------------")

    @Login.govern_login("18048054262", govern)
    def test_001(self):
        """添加日照中心"""
        print("日照中心名称：" + self.sunlightName)
        param = {
            "sunlightName": self.sunlightName,
            "detailAddress": "api测试日照详细地址",
            "address": "5101090201",
            "sunlightType": "4",
            "password": "123456",
            "state": "1",
            'nature': '1'
        }
        res = self.yang_lao.add_sunlight(case_name="添加日照中心", param=param)
        print("【添加日照中心】：%s" % res.json())
        assert "添加成功" == res.json()["detail"]

    def test_002(self):
        """根据日照名称查询"""
        param = {
            "sunlightName": self.sunlightName
        }
        res = self.yang_lao.sunlight_manage(case_name="根据日照名称查询", param=param)
        self.bid.append(res.json()["pageView"]["records"][0]["id"])
        print("【根据日照名称查询-日照ID】：%s" % self.bid[0])
        print("【根据日照名称查询】：%s" % res.json())

    def test_003(self):
        """添加日照评估申请"""
        param = {
            "agenciesId": "44",
            "assessmentTypeId": "2",
            "schemeId": "95",
            "bId": self.bid[0],
            "districtId": "5101090201"
        }
        res = self.yang_lao.sunlight_apply_add(case_name="添加日照评估申请",param=param)
        print("【添加日照评估申请】：%s" % res.json())
        assert "添加成功" == res.json()["detail"]

    def test_004(self):
        """查询日照评估ID"""
        param = {
            "businessName": self.sunlightName,
            "address": "51010902"
        }
        res = self.yang_lao.sunlight_apply_list(case_name="查询日照评估ID", param=param)
        print("查询日照评估ID,返回json数据：%s" % res.json())

        self.record_id.append(res.json()["pageView"]["records"][0]["id"])
        print("日照评估ID：%s " % self.record_id)

    @Login.agencies_app_login("18048054260", agencies_pwd)
    def test_005(self):
        """app下载评估申请"""
        assert len(self.record_id) != 0
        print(self.record_id[0])
        param = {
            'name': 'assess_token',
            'schemeId': '95',
            'recordId': self.record_id[0],
            'type': '1',
            'userId': '86'
        }
        res = self.agencies.query_scheme_subject_list(case_name="app下载评估申请", param=param)
        print("【app下载评估申请】接口返回数据：%s" % res.json())
        self.assertEqual(res.json()['detail'], 'success')

    def test_006(self):
        """开始评估"""
        param = {
            'recordId': self.record_id[0],
            'tude': '104.07489161914495,30.54035684045281',
            'bId': self.bid[0],
            'licencesImages': 'http://file.chinaylzl.com/test/assessmentUpload/2018/12/10/7f1ec2287a8a4796a4be88b1f37abf11.jpeg,'
                              'http://file.chinaylzl.com/test/assessmentUpload/2018/12/10/2ddc1a55ec0a4b67818dee89e2cd16d2.jpeg,'
                              'http://file.chinaylzl.com/test/assessmentUpload/2018/12/10/cc12e0aa660c44299667b69c3451aba9.jpeg,'
                              'http://file.chinaylzl.com/test/assessmentUpload/2018/12/10/38a485f40987499797423f9e2f1ef0b0.jpeg'
        }
        res = self.agencies.update(case_name="开始评估", param=param)
        print('请求返回数据：%s' % res.json())
        self.assertEqual(res.json()['detail'], 'success')

    def test_007(self):
        """计算分数"""
        id = self.record_id[0]
        param = {
            'name': 'assess_token',
            'agencyId': '44',
            'answer': '[{"answerId":1077,"parentId":610,"recordId":%d,"subjectId":618},{"answerId":719,"parentId":401,'
                      '"recordId":%d,"subjectId":403},{"answerId":1038,"parentId":464,"recordId":%d,"subjectId":538},'
                      '{"answerId":1094,"parentId":610,"recordId":%d,"subjectId":626},{"answerId":1036,"parentId":464,'
                      '"recordId":%d,"subjectId":631},{"answerId":1059,"parentId":610,"recordId":%d,"subjectId":612},'
                      '{"answerId":1084,"parentId":610,"recordId":%d,"subjectId":622},{"answerId":1079,"parentId":610,'
                      '"recordId":%d,"subjectId":620},{"answerId":1053,"parentId":416,"recordId":%d,"subjectId":500},'
                      '{"answerId":1066,"parentId":610,"recordId":%d,"subjectId":614},{"answerId":1091,"parentId":610,'
                      '"recordId":%d,"subjectId":625},{"answerId":1071,"parentId":610,"recordId":%d,"subjectId":615},'
                      '{"answerId":1049,"parentId":416,"recordId":%d,"subjectId":632},{"answerId":1034,"parentId":464,'
                      '"recordId":%d,"subjectId":536},{"answerId":744,"parentId":416,"recordId":%d,"subjectId":418},'
                      '{"answerId":1062,"parentId":610,"recordId":%d,"subjectId":613},{"answerId":1032,"parentId":627,'
                      '"recordId":%d,"subjectId":629},{"answerId":721,"parentId":401,"recordId":%d,"subjectId":481},'
                      '{"answerId":746,"parentId":416,"recordId":%d,"subjectId":486},{"answerId":748,"parentId":416,'
                      '"recordId":%d,"subjectId":487},{"answerId":725,"parentId":401,"recordId":%d,"subjectId":405},'
                      '{"answerId":750,"parentId":416,"recordId":%d,"subjectId":488},{"answerId":752,"parentId":416,'
                      '"recordId":%d,"subjectId":489},{"answerId":727,"parentId":401,"recordId":%d,"subjectId":482},'
                      '{"answerId":754,"parentId":416,"recordId":%d,"subjectId":490},{"answerId":756,"parentId":416,'
                      '"recordId":%d,"subjectId":491},{"answerId":731,"parentId":401,"recordId":%d,"subjectId":483},'
                      '{"answerId":758,"parentId":416,"recordId":%d,"subjectId":492},{"answerId":734,"parentId":401,'
                      '"recordId":%d,"subjectId":484},{"answerId":760,"parentId":416,"recordId":%d,"subjectId":493},'
                      '{"answerId":737,"parentId":401,"recordId":%d,"subjectId":409},{"answerId":763,"parentId":416,'
                      '"recordId":%d,"subjectId":494},{"answerId":740,"parentId":401,"recordId":%d,"subjectId":485},'
                      '{"answerId":766,"parentId":416,"recordId":%d,"subjectId":495},{"answerId":769,"parentId":416,'
                      '"recordId":%d,"subjectId":496},{"answerId":772,"parentId":416,"recordId":%d,"subjectId":497},'
                      '{"answerId":775,"parentId":416,"recordId":%d,"subjectId":498},{"answerId":778,"parentId":416,'
                      '"recordId":%d,"subjectId":420},{"answerId":781,"parentId":416,"recordId":%d,"subjectId":422},'
                      '{"answerId":790,"parentId":443,"recordId":%d,"subjectId":445},{"answerId":794,"parentId":443,'
                      '"recordId":%d,"subjectId":447},{"answerId":796,"parentId":443,"recordId":%d,"subjectId":501},'
                      '{"answerId":799,"parentId":443,"recordId":%d,"subjectId":502},{"answerId":801,"parentId":443,'
                      '"recordId":%d,"subjectId":449},{"answerId":803,"parentId":443,"recordId":%d,"subjectId":503},'
                      '{"answerId":805,"parentId":443,"recordId":%d,"subjectId":451},{"answerId":809,"parentId":443,'
                      '"recordId":%d,"subjectId":453},{"answerId":825,"parentId":443,"recordId":%d,"subjectId":455},'
                      '{"answerId":827,"parentId":443,"recordId":%d,"subjectId":504},{"answerId":829,"parentId":443,'
                      '"recordId":%d,"subjectId":457},{"answerId":831,"parentId":443,"recordId":%d,"subjectId":505},'
                      '{"answerId":833,"parentId":443,"recordId":%d,"subjectId":459},{"answerId":835,"parentId":443,'
                      '"recordId":%d,"subjectId":506},{"answerId":837,"parentId":443,"recordId":%d,"subjectId":461},'
                      '{"answerId":839,"parentId":443,"recordId":%d,"subjectId":507},{"answerId":841,"parentId":443,'
                      '"recordId":%d,"subjectId":463},{"answerId":843,"parentId":443,"recordId":%d,"subjectId":508},'
                      '{"answerId":845,"parentId":443,"recordId":%d,"subjectId":509},{"answerId":847,"parentId":443,'
                      '"recordId":%d,"subjectId":510},{"answerId":849,"parentId":443,"recordId":%d,"subjectId":511},'
                      '{"answerId":851,"parentId":443,"recordId":%d,"subjectId":512},{"answerId":853,"parentId":443,'
                      '"recordId":%d,"subjectId":513},{"answerId":855,"parentId":443,"recordId":%d,"subjectId":514},'
                      '{"answerId":857,"parentId":443,"recordId":%d,"subjectId":515},{"answerId":859,"parentId":443,'
                      '"recordId":%d,"subjectId":516},{"answerId":862,"parentId":464,"recordId":%d,"subjectId":466},'
                      '{"answerId":864,"parentId":464,"recordId":%d,"subjectId":517},{"answerId":866,"parentId":464,'
                      '"recordId":%d,"subjectId":468},{"answerId":868,"parentId":464,"recordId":%d,"subjectId":470},'
                      '{"answerId":870,"parentId":464,"recordId":%d,"subjectId":472},{"answerId":872,"parentId":464,'
                      '"recordId":%d,"subjectId":474},{"answerId":874,"parentId":464,"recordId":%d,"subjectId":476},'
                      '{"answerId":876,"parentId":464,"recordId":%d,"subjectId":478},{"answerId":878,"parentId":464,'
                      '"recordId":%d,"subjectId":480},{"answerId":880,"parentId":464,"recordId":%d,"subjectId":519},'
                      '{"answerId":882,"parentId":464,"recordId":%d,"subjectId":521},{"answerId":884,"parentId":464,'
                      '"recordId":%d,"subjectId":523},{"answerId":886,"parentId":464,"recordId":%d,"subjectId":525},'
                      '{"answerId":888,"parentId":464,"recordId":%d,"subjectId":527},{"answerId":890,"parentId":464,'
                      '"recordId":%d,"subjectId":529},{"answerId":892,"parentId":464,"recordId":%d,"subjectId":531},'
                      '{"answerId":894,"parentId":464,"recordId":%d,"subjectId":532},{"answerId":896,"parentId":464,'
                      '"recordId":%d,"subjectId":533},{"answerId":898,"parentId":464,"recordId":%d,"subjectId":534},'
                      '{"answerId":904,"parentId":464,"recordId":%d,"subjectId":540},{"answerId":906,"parentId":464,'
                      '"recordId":%d,"subjectId":541},{"answerId":908,"parentId":464,"recordId":%d,"subjectId":542},'
                      '{"answerId":910,"parentId":464,"recordId":%d,"subjectId":543},{"answerId":912,"parentId":464,'
                      '"recordId":%d,"subjectId":545},{"answerId":914,"parentId":464,"recordId":%d,"subjectId":546},'
                      '{"answerId":916,"parentId":464,"recordId":%d,"subjectId":548},{"answerId":918,"parentId":464,'
                      '"recordId":%d,"subjectId":549},{"answerId":920,"parentId":464,"recordId":%d,"subjectId":550},'
                      '{"answerId":922,"parentId":464,"recordId":%d,"subjectId":551},{"answerId":924,"parentId":464,'
                      '"recordId":%d,"subjectId":553},{"answerId":926,"parentId":464,"recordId":%d,"subjectId":555},'
                      '{"answerId":928,"parentId":464,"recordId":%d,"subjectId":557},{"answerId":930,"parentId":464,'
                      '"recordId":%d,"subjectId":559},{"answerId":932,"parentId":464,"recordId":%d,"subjectId":560},'
                      '{"answerId":934,"parentId":464,"recordId":%d,"subjectId":561},{"answerId":936,"parentId":464,'
                      '"recordId":%d,"subjectId":562},{"answerId":938,"parentId":563,"recordId":%d,"subjectId":565},'
                      '{"answerId":940,"parentId":563,"recordId":%d,"subjectId":567},{"answerId":942,"parentId":563,'
                      '"recordId":%d,"subjectId":569},{"answerId":944,"parentId":563,"recordId":%d,"subjectId":571},'
                      '{"answerId":947,"parentId":563,"recordId":%d,"subjectId":573},{"answerId":950,"parentId":563,'
                      '"recordId":%d,"subjectId":575},{"answerId":952,"parentId":563,"recordId":%d,"subjectId":576},'
                      '{"answerId":954,"parentId":563,"recordId":%d,"subjectId":578},{"answerId":956,"parentId":563,'
                      '"recordId":%d,"subjectId":579},{"answerId":958,"parentId":563,"recordId":%d,"subjectId":580},'
                      '{"answerId":960,"parentId":563,"recordId":%d,"subjectId":581},{"answerId":962,"parentId":563,'
                      '"recordId":%d,"subjectId":583},{"answerId":964,"parentId":563,"recordId":%d,"subjectId":585},'
                      '{"answerId":966,"parentId":563,"recordId":%d,"subjectId":586},{"answerId":968,"parentId":563,'
                      '"recordId":%d,"subjectId":587},{"answerId":970,"parentId":563,"recordId":%d,"subjectId":588},'
                      '{"answerId":973,"parentId":563,"recordId":%d,"subjectId":589},{"answerId":977,"parentId":563,'
                      '"recordId":%d,"subjectId":591},{"answerId":980,"parentId":563,"recordId":%d,"subjectId":593},'
                      '{"answerId":983,"parentId":563,"recordId":%d,"subjectId":595},{"answerId":985,"parentId":563,'
                      '"recordId":%d,"subjectId":596},{"answerId":987,"parentId":563,"recordId":%d,"subjectId":597},'
                      '{"answerId":990,"parentId":563,"recordId":%d,"subjectId":599},{"answerId":992,"parentId":563,'
                      '"recordId":%d,"subjectId":601},{"answerId":994,"parentId":563,"recordId":%d,"subjectId":603},'
                      '{"answerId":996,"parentId":563,"recordId":%d,"subjectId":605},{"answerId":998,"parentId":563,'
                      '"recordId":%d,"subjectId":607},{"answerId":1000,"parentId":563,"recordId":%d,"subjectId":609},'
                      '{"answerId":1015,"parentId":610,"recordId":%d,"subjectId":617},{"answerId":1026,"parentId":610,'
                      '"recordId":%d,"subjectId":624}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id)

        }
        res = self.agencies.calc_score(case_name="计算分数", param=param)
        print('请求返回数据：%s' % res.json())
        self.assertEqual(res.json()['detail'], 'success')

    def test_008(self):
        """上传评估结果"""
        id = self.record_id[0]
        param = {
            'name': 'assess_token',
            'userId': '86',
            'user2Id': '85',
            'conclusion': 'api测试数据：评估结果',
            'assessmentPhotos': '',
            'answer': '[{"answerId":1077,"parentId":610,"recordId":%d,"subjectId":618},{"answerId":719,"parentId":401,'
                      '"recordId":%d,"subjectId":403},{"answerId":1038,"parentId":464,"recordId":%d,"subjectId":538},'
                      '{"answerId":1094,"parentId":610,"recordId":%d,"subjectId":626},{"answerId":1036,"parentId":464,'
                      '"recordId":%d,"subjectId":631},{"answerId":1059,"parentId":610,"recordId":%d,"subjectId":612},'
                      '{"answerId":1084,"parentId":610,"recordId":%d,"subjectId":622},{"answerId":1079,"parentId":610,'
                      '"recordId":%d,"subjectId":620},{"answerId":1053,"parentId":416,"recordId":%d,"subjectId":500},'
                      '{"answerId":1066,"parentId":610,"recordId":%d,"subjectId":614},{"answerId":1091,"parentId":610,'
                      '"recordId":%d,"subjectId":625},{"answerId":1071,"parentId":610,"recordId":%d,"subjectId":615},'
                      '{"answerId":1049,"parentId":416,"recordId":%d,"subjectId":632},{"answerId":1034,"parentId":464,'
                      '"recordId":%d,"subjectId":536},{"answerId":744,"parentId":416,"recordId":%d,"subjectId":418},'
                      '{"answerId":1062,"parentId":610,"recordId":%d,"subjectId":613},{"answerId":1032,"parentId":627,'
                      '"recordId":%d,"subjectId":629},{"answerId":721,"parentId":401,"recordId":%d,"subjectId":481},'
                      '{"answerId":746,"parentId":416,"recordId":%d,"subjectId":486},{"answerId":748,"parentId":416,'
                      '"recordId":%d,"subjectId":487},{"answerId":725,"parentId":401,"recordId":%d,"subjectId":405},'
                      '{"answerId":750,"parentId":416,"recordId":%d,"subjectId":488},{"answerId":752,"parentId":416,'
                      '"recordId":%d,"subjectId":489},{"answerId":727,"parentId":401,"recordId":%d,"subjectId":482},'
                      '{"answerId":754,"parentId":416,"recordId":%d,"subjectId":490},{"answerId":756,"parentId":416,'
                      '"recordId":%d,"subjectId":491},{"answerId":731,"parentId":401,"recordId":%d,"subjectId":483},'
                      '{"answerId":758,"parentId":416,"recordId":%d,"subjectId":492},{"answerId":734,"parentId":401,'
                      '"recordId":%d,"subjectId":484},{"answerId":760,"parentId":416,"recordId":%d,"subjectId":493},'
                      '{"answerId":737,"parentId":401,"recordId":%d,"subjectId":409},{"answerId":763,"parentId":416,'
                      '"recordId":%d,"subjectId":494},{"answerId":740,"parentId":401,"recordId":%d,"subjectId":485},'
                      '{"answerId":766,"parentId":416,"recordId":%d,"subjectId":495},{"answerId":769,"parentId":416,'
                      '"recordId":%d,"subjectId":496},{"answerId":772,"parentId":416,"recordId":%d,"subjectId":497},'
                      '{"answerId":775,"parentId":416,"recordId":%d,"subjectId":498},{"answerId":778,"parentId":416,'
                      '"recordId":%d,"subjectId":420},{"answerId":781,"parentId":416,"recordId":%d,"subjectId":422},'
                      '{"answerId":790,"parentId":443,"recordId":%d,"subjectId":445},{"answerId":794,"parentId":443,'
                      '"recordId":%d,"subjectId":447},{"answerId":796,"parentId":443,"recordId":%d,"subjectId":501},'
                      '{"answerId":799,"parentId":443,"recordId":%d,"subjectId":502},{"answerId":801,"parentId":443,'
                      '"recordId":%d,"subjectId":449},{"answerId":803,"parentId":443,"recordId":%d,"subjectId":503},'
                      '{"answerId":805,"parentId":443,"recordId":%d,"subjectId":451},{"answerId":809,"parentId":443,'
                      '"recordId":%d,"subjectId":453},{"answerId":825,"parentId":443,"recordId":%d,"subjectId":455},'
                      '{"answerId":827,"parentId":443,"recordId":%d,"subjectId":504},{"answerId":829,"parentId":443,'
                      '"recordId":%d,"subjectId":457},{"answerId":831,"parentId":443,"recordId":%d,"subjectId":505},'
                      '{"answerId":833,"parentId":443,"recordId":%d,"subjectId":459},{"answerId":835,"parentId":443,'
                      '"recordId":%d,"subjectId":506},{"answerId":837,"parentId":443,"recordId":%d,"subjectId":461},'
                      '{"answerId":839,"parentId":443,"recordId":%d,"subjectId":507},{"answerId":841,"parentId":443,'
                      '"recordId":%d,"subjectId":463},{"answerId":843,"parentId":443,"recordId":%d,"subjectId":508},'
                      '{"answerId":845,"parentId":443,"recordId":%d,"subjectId":509},{"answerId":847,"parentId":443,'
                      '"recordId":%d,"subjectId":510},{"answerId":849,"parentId":443,"recordId":%d,"subjectId":511},'
                      '{"answerId":851,"parentId":443,"recordId":%d,"subjectId":512},{"answerId":853,"parentId":443,'
                      '"recordId":%d,"subjectId":513},{"answerId":855,"parentId":443,"recordId":%d,"subjectId":514},'
                      '{"answerId":857,"parentId":443,"recordId":%d,"subjectId":515},{"answerId":859,"parentId":443,'
                      '"recordId":%d,"subjectId":516},{"answerId":862,"parentId":464,"recordId":%d,"subjectId":466},'
                      '{"answerId":864,"parentId":464,"recordId":%d,"subjectId":517},{"answerId":866,"parentId":464,'
                      '"recordId":%d,"subjectId":468},{"answerId":868,"parentId":464,"recordId":%d,"subjectId":470},'
                      '{"answerId":870,"parentId":464,"recordId":%d,"subjectId":472},{"answerId":872,"parentId":464,'
                      '"recordId":%d,"subjectId":474},{"answerId":874,"parentId":464,"recordId":%d,"subjectId":476},'
                      '{"answerId":876,"parentId":464,"recordId":%d,"subjectId":478},{"answerId":878,"parentId":464,'
                      '"recordId":%d,"subjectId":480},{"answerId":880,"parentId":464,"recordId":%d,"subjectId":519},'
                      '{"answerId":882,"parentId":464,"recordId":%d,"subjectId":521},{"answerId":884,"parentId":464,'
                      '"recordId":%d,"subjectId":523},{"answerId":886,"parentId":464,"recordId":%d,"subjectId":525},'
                      '{"answerId":888,"parentId":464,"recordId":%d,"subjectId":527},{"answerId":890,"parentId":464,'
                      '"recordId":%d,"subjectId":529},{"answerId":892,"parentId":464,"recordId":%d,"subjectId":531},'
                      '{"answerId":894,"parentId":464,"recordId":%d,"subjectId":532},{"answerId":896,"parentId":464,'
                      '"recordId":%d,"subjectId":533},{"answerId":898,"parentId":464,"recordId":%d,"subjectId":534},'
                      '{"answerId":904,"parentId":464,"recordId":%d,"subjectId":540},{"answerId":906,"parentId":464,'
                      '"recordId":%d,"subjectId":541},{"answerId":908,"parentId":464,"recordId":%d,"subjectId":542},'
                      '{"answerId":910,"parentId":464,"recordId":%d,"subjectId":543},{"answerId":912,"parentId":464,'
                      '"recordId":%d,"subjectId":545},{"answerId":914,"parentId":464,"recordId":%d,"subjectId":546},'
                      '{"answerId":916,"parentId":464,"recordId":%d,"subjectId":548},{"answerId":918,"parentId":464,'
                      '"recordId":%d,"subjectId":549},{"answerId":920,"parentId":464,"recordId":%d,"subjectId":550},'
                      '{"answerId":922,"parentId":464,"recordId":%d,"subjectId":551},{"answerId":924,"parentId":464,'
                      '"recordId":%d,"subjectId":553},{"answerId":926,"parentId":464,"recordId":%d,"subjectId":555},'
                      '{"answerId":928,"parentId":464,"recordId":%d,"subjectId":557},{"answerId":930,"parentId":464,'
                      '"recordId":%d,"subjectId":559},{"answerId":932,"parentId":464,"recordId":%d,"subjectId":560},'
                      '{"answerId":934,"parentId":464,"recordId":%d,"subjectId":561},{"answerId":936,"parentId":464,'
                      '"recordId":%d,"subjectId":562},{"answerId":938,"parentId":563,"recordId":%d,"subjectId":565},'
                      '{"answerId":940,"parentId":563,"recordId":%d,"subjectId":567},{"answerId":942,"parentId":563,'
                      '"recordId":%d,"subjectId":569},{"answerId":944,"parentId":563,"recordId":%d,"subjectId":571},'
                      '{"answerId":947,"parentId":563,"recordId":%d,"subjectId":573},{"answerId":950,"parentId":563,'
                      '"recordId":%d,"subjectId":575},{"answerId":952,"parentId":563,"recordId":%d,"subjectId":576},'
                      '{"answerId":954,"parentId":563,"recordId":%d,"subjectId":578},{"answerId":956,"parentId":563,'
                      '"recordId":%d,"subjectId":579},{"answerId":958,"parentId":563,"recordId":%d,"subjectId":580},'
                      '{"answerId":960,"parentId":563,"recordId":%d,"subjectId":581},{"answerId":962,"parentId":563,'
                      '"recordId":%d,"subjectId":583},{"answerId":964,"parentId":563,"recordId":%d,"subjectId":585},'
                      '{"answerId":966,"parentId":563,"recordId":%d,"subjectId":586},{"answerId":968,"parentId":563,'
                      '"recordId":%d,"subjectId":587},{"answerId":970,"parentId":563,"recordId":%d,"subjectId":588},'
                      '{"answerId":973,"parentId":563,"recordId":%d,"subjectId":589},{"answerId":977,"parentId":563,'
                      '"recordId":%d,"subjectId":591},{"answerId":980,"parentId":563,"recordId":%d,"subjectId":593},'
                      '{"answerId":983,"parentId":563,"recordId":%d,"subjectId":595},{"answerId":985,"parentId":563,'
                      '"recordId":%d,"subjectId":596},{"answerId":987,"parentId":563,"recordId":%d,"subjectId":597},'
                      '{"answerId":990,"parentId":563,"recordId":%d,"subjectId":599},{"answerId":992,"parentId":563,'
                      '"recordId":%d,"subjectId":601},{"answerId":994,"parentId":563,"recordId":%d,"subjectId":603},'
                      '{"answerId":996,"parentId":563,"recordId":%d,"subjectId":605},{"answerId":998,"parentId":563,'
                      '"recordId":%d,"subjectId":607},{"answerId":1000,"parentId":563,"recordId":%d,"subjectId":609},'
                      '{"answerId":1015,"parentId":610,"recordId":%d,"subjectId":617},{"answerId":1026,"parentId":610,'
                      '"recordId":%d,"subjectId":624}]'
                      % (id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id,
                         id, id, id, id, id, id, id, id, id, id, id)
        }
        res = self.agencies.save_answer(case_name="上传评估结果", param=param)
        print('请求返回数据：%s' % res.json())
        self.assertEqual(res.json()['detail'], 'success')

    @classmethod
    def tearDownClass(cls):
        Logger().info("------------------------ 日照评估 END------------------------")
        print("------------------------ 日照评估 END------------------------")


if __name__ == "__main__":
    unittest.main()