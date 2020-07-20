#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

'''
支付成功-系统提示页面
'''

from PageLocators.H5.SystemPoint.Pay_Success import *
from Common.find_element import FindElement


# 支付成功
class PaySuccessPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 加入焕商
    def get_join_element(self):
        return self.fd.find_element(join)

    # 关闭弹窗
    def get_close_elements(self):
        return self.fd.find_element(close_pop_ups)

    # 支付成功
    def get_title_element(self):
        return self.fd.find_element(title)

    # 支付方式
    def get_pay_method_element(self):
        return self.fd.find_element(pay_method)

    # 支付金额
    def get_pay_money_element(self):
        return self.fd.find_element(pay_money)

    # 支付服务费
    def get_pay_service_element(self):
        return self.fd.find_element(pay_service)

    # 查看订单
    def get_look_order_element(self):
        return self.fd.find_element(look_order)

    # 返回首页
    def get_return_home_element(self):
        return self.fd.find_element(return_home)
