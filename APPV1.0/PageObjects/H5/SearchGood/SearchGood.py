#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py

import time
from PageLocators.H5.SearchGood import SearchGood
from Common.BasePage import BasePage


class SearchGoodPage(BasePage):



    # 搜索框-输入
    def send_search(self, good_name):
        time.sleep(0.5)
        self.logger.info("搜索框-输入文字是:" + good_name)
        self.get_element(SearchGood.send_search).send_keys(good_name)
        self.driver.keyevent(66)
        self.choose_first_good()

    # 商品tap
    def good_tap(self):
        self.get_element(SearchGood.good_tap).click()

    # 店铺tap
    def shop_tap(self):
        self.get_element(SearchGood.shop_tap).click()

    # 综合
    def Comprehensive(self):
        self.get_element(SearchGood.Comprehensive).click()

    # 全新
    def new(self):
        self.get_element(SearchGood.new).click()

    # 人气
    def hot(self):
        self.get_element(SearchGood.hot).click()

    # 价格
    def price(self):
        self.get_element(SearchGood.price).click()

    # 筛选
    def filter(self):
        self.get_element(SearchGood.filter).click()

    # 商品
    def choose_first_good(self):
        self.get_element(SearchGood.good).click()

    # 进店
    def go_shop(self):
        self.get_element(SearchGood.go_shop).click()

    # 搜索-店铺-商品
    def shop_good(self):
        self.get_element(SearchGood.shop_good).click()
