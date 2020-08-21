#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/23 14:20
# @Author :春衫
# @File :publishcommodity_page.py

import time
from PageLocators.H5.PubilcGood import EntityGood as EG
from PageLocators.H5.PubilcGood import  CouponGood_Page as CG
from PageLocators.H5.PubilcGood import ServerGood as BS
from Common.project_path import *
from Common.find_element import FindElement
from PageObjects.Web.new.EntityGood_Page import EntityGood
from Handle.H5.PublishGood.UploadImage import UploadImage


# 发布商品-商品类型
class PublishGood(object):

    def __init__(self, driver):
        self.driver = driver
        self.find_element=FindElement(self.driver)
        self.publish_entity_good=EntityGood(self.driver)
        self.uploadimage=UploadImage(self.driver)


    def upload_image(self,product_image):
        # 上传图片
        self.find_element.find_element(product_image).click()
        os.system(image_path)
        time.sleep(2)

    # 发布实物商品
    def publish_entity_good(self, product_title, product_description, property_1, property_2, purchase_price, sell_price, stock,
                   limit_quantity):
        #上传图片
        self.uploadimage.upload_image()

        # 输入商品标题
        self.find_element.find_element(EG.product_title).send_keys(product_title)
        # 点击商品描述
        self.find_element.find_element(EG.product_detail).click()
        # 输入商品详情
        self.find_element.find_element(EG.product_description).send_keys(product_description)
        # 商品详情页上传商品
        self.find_element.find_element(EG.product_description_image).click()
        os.system(project_path.project_path)
        time.sleep(2)
        # 点击完成，回到商品详情页
        self.find_element.find_element(EG.finish).click()
        # 点击品相
        self.find_element.find_element(EG.quality).click()
        time.sleep(2)
        # 选择全新
        self.find_element.find_element(EG.quality_new).click()
        # 选择分类
        self.find_element.find_element(EG.category).click()
        # 选择二级分类
        self.find_element.find_element(EG.second_categpry).click()
        # 选择三级分类
        self.find_element.find_element(EG.third_categpry).click()
        # 点击商品类型
        self.find_element.find_element(EG.product_type).click()
        time.sleep(2)
        # 选择商品类型
        self.find_element.find_element(EG.product_type_select).click()
        time.sleep(2)
        # 点击规格
        self.find_element.find_element(EG.specification).click()
        # 进入商品规格页面，输入属性
        self.find_element.find_element(EG.property_1).send_keys(property_1)
        self.find_element.find_element(EG.property_2).send_keys(property_2)
        self.find_element.find_element(EG.specification_image).click()
        os.system(project_path.project_path)
        time.sleep(1)
        # 下一步
        self.find_element.find_element(EG.next).click()
        # 进货价
        self.find_element.find_element(EG.purchase_price).send_keys(
            purchase_price)
        self.find_element.find_element(EG.sell_price).send_keys(sell_price)
        self.find_element.find_element(EG.stock).send_keys(stock)
        # 确定
        self.find_element.find_element(EG.determine).click()
        # 运费
        self.find_element.find_element(EG.fare).click()
        time.sleep(2)
        # 运费类型
        self.find_element.find_element(EG.fare_manner).click()
        time.sleep(1)
        # 限购数量
        self.find_element.find_element(EG.limit_quantity).send_keys(
            limit_quantity)

    # 立即上架
    def submit(self, submit):
        time.sleep(2)
        self.find_element.find_element(submit).click()

    # 放入仓库
    def storage(self, storage):
        time.sleep(2)
        self.find_element.find_element(storage).click()

    # 发布本地生活
    def Local_Life(self, product_title, product_description, total_price, stock, limit_quantity):
        # 上传图片
        self.upload_image(EG.product_image)

        # 输入商品标题
        self.find_element.find_element(CG.product_title).send_keys(product_title)
        # 输入商品详情
        self.find_element.find_element(CG.product_description).send_keys(
            product_description)
        # 选择分类
        self.find_element.find_element(CG.classification).click()
        # 选择二级分类
        self.find_element.find_element(CG.second_classification).click()
        # 选择三级分类
        self.find_element.find_element(CG.third_classification).click()
        # 点击券类
        self.find_element.find_element(CG.coupon).click()
        # 选择券类
        self.find_element.find_element(CG.coupon_classification).click()
        # 点击确认
        self.find_element.find_element(CG.determine).click()
        # 商品总价
        self.find_element.find_element(CG.total_price).send_keys(total_price)
        # 商品库存
        self.find_element.find_element(CG.stock).send_keys(stock)
        # 限购数量
        self.find_element.find_element(CG.limit_quantity).send_keys(
            limit_quantity)

    # 发布商企服务
    def Business_Services(self, product_title, product_description, total_price, subsist, stock, limit_quantity):
        # 上传图片
        self.upload_image(EG.product_image)

        # 输入商品标题
        self.find_element.find_element(BS.product_title).send_keys(product_title)
        # 输入商品详情
        self.find_element.find_element(BS.product_description).send_keys(
            product_description)
        # 选择分类
        self.find_element.find_element(BS.classification).click()
        # 选择二级分类
        self.find_element.find_element(BS.second_classification).click()
        # 选择三级分类
        self.find_element.find_element(BS.third_classification).click()
        # 商品总价
        self.find_element.find_element(BS.total_price).send_keys(total_price)
        # 预付款
        self.find_element.find_element(BS.subsist).send_keys(subsist)
        # 商品库存
        self.find_element.find_element(BS.stock).send_keys(stock)
        # 限购数量
        self.find_element.find_element(BS.limit_quantity).send_keys(
            limit_quantity)