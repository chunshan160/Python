#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

from PageLocators.H5.ConfirmOrder import ConfirmOrder as CO
from Common.BasePage import BasePage

class ConfirmOrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 选择收货地址
    def select_address(self):
        self.get_element(CO.select_address).click()

    # 新建地址
    def new_address(self):
        self.get_element(CO.new_address).click()

    #填写收货地址信息
    def input_address(self):
        pass

    #选择收货地址
    def choose_address(self):
        pass

    # 管理地址
    def manage_address(self):
        self.get_element(CO.manage_address).click()

    # 默认地址
    def default_address(self):
        self.get_element(CO.default_address).click()

    # 优惠券
    def coupon(self):
        self.get_element(CO.coupon).click()

    # 买家留言
    def buyer_message(self):
        self.get_element(CO.buyer_message).click()

    # 提交订单
    def submit_order(self):
        self.get_element(CO.submit_order).click()


    #提交订单
    def submit_order_now(self):
        text=self.get_element(CO.select_address).text
        if text=="请选择收货地址":
            self.select_address()
            self.new_address()
            self.input_address()
            self.choose_address()
        self.submit_order()
    
    
