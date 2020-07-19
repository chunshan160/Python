#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 16:07
# @Author :春衫
# @File :EntityGood_Page.py

import time
from PageObjects.H5.PublishGood.EntityGood_Page import EntityGoodPage
from Handle.H5.PublishGood.UploadImage import UploadImage
from Common.user_log import UserLog


# 发布实物商品
class EntityGoodHandle:

    def __init__(self, driver):
        self.entity_good_p = EntityGoodPage(driver)
        self.up_image = UploadImage(driver)
        self.logger = UserLog()

    # 上传主图
    def upload_main_image(self):
        self.up_image.upload_main_image()

    # 上传详情图片
    def upload_description_image(self):
        self.up_image.upload_description_image()

    #上传规格图片
    def upload_specification_image(self):
        self.up_image.upload_specification_image()

    # 输入商品标题
    def send_product_title(self, product_title):
        self.logger.info("输入的商品标题是:" + product_title)
        self.entity_good_p.get_product_title_element().send_keys(product_title)

    # 点击商品描述
    def get_product_detail_element(self):
        self.entity_good_p.get_product_detail_element().click()

    # 输入商品详情
    def get_product_description_element(self, product_description):
        self.logger.info("输入商品详情:" + product_description)
        self.entity_good_p.get_product_description_element().send_keys(product_description)

    # 商品详情页上传商品
    def get_product_description_image_element(self):
        self.upload_description_image()

    # 点击完成，回到商品详情页
    def get_finish_element(self):
        self.entity_good_p.get_finish_element().click()

    # 点击品相
    def get_quality_element(self):
        self.entity_good_p.get_quality_element().click()

    # 选择全新
    def get_quality_new_element(self):
        time.sleep(2)
        self.entity_good_p.get_quality_new_element().click()

    # 选择分类
    def get_category_element(self):
        self.entity_good_p.get_category_element().click()

    # 选择二级分类
    def get_second_categpry_element(self):
        time.sleep(2)
        self.entity_good_p.get_second_categpry_element().click()

    # 选择三级分类
    def get_third_categpry_element(self):
        self.entity_good_p.get_third_categpry_element().click()

    # 点击商品类型
    def get_product_type_element(self):
        self.entity_good_p.get_product_type_element().click()

    # 选择商品类型
    def get_product_type_select_element(self):
        time.sleep(2)
        self.entity_good_p.get_product_type_select_element().click()

    # 点击规格
    def get_specification_element(self):
        self.entity_good_p.get_specification_element().click()

    # 进入商品规格页面，输入属性
    def get_property_1_element(self, property_1):
        self.logger.info("输入的商品规格是:" + property_1)
        self.entity_good_p.get_property_1_element().send_keys(property_1)

    def get_property_2_element(self, property_2):
        self.logger.info("输入的商品属性是:" + property_2)
        self.entity_good_p.get_property_2_element().send_keys(property_2)

    # 上传规格图片
    def get_specification_image_element(self):
        self.upload_specification_image()

    # 下一步
    def get_next_element(self):
        self.entity_good_p.get_next_element().click()

    # 进货价
    def get_purchase_price_element(self, purchase_price):
        self.logger.info("输入的商品进货价是:" + purchase_price)
        self.entity_good_p.get_purchase_price_element().send_keys(purchase_price)

    # 出售价
    def get_sell_price_element(self, sell_price):
        self.logger.info("输入的商品出售价是:" + sell_price)
        self.entity_good_p.get_sell_price_element().send_keys(sell_price)

    # 库存
    def get_stock_element(self, stock):
        self.logger.info("输入的商品库存是:" + stock)
        self.entity_good_p.get_stock_element().send_keys(stock)

    # 确定
    def get_determine_element(self):
        self.entity_good_p.get_determine_element().click()

    # 运费
    def get_fare_element(self):
        self.entity_good_p.get_fare_element().click()

    # 运费类型
    def get_fare_manner_element(self):
        time.sleep(2)
        self.entity_good_p.get_fare_manner_element().click()

    # 限购数量
    def get_limit_quantity_element(self, limit_quantity):
        self.logger.info("输入的商品限购数量是:" + limit_quantity)
        self.entity_good_p.get_limit_quantity_element().send_keys(limit_quantity)

    # 立即上架
    def get_submit_element(self):
        self.entity_good_p.get_submit_element().click()

    # 放入仓库
    def get_storage_element(self):
        self.entity_good_p.get_storage_element().click()

    # 获取错误提示文字信息
    def get_error_text(self):
        try:
            text = self.entity_good_p.get_error_text_element().text
        except:
            text = None
        return text
