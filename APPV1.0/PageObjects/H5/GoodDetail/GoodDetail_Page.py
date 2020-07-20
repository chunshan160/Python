#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 16:17
#@Author :春衫
#@File :GoodDetail_Page.py

from PageLocators.H5.GoodDetail import GoodDetail as GD
from Common.find_element import FindElement


class GoodDetailPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 顶部商品
    def get_top_good_element(self):
        return self.fd.find_element(GD.top_good)

    #顶部详情
    def get_top_detail_element(self):
        return self.fd.find_element(GD.top_detail)

    #顶部评价
    def get_top_evaluation_element(self):
        return self.fd.find_element(GD.top_evaluation)
    #店铺
    def get_shop_element(self):
        return self.fd.find_element(GD.shop)

    #收藏
    def get_collection_element(self):
        return self.fd.find_element(GD.collection)

    #聊天
    def get_chat_element(self):
        return self.fd.find_element(GD.chat)

    #加入购物车
    def get_add_car_element(self):
        return self.fd.find_element(GD.add_car)

    #立即购买
    def get_buy_now_element(self):
        return self.fd.find_element(GD.buy_now)

    #-
    def get_less_element(self):
        return self.fd.find_element(GD.less)

    #购买数量
    def get_add_munber_element(self):
        return self.fd.find_element(GD.add_munber)

    #+
    def get_add_element(self):
        return self.fd.find_element(GD.add)

    #确定
    def get_confirm_element(self):
        return self.fd.find_element(GD.confirm)