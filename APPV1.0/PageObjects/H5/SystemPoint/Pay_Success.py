#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

'''
支付成功-系统提示页面
'''

from PageLocators.H5.SystemPoint.Pay_Success import *
from Common.BasePage import BasePage


# 支付成功
class PaySuccessPage(BasePage):



    # 加入焕商
    def join(self):
        self.get_element(join).click()

    # 关闭弹窗
    def close_windows(self):
        self.get_element(close_pop_ups).click()

    # 支付成功
    def title_text(self):
        return self.get_element(title).text

    # 支付方式
    def pay_method_text(self):
        return self.get_element(pay_method).text

    # 支付金额
    def pay_money_text(self):
        return self.get_element(pay_money).text

    # 支付服务费
    def pay_service_text(self):
        return self.get_element(pay_service).text

    # 查看订单
    def look_order(self):
        self.get_element(look_order).click()

    # 返回首页
    def return_home(self):
        self.get_element(return_home).click()
