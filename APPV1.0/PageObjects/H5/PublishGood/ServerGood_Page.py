#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:35
# @Author :春衫
# @File :ServerGood_Page.py

import time
from Common.user_log import UserLog
from PageLocators.H5.PubilcGood import ServerGood as SG
from PageLocators.H5.PubilcGood import PubilcGoodCommon
from Common.BasePage import BasePage


# 发布商企服务
class ServicesGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title, text=""):
        doc = text + "输入商品标题-"
        time.sleep(0.5)
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(SG.product_title, product_title, doc=doc)

    # 输入商品详情
    def product_description(self, product_description, text=""):
        doc = text + "输入商品详情-"
        time.sleep(0.5)
        UserLog().info("输入商品详情是:" + product_description)
        self.input_text(SG.product_description, product_description, doc=doc)

    # 选择分类
    def category(self, text=""):
        doc = text + "选择分类-"
        self.click_element(SG.category, doc=doc)

    # 选择二级分类
    def second_categpry(self, text=""):
        doc = text + "选择二级分类-"
        self.click_elements(SG.second_categpry,0, doc=doc)

    # 选择三级分类
    def third_categpry(self, text=""):
        doc = text + "选择三级分类-"
        self.click_elements(SG.third_categpry,0, doc=doc)

    # 商品总价
    def total_price(self, total_price, text=""):
        doc = text + "商品总价-"
        time.sleep(0.5)
        UserLog().info("输入商品总价是:" + total_price)
        self.input_text(SG.total_price, total_price, doc=doc)

    # 预付款
    def subsist(self, subsist, text=""):
        doc = text + "预付款-"
        time.sleep(0.5)
        UserLog().info("输入预付款是:" + subsist)
        self.input_text(SG.subsist, subsist, doc=doc)

    # 商品库存
    def stock(self, stock, text=""):
        doc = text + "商品库存-"
        time.sleep(0.5)
        UserLog().info("输入商品库存是:" + stock)
        self.input_text(SG.stock, stock, doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + "限购数量-"
        time.sleep(0.5)
        UserLog().info("输入限购数量是:" + limit_quantity)
        self.input_text(SG.limit_quantity, limit_quantity, doc=doc)

    # 发布商企服务商品
    def services_good_information(self, product_title, product_description, total_price, subsist, stock, limit_quantity,
                                  text=""):
        doc = text + "发布商企服务商品-"
        # 上传主图-选择图片-点击确定
        self.app_upload_image(PubilcGoodCommon.product_image, PubilcGoodCommon.check_image, PubilcGoodCommon.btn_ok,
                              doc=doc)
        # 输入商品标题
        self.product_title(product_title, text=doc)
        # 输入商品详情
        self.product_description(product_description, text=doc)
        # 选择分类
        self.category(text=doc)
        # 选择二级分类
        self.second_categpry(text=doc)
        # 选择三级分类
        self.third_categpry(text=doc)
        # 商品总价
        self.total_price(total_price, text=doc)
        # 预付款
        self.subsist(subsist, text=doc)
        # 商品库存
        self.stock(stock, text=doc)
        # 限购数量
        self.limit_quantity(limit_quantity, text=doc)
