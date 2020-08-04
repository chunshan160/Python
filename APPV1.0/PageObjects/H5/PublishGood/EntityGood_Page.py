#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/23 14:20
# @Author :春衫
# @File :publishcommodity_page.py

import time
from PageLocators.H5.PubilcGood import EntityGood as EG
from Common.BasePage import BasePage


# 发布实物商品
class EntityGoodPage(BasePage):



    # 点击上传主图
    def upload_image(self):
        time.sleep(0.5)
        self.get_element(EG.product_image).click()

    # 选择图片
    def check_image(self):
        time.sleep(0.5)
        self.get_element(EG.check_image).click()

    # 点击确定
    def btn_ok(self):
        time.sleep(0.5)
        self.get_element(EG.btn_ok).click()

    # 输入商品标题
    def product_title(self, product_title):
        time.sleep(0.5)
        self.logger.info("输入的商品标题是:" + product_title)
        self.get_element(EG.product_title).send_keys(product_title)

    # 点击商品描述
    def product_detail(self):
        time.sleep(0.5)
        self.get_element(EG.product_detail).click()

    # 输入商品详情
    def product_description(self, product_description):
        time.sleep(0.5)
        self.logger.info("输入商品详情:" + product_description)
        self.get_element(EG.product_description).send_keys(product_description)

    # 商品详情页-上传商品图片
    def description_image(self):
        time.sleep(0.5)
        self.get_element(EG.description_image).click()

    # 点击完成，回到商品详情页
    def finish(self):
        time.sleep(0.5)
        self.get_element(EG.finish).click()

    # 点击品相
    def quality(self):
        time.sleep(0.5)
        self.get_element(EG.quality).click()

    # 选择全新
    def quality_new(self):
        time.sleep(0.5)
        self.get_element(EG.quality_new).click()

    # 选择分类
    def category(self):
        time.sleep(0.5)
        self.get_element(EG.category).click()

    # 选择二级分类
    def second_categpry(self):
        time.sleep(0.5)
        self.get_element(EG.second_categpry).click()

    # 选择三级分类
    def third_categpry(self):
        time.sleep(0.5)
        self.get_element(EG.third_categpry).click()

    # 点击商品类型
    def product_type(self):
        time.sleep(0.5)
        self.get_element(EG.product_type).click()

    # 选择商品类型
    def product_type_select(self):
        time.sleep(0.5)
        self.get_element(EG.product_type_select).click()

    # 点击规格
    def specification(self):
        time.sleep(0.5)
        self.get_element(EG.specification).click()

    # 进入商品规格页面，输入属性
    def property_1(self, property_1):
        time.sleep(0.5)
        self.logger.info("输入的商品规格是:" + property_1)
        self.get_element(EG.property_1).send_keys(property_1)

    def property_2(self, property_2):
        time.sleep(0.5)
        self.logger.info("输入的商品属性是:" + property_2)
        self.get_element(EG.property_2).send_keys(property_2)

    # 上传规格图片
    def upload_specification_image(self):
        time.sleep(0.5)
        self.get_element(EG.upload_specification_image).click()

    # 选择规格图片
    def check_specification_image(self):
        time.sleep(0.5)
        self.get_element(EG.check_specification_image).click()

    # 下一步
    def next(self):
        time.sleep(0.5)
        self.get_element(EG.next).click()

    # 进货价
    def purchase_price(self, purchase_price):
        time.sleep(0.5)
        self.logger.info("输入的商品进货价是:" + purchase_price)
        self.get_element(EG.purchase_price).send_keys(purchase_price)

    # 出售价
    def sell_price(self, sell_price):
        time.sleep(0.5)
        self.logger.info("输入的商品出售价是:" + sell_price)
        self.get_element(EG.sell_price).send_keys(sell_price)

    # 库存
    def stock(self, stock):
        time.sleep(0.5)
        self.logger.info("输入的商品库存是:" + stock)
        self.get_element(EG.stock).send_keys(stock)

    # 确定
    def determine(self):
        time.sleep(0.5)
        self.get_element(EG.determine).click()

    # 运费
    def fare(self):
        time.sleep(0.5)
        self.get_element(EG.fare).click()

    # 运费类型-包邮
    def fare_manner(self):
        time.sleep(0.5)
        self.get_element(EG.fare_manner).click()

    # 限购数量
    def limit_quantity(self, limit_quantity):
        time.sleep(0.5)
        self.logger.info("输入的商品限购数量是:" + limit_quantity)
        self.get_element(EG.limit_quantity).send_keys(limit_quantity)

    # 品牌
    def brand(self, brand):
        time.sleep(0.5)
        self.logger.info("输入的商品品牌是:" + brand)
        self.get_element(EG.brand).send_keys(brand)

    # 生产日期
    def production_Date(self):
        time.sleep(0.5)
        self.get_element(EG.production_Date)

    # 生产日期-完成
    def production_Date_ok(self):
        time.sleep(0.5)
        self.get_element(EG.production_Date_ok)

    # 保质期
    def shelf_life(self):
        time.sleep(0.5)
        self.get_element(EG.shelf_life)

    # 产地
    def address(self):
        time.sleep(0.5)
        self.get_element(EG.address)

    # 制造商
    def manufacturer(self):
        time.sleep(0.5)
        self.get_element(EG.manufacturer)

    # 生产许可证编号
    def production_number(self):
        time.sleep(0.5)
        self.get_element(EG.production_number)


    # 发布实物商品
    def publish_entity_good(self, product_title, product_description, property_1, property_2, purchase_price,
             sell_price, stock, limit_quantity):
        # 上传主图
        self.upload_image()
        # 选择图片
        self.check_image()
        # 点击确定
        self.btn_ok()
        # 输入商品标题
        self.product_title(product_title)
        # 点击商品描述
        self.product_detail()
        # 输入商品详情
        self.product_description(product_description)
        # 商品详情页上传商品
        self.description_image()
        # 选择图片
        self.check_image()
        # 点击确定
        self.btn_ok()
        # 点击完成，回到商品详情页
        self.finish()
        # 点击品相
        self.quality()
        # 选择全新
        self.quality_new()
        # 选择分类
        self.category()
        # 选择二级分类
        self.second_categpry()
        # 选择三级分类
        self.third_categpry()
        # 点击商品类型
        self.product_type()
        # 选择商品类型
        self.product_type_select()
        # 点击规格
        self.specification()
        # 进入商品规格页面，输入属性
        self.property_1(property_1)
        self.property_2(property_2)
        # 上传规格图片
        self.upload_specification_image()
        # 选择规格图片
        self.check_specification_image()
        # 下一步
        self.next()
        # 进货价
        self.purchase_price(purchase_price)
        # 出售价
        self.sell_price(sell_price)
        # 库存
        self.stock(stock)
        # 确定
        self.determine()
        # 运费
        self.fare()
        # 运费类型
        self.fare_manner()
        # 限购数量
        self.limit_quantity(limit_quantity)
