#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py


from Handle.H5.Pay.Pay_Handle import PayHandle


class PayBusiness:

    def __init__(self, driver):
        self.driver=driver
        self.pay_h = PayHandle(driver)

    # 更换支付方式
    def click_replace_pay(self):
        self.pay_h.click_replace_pay()

    # 易贝
    def click_cbp_pay(self):
        self.click_confirm_pay()
        self.pay_password()

    # 易贝券
    def click_voucher_pay(self):
        self.click_replace_pay()
        self.pay_h.click_voucher_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 抵工资
    def click_wages_pay(self):
        self.click_replace_pay()
        self.pay_h.click_wages_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 家人购
    def click_family_pay(self):
        self.click_replace_pay()
        self.pay_h.click_family_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 现金
    def click_cash_pay(self):
        self.click_replace_pay()
        self.pay_h.click_cash_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 微信
    def click_wechat_pay(self):
        self.click_replace_pay()
        self.pay_h.click_wechat_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 支付宝
    def click_alibaba_pay(self):
        self.click_replace_pay()
        self.pay_h.click_alibaba_pay()
        self.click_confirm_pay()
        self.pay_password()

    # 确认支付
    def click_confirm_pay(self):
        self.pay_h.click_confirm_pay()

    def pay_password(self):
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)
        self.driver.keyevent(11)
        self.driver.keyevent(12)
        self.driver.keyevent(13)


