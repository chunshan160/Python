#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/4 19:01
# @Author :春衫
# @File :unit_testing.py

# 接口测试的本质  就是测试类里面的函数  通过数据驱动
# 单元测试的本质  测试函数代码级别  通过代码级别
# 单元测试的框架 unittest+request  pytest+WEB--》 request
# pytest+jenkins+allure

# 功能测试
# 写用例  TestCase
# 执行用例  1: TestSuite 存储用例  2:TestLoader 找用例，加载用例，存到1TestSuite里面
# 对比实际结果和期望结果  判断用例是否通过  #断言 Assert
# 出具测试报告  TextTestRunner

import unittest
from home_work.learn.math_method import MathMethod


class TestMathMethod(unittest.TestCase):  # 继承 unittest里面的TestCase专门来写用例
    # 编写测试用例
    # 1:一个用例就是一个函数 不能传参  只有self关键字
    # 2:所有的用例 (所有的函数都是test开头 test_1)
    def test_add_two_positive(self):  # 两个正数相加 1+1
        res = MathMethod(1, 1).add()
        print("1+1的结果是：", res)
        # 断言
        try:  # 异常处理
            self.assertEqual(3, res, "两个1相加出错了！")
        except AssertionError as e:
            print("出错啦！断言错误是{0}".format(e))
            raise e  # 异常处理完后记得抛出


if __name__ == '__main__':
    unittest.main()
