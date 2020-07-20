#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index_Handle.py

import time
from PageObjects.H5.Index.Index import IndexPage


class IndexHandle:

    def __init__(self, driver):
        self.index_p = IndexPage(driver)

    # 首页定位
    def click_location(self):
        time.sleep(0.5)
        self.index_p.get_location_element().click()

    # 搜索框
    def click_search(self):
        time.sleep(1)
        self.index_p.get_search_element().click()

    # 易购车
    def click_shopping_car(self):
        time.sleep(0.5)
        self.index_p.get_shopping_car_element().click()

    # 扫一扫
    def click_scan_code(self):
        time.sleep(0.5)
        self.index_p.get_scan_code_element().click()

    # 首页询问城市定位
    # ask_location = ("id","//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")

    # 首页-我的
    def click_my_index(self):
        time.sleep(0.5)
        self.index_p.get_my_index_element().click()

    # 易货信用
    def click_credit_good(self):
        time.sleep(0.5)
        self.index_p.get_credit_good_element().click()

    # 焕焕商机
    def click_business(self):
        time.sleep(0.5)
        self.index_p.get_business_element().click()

    # 首页点击发布商品
    def click_publish_good(self):
        time.sleep(0.5)
        self.index_p.get_publish_good_element().click()
