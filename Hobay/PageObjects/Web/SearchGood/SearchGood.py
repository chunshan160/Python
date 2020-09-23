#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 15:52
# @Author :春衫
# @File :SearchGood_Business.py
from selenium.webdriver.common.keys import Keys

from Common.user_log import UserLog
from PageLocators.Web.SearchGood import SearchGood
from Common.BasePage import BasePage


class SearchGoodPage(BasePage):

    # 搜索框-输入
    def send_search(self, good_name, text=""):
        doc=text+"搜索框-输入-"
        UserLog().info("搜索框-输入文字是:" + good_name)
        self.input_text(SearchGood.send_search,good_name,doc=doc)
        self.get_element(SearchGood.send_search, doc).send_keys(Keys.ENTER)
        self.choose_first_good(good_name,text=doc)

    # 商品tap
    def good_tap(self, text=""):
        doc = text + "点击商品tap-"
        self.click_element(SearchGood.good_tap,doc=doc)

    # 店铺tap
    def shop_tap(self, text=""):
        doc = text + "点击店铺tap-"
        self.click_element(SearchGood.shop_tap,doc=doc)

    # 综合
    def Comprehensive(self, text=""):
        doc = text + "点击综合tap-"
        self.click_element(SearchGood.Comprehensive,doc=doc)

    # 全新
    def new(self, text=""):
        doc = text + "点击全新tap-"
        self.click_element(SearchGood.new,doc=doc)

    # 人气
    def hot(self, text=""):
        doc = text + "点击人气tap-"
        self.click_element(SearchGood.hot,doc=doc)

    # 价格
    def price(self, text=""):
        doc = text + "点击价格tap-"
        self.click_element(SearchGood.price,doc=doc)

    # 筛选
    def filter(self, text=""):
        doc = text + "点击筛选tap-"
        self.click_element(SearchGood.filter,doc=doc)

    # 商品
    def choose_first_good(self,good_name, text=""):
        doc = text + "点击第一件商品-"
        new_locator = self.locator_by_text(SearchGood.good, good_name)
        self.click_element(new_locator,doc=doc)

    # 进店
    def go_shop(self, text=""):
        doc = text + "点击进店按钮-"
        self.click_element(SearchGood.go_shop,doc=doc)

    # 搜索-店铺-商品
    def shop_good(self, text=""):
        doc = text + "点击商品-"
        self.click_element(SearchGood.shop_good,doc=doc)
