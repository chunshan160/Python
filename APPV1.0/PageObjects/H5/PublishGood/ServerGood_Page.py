#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:35
# @Author :春衫
# @File :ServerGood_Page.py

import time

from Common.user_log import UserLog
from PageLocators.H5.PubilcGood import ServerGood as SG
from Common.BasePage import BasePage


# 发布商企服务
class ServicesGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title):
        time.sleep(0.5)
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(SG.product_title,product_title)

    # 输入商品详情
    def product_description(self, product_description):
        time.sleep(0.5)
        UserLog().info("输入商品详情是:" + product_description)
        self.input_text(SG.product_description,product_description)

    # 选择分类
    def category(self):
        self.click_element(SG.category).click()

    # 选择二级分类
    def second_categpry(self):
        self.click_element(SG.second_categpry).click()

    # 选择三级分类
    def third_categpry(self):
        self.click_element(SG.third_categpry).click()

    # 商品总价
    def total_price(self, total_price):
        time.sleep(0.5)
        UserLog().info("输入商品总价是:" + total_price)
        self.input_text(SG.total_price,total_price)

    # 预付款
    def subsist(self, subsist):
        time.sleep(0.5)
        UserLog().info("输入预付款是:" + subsist)
        self.input_text(SG.subsist,subsist)

    # 商品库存
    def stock(self, stock):
        time.sleep(0.5)
        UserLog().info("输入商品库存是:" + stock)
        self.input_text(SG.stock,stock)

    # 限购数量
    def limit_quantity(self, limit_quantity):
        time.sleep(0.5)
        UserLog().info("输入限购数量是:" + limit_quantity)
        self.input_text(SG.limit_quantity,limit_quantity)

    # 发布商企服务商品
    def services_good_information(self, product_title, product_description, total_price, subsist, stock, limit_quantity):
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
        self.category()
        # 选择二级分类
        self.second_categpry()
        # 选择三级分类
        self.third_categpry()
        # 商品总价
        self.total_price(total_price)
        # 预付款
        self.subsist(subsist)
        # 商品库存
        self.stock(stock)
        # 限购数量
        self.limit_quantity(limit_quantity)
