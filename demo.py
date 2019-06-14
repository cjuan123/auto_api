"""
@version: 1.0
@author: chenj
@file: demo.py
@time: 2019/5/19 10:43
"""
import unittest
import ddt
import ddt_tool

@ddt.ddt
class Demo(unittest.TestCase):

    @ddt.data(*ddt_tool.data())
    def test(self, name):
        print(name[4])


if __name__ == '__main__':
    unittest.main()