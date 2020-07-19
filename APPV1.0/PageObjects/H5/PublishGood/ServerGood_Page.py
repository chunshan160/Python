#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:35
#@Author :春衫
#@File :ServerGood_Page.py


from PageLocators.H5.PubilcGood import ServerGood as SG
from Common.find_element import FindElement


# 发布商企服务
class ServicesGoodPage:

    def __init__(self, driver):
        self.fd=FindElement(driver)

    # 上传图片
    def get_upload_image_element(self):
        return self.fd.find_element(SG.product_image)

    # 选择图片
    def get_check_image_element(self):
        return self.fd.find_element(SG.check_image)

    # 点击确定
    def get_btn_ok_element(self):
        return self.fd.find_element(SG.btn_ok)

    # 输入商品标题
    def get_product_title_element(self):
        return self.fd.find_element(SG.product_title)

    # 输入商品详情
    def get_product_description_element(self):
        return self.fd.find_element(SG.product_description)

    # 选择分类
    def get_category_element(self):
        return self.fd.find_element(SG.category)

    # 选择二级分类
    def get_second_categpry_element(self):
        return self.fd.find_element(SG.second_categpry)

    # 选择三级分类
    def get_third_categpry_element(self):
        return self.fd.find_element(SG.third_categpry)

    # 商品总价
    def get_total_price_element(self):
        return self.fd.find_element(SG.total_price)

    # 预付款
    def get_subsist_element(self):
        return self.fd.find_element(SG.subsist)

    # 商品库存
    def get_stock_element(self):
        return self.fd.find_element(SG.stock)

    # 限购数量
    def get_limit_quantity_element(self):
        return self.fd.find_element(SG.limit_quantity)

    # 立即上架
    def get_submit_element(self):
        return self.fd.find_element(SG.submit)

    # 放入仓库
    def get_storage_element(self):
        return self.fd.find_element(SG.storage)

    # 获取错误提示元素
    def get_error_text_element(self):
        return self.fd.find_element(SG.error_toast)