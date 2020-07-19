#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 16:42
# @Author :春衫
# @File :EntityGood.py
import time

from Handle.H5.PublishGood.EntityGood_Handle import EntityGoodHandle


class EntityGoodBusiness:
    def __init__(self, driver):
        self.entity_good_h = EntityGoodHandle(driver)

    def publish_entity_good(self, product_title, product_description, property_1, property_2, purchase_price,
                            sell_price, stock, limit_quantity):
        # 上传主图
        self.entity_good_h.upload_main_image()
        # 输入商品标题
        self.entity_good_h.send_product_title(product_title)
        # 点击商品描述
        self.entity_good_h.get_product_detail_element()
        # 输入商品详情
        self.entity_good_h.get_product_description_element(product_description)
        # 商品详情页上传商品
        self.entity_good_h.get_product_description_image_element()
        # 点击完成，回到商品详情页
        self.entity_good_h.get_finish_element()
        # 点击品相
        self.entity_good_h.get_quality_element()
        # 选择全新
        self.entity_good_h.get_quality_new_element()
        # 选择分类
        self.entity_good_h.get_category_element()
        # 选择二级分类
        self.entity_good_h.get_second_categpry_element()
        # 选择三级分类
        self.entity_good_h.get_third_categpry_element()
        # 点击商品类型
        self.entity_good_h.get_product_type_element()
        # 选择商品类型
        self.entity_good_h.get_product_type_select_element()
        # 点击规格
        self.entity_good_h.get_specification_element()
        # 进入商品规格页面，输入属性
        self.entity_good_h.get_property_1_element(property_1)
        self.entity_good_h.get_property_2_element(property_2)
        # 上传规格图片
        self.entity_good_h.get_specification_image_element()
        # 下一步
        self.entity_good_h.get_next_element()
        # 进货价
        self.entity_good_h.get_purchase_price_element(purchase_price)
        # 出售价
        self.entity_good_h.get_sell_price_element(sell_price)
        # 库存
        self.entity_good_h.get_stock_element(stock)
        # 确定
        self.entity_good_h.get_determine_element()
        # 运费
        self.entity_good_h.get_fare_element()
        # 运费类型
        self.entity_good_h.get_fare_manner_element()
        # 限购数量
        self.entity_good_h.get_limit_quantity_element(limit_quantity)

    # 立即上架
    def submit(self):
        self.entity_good_h.get_submit_element()

    #放入仓库
    def storage(self):
        self.entity_good_h.get_storage_element()

    #错误信息
    def get_error_text(self,expected_text):
        self.submit()
        time.sleep(2)
        try:
            if self.entity_good_h.get_error_text() == expected_text:
                return True
        except:
            return False
