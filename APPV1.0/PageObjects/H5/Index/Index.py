#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index.py

from PageLocators.H5.Index import Index
from Common.BasePage import BasePage


class IndexPage(BasePage):

    # 首页定位
    def location(self,text=""):
        doc=text+"点击【定位】按钮-"
        self.click_element(Index.location, doc=doc)

    # 搜索框
    def search(self,text=""):
        doc = text+"点击【搜索栏】-"
        self.click_element(Index.search, doc=doc)

    # 易购车
    def shopping_car(self,text=""):
        doc = text+"点击【易购车】按钮-"
        self.click_element(Index.shopping_car, doc=doc)

    # 扫一扫
    def scan_code(self,text=""):
        doc = text + "点击【扫一扫】按钮-"
        self.click_element(Index.scan_code, doc=doc)

    # 首页询问城市定位
    # ask_location = ("id","//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")
