#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:32
# @Author :春衫
# @File :CouponGood_Page.py

import time
from PageLocators.H5.PubilcGood import CouponGood as CG
from Common.BasePage import BasePage


# 发布本地生活
class CouponGoodPage(BasePage):



    # 点击上传主图
    def upload_image(self):
        time.sleep(0.5)
        self.get_element(CG.product_image).click()

    # 选择图片
    def check_image(self):
        self.get_element(CG.check_image).click()

    # 点击确定
    def btn_ok(self):
        self.get_element(CG.btn_ok).click()

    # 输入商品标题
    def product_title(self, product_title):
        time.sleep(0.5)
        UserLog().info("输入的商品标题是:" + product_title)
        self.get_element(CG.product_title).send_keys(product_title)

    # 输入商品详情
    def product_description(self, product_description):
        time.sleep(0.5)
        UserLog().info("输入商品详情:" + product_description)
        self.get_element(CG.product_description).send_keys(product_description)

    # 选择分类
    def categpry(self):
        time.sleep(0.5)
        self.get_element(CG.category).click()

    # 选择二级分类
    def second_categpry(self):
        time.sleep(0.5)
        self.get_element(CG.second_categpry).click()

    # 选择三级分类
    def third_categpry(self):
        time.sleep(0.5)
        self.get_element(CG.third_categpry).click()

    # 点击券类
    def coupon(self):
        time.sleep(0.5)
        self.get_element(CG.coupon).click()

    # 选择券类
    def coupon_categpry(self):
        time.sleep(0.5)
        self.get_element(CG.coupon_categpry, 1).click()

    # 商品总价
    def total_price(self, total_price):
        time.sleep(0.5)
        UserLog().info("输入的商品总价是:" + total_price)
        self.get_element(CG.total_price).send_keys(total_price)

    # 商品库存
    def stock(self, stock):
        time.sleep(0.5)
        UserLog().info("输入的商品库存是:" + stock)
        self.get_element(CG.stock).send_keys(stock)

    # 限购数量
    def limit_quantity(self, limit_quantity):
        time.sleep(0.5)
        UserLog().info("输入的商品限购数量是:" + limit_quantity)
        self.get_element(CG.limit_quantity).send_keys(limit_quantity)

    #发布本地生活
    def publish_coupon_good(self, product_title, product_description, total_price, stock, limit_quantity):
        # 上传主图
        self.upload_image()
        # 选择图片
        self.check_image()
        # 点击确定
        self.btn_ok()
        # 输入商品标题
        self.product_title(product_title)
        # 输入商品详情
        self.product_description(product_description)
        # 选择分类
        self.categpry()
        # 选择二级分类
        self.second_categpry()
        # 选择三级分类
        self.third_categpry()
        # 点击券类
        self.coupon()
        # 选择券类
        self.coupon_categpry()
        # 商品总价
        self.total_price(total_price)
        # 商品库存
        self.stock(stock)
        # 限购数量
        self.limit_quantity(limit_quantity)
