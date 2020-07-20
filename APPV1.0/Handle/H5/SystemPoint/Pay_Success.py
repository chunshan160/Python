#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

'''
支付成功-系统提示页面
'''
import time

from PageObjects.H5.SystemPoint.Pay_Success import PaySuccessPage


# 提交审核成功
class PaySuccessHandle:

    def __init__(self, driver):
        self.pay_success_p = PaySuccessPage(driver)

    # 加入焕商
    def click_join(self):
        self.pay_success_p.get_join_element().click()

    # 关闭弹窗
    def click_close(self):
        time.sleep(1)
        self.pay_success_p.get_close_elements().click()

    # 支付成功
    def get_title(self):
        try:
            text = self.pay_success_p.get_title_element().text
            return text
        except:
            print("没有找到【支付成功】这个元素")

    # 支付方式
    def get_pay_method(self):
        try:
            text = self.pay_success_p.get_pay_method_element().text
            return text
        except:
            print("没有找到【支付方式】这个元素")

    # 支付金额
    def get_pay_money(self):
        try:
            text = self.pay_success_p.get_pay_money_element().text
            return text
        except:
            print("没有找到【支付金额】这个元素")

    # 支付服务费
    def get_pay_service(self):
        try:
            text = self.pay_success_p.get_pay_service_element().text
            return text
        except:
            print("没有找到【支付服务费】这个元素")

    # 查看订单
    def click_look_order(self):
        self.pay_success_p.get_look_order_element().click()

    # 返回首页
    def click_return_home(self):
        self.pay_success_p.get_return_home_element().click()
