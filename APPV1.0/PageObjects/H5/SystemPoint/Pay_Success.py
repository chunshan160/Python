#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

'''
支付成功-系统提示页面
'''
import time

from PageLocators.H5.SystemPoint.Pay_Success import *
from Common.BasePage import BasePage


# 支付成功
class PaySuccessPage(BasePage):

    # 加入焕商
    def join(self,text=""):
        doc=text+"点击【加入焕商】按钮-"
        self.click_element(join,doc=doc)

    # 关闭弹窗
    def close_windows(self,text=""):
        doc=text+"关闭弹窗-"
        time.sleep(2)
        if self.get_element(close_pop_ups, doc=doc):
            self.click_element(close_pop_ups,doc=doc)

    # 支付成功
    def title_text(self,text=""):
        doc=text+"获取【支付成功】文本-"
        return self.get_text(title,doc=doc)

    # 支付方式
    def pay_method_text(self,text=""):
        doc=text+"获取【支付方式】文本-"
        return self.get_text(pay_method,doc=doc)

    # 支付金额
    def pay_money_text(self,text=""):
        doc=text+"获取【支付金额】文本-"
        return self.get_text(pay_money,doc=doc)

    # 支付服务费
    def pay_service_text(self,text=""):
        doc=text+"获取【支付服务费】文本-"
        return self.get_text(pay_service,doc=doc)

    # 查看订单
    def look_order(self,text=""):
        doc=text+"点击【查看订单】按钮-"
        self.click_element(look_order,doc=doc)

    # 返回首页
    def return_home(self,text=""):
        doc=text+"点击【返回首页】按钮-"
        self.click_element(return_home,doc=doc)
