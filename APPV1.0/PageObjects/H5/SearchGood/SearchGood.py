#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py

import time

from Common.user_log import UserLog
from PageLocators.H5.SearchGood import SearchGood
from Common.BasePage import BasePage


class SearchGoodPage(BasePage):

    # 搜索框-输入
    def send_search(self, good_name):
        time.sleep(0.5)
        UserLog().info("搜索框-输入文字是:" + good_name)
        self.input_text(SearchGood.send_search,good_name)
        self.driver.keyevent(66)
        self.choose_first_good()

    # 商品tap
    def good_tap(self):
        self.click_element(SearchGood.good_tap)

    # 店铺tap
    def shop_tap(self):
        self.click_element(SearchGood.shop_tap)

    # 综合
    def Comprehensive(self):
        self.click_element(SearchGood.Comprehensive)

    # 全新
    def new(self):
        self.click_element(SearchGood.new)

    # 人气
    def hot(self):
        self.click_element(SearchGood.hot)

    # 价格
    def price(self):
        self.click_element(SearchGood.price)

    # 筛选
    def filter(self):
        self.click_element(SearchGood.filter)

    # 商品
    def choose_first_good(self):
        self.click_element(SearchGood.good)

    # 进店
    def go_shop(self):
        self.click_element(SearchGood.go_shop)

    # 搜索-店铺-商品
    def shop_good(self):
        self.click_element(SearchGood.shop_good)
