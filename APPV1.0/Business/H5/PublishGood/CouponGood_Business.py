#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 9:50
# @Author :春衫
# @File :CouponGood_Business.py

from Handle.H5.PublishGood.CouponGood_Handle import CouponGoodHandle


class CouponGoodBusiness:

    def __init__(self, driver):
        self.coupon_good_h = CouponGoodHandle(driver)

    def publish_coupon_good(self,product_title,product_description,total_price,stock,limit_quantity):
        
        # 上传主图
        self.coupon_good_h.upload_main_image()
        # 选择图片
        self.coupon_good_h.check_image()
        # 点击确定
        self.coupon_good_h.btn_ok()
        # 输入商品标题
        self.coupon_good_h.coupon_good(product_title)
        # 输入商品详情
        self.coupon_good_h.product_description(product_description)
        # 选择分类
        self.coupon_good_h.categpry()
        # 选择二级分类
        self.coupon_good_h.second_categpry()
        # 选择三级分类
        self.coupon_good_h.third_categpry()
        # 点击券类
        self.coupon_good_h.coupon()
        # 选择券类
        self.coupon_good_h.coupon_categpry()
        # 商品总价
        self.coupon_good_h.total_price(total_price)
        # 商品库存
        self.coupon_good_h.stock(stock)
        # 限购数量
        self.coupon_good_h.limit_quantity(limit_quantity)

    # 立即上架
    def submit(self):
        self.coupon_good_h.submit()

    # 放入仓库
    def storage(self):
        self.coupon_good_h.storage()

    # 错误信息
    def error_text(self, expected_text):
        self.submit()
        try:
            if self.coupon_good_h.error_text() == expected_text:
                return True
        except:
            return False