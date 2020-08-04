#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py

import time

from PageObjects.H5.SearchGood.SearchGood import SearchGoodPage


class SearchGoodHandle:

    def __init__(self, driver):
        self.search_good_p = SearchGoodPage(driver)

    # 搜索框-输入
    def send_search(self, good_name):
        time.sleep(0.5)
        self.search_good_p.get_send_search_element().send_keys(good_name)

    # 商品tap
    def click_good_tap(self):
        time.sleep(0.5)
        self.search_good_p.get_good_tap_element().click()

    # 店铺tap
    def click_shop_tap(self):
        time.sleep(0.5)
        self.search_good_p.get_shop_tap_element().click()

    # 综合
    def click_Comprehensive(self):
        time.sleep(0.5)
        self.search_good_p.get_Comprehensive_element().click()

    # 全新
    def click_new(self):
        time.sleep(0.5)
        self.search_good_p.get_new_element().click()

    # 人气
    def click_hot(self):
        time.sleep(0.5)
        self.search_good_p.get_hot_element().click()

    # 价格
    def click_price(self):
        time.sleep(0.5)
        self.search_good_p.get_price_element().click()

    # 筛选
    def click_filter(self):
        time.sleep(0.5)
        self.search_good_p.get_filter_element().click()

    # 商品
    def click_good(self):
        time.sleep(1)
        self.search_good_p.get_good_element().click()

    # 进店
    def click_go_shop(self):
        time.sleep(0.5)
        self.search_good_p.get_go_shop_element().click()

    # 搜索-店铺-商品
    def click_shop_good(self):
        time.sleep(0.5)
        self.search_good_p.get_shop_good_element().click()
