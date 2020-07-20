#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 16:17
# @Author :春衫
# @File :GoodDetail_Business.py

from Handle.H5.GoodDetail.GoodDetail_Handle import GoodDetailHandle


class GoodDetailBusiness:

    def __init__(self, driver):
        self.good_detail_h = GoodDetailHandle(driver)

    #购买商品
    def buy_good(self):
        #点击立即购买 - 数量加一 - 确认
        self.click_buy_now()
        self.click_add()
        self.click_confirm()

    # 顶部商品
    def click_top_good(self):
        self.good_detail_h.click_top_good()

    # 顶部详情
    def click_top_detail(self):
        self.good_detail_h.click_top_detail()

    # 顶部评价
    def click_top_evaluation(self):
        self.good_detail_h.click_top_evaluation()

    # 店铺
    def click_shop(self):
        self.good_detail_h.click_shop()

    # 收藏
    def click_collection(self):
        self.good_detail_h.click_collection()

    # 聊天
    def click_chat(self):
        self.good_detail_h.click_chat()

    # 加入购物车
    def click_add_car(self):
        self.good_detail_h.click_add_car()

    # 立即购买
    def click_buy_now(self):
        self.good_detail_h.click_buy_now()

    # -
    def click_less(self):
        self.good_detail_h.click_less()

    # 购买数量
    def send_add_munber(self):
        self.good_detail_h.send_add_munber()

    # +
    def click_add(self):
        self.good_detail_h.click_add()

    #确定
    def click_confirm(self):
        self.good_detail_h.click_confirm()