#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

from PageLocators.Web.Pay import Pay
from Common.BasePage import BasePage


class PayPage(BasePage):

    # 更换支付方式
    def replace_pay(self, text=""):
        doc = text + "点击【更换支付方式】按钮-"
        self.click_element(Pay.replace_pay, doc=doc)

    # 易贝
    def cbp_pay(self, text=""):
        doc = text + "点击【易贝】选项-"
        self.click_element(Pay.cbp_pay, doc=doc)

    # 易贝券
    def voucher_pay(self, text=""):
        doc = text + "点击【易贝券】选项-"
        self.click_element(Pay.voucher_pay, doc=doc)

    # 抵工资
    def wages_pay(self, text=""):
        doc = text + "点击【抵工资】选项-"
        self.click_element(Pay.wages_pay, doc=doc)

    # 家人购
    def family_pay(self, text=""):
        doc = text + "点击【家人购】选项-"
        self.click_element(Pay.family_pay, doc=doc)

    # 现金
    def cash_pay(self, text=""):
        doc = text + "点击【现金】选项-"
        self.click_element(Pay.cash_pay, doc=doc)

    # 微信
    def wechat_pay(self, text=""):
        doc = text + "点击【微信】选项-"
        self.click_element(Pay.wechat_pay, doc=doc)

    # # 支付宝
    # def alibaba_pay(self, text=""):
    #     doc = text + "点击【支付宝】选项-"
    #     self.click_element(Pay.alibaba_pay, doc=doc)

    # 确认支付
    def confirm_pay(self, text=""):
        doc = text + "点击【确认支付】按钮-"
        self.click_element(Pay.confirm_pay, doc=doc)

    #支付
    def payment_method(self, payment_method, text=""):
        if payment_method != "易贝":
            # 点击更换支付方式
            self.replace_pay(text)
            if payment_method == "易贝券":
                self.voucher_pay(text)
            elif payment_method == "抵工资":
                self.wages_pay(text)
            elif payment_method == "家人购":
                self.family_pay(text)
            elif payment_method == "现金":
                # 选择支付方式
                self.cash_pay(text)
            elif payment_method == "微信":
                self.wechat_pay(text)
            # elif payment_method == "支付宝":
            #     self.alibaba_pay(text)

        self.confirm_pay(text)
        self.pay_password(text)
