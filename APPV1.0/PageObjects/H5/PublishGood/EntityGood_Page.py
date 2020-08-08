#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/23 14:20
# @Author :春衫
# @File :publishcommodity_page.py

import time
from Common.user_log import UserLog
from PageLocators.H5 import Common
from PageLocators.H5.PubilcGood import EntityGood as EG
from PageLocators.H5.PubilcGood import PubilcGoodCommon as PGCommon
from Common.BasePage import BasePage


# 发布实物商品
class EntityGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title, text=""):
        doc = text + "输入商品标题-"
        time.sleep(0.5)
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(EG.product_title, product_title, doc=doc)

    # 点击商品描述
    def product_detail(self, text=""):
        doc = text + "点击【商品描述】选项-"
        time.sleep(0.5)
        self.click_element(EG.product_detail, doc=doc)

    # 输入商品详情
    def product_description(self, product_description, text=""):
        doc = text + "输入商品详情-"
        time.sleep(0.5)
        self.input_text(EG.product_description, product_description, doc=doc)
        UserLog().info("输入商品详情:" + product_description)

    # 商品详情页-上传商品图片
    def description_image(self, text=""):
        doc = text + "商品详情页-点击【上传商品图片】按钮-"
        time.sleep(0.5)
        self.click_element(EG.description_btn, doc=doc)

    # 点击完成，回到商品详情页
    def finish(self, text=""):
        doc = text + "点击【完成】按钮-"
        time.sleep(0.5)
        self.click_element(EG.finish, doc=doc)

    # 点击品相
    def quality(self, text=""):
        doc = text + "点击【品相】选项-"
        time.sleep(0.5)
        self.click_element(EG.quality, doc=doc)

    # 选择全新
    def quality_new(self, text=""):
        doc = text + "点击【全新】选项-"
        time.sleep(0.5)
        self.click_element(EG.quality_new, doc=doc)

    # 选择分类
    def category(self, text=""):
        doc = text + "点击【分类】选项-"
        time.sleep(0.5)
        self.click_element(EG.category, doc=doc)

    # 选择二级分类
    def second_categpry(self, text=""):
        doc = text + "点击【二级分类】选项-"
        time.sleep(1)
        self.click_elements(EG.second_categpry,0, doc=doc)

    # 选择三级分类
    def third_categpry(self, text=""):
        doc = text + "选择【三级分类】选项-"
        time.sleep(0.5)
        self.click_elements(EG.third_categpry,0, doc=doc)

    # 点击商品类型
    def product_type(self, text=""):
        doc = text + "点击【商品类型】选项-"
        time.sleep(0.5)
        self.click_element(EG.product_type, doc=doc)

    # 选择商品类型
    def product_type_select(self, text=""):
        doc = text + "选择【商品类型】选项-"
        time.sleep(0.5)
        self.click_elements(EG.product_type_select,0, doc=doc)

    # 点击规格
    def specification(self, text=""):
        doc = text + "点击【规格】选项-"
        time.sleep(0.5)
        self.click_element(EG.specification, doc=doc)

    # 输入商品规格
    def property_1(self, property_1, text=""):
        doc = text + "输入商品规格-"
        time.sleep(0.5)
        UserLog().info("输入的商品规格是:" + property_1)
        self.input_text(EG.property_1, property_1, doc=doc)

    # 输入商品属性
    def property_2(self, property_2, text=""):
        doc = text + "输入商品属性-"
        time.sleep(0.5)
        UserLog().info("输入的商品属性是:" + property_2)
        self.input_text(EG.property_2, property_2, doc=doc)

    # 上传规格图片
    def upload_specification_image(self, text=""):
        doc = text + "点击上传规格图片-"
        time.sleep(0.5)
        self.click_element(EG.upload_specification_image, doc=doc)

    # 选择规格图片
    def check_specification_image(self, text=""):
        doc = text + "选择规格图片-"
        time.sleep(0.5)
        self.click_element(EG.check_specification_image, doc=doc)

    # 下一步
    def next(self, text=""):
        doc = text + "点击【下一步】按钮-"
        time.sleep(0.5)
        self.click_element(EG.next, doc=doc)

    # 进货价
    def purchase_price(self, purchase_price, text=""):
        doc = text + "输入进货价-"
        time.sleep(0.5)
        UserLog().info("输入的商品进货价是:" + purchase_price)
        self.input_text(EG.purchase_price, purchase_price, doc=doc)

    # 出售价
    def sell_price(self, sell_price, text=""):
        doc = text + "输入出售价-"
        time.sleep(0.5)
        UserLog().info("输入的商品出售价是:" + sell_price)
        self.input_text(EG.sell_price, sell_price, doc=doc)

    # 库存
    def stock(self, stock, text=""):
        doc = text + "输入库存-"
        time.sleep(0.5)
        UserLog().info("输入的商品库存是:" + stock)
        self.input_text(EG.stock, stock, doc=doc)

    # 确定
    def determine(self, text=""):
        doc = text + "点击【确定】按钮-"
        time.sleep(0.5)
        self.click_element(EG.determine, doc=doc)

    # 运费
    def fare(self, text=""):
        doc = text + "点击【运费】选项-"
        time.sleep(0.5)
        self.click_element(EG.fare, doc=doc)

    # 运费类型-包邮
    def fare_manner(self, text=""):
        doc = text + "选择【包邮】选项-"
        time.sleep(0.5)
        self.click_elements(EG.fare_manner,0, doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + "输入限购数量-"
        time.sleep(0.5)
        UserLog().info("输入的商品限购数量是:" + limit_quantity)
        self.input_text(EG.limit_quantity, limit_quantity, doc=doc)

    # 品牌
    def brand(self, brand, text=""):
        doc = text + "输入商品品牌-"
        time.sleep(0.5)
        UserLog().info("输入的商品品牌是:" + brand)
        self.input_text(EG.brand, brand, doc=doc)

    # 生产日期
    def production_Date(self, text=""):
        doc = text + "点击【生产日期】选项-"
        time.sleep(0.5)
        self.click_element(EG.production_Date, doc=doc)

    # 生产日期-完成
    def production_Date_ok(self, text=""):
        doc = text + "点击【完成】按钮-"
        time.sleep(0.5)
        self.click_element(EG.production_Date_ok, doc=doc)

    # 保质期
    def shelf_life(self, number, text=""):
        doc = text + "输入保质期-"
        time.sleep(0.5)
        UserLog().info("输入的保质期是:" + number)
        self.input_text(EG.shelf_life, number, doc=doc)

    # 产地
    def address(self, address, text=""):
        doc = text + "输入产地-"
        time.sleep(0.5)
        UserLog().info("输入的产地是:" + address)
        self.input_text(EG.address, address, doc=doc)

    # 制造商
    def manufacturer(self, manufacturer, text=""):
        doc = text + "输入制造商-"
        time.sleep(0.5)
        UserLog().info("输入的制造商是:" + manufacturer)
        self.input_text(EG.manufacturer, manufacturer, doc=doc)

    # 生产许可证编号
    def production_number(self, production_number, text=""):
        doc = text + "输入生产许可证编号-"
        time.sleep(0.5)
        UserLog().info("输入的生产许可证编号是:" + production_number)
        self.input_text(EG.production_number, production_number, doc=doc)

    # 发布实物商品
    def entity_good_information(self, product_title, product_description, property_1, property_2, purchase_price,
                                sell_price, stock, limit_quantity, text=""):
        # 上传主图-选择图片-点击确定
        self.app_upload_image(PGCommon.product_image, PGCommon.check_image, PGCommon.btn_ok, doc=text)
        # 输入商品标题
        self.product_title(product_title, text)
        # # 点击商品描述
        self.product_detail()
        # 输入商品详情
        self.product_description(product_description, text="")
        # 商品详情页上传商品
        self.app_upload_image(EG.description_btn, PGCommon.check_image, PGCommon.btn_ok, doc=text)
        # 点击完成，回到商品详情页
        self.finish(text)
        # 点击品相
        self.quality(text)
        # 选择全新
        self.quality_new(text)
        # 选择分类
        self.category(text)
        # 选择二级分类
        self.second_categpry(text)
        # 选择三级分类
        self.third_categpry(text)
        # 点击商品类型
        self.product_type(text)
        # 选择商品类型
        self.product_type_select(text)
        # 点击规格
        self.specification(text)
        # 进入商品规格页面，输入属性
        self.property_1(property_1, text)
        self.property_2(property_2, text)
        # 上传规格图片
        self.upload_specification_image(text)
        # 选择规格图片
        self.check_specification_image(text)
        # 下一步
        self.next(text)
        # 进货价
        self.purchase_price(purchase_price, text)
        # 出售价
        self.sell_price(sell_price, text)
        # 库存
        self.stock(stock, text)
        # 确定
        self.determine(text)
        # 运费
        self.fare(text)
        # 运费类型
        self.fare_manner(text)
