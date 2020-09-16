#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:35
# @Author :春衫
# @File :ServerGood_Page.py

import time
from Common.user_log import UserLog
from PageLocators.Android.PubilcGood import ServerGood as SG
from PageLocators.Android.PubilcGood import PubilcGoodCommon as PGCommon
from PageObjects.Android.PublishGood.PublishGoodCommon import PublishGoodCommon
from Common.BasePage import BasePage


# 发布商企服务


class ServicesGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title, text=""):
        doc = text + "输入商品标题-"
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(SG.product_title, product_title, doc=doc)

    # 输入商品详情
    def product_description(self, product_description, text=""):
        doc = text + "输入商品详情-"
        UserLog().info("输入商品详情是:" + product_description)
        self.input_text(SG.product_description, product_description, doc=doc)

    # 选择分类
    def category(self, text=""):
        doc = text + "点击【分类】选项-"
        self.click_element(PGCommon.category, doc=doc)

    # 选择二级分类
    def second_category(self, name, text=""):
        doc = text + "点击【二级分类】选项-"
        new_locator = self.locator_by_text(PGCommon.second_category, name)
        self.click_element(new_locator, doc=doc)

    # 选择三级分类
    def third_category(self, name, text=""):
        doc = text + "选择【三级分类】选项-"
        new_locator = self.locator_by_text(PGCommon.third_category, name)
        self.click_element(new_locator, doc=doc)

    # 商品总价
    def total_price(self, total_price, text=""):
        doc = text + "商品总价-"
        UserLog().info("输入商品总价是:" + total_price)
        self.input_text(SG.total_price, total_price, doc=doc)

    # 预付款
    def subsist(self, subsist, text=""):
        doc = text + "预付款-"
        UserLog().info("输入预付款是:" + subsist)
        self.input_text(SG.subsist, subsist, doc=doc)

    # 商品库存
    def stock(self, stock, text=""):
        doc = text + "商品库存-"
        UserLog().info("输入商品库存是:" + stock)
        self.input_text(SG.stock, stock, doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + "限购数量-"
        UserLog().info("输入限购数量是:" + limit_quantity)
        self.input_text(SG.limit_quantity, limit_quantity, doc=doc)

    # 发布商企服务商品
    def services_good_information(self, product_title, product_description, second_category_name, third_category_name,
                                  total_price, subsist, stock, text=""):
        doc = text + "发布商企服务商品-"
        # 上传主图-选择图片-点击确定
        PublishGoodCommon(self.driver).upload_product_image(text=doc)
        # 输入商品标题
        self.product_title(product_title, text=doc)
        # 输入商品详情
        self.product_description(product_description, text=doc)
        # 选择分类
        PublishGoodCommon(self.driver).category(text=doc)
        # 选择二级分类
        PublishGoodCommon(self.driver).second_category(second_category_name, text=doc)
        # 选择三级分类
        PublishGoodCommon(self.driver).third_category(third_category_name, text=doc)
        # 商品总价
        self.total_price(total_price, text=doc)
        # 预付款
        self.subsist(subsist, text=doc)
        # 商品库存
        self.stock(stock, text=doc)
