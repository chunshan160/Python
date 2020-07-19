#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 16:07
# @Author :春衫
# @File :EntityGood_Handle.py

import time
from PageObjects.H5.PublishGood.EntityGood_Page import EntityGoodPage
from Common.user_log import UserLog


# 发布实物商品
class EntityGoodHandle:

    def __init__(self, driver):
        self.entity_good_p = EntityGoodPage(driver)
        self.logger = UserLog()

    # 上传主图
    def upload_main_image(self):
        time.sleep(0.5)
        self.entity_good_p.get_upload_image_element().click()

    # 选择图片
    def check_main_image(self):
        time.sleep(0.5)
        self.entity_good_p.get_check_image_element().click()

    # 点击确定
    def btn_ok(self):
        time.sleep(0.5)
        self.entity_good_p.get_btn_ok_element().click()

    # 输入商品标题
    def send_product_title(self, product_title):
        time.sleep(0.5)
        self.logger.info("输入的商品标题是:" + product_title)
        self.entity_good_p.get_product_title_element().send_keys(product_title)

    # 点击商品描述
    def product_detail(self):
        time.sleep(0.5)
        self.entity_good_p.get_product_detail_element().click()

    # 输入商品详情
    def product_description(self, product_description):
        time.sleep(0.5)
        self.logger.info("输入商品详情:" + product_description)
        self.entity_good_p.get_product_description_element().send_keys(product_description)

    # 商品详情页上传商品
    def product_description_image(self):
        time.sleep(0.5)
        self.entity_good_p.get_description_image_element().click()

    # 点击完成，回到商品详情页
    def finish(self):
        time.sleep(0.5)
        self.entity_good_p.get_finish_element().click()

    # 点击品相
    def quality(self):
        time.sleep(0.5)
        self.entity_good_p.get_quality_element().click()

    # 选择全新
    def quality_new(self):
        time.sleep(0.5)
        self.entity_good_p.get_quality_new_element().click()

    # 选择分类
    def category(self):
        time.sleep(0.5)
        self.entity_good_p.get_category_element().click()

    # 选择二级分类
    def second_categpry(self):
        time.sleep(1)
        self.entity_good_p.get_second_categpry_element().click()

    # 选择三级分类
    def third_categpry(self):
        time.sleep(0.5)
        self.entity_good_p.get_third_categpry_element().click()

    # 点击商品类型
    def product_type(self):
        time.sleep(0.5)
        self.entity_good_p.get_product_type_element().click()

    # 选择商品类型
    def product_type_select(self):
        time.sleep(0.5)
        self.entity_good_p.get_product_type_select_element().click()

    # 点击规格
    def specification(self):
        time.sleep(0.5)
        self.entity_good_p.get_specification_element().click()

    # 进入商品规格页面，输入属性
    def property_1(self, property_1):
        time.sleep(0.5)
        self.logger.info("输入的商品规格是:" + property_1)
        self.entity_good_p.get_property_1_element().send_keys(property_1)

    def property_2(self, property_2):
        time.sleep(0.5)
        self.logger.info("输入的商品属性是:" + property_2)
        self.entity_good_p.get_property_2_element().send_keys(property_2)

    # 上传规格图片
    def upload_specification_image(self):
        time.sleep(1)
        self.entity_good_p.get_upload_specification_image_element().click()

    # 选择规格图片
    def check_specification_image(self):
        time.sleep(0.5)
        self.entity_good_p.get_check_specification_image_element().click()

    # 下一步
    def next(self):
        time.sleep(1)
        self.entity_good_p.get_next_element().click()

    # 进货价
    def purchase_price(self, purchase_price):
        time.sleep(0.5)
        self.logger.info("输入的商品进货价是:" + purchase_price)
        self.entity_good_p.get_purchase_price_element().send_keys(purchase_price)

    # 出售价
    def sell_price(self, sell_price):
        time.sleep(0.5)
        self.logger.info("输入的商品出售价是:" + sell_price)
        self.entity_good_p.get_sell_price_element().send_keys(sell_price)

    # 库存
    def stock(self, stock):
        time.sleep(0.5)
        self.logger.info("输入的商品库存是:" + stock)
        self.entity_good_p.get_stock_element().send_keys(stock)

    # 确定
    def determine(self):
        time.sleep(0.5)
        self.entity_good_p.get_determine_element().click()

    # 运费
    def fare(self):
        time.sleep(0.5)
        self.entity_good_p.get_fare_element().click()

    # 运费类型
    def fare_manner(self):
        time.sleep(0.5)
        self.entity_good_p.get_fare_manner_element().click()

    # 限购数量
    def limit_quantity(self, limit_quantity):
        time.sleep(0.5)
        self.logger.info("输入的商品限购数量是:" + limit_quantity)
        self.entity_good_p.get_limit_quantity_element().send_keys(limit_quantity)

    # 品牌
    def brand(self, brand):
        time.sleep(0.5)
        self.logger.info("输入的商品品牌是:" + brand)
        self.entity_good_p.get_brand_element().send_keys(brand)

    # 生产日期
    def production_Date(self):
        time.sleep(0.5)
        self.entity_good_p.get_production_Date_element()

    # 生产日期-完成
    def production_Date_ok(self):
        time.sleep(0.5)
        self.entity_good_p.production_Date_ok_element().click()

    # 保质期
    def shelf_life(self):
        time.sleep(0.5)
        self.entity_good_p.get_shelf_life_element()

    # 产地
    def address(self):
        time.sleep(0.5)
        self.entity_good_p.get_address_element()

    # 制造商
    def manufacturer(self):
        time.sleep(0.5)
        self.entity_good_p.get_manufacturer_element()

    # 生产许可证编号
    def production_number(self):
        time.sleep(0.5)
        self.entity_good_p.get_production_number_element()

    # 立即上架
    def submit(self):
        time.sleep(0.5)
        self.entity_good_p.get_submit_element().click()

    # 放入仓库
    def storage(self):
        time.sleep(0.5)
        self.entity_good_p.get_storage_element().click()

    # 获取错误提示文字信息
    def error_text(self):
        text = self.entity_good_p.get_error_text_element().text
        return text
