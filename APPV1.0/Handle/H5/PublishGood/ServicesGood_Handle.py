#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 13:11
# @Author :春衫
# @File :ServicesGood_Handle.py

import time
from PageObjects.H5.PublishGood.ServerGood_Page import ServicesGoodPage
from Common.user_log import UserLog


# 发布商企服务
class ServicesGoodHandle:

    def __init__(self, driver):
        self.services_good_p = ServicesGoodPage(driver)
        self.logger = UserLog()

    # 上传主图
    def upload_main_image(self):
        time.sleep(0.5)
        self.services_good_p.get_upload_image_element().click()

    # 选择图片
    def check_image(self):
        time.sleep(0.5)
        self.services_good_p.get_check_image_element().click()

    # 点击确定
    def btn_ok(self):
        time.sleep(0.5)
        self.services_good_p.get_btn_ok_element().click()

    # 输入商品标题
    def product_title(self, product_title):
        time.sleep(0.5)
        self.logger.info("输入的商品标题是:" + product_title)
        self.services_good_p.get_product_title_element().send_keys(product_title)

    # 输入商品详情
    def product_description(self, product_description):
        time.sleep(0.5)
        self.logger.info("输入商品详情:" + product_description)
        self.services_good_p.get_product_description_element().send_keys(product_description)

    # 选择分类
    def categpry(self):
        time.sleep(0.5)
        self.services_good_p.get_category_element().click()

    # 选择二级分类
    def second_categpry(self):
        time.sleep(0.5)
        self.services_good_p.get_second_categpry_element().click()

    # 选择三级分类
    def third_categpry(self):
        time.sleep(0.5)
        self.services_good_p.get_third_categpry_element().click()

    # 商品总价
    def total_price(self, total_price):
        time.sleep(0.5)
        self.services_good_p.get_total_price_element().send_keys(total_price)

    # 预付款
    def subsist(self, subsist):
        time.sleep(0.5)
        self.services_good_p.get_subsist_element().send_keys(subsist)

    # 商品库存
    def stock(self, stock):
        time.sleep(0.5)
        self.services_good_p.get_stock_element().send_keys(stock)

    # 限购数量
    def limit_quantity(self, limit_quantity):
        time.sleep(0.5)
        self.services_good_p.get_limit_quantity_element().send_keys(limit_quantity)

    # 立即上架
    def submit(self):
        time.sleep(0.5)
        self.services_good_p.get_submit_element().click()

    # 放入仓库
    def storage(self):
        time.sleep(0.5)
        self.services_good_p.get_storage_element().click()

    # 获取错误提示元素
    def error_text(self):
        time.sleep(0.5)
        text = self.services_good_p.get_error_text_element().text
        return text
