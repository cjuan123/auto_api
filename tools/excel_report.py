# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: excel_report.py
@time: 2019/7/8 16:43
@desc：
"""
import xlsxwriter


class ExcelReport(object):

    def __init__(self):
        self.workbook = xlsxwriter.Workbook("excel_report.xlsx")
        self.sheet_profile = self.workbook.add_worksheet("测试总况")
        self.sheet_info = self.workbook.add_worksheet("测试详情")

    # 表头样式
    def head_1_format(self):
        self.workbook.add_format({'align': 'center', 'valign': 'vcenter', "bold": 1, "font_size": 18})

    def head_2_format(self):
        self.workbook.add_format({"bold": 1, 'align': 'center', 'valign': 'vcenter'})

    # 数据样式
    def data_format(self):
        self.workbook.add_format({'align': 'center', 'valign': 'vcenter'})

    # 设置列宽度
    def set_column_width(self, worksheet):
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)

    # 设置行高度
    def set_rows_heigh(self, worksheet):
        worksheet.set_default_row(30)

    # 生成饼图
    def chart_pie(self, worksheet):
        chart = self.workbook.add_chart({"type": "pie"})
        chart.add_series({
            "name": "测试用例统计",
            "categories": "=测试总况!$D$5:$D$6",
            "values": "=测试总况!$E$5:$E$6",
        })
        chart.set_title({"name": "测试统计"})
        chart.set_style(10)
        worksheet.insert_chart("A9", chart, {"x_offset": 25, "y_offset": 10})

    # 测试概况
    def test_profile(self, worksheet, data):
        # 合并单元格
        worksheet.merge_range("A1:F1", "测试报告总概况", self.head_1_format())
        worksheet.merge_range("A2:F2", "测试概括", self.head_1_format())

        # 表头
        worksheet.merge_range("A3:A6", "测试", self.head_2_format())
        worksheet.write("B3", "项目名称", self.head_2_format())
        worksheet.write("B4", "接口版本", self.head_2_format())
        worksheet.write("B5", "脚本语言", self.head_2_format())
        worksheet.write("B6", "测试网络", self.head_2_format())

        worksheet.write("D3", "接口总数", self.head_2_format())
        worksheet.write("D4", "测试日期", self.head_2_format())
        worksheet.write("D5", "通过总数", self.head_2_format())
        worksheet.write("D6", "失败总数", self.head_2_format())

        # 给单元格写入数据
        worksheet.write("C3", data["test_name"], self.data_format())
        worksheet.write("C4", data["test_version"], self.data_format())
        worksheet.write("C5", data["test_language"], self.data_format())
        worksheet.write("C6", data["test_net"], self.data_format())

        worksheet.write("E3", data["test_sum"], self.data_format())
        worksheet.write("E4", data["test_data"], self.data_format())
        worksheet.write("E5", data["test_success"], self.data_format())
        worksheet.write("E6", data["test_failed"], self.data_format())

    # 测试详情
    def test_info(self, worksheet, data):
        worksheet.merge_range("A1:H1", "测试详情", self.head_1_format())
        worksheet.write("A2", "用例ID", self.head_2_format())
        worksheet.write("B2", "接口名称", self.head_2_format())
        worksheet.write("C2", "接口协议", self.head_2_format())
        worksheet.write("D2", "接口地址", self.head_2_format())
        worksheet.write("E2", "参数", self.head_2_format())
        worksheet.write("F2", "预期结果", self.head_2_format())
        worksheet.write("G2", "实际结果", self.head_2_format())
        worksheet.write("H2", "测试结果", self.head_2_format())

        temp = 3
        for item in data["info"]:
            worksheet.write("A" + str(temp), item["t_id"], self.data_format())

            worksheet.write("B" + str(temp), item["t_name"], self.data_format())
            worksheet.write("C" + str(temp), item["t_method"], self.data_format())
            worksheet.write("D" + str(temp), item["t_param"], self.data_format())
            worksheet.write("E" + str(temp), item["t_url"], self.data_format())
            worksheet.write("F" + str(temp), item["t_hope"], self.data_format())
            worksheet.write("G" + str(temp), item["t_actual"], self.data_format())
            worksheet.write("H" + str(temp), item["t_result"], self.data_format())
            temp = temp + 1

    # 关闭excel文件
    def close(self):
        self.workbook.close()
