#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 16:42
# @Author :春衫
# @File :EntityGood_Business.py


from Handle.H5.PublishGood.EntityGood_Handle import EntityGoodHandle


class EntityGoodBusiness:

    def __init__(self, driver):
        self.entity_good_h = EntityGoodHandle(driver)

    def publish_entity_good(self, product_title, product_description, property_1, property_2, purchase_price,
                            sell_price, stock, limit_quantity):

        # 上传主图
        self.entity_good_h.upload_main_image()
        # 选择图片
        self.entity_good_h.check_main_image()
        # 点击确定
        self.entity_good_h.btn_ok()
        # 输入商品标题
        self.entity_good_h.send_product_title(product_title)
        # 点击商品描述
        self.entity_good_h.product_detail()
        # 输入商品详情
        self.entity_good_h.product_description(product_description)
        # 商品详情页上传商品
        self.entity_good_h.product_description_image()
        # 选择图片
        self.entity_good_h.check_main_image()
        # 点击确定
        self.entity_good_h.btn_ok()
        # 点击完成，回到商品详情页
        self.entity_good_h.finish()
        # 点击品相
        self.entity_good_h.quality()
        # 选择全新
        self.entity_good_h.quality_new()
        # 选择分类
        self.entity_good_h.category()
        # 选择二级分类
        self.entity_good_h.second_categpry()
        # 选择三级分类
        self.entity_good_h.third_categpry()
        # 点击商品类型
        self.entity_good_h.product_type()
        # 选择商品类型
        self.entity_good_h.product_type_select()
        # 点击规格
        self.entity_good_h.specification()
        # 进入商品规格页面，输入属性
        self.entity_good_h.property_1(property_1)
        self.entity_good_h.property_2(property_2)
        # 上传规格图片
        self.entity_good_h.upload_specification_image()
        # 选择规格图片
        self.entity_good_h.check_specification_image()
        # 下一步
        self.entity_good_h.next()
        # 进货价
        self.entity_good_h.purchase_price(purchase_price)
        # 出售价
        self.entity_good_h.sell_price(sell_price)
        # 库存
        self.entity_good_h.stock(stock)
        # 确定
        self.entity_good_h.determine()
        # 运费
        self.entity_good_h.fare()
        # 运费类型
        self.entity_good_h.fare_manner()
        # 限购数量
        self.entity_good_h.limit_quantity(limit_quantity)

    # 立即上架
    def submit(self):
        self.entity_good_h.submit()

    #放入仓库
    def storage(self):
        self.entity_good_h.storage()

    #错误信息
    def error_text(self,expected_text):
        self.submit()
        try:
            if self.entity_good_h.error_text() == expected_text:
                return True
        except:
            return False
