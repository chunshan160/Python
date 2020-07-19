#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:32
#@Author :春衫
#@File :CouponGood_Page.py


from PageLocators.H5.PubilcGood import EntityGood as EG
from PageLocators.H5.PubilcGood import CouponGood as CG
from Common.find_element import FindElement


# 发布本地生活
class CouponGoodPage:

    def __init__(self, driver):
        self.driver = driver
        self.find_element=FindElement(self.driver)

    # 上传图片
    def upload_image(self):
        return self.find_element.find_element(EG.product_image)

    # 输入商品标题
    def coupon_good(self):
        return self.find_element.find_element(CG.product_title)

    # 输入商品详情
    def product_description(self):
        return self.find_element.find_element(CG.product_description)

    # 选择分类
    def classification(self):
        return self.find_element.find_element(CG.classification)

    # 选择二级分类
    def second_classification_(self):
        return self.find_element.find_element(CG.second_classification)

    # 选择三级分类
    def third_classification(self):
        return self.find_element.find_element(CG.third_classification)

    # 点击券类
    def coupon(self):
        return self.find_element.find_element(CG.coupon)

    # 选择券类
    def coupon_classification(self):
        return self.find_element.find_element(CG.coupon_classification)

    # 点击确认
    def determine(self):
        return self.find_element.find_element(CG.determine)

    # 商品总价
    def total_price(self):
        return self.find_element.find_element(CG.total_price)

    # 商品库存
    def stock(self):
        return self.find_element.find_element(CG.stock)

    # 限购数量
    def limit_quantity(self):
        return self.find_element.find_element(CG.limit_quantity)