#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 16:17
# @Author :春衫
# @File :GoodDetail_Page.py

import time
from PageLocators.H5.GoodDetail import GoodDetail as GD
from Common.BasePage import BasePage


class GoodDetailPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 顶部商品
    def top_good(self):
        self.get_element(GD.top_good).click()

    # 顶部详情
    def top_detail(self):
        self.get_element(GD.top_detail).click()

    # 顶部评价
    def top_evaluation(self):
        self.get_element(GD.top_evaluation).click()

    # 店铺
    def shop(self):
        self.get_element(GD.shop).click()

    # 收藏
    def collection(self):
        self.get_element(GD.collection).click()

    # 聊天
    def chat(self):
        self.get_element(GD.chat).click()

    # 加入购物车
    def add_car(self):
        self.get_element(GD.add_car).click()

    # 立即购买
    def buy_now(self):
        self.get_element(GD.buy_now).click()

    # -
    def less(self):
        self.get_element(GD.less).click()

    # 购买数量
    def add_munber(self, munber):
        time.sleep(0.5)
        self.logger.info("输入的商品数量是:" + munber)
        self.get_element(GD.add_munber).send_keys(munber)

    # +
    def add(self):
        self.get_element(GD.add).click()

    # 确定
    def confirm(self):
        self.get_element(GD.confirm).click()

    # 购买商品
    def bug_good(self,munber=False):
        self.buy_now()
        if munber is not False:
            self.add_munber(munber)
        else:
            self.add()
        self.confirm()
