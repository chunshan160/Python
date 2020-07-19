#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/23 14:20
# @Author :春衫
# @File :publishcommodity_page.py


from PageLocators.H5.PubilcGood import EntityGood as EG
from Common.find_element import FindElement


# 发布实物商品
class EntityGoodPage:

    def __init__(self, driver):
        self.fd=FindElement(driver)

    #上传图片
    def get_upload_image_element(self):
        return self.fd.find_element(EG.product_image)

    # 输入商品标题
    def get_product_title_element(self):
        return self.fd.find_element(EG.product_title)
    
    # 点击商品描述
    def get_product_detail_element(self):
        return self.fd.find_element(EG.product_detail)
    
    # 输入商品详情
    def get_product_description_element(self):
        return self.fd.find_element(EG.product_description)

    # 商品详情页上传商品
    def get_product_description_image_element(self):
        return self.fd.find_element(EG.product_description_image)

    # 点击完成，回到商品详情页
    def get_finish_element(self):
        return self.fd.find_element(EG.finish)

    # 点击品相
    def get_quality_element(self):
        return self.fd.find_element(EG.quality)

    # 选择全新
    def get_quality_new_element(self):
        return self.fd.find_element(EG.quality_new)

    # 选择分类
    def get_category_element(self):
        return self.fd.find_element(EG.category)

    # 选择二级分类
    def get_second_categpry_element(self):
        return self.fd.find_element(EG.second_categpry)

    # 选择三级分类
    def get_third_categpry_element(self):
        return self.fd.find_element(EG.third_categpry)

    # 点击商品类型
    def get_product_type_element(self):
        return self.fd.find_element(EG.product_type)

    # 选择商品类型
    def get_product_type_select_element(self):
        return self.fd.find_element(EG.product_type_select)

    # 点击规格
    def get_specification_element(self):
        return self.fd.find_element(EG.specification)

    # 进入商品规格页面，输入属性
    def get_property_1_element(self):
        return self.fd.find_element(EG.property_1)

    def get_property_2_element(self):
        return self.fd.find_element(EG.property_2)

    # 规格图片
    def get_specification_image_element(self):
        return self.fd.find_element(EG.specification_image)

    # 下一步
    def get_next_element(self):
        return self.fd.find_element(EG.next)

    # 进货价
    def get_purchase_price_element(self):
        return self.fd.find_element(EG.purchase_price)

    #出售价
    def get_sell_price_element(self):
        return self.fd.find_element(EG.sell_price)

    #库存
    def get_stock_element(self):
        return self.fd.find_element(EG.stock)

    # 确定
    def get_determine_element(self):
        return self.fd.find_element(EG.determine)

    # 运费
    def get_fare_element(self):
        return self.fd.find_element(EG.fare)

    # 运费类型
    def get_fare_manner_element(self):
        return self.fd.find_element(EG.fare_manner)

    # 限购数量
    def get_limit_quantity_element(self):
        return self.fd.find_element(EG.limit_quantity)

    # 立即上架
    def get_submit_element(self):
        return self.fd.find_element(EG.submit)

    # 放入仓库
    def get_storage_element(self):
        return self.fd.find_element(EG.storage)

    # 获取错误提示元素
    def get_error_text_element(self):
        return self.fd.find_element(EG.error_toast)