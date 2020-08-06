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
        self.click_element(join)

    # 关闭弹窗
    def close_windows(self):
        self.click_element(close_pop_ups)

    # 支付成功
    def title_text(self):
        return self.get_text(title)

    # 支付方式
    def pay_method_text(self):
        return self.get_text(pay_method)

    # 支付金额
    def pay_money_text(self):
        return self.get_text(pay_money)

    # 支付服务费
    def pay_service_text(self):
        return self.get_text(pay_service)

    # 查看订单
    def look_order(self):
        self.click_element(look_order)

    # 返回首页
    def return_home(self):
        self.click_element(return_home)
