#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

from PageLocators.H5.Pay import Pay
from Common.find_element import FindElement


class PayPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 更换支付方式
    def get_replace_pay_element(self):
        return self.fd.find_element(Pay.replace_pay)

    # 易贝
    def get_cbp_pay_element(self):
        return self.fd.find_element(Pay.cbp_pay)

    # 易贝券
    def get_voucher_pay_element(self):
        return self.fd.find_element(Pay.voucher_pay)

    # 抵工资
    def get_wages_pay_element(self):
        return self.fd.find_element(Pay.wages_pay)

    #家人购
    def get_family_pay_element(self):
        return self.fd.find_element(Pay.family_pay)

    # 现金
    def get_cash_pay_element(self):
        return self.fd.find_element(Pay.cash_pay)

    # 微信
    def get_wechat_pay_element(self):
        return self.fd.find_element(Pay.wechat_pay)

    # 支付宝
    def get_alibaba_pay_element(self):
        return self.fd.find_element(Pay.alibaba_pay)

    # 确认支付
    def get_confirm_pay_element(self):
        return self.fd.find_element(Pay.confirm_pay)
