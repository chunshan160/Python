#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py

from PageLocators.H5.SearchGood import SearchGood
from Common.find_element import FindElement


class SearchGoodPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 搜索框-输入
    def get_send_search_element(self):
        return self.fd.find_element(SearchGood.send_search)

    # 商品tap
    def get_good_tap_element(self):
        return self.fd.find_element(SearchGood.good_tap)

    # 店铺tap
    def get_shop_tap_element(self):
        return self.fd.find_element(SearchGood.shop_tap)

    # 综合
    def get_Comprehensive_element(self):
        return self.fd.find_element(SearchGood.Comprehensive)

    # 全新
    def get_new_element(self):
        return self.fd.find_element(SearchGood.new)

    # 人气
    def get_hot_element(self):
        return self.fd.find_element(SearchGood.hot)

    # 价格
    def get_price_element(self):
        return self.fd.find_element(SearchGood.price)

    # 筛选
    def get_filter_element(self):
        return self.fd.find_element(SearchGood.filter)

    # 商品
    def get_good_element(self):
        return self.fd.find_element(SearchGood.good)

    # 进店
    def get_go_shop_element(self):
        return self.fd.find_element(SearchGood.go_shop)

    # 搜索-店铺-商品
    def get_shop_good_element(self):
        return self.fd.find_element(SearchGood.shop_good)
