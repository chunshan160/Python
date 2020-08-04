#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index.py

from PageLocators.H5.Index import Index
from Common.BasePage import BasePage


class IndexPage(BasePage):

    # 首页定位
    def location(self):
        self.get_element(Index.location)

    # 搜索框
    def search(self):
        self.get_element(Index.search).click()

    # 易购车
    def shopping_car(self):
        self.get_element(Index.shopping_car)

    # 扫一扫
    def scan_code(self):
        self.get_element(Index.scan_code)

    # 首页询问城市定位
    # ask_location = ("id","//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")

    # 首页-我的
    def my_index(self):
        self.get_element(Index.my_index)

    # 易货信用
    def credit_good(self):
        self.get_element(Index.credit_good)

    # 焕焕商机
    def business(self):
        self.get_element(Index.business)

    # 首页点击发布商品
    def publish_good(self):
        self.get_element(Index.publish_good)
