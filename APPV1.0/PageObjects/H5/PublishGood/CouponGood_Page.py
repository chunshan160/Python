#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:32
# @Author :春衫
# @File :CouponGood_Page.py

import time
from Common.user_log import UserLog
from PageLocators.H5.PubilcGood import CouponGood as CG
from PageLocators.H5.PubilcGood import Common
from Common.BasePage import BasePage


# 发布本地生活
class CouponGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title, text=""):
        doc = text + "输入商品标题-"
        time.sleep(0.5)
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(CG.product_title, product_title,doc=doc)

    # 输入商品详情
    def product_description(self, product_description, text=""):
        doc = text + "输入商品详情-"
        time.sleep(0.5)
        UserLog().info("输入商品详情:" + product_description)
        self.input_text(CG.product_description, product_description,doc=doc)

    # 选择分类
    def categpry(self, text=""):
        doc = text + "点击【分类】按钮-"
        time.sleep(0.5)
        self.click_element(CG.category,doc=doc)

    # 选择二级分类
    def second_categpry(self, text=""):
        doc = text + "点击【二级分类】选项-"
        time.sleep(0.5)
        self.click_element(CG.second_categpry,doc=doc)

    # 选择三级分类
    def third_categpry(self, text=""):
        doc = text + "选择第一个【三级分类】选项-"
        time.sleep(0.5)
        self.click_element(CG.third_categpry,doc=doc)

    # 点击券类
    def coupon(self, text=""):
        doc = text + "点击【券类】按钮-"
        time.sleep(0.5)
        self.click_element(CG.coupon,doc=doc)

    # 选择券类
    def coupon_categpry(self, text=""):
        doc = text + "点击【券类】按钮-"
        time.sleep(0.5)
        self.click_element(CG.coupon_categpry,doc=doc)

    # 商品总价
    def total_price(self, total_price, text=""):
        doc = text + "输入商品总价-"
        time.sleep(0.5)
        UserLog().info("输入的商品总价是:" + total_price)
        self.input_text(CG.total_price, total_price,doc=doc)

    # 商品库存
    def stock(self, stock, text=""):
        doc = text + "输入商品库存-"
        time.sleep(0.5)
        UserLog().info("输入的商品库存是:" + stock)
        self.input_text(CG.stock, stock,doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + "输入限购数量-"
        time.sleep(0.5)
        UserLog().info("输入的商品限购数量是:" + limit_quantity)
        self.input_text(CG.limit_quantity, limit_quantity,doc=doc)

    # 发布本地生活
    def coupon_good_information(self, product_title, product_description, total_price, stock, limit_quantity, text=""):
        # 上传主图-选择图片-点击确定
        self.app_upload_image(Common.product_image,Common.check_image,Common.btn_ok,doc=text)
        # 输入商品标题
        self.product_title(product_title, text)
        # 输入商品详情
        self.product_description(product_description, text)
        # 选择分类
        self.categpry(text)
        # 选择二级分类
        self.second_categpry(text)
        # 选择三级分类
        self.third_categpry(text)
        # 点击券类
        self.coupon(text)
        # 选择券类
        self.coupon_categpry(text)
        # 商品总价
        self.total_price(total_price, text)
        # 商品库存
        self.stock(stock, text)
        # 限购数量
        self.limit_quantity(limit_quantity, text)
