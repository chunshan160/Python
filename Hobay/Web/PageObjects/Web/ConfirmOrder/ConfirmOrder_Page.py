#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

import time
from Web.PageLocators.Web.ConfirmOrder import ConfirmOrder as CO
from Common.BasePage import BasePage


class ConfirmOrderPage(BasePage):

    # 选择收货地址
    def select_address(self, text=""):
        doc = text + "点击【选择收货地址】选项-"
        self.click_element(CO.select_address, doc=doc)

    # 管理地址
    def manage_address(self, text=""):
        doc = text + "点击【管理地址】按钮-"
        self.click_element(CO.manage_address, doc=doc)

    # 新建地址
    def new_address(self, text=""):
        doc = text + "点击【新建地址】按钮-"
        self.click_element(CO.new_address, doc=doc)

    # 填写收货地址信息
    def input_address(self, default=True, text=""):
        doc = text + "填写收货地址信息"
        # 输入收货人姓名
        self.input_text(CO.name, "测试", doc=doc)
        # 输入手机号
        self.input_text(CO.phone, "11111111111", doc=doc)
        # 点击所在地区
        self.click_element(CO.address, doc=doc)
        time.sleep(0.5)
        # 省
        self.click_element(CO.province, doc=doc)
        # 市
        self.click_element(CO.city, doc=doc)
        # 区
        self.click_element(CO.area, doc=doc)
        time.sleep(0.5)
        # 输入详细地址
        self.input_text(CO.detailed_address, "测试测试测试详细地址", doc=doc)
        if default is True:
            # 设为默认地址
            self.click_element(CO.default_address, doc=doc)

    # 点击保存
    def save(self, text=""):
        doc = text + "点击保存"
        self.click_element(CO.save, doc=doc)
        time.sleep(0.5)

    # 选择收货地址
    def choose_address(self, text=""):
        doc = text + "选择第一个收货地址-"
        self.click_element(CO.choose_first_address, doc=doc)

    # 优惠券
    def coupon(self, text=""):
        doc = text + "点击【优惠券】选项-"
        self.click_element(CO.coupon, doc=doc)

    # 买家留言
    def buyer_message(self, text=""):
        doc = text + "点击【买家留言】栏-"
        self.click_element(CO.buyer_message, doc=doc)

    # 提交订单
    def submit_order_button(self, text=""):
        doc = text + "点击【提交订单】按钮-"
        self.click_element(CO.submit_order, doc=doc)

    '''
    具体业务流程
    '''

    # 提交订单 实物商品
    def entity_goods_submit_order(self, text=""):
        doc = text + "点击【提交订单】按钮-"
        text = self.get_text(CO.select_address, doc=doc)
        if text == "请选择收货地址":
            self.select_address(text=doc)
            # 如果找不到默认地址
            if self.ele_if_exist(CO.default_address) == False:
                # 新建地址
                self.new_address(text=doc)
                # 输入地址信息
                self.input_address(text=doc)
                self.save(text=doc)
            # 选择第一个地址
            self.choose_address(text=doc)
        self.submit_order_button(text=doc)

    # 提交订单 本地生活
    def coupon_goods_submit_order(self, text=""):
        doc = text + "点击【提交订单】按钮-"
        self.submit_order_button(text=doc)

    # 提交订单 商企服务
    def server_goods_submit_order(self, text=""):
        doc = text + "点击【提交订单】按钮-"
        self.submit_order_button(text=doc)
