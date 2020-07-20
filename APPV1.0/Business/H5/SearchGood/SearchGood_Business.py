#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py
import time

from Handle.H5.SearchGood.SearchGood_Handle import SearchGoodHandle


class SearchGoodBusiness:

    def __init__(self, driver):
        self.driver=driver
        self.search_good_h = SearchGoodHandle(driver)

    #输入商品名，点击搜索，选择商品
    def search_good(self,good_name):
        self.send_search(good_name)
        self.driver.keyevent(66)
        self.click_good()

    # 搜索框-输入
    def send_search(self, good_name):
        self.search_good_h.send_search(good_name)
        time.sleep(1)

    # 商品tap
    def click_good_tap(self):
        self.search_good_h.click_good_tap()

    # 店铺tap
    def click_shop_tap(self):
        self.search_good_h.click_shop_tap()

    # 综合
    def click_Comprehensive(self):
        self.search_good_h.click_Comprehensive()

    # 全新
    def click_new(self):
        self.search_good_h.click_new()

    # 人气
    def click_hot(self):
        self.search_good_h.click_hot()

    # 价格
    def click_price(self):
        self.search_good_h.click_price()

    # 筛选
    def click_filter(self):
        self.search_good_h.click_filter()

    # 商品
    def click_good(self):
        self.search_good_h.click_good()

    # 进店
    def click_go_shop(self):
        self.search_good_h.click_go_shop()

    # 搜索-店铺-商品
    def click_shop_good(self):
        self.search_good_h.click_shop_good()
