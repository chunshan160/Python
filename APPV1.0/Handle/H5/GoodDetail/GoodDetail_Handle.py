#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 16:17
# @Author :春衫
# @File :GoodDetail_Business.py

import time
from PageObjects.H5.GoodDetail.GoodDetail_Page import GoodDetailPage


class GoodDetailHandle:

    def __init__(self, driver):
        self.good_detail_p = GoodDetailPage(driver)

    # 顶部商品
    def click_top_good(self):
        time.sleep(0.5)
        self.good_detail_p.get_top_good_element().click()

    # 顶部详情
    def click_top_detail(self):
        time.sleep(0.5)
        self.good_detail_p.get_top_detail_element().click()

    # 顶部评价
    def click_top_evaluation(self):
        time.sleep(0.5)
        self.good_detail_p.get_top_evaluation_element().click()

    # 店铺
    def click_shop(self):
        time.sleep(0.5)
        self.good_detail_p.get_shop_element().click()

    # 收藏
    def click_collection(self):
        time.sleep(0.5)
        self.good_detail_p.get_collection_element().click()

    # 聊天
    def click_chat(self):
        time.sleep(0.5)
        self.good_detail_p.get_chat_element().click()

    # 加入购物车
    def click_add_car(self):
        time.sleep(0.5)
        self.good_detail_p.get_add_car_element().click()

    # 立即购买
    def click_buy_now(self):
        time.sleep(2)
        self.good_detail_p.get_buy_now_element().click()

    # -
    def click_less(self):
        time.sleep(0.5)
        self.good_detail_p.get_less_element().click()

    # 购买数量
    def send_add_munber(self):
        time.sleep(0.5)
        self.good_detail_p.get_add_munber_element().send_keys()

    # +
    def click_add(self):
        time.sleep(1)
        self.good_detail_p.get_add_element().click()

    # 确定
    def click_confirm(self):
        time.sleep(1)
        self.good_detail_p.get_confirm_element().click()
