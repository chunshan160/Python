#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index_Business.py

from Handle.H5.Index.Index_Handle import IndexHandle


class IndexBusiness:

    def __init__(self, driver):
        self.index_h = IndexHandle(driver)

    # 首页定位
    def click_location(self):
        self.index_h.click_location()

    # 搜索框
    def click_search(self):
        self.index_h.click_search()

    # 易购车
    def click_shopping_car(self):
        self.index_h.click_shopping_car()

    # 扫一扫
    def click_scan_code(self):
        self.index_h.click_scan_code()

    # 首页询问城市定位
    # ask_location = ("id","//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")

    # 首页-我的
    def click_my_index(self):
        self.index_h.click_my_index()

    # 易货信用
    def click_credit_good(self):
        self.index_h.click_credit_good()

    # 焕焕商机
    def click_business(self):
        self.index_h.click_business()

    # 首页点击发布商品
    def click_publish_good(self):
        self.index_h.click_publish_good()
