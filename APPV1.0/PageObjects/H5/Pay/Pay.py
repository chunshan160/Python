#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

from PageLocators.H5.Pay import Pay
from Common.BasePage import BasePage


class PayPage(BasePage):

    def __init__(self, driver):
        self.driver=driver

    # 更换支付方式
    def replace_pay(self):
        self.get_element(Pay.replace_pay).click()

    # 易贝
    def cbp_pay(self):
        self.get_element(Pay.cbp_pay).click()

    # 易贝券
    def voucher_pay(self):
        self.get_element(Pay.voucher_pay).click()

    # 抵工资
    def wages_pay(self):
        self.get_element(Pay.wages_pay).click()

    #家人购
    def family_pay(self):
        self.get_element(Pay.family_pay).click()

    # 现金
    def cash_pay(self):
        self.get_element(Pay.cash_pay).click()

    # 微信
    def wechat_pay(self):
        self.get_element(Pay.wechat_pay).click()

    # 支付宝
    def alibaba_pay(self):
        self.get_element(Pay.alibaba_pay).click()

    # 确认支付
    def confirm_pay(self):
        self.get_element(Pay.confirm_pay).click()

    # 易贝-支付
    def click_cbp_pay(self):
        self.confirm_pay()
        self.pay_password()

    # 易贝券-支付
    def click_voucher_pay(self):
        self.replace_pay()
        self.voucher_pay()
        self.confirm_pay()
        self.pay_password()

    # 抵工资-支付
    def click_wages_pay(self):
        self.replace_pay()
        self.wages_pay()
        self.confirm_pay()
        self.pay_password()

    # 家人购-支付
    def click_family_pay(self):
        self.replace_pay()
        self.family_pay()
        self.confirm_pay()
        self.pay_password()

    # 现金-支付
    def click_cash_pay(self):
        self.replace_pay()
        self.cash_pay()
        self.confirm_pay()
        self.pay_password()

    # 微信-支付
    def click_wechat_pay(self):
        self.replace_pay()
        self.wechat_pay()
        self.confirm_pay()
        self.pay_password()

    # 支付宝-支付
    def click_alibaba_pay(self):
        self.replace_pay()
        self.alibaba_pay()
        self.confirm_pay()
        self.pay_password()

    # 输入支付密码
    def pay_password(self):
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)
        self.driver.keyevent(11)
        self.driver.keyevent(12)
        self.driver.keyevent(13)
