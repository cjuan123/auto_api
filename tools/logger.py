# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: logger.py
@time: 2019/6/13 17:24
@desc：日志类
"""
import logging, os, time
from tools.file_path import FilePath


class Logger:

    file_path = FilePath()

    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    log_path = os.path.join(file_path.log_path(), "%s.log" % time.strftime('%Y_%m_%d'))
    # handler = logging.FileHandler(r"F:\auto_api\logs\log.txt", encoding="utf-8")
    handler = logging.FileHandler(log_path, encoding="utf-8")

    def write_info(self):
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def info(self, message):
        self.write_info()
        self.logger.info(message)

    def debug(self, message):
        self.write_info()
        self.logger.debug(message)

    def warning(self, message):
        self.write_info()
        self.logger.warning(message)

    def error(self, message):
        self.write_info()
        self.logger.error(message)
