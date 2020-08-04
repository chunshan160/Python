#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

import time
from PageObjects.H5.Pay.Pay import PayPage


class PayHandle:

    def __init__(self, driver):
        self.pay_p = PayPage(driver)

    # 更换支付方式
    def click_replace_pay(self):
        time.sleep(1)
        self.pay_p.get_replace_pay_element().click()

    # 易贝
    def click_cbp_pay(self):
        time.sleep(0.5)
        self.pay_p.get_cbp_pay_element().click()

    # 易贝券
    def click_voucher_pay(self):
        time.sleep(0.5)
        self.pay_p.get_voucher_pay_element().click()

    # 抵工资
    def click_wages_pay(self):
        time.sleep(0.5)
        self.pay_p.get_wages_pay_element().click()

    # 家人购
    def click_family_pay(self):
        time.sleep(0.5)
        self.pay_p.get_family_pay_element().click()

    # 现金
    def click_cash_pay(self):
        time.sleep(0.5)
        self.pay_p.get_cash_pay_element().click()

    # 微信
    def click_wechat_pay(self):
        time.sleep(0.5)
        self.pay_p.get_wechat_pay_element().click()

    # 支付宝
    def click_alibaba_pay(self):
        time.sleep(0.5)
        self.pay_p.get_alibaba_pay_element().click()

    # 确认支付
    def click_confirm_pay(self):
        time.sleep(1)
        self.pay_p.get_confirm_pay_element().click()
