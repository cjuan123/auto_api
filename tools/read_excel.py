"""
@version: 1.0
@author: chenj
@file: read_excel.py
@time: 2019/5/19 16:03
@desc: 读取excel工具类
"""
import xlrd
import os
from tools.file_path import FilePath


class ReadExcel:

    def __init__(self, excel_path, sheet_name):
        self.root_path = FilePath().excel_path()
        self.path = os.path.join(self.root_path, excel_path)
        # 打开excel文件
        work_book = xlrd.open_workbook(self.path, encoding_override="utf-8")
        self.data_sheet = work_book.sheet_by_name(sheet_name)

    def row_num(self):
        """获取行数"""
        row_num = self.data_sheet.nrows  # 行数
        return int(row_num)

    def col_num(self):
        """获取列数"""
        col_num = self.data_sheet.ncols  # 列数
        return col_num

    def row_values(self):
        row_values = []
        for num in range(1, self.row_num()):
            row_values.append(self.data_sheet.row_values(num))
        return row_values

    def row_value(self, api_name):
        row_values = []
        for num in range(1, len(self.data_sheet.col_values(1))):
            if self.data_sheet.row_values(num)[1] == api_name:
                row_values.append(self.data_sheet.row_values(num))
        return row_values

    def col_values(self):
        col_values = []
        for num in range(1, self.col_num()):
            col_values.append(self.data_sheet.col_values(num))
        return col_values

    def col_value(self):
        col_values = []
        for num in range(1, len(self.data_sheet.col_values(1))):
            if self.data_sheet.row_values(num)[1] == "get_user_by_id_card":
                print(self.data_sheet.row_values(num))





# excel_dir = "case_data.xlsx"
# readExcel = ReadExcel(excel_dir, "cater")
# # readExcel.row_value()
# # print(readExcel.row_value()[0][1])
#
# readExcel.col_value()