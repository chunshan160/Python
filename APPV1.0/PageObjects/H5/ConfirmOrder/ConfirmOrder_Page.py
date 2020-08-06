#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

import time
from PageLocators.H5.ConfirmOrder import ConfirmOrder as CO
from Common.BasePage import BasePage


class ConfirmOrderPage(BasePage):

    # 选择收货地址
    def select_address(self,text=""):
        doc=text+"点击【选择收货地址】选项-"
        self.click_element(CO.select_address,doc =doc)

    # 管理地址
    def manage_address(self,text=""):
        doc=text+"点击【管理地址】按钮-"
        self.click_element(CO.manage_address, doc=doc)

    # 新建地址
    def new_address(self,text=""):
        doc = text + "点击【新建地址】按钮-"
        self.click_element(CO.new_address,doc =doc)

    # 填写收货地址信息
    def input_address(self, model="MI 8", default=True,text=""):
        doc = text + "填写收货地址信息"
        tap = CO.address[model]
        # 点击输入收货人姓名
        self.touch(tap["输入收货人姓名"][0], tap["输入收货人姓名"][1],doc=doc+"点击【输入收货人姓名】栏-")
        # 输入收货人姓名
        self.driver.keyevent(45)
        # 点击输入手机号
        self.touch(tap["输入收货人手机号码"][0], tap["输入收货人手机号码"][1],doc=doc+"点击【输入手机号】栏-")
        # 输入手机号
        self.send_phone_number(11111111111,doc=doc+"输入手机号-")
        # 点击所在地区
        self.touch(tap["选择所在地区"][0], tap["选择所在地区"][1],doc=doc+"点击【所在地区】栏-")
        time.sleep(0.5)
        # 省
        self.touch(tap["省"][0], tap["省"][1],doc=doc+"点击【省】选项-")
        # 市
        self.touch(tap["市"][0], tap["市"][1],doc=doc+"点击【市】选项-")
        # 区
        self.touch(tap["区"][0], tap["区"][1],doc=doc+"点击【区】选项-")
        time.sleep(0.5)
        # 点击详细地址
        self.touch(tap["输入地址"][0], tap["输入地址"][1],doc=doc+"点击【详细地址】栏-")
        # 输入详细地址
        self.driver.keyevent(45)
        if default is True:
            # 设为默认地址
            self.touch(tap["设为默认地址"][0], tap["设为默认地址"][1],doc=doc+"点击【设为默认地址】按钮-")
        # 点击保存
        self.click_element(CO.save,doc =doc+"点击【保存】按钮-")
        time.sleep(0.5)

    # 选择收货地址
    def choose_address(self,text=""):
        doc=text+"选择第一个收货地址-"
        self.click_element(CO.choose_first_address,doc =doc)

    # 默认地址
    def default_address(self,text=""):
        doc=text+"检查是否有默认地址-"
        try:
            return self.get_text(CO.default_address,doc =doc)
        except:
            return None

    # 优惠券
    def coupon(self,text=""):
        doc=text+"点击【优惠券】选项-"
        self.click_element(CO.coupon,doc =doc)

    # 买家留言
    def buyer_message(self,text=""):
        doc = text + "点击【买家留言】栏-"
        self.click_element(CO.buyer_message,doc =doc)

    # 提交订单
    def submit_order(self,text=""):
        doc = text + "点击【提交订单】按钮-"
        self.click_element(CO.submit_order,doc =doc)

    # 提交订单
    def submit_order_now(self,text=""):
        doc = text + "点击【提交订单】按钮-"
        text = self.get_text(CO.select_address,doc =doc)
        if text == "请选择收货地址":
            self.select_address()
            if self.default_address()==None:
                self.new_address()
                self.input_address()
            self.choose_address()
        self.submit_order()
