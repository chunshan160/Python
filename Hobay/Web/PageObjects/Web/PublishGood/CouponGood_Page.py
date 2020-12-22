#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:32
# @Author :春衫
# @File :CouponGood_Page.py


from Common.user_log import UserLog
from Web.PageLocators.Web.PubilcGood import CouponGood as CG
from Web.PageObjects.Web import PublishGoodCommon
from Common.BasePage import BasePage


# 发布本地生活


class CouponGoodPage(BasePage):

    # 输入商品标题
    def product_title(self, product_title, text=""):
        doc = text + "输入商品标题-"
        UserLog().info("输入的商品标题是:" + product_title)
        self.input_text(CG.product_title, product_title, doc=doc)

    # 输入商品详情
    def product_description(self, product_description, text=""):
        doc = text + "输入商品详情-"
        UserLog().info("输入商品详情:" + product_description)
        self.input_text(CG.product_description, product_description, doc=doc)

    # 点击券类
    def coupon(self, text=""):
        doc = text + "点击【券类】按钮-"
        self.click_element(CG.coupon, doc=doc)

    # 选择券类
    def coupon_category(self, category_type, text=""):
        doc = text + f"选择【{category_type}】-"
        new_locator = self.locator_by_text(CG.coupon_category, category_type)
        self.click_element(new_locator, doc=doc)

    # 商品总价
    def total_price(self, total_price, text=""):
        doc = text + "输入商品总价-"
        UserLog().info("输入的商品总价是:" + total_price)
        self.input_text(CG.total_price, total_price, doc=doc)

    # 商品库存
    def stock(self, stock, text=""):
        doc = text + "输入商品库存-"
        UserLog().info("输入的商品库存是:" + stock)
        self.input_text(CG.stock, stock, doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + "输入限购数量-"
        UserLog().info("输入的商品限购数量是:" + limit_quantity)
        self.input_text(CG.limit_quantity, limit_quantity, doc=doc)

    # 发布本地生活
    def coupon_good_information(self, product_title, product_description, second_category_name, third_category_name,
                                category_type, total_price, stock, text=""):
        doc = text + "发布本地生活商品-"
        # 上传主图-选择图片-点击确定
        PublishGoodCommon(self.driver).upload_product_image(text=doc)
        # 输入商品标题
        self.product_title(product_title, text=doc)
        # 输入商品详情
        self.product_description(product_description, text=doc)
        # 选择分类
        PublishGoodCommon(self.driver).category(text=doc)
        # 选择二级分类
        PublishGoodCommon(self.driver).second_category(second_category_name, text=doc)
        # 选择三级分类
        PublishGoodCommon(self.driver).third_category(third_category_name, text=doc)
        # 点击券类
        self.coupon(text=doc)
        # 选择券类
        self.coupon_category(category_type, text=doc)
        # 商品总价
        self.total_price(total_price, text=doc)
        # 商品库存
        self.stock(stock, text=doc)
