#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index_Business.py

from PageLocators.H5.Index import Index
from Common.find_element import FindElement


class IndexPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 首页定位
    def get_location_element(self):
        return self.fd.find_element(Index.location)

    # 搜索框
    def get_search_element(self):
        return self.fd.find_element(Index.search)

    # 易购车
    def get_shopping_car_element(self):
        return self.fd.find_element(Index.shopping_car)

    # 扫一扫
    def get_scan_code_element(self):
        return self.fd.find_element(Index.scan_code)

    # 首页询问城市定位
    # ask_location = ("id","//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")

    # 首页-我的
    def get_my_index_element(self):
        return self.fd.find_element(Index.my_index)

    # 易货信用
    def get_credit_good_element(self):
        return self.fd.find_element(Index.credit_good)

    # 焕焕商机
    def get_business_element(self):
        return self.fd.find_element(Index.business)

    # 首页点击发布商品
    def get_publish_good_element(self):
        return self.fd.find_element(Index.publish_good)
