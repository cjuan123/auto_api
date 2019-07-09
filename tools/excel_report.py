# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: excel_report.py
@time: 2019/7/8 16:43
@desc：excel测试报告
"""
import xlsxwriter
import time, os
from tools.file_path import FilePath


class ExcelReport(object):

    def __init__(self):
        self.path = os.path.join(FilePath().reports_path(), "test_reports_%s.xlsx" % time.strftime('%Y_%m_%d'))
        self.workbook = xlsxwriter.Workbook(self.path)
        # self.workbook = xlsxwriter.Workbook("excel_report.xlsx")
        self.sheet_profile = self.workbook.add_worksheet("测试总况")
        self.sheet_info = self.workbook.add_worksheet("测试详情")

    # 表头样式
    def head_1_format(self):
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter', "border": 3, "bold": 1,
                                         "font_size": 18})

    def head_2_format(self):
        return self.workbook.add_format({"bold": 1, 'align': 'center', 'valign': 'vcenter', "border": 3,
                                         "font_size": 15, 'bg_color': '#B4EEB4'})

    # 数据样式
    def data_format(self):
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter', "border": 1})

    def data_format_fail(self):
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bg_color': '#CD5B45', "border": 1})

    def data_format_success(self):
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bg_color': '#87CEEB', "border": 1})

    # 设置列宽度
    def set_column_width(self, worksheet):
        worksheet.set_column("A:A", 20)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)

    # 设置行高度
    def set_rows_heigh(self, worksheet):
        worksheet.set_default_row(30)

    # 生成饼图
    def chart_pie(self):
        chart = self.workbook.add_chart({"type": "pie"})
        chart.add_series({
            "name": "测试用例统计",
            "categories": "=测试总况!$D$5:$D$6",
            "values": "=测试总况!$E$5:$E$6",
        })
        chart.set_title({"name": "测试统计"})
        chart.set_style(10)
        self.sheet_profile.insert_chart("A9", chart, {"x_offset": 200, "y_offset": 10})

    # 测试概况
    def test_profile(self, data):
        self.set_rows_heigh(self.sheet_profile)
        self.set_column_width(self.sheet_profile)

        self.chart_pie()

        # 合并单元格
        self.sheet_profile.merge_range("A1:F1", "测试报告总概况", self.head_1_format())
        self.sheet_profile.merge_range("A2:F2", "测试概括", self.head_1_format())

        # 表头
        self.sheet_profile.merge_range("A3:A6", "接口测试", self.head_2_format())
        self.sheet_profile.write("B3", "项目名称", self.head_2_format())
        self.sheet_profile.write("B4", "接口版本", self.head_2_format())
        self.sheet_profile.write("B5", "脚本语言", self.head_2_format())
        self.sheet_profile.write("B6", "测试环境", self.head_2_format())

        self.sheet_profile.write("D3", "测试日期", self.head_2_format())
        self.sheet_profile.write("D4", "接口总数", self.head_2_format())
        self.sheet_profile.write("D5", "通过总数", self.head_2_format())
        self.sheet_profile.write("D6", "失败总数", self.head_2_format())

        self.sheet_profile.write("F3", "花费时间", self.head_2_format())

        # 给单元格写入数据
        self.sheet_profile.write("C3", data["test_name"], self.data_format())
        self.sheet_profile.write("C4", data["test_version"], self.data_format())
        self.sheet_profile.write("C5", data["test_language"], self.data_format())
        self.sheet_profile.write("C6", data["test_net"], self.data_format())

        self.sheet_profile.write("E3", data["test_date"], self.data_format())
        self.sheet_profile.write("E4", data["test_sum"], self.data_format())
        self.sheet_profile.write("E5", data["test_success"], self.data_format())
        self.sheet_profile.write("E6", data["test_failed"], self.data_format())

        self.sheet_profile.merge_range("F4:F6", data["test_time"], self.data_format())

    # 测试详情
    def test_info(self, data):
        self.set_rows_heigh(self.sheet_info)
        self.set_column_width(self.sheet_info)
        self.sheet_info.merge_range("A1:H1", "测试详情", self.head_1_format())
        self.sheet_info.write("A2", "模块", self.head_2_format())
        self.sheet_info.write("B2", "用例ID", self.head_2_format())
        self.sheet_info.write("C2", "用例名称", self.head_2_format())
        self.sheet_info.write("D2", "请求方法", self.head_2_format())
        self.sheet_info.write("E2", "请求参数", self.head_2_format())
        self.sheet_info.write("F2", "预期结果", self.head_2_format())
        self.sheet_info.write("G2", "实际结果", self.head_2_format())
        self.sheet_info.write("H2", "测试结果", self.head_2_format())
        # self.sheet_info.write("H2", "测试结果", self.head_2_format())

        temp = 3
        for num in range(len(data)):
            self.sheet_info.write("A" + str(temp), data[num]["t_moudle"], self.data_format())
            self.sheet_info.write("B" + str(temp), data[num]["t_id"], self.data_format())
            self.sheet_info.write("C" + str(temp), data[num]["t_name"], self.data_format())
            self.sheet_info.write("D" + str(temp), data[num]["t_method"], self.data_format())
            self.sheet_info.write("E" + str(temp), data[num]["t_param"], self.data_format())
            self.sheet_info.write("F" + str(temp), data[num]["t_hope"], self.data_format())
            self.sheet_info.write("G" + str(temp), data[num]["t_actual"], self.data_format())
            if data[num]["t_result"] == "通过":
                self.sheet_info.write("H" + str(temp), data[num]["t_result"], self.data_format_success())
            else:
                self.sheet_info.write("H" + str(temp), data[num]["t_result"], self.data_format_fail())
            temp += 1

    # 关闭excel文件
    def close(self):
        self.workbook.close()


if __name__ == '__main__':
    e = ExcelReport()

    e.test_profile(data={"test_name": "智商", "test_version": "v2.0.8", "test_language": "python 3.0", "test_net": "wifi",
                         "test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"})
    e.close()