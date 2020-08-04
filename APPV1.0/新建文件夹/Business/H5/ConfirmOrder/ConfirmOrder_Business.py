#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Business.py


from Handle.H5.ConfirmOrder.ConfirmOrder_Handle import ConfirmOrderHandle

class ConfirmOrderBusiness:

    def __init__(self, driver):
        self.confirm_order_h = ConfirmOrderHandle(driver)

    #确认订单
    def confirm_order(self):
        self.click_submit_order()

    # 选择收货地址
    def click_select_address(self):
        self.confirm_order_h.click_select_address()

    # 新建地址
    def click_new_address(self):
        self.confirm_order_h.click_new_address()

    # 管理地址
    def click_manage_address(self):
        self.confirm_order_h.click_manage_address()

    # 默认地址
    def click_default_address(self):
        self.confirm_order_h.click_default_address()

    # 优惠券
    def click_coupon(self):
        self.confirm_order_h.click_coupon()

    # 买家留言
    def click_buyer_message(self):
        self.confirm_order_h.click_buyer_message()

    # 提交订单
    def click_submit_order(self):
        self.confirm_order_h.click_submit_order()
