# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: ddt_tool.py
@time: 2019/6/14 16:28
@desc：
"""
from tools.read_excel import ReadExcel


def excel_data():
    case_data = []
    read_excel = ReadExcel("case_data.xlsx")
    values = read_excel.row_value()
    for i in range(values.__len__()):
        case_data.append(values[i])
    return case_data


