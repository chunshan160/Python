#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 16:17
# @Author :春衫
# @File :GoodDetail_Page.py

import time
from Common.user_log import UserLog
from PageLocators.Android.GoodDetail import GoodDetail as GD
from Common.BasePage import BasePage


class GoodDetailPage(BasePage):

    # 顶部商品
    def top_good(self, text=""):
        doc = text + "点击切换【商品】页面-"
        self.click_element(GD.top_good, doc=doc)

    # 店铺详情详情
    def top_detail(self, text=""):
        doc = text + "点击切换【详情】页面-"
        self.click_element(GD.top_detail, doc=doc)

    # 店铺详情评价
    def top_evaluation(self, text=""):
        doc = text + "点击切换【评价】页面-"
        self.click_element(GD.top_evaluation, doc=doc)

    # 店铺
    def shop(self, text=""):
        doc = text + "点击【店铺】按钮-"
        self.click_element(GD.shop, doc=doc)

    # 收藏
    def collection(self, text=""):
        doc = text + "点击【收藏】按钮-"
        self.click_element(GD.collection, doc=doc)

    # 聊天
    def chat(self, text=""):
        doc = text + "点击【聊天】按钮-"
        self.click_element(GD.chat, doc=doc)

    # 加入购物车
    def add_car(self, text=""):
        doc = text + "点击【加入购物车】按钮-"
        self.click_element(GD.add_car, doc=doc)

    # 立即购买
    def buy_now(self, text=""):
        doc = text + "点击【立即购卖】按钮-"
        self.click_element(GD.buy_now, doc=doc)

    # -
    def less(self, text=""):
        doc = text + "点击数量【-】按钮-"
        self.click_element(GD.less, doc=doc)

    # 购买数量
    def add_munber(self, munber, text=""):
        doc = text + "点击【购买数量】输入框-"
        time.sleep(0.5)
        UserLog().info("输入的商品数量是:" + munber)
        self.input_text(GD.add_munber, munber, doc=doc)

    # +
    def add(self, text=""):
        doc = text + "点击数量【+】按钮-"
        self.click_element(GD.add, doc=doc)

    # 确定
    def confirm(self, text=""):
        doc = text + "点击【确定】按钮-"
        self.click_element(GD.confirm, doc=doc)

    # 购买商品
    def buy_good(self, munber=False, text=""):
        self.buy_now(text)
        if munber is not False:
            self.add_munber(munber, text)
        else:
            self.add(text)
        self.confirm(text)
