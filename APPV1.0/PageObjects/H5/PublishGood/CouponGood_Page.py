#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:32
#@Author :春衫
#@File :CouponGood_Page.py

from PageLocators.H5.PubilcGood import CouponGood as CG
from Common.find_element import FindElement


# 发布本地生活
class CouponGoodPage:

    def __init__(self, driver):
        self.fd=FindElement(driver)

    # 点击上传主图
    def get_upload_image_element(self):
        return self.fd.find_element(CG.product_image)

    # 选择图片
    def get_check_image_element(self):
        return self.fd.find_element(CG.check_image)

    # 点击确定
    def get_btn_ok_element(self):
        return self.fd.find_element(CG.btn_ok)

    # 输入商品标题
    def get_product_title_element(self):
        return self.fd.find_element(CG.product_title)

    # 输入商品详情
    def get_product_description_element(self):
        return self.fd.find_element(CG.product_description)

    # 选择分类
    def get_categpry_element(self):
        return self.fd.find_element(CG.category)

    # 选择二级分类
    def get_second_categpry_element(self):
        return self.fd.find_element(CG.second_categpry)

    # 选择三级分类
    def get_third_categpry_element(self):
        return self.fd.find_element(CG.third_categpry)

    # 点击券类
    def get_coupon_element(self):
        return self.fd.find_element(CG.coupon)

    # 选择券类
    def get_coupon_categpry_element(self):
        return self.fd.find_element(CG.coupon_categpry,1)

    # 商品总价
    def get_total_price_element(self):
        return self.fd.find_element(CG.total_price)

    # 商品库存
    def get_stock_element(self):
        return self.fd.find_element(CG.stock)

    # 限购数量
    def get_limit_quantity_element(self):
        return self.fd.find_element(CG.limit_quantity)

    # 立即上架
    def get_submit_element(self):
        return self.fd.find_element(CG.submit)

    # 放入仓库
    def get_storage_element(self):
        return self.fd.find_element(CG.storage)

    # 获取错误提示元素
    def get_error_text_element(self):
        return self.fd.find_element(CG.error_toast)