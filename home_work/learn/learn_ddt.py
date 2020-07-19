#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/9 14:16
# @Author :春衫
# @File :learn_ddt.py


# ddt ddt+unittest 来进行数据的处理第三方库
# 装饰器 会在你的函数运行之前运行

import unittest
from ddt import ddt, data, unpack

test_data = [1, 3]
test_data_2 = [[1, 3], [4, 5]]
test_data_3 = [[1, 3, 7], [4, 5, 8]]
test_data_4 = [{"No": "1", "Name": "小白"}, {"No": "2", "Name": "小黄"}]


# unpack  根据逗号进行拆分  必须一一对应赋值
# 如果unpack后的参数 少于5个 推荐用unpack  要注意参数不对等的情况

@ddt  # 装饰测试类
class TestMath(unittest.TestCase):

    # @data(*test_data)  # *args  脱外套 拆解 拿到几个数据 就执行几条用例
    # def test_print_data(self, item):  # 测试用例
    #     print("item", item)

    # @data(*test_data_2)  # *args  脱外套 一层 拆解 拿到几个数据 就执行几条用例
    # def test_print_data(self, item):  # 测试用例
    #     print("item", item)

    # @data(*test_data_3)  # *args  脱外套 拆解 拿到几个数据 就执行几条用例
    # # 拆成 [1, 3, 7],[4, 5, 8] 两个值  运行两次
    # @unpack
    # # 根据逗号拆分 第一次1、3、7  第二次4、5、8    每次必须要用三个变量来接受
    # def test_print_data(self, a, b, c):  # 测试用例
    #     print("a", a, "b", b)
    #     print("a:", a, " b:", b, " c:", c)

    @data(*test_data_4)
    def test_print_data(self, a):
        print("No", a["No"])
        print("Name", a["Name"])

    ##如果你要对字典进行unpack 参数名要与你的字典key对应
    # @data(*test_data_4)
    # @unpack
    # def test_print_data(self, No, Name):
    #     print("No", No, "Name", Name)
