#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:35
#@Author :春衫
#@File :ServerGood_Page.py

from PageLocators.H5.PubilcGood import EntityGood as EG
from PageLocators.H5.PubilcGood import ServerGood as BS
from Common.find_element import FindElement


# 发布商企服务
class ServicesGoodPage:

    def __init__(self, driver):
        self.find_element=FindElement(driver)

    # 上传图片
    def upload_image(self):
        return self.find_element.find_element(EG.product_image)


    # 输入商品标题
    def services_good(self):
        return self.find_element.find_element(BS.product_title)

    # 输入商品详情
    def product_description(self):
        return self.find_element.find_element(BS.product_description)

    # 选择分类
    def classification(self):
        return self.find_element.find_element(BS.classification)

    # 选择二级分类
    def second_classification(self):
        return self.find_element.find_element(BS.second_classification)

    # 选择三级分类
    def third_classification(self):
        return self.find_element.find_element(BS.third_classification)

    # 商品总价
    def total_price(self):
        return self.find_element.find_element(BS.total_price)

    # 预付款
    def subsist(self):
        return self.find_element.find_element(BS.subsist)

    # 商品库存
    def stock(self):
        return self.find_element.find_element(BS.stock)

    # 限购数量
    def limit_quantity(self):
        return self.find_element.find_element(BS.limit_quantity)