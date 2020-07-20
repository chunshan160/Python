#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

'''
支付成功-系统提示页面
'''

import time
from Handle.H5.SystemPoint.Pay_Success import PaySuccessHandle


# 提交审核成功
class PaySuccessBusiness:

    def __init__(self, driver):
        self.pay_success_h = PaySuccessHandle(driver)

    # 加入焕商
    def click_join(self):
        self.pay_success_h.click_join()

    # 关闭弹窗
    def click_closes(self):
        self.pay_success_h.click_close()

    # 支付成功
    def get_title(self):
        time.sleep(2)
        text = self.pay_success_h.get_title()
        if text == "支付成功":
            return True
        else:
            return False

    '''
    暂时先不考虑支付金额的校验
    # 支付方式
    def get_pay_method(self):
        time.sleep(2)
        text = self.pay_success_h.get_pay_method()
        if text == "支付成功":
            return True
        else:
            return False

    # 支付金额
    def get_pay_money(self):
        time.sleep(2)
        text = self.pay_success_h.get_pay_money()
        if text == "支付成功":
            return True
        else:
            return False

    # 支付服务费
    def get_pay_service(self):
        time.sleep(2)
        text = self.pay_success_h.get_pay_service()
        if text == "支付成功":
            return True
        else:
            return False
    '''

    # 查看订单
    def click_look_order(self):
        self.pay_success_h.click_look_order()

    # 返回首页
    def click_return_home(self):
        self.pay_success_h.click_return_home()
