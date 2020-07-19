#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/23 14:20
# @Author :春衫
# @File :publishcommodity_page.py

import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_dev1.PageLocators.H5.PublishGood import Real_Goods as RG
from web_dev1.PageLocators.H5.PublishGood import Local_Life as LL
from web_dev1.PageLocators.H5.PublishGood import Business_Services as BS
from web_dev1.PageLocators.H5.PublishGood import Pubilc


# 发布商品-商品类型
class Product:

    def __init__(self, driver):
        self.driver = driver

    # 实物类
    def Real_Goods(self, product_title, product_description, property_1, property_2, purchase_price, sell_price, stock,
                   limit_quantity):
        # 上传图片
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品标题
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_title))).send_keys(
            product_title)
        # 点击商品描述
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_detail))).click()
        # 输入商品详情
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_description))).send_keys(
            product_description)
        # 商品详情页上传商品
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_description_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 点击完成，回到商品详情页
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.finish))).click()
        # 点击品相
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality))).click()
        time.sleep(2)
        # 选择全新
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality_new))).click()
        # 选择分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.category))).click()
        # 选择二级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.second_categpry))).click()
        # 选择三级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.third_categpry))).click()
        # 点击商品类型
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_type))).click()
        time.sleep(2)
        # 选择商品类型
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_type_select))).click()
        time.sleep(2)
        # 点击规格
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.specification))).click()
        # 进入商品规格页面，输入属性
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_1))).send_keys(property_1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_2))).send_keys(property_2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.specification_image))).click()
        os.system(Pubilc.path)
        time.sleep(1)
        # 下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.next))).click()
        # 进货价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.purchase_price))).send_keys(
            purchase_price)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.sell_price))).send_keys(sell_price)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.stock))).send_keys(stock)
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.determine))).click()
        # 运费
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare))).click()
        time.sleep(2)
        # 运费类型
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare_manner))).click()
        time.sleep(1)
        # 限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.limit_quantity))).send_keys(
            limit_quantity)

    # 立即上架
    def submit(self, submit):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((submit))).click()

    # 放入仓库
    def storage(self, storage):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((storage))).click()

    # 发布本地生活
    def Local_Life(self, product_title, product_description, total_price, stock, limit_quantity):
        # 上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品标题
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LL.product_title))).send_keys(product_title)
        # 输入商品详情
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LL.product_description))).send_keys(
            product_description)
        # 选择分类
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LL.classification))).click()
        # 选择二级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.classification_Secondary))).click()
        # 选择三级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.classification_Third_grade))).click()
        # 点击券类
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LL.coupon))).click()
        # 选择券类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.coupon_classification))).click()
        # 点击确认
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.determine))).click()
        # 商品总价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.total_price))).send_keys(total_price)
        # 商品库存
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LL.stock))).send_keys(stock)
        # 限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.limit_quantity))).send_keys(
            limit_quantity)

    # 发布商企服务
    def Business_Services(self, product_title, product_description, total_price, subsist, stock, limit_quantity):
        # 上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品标题
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((BS.product_title))).send_keys(product_title)
        # 输入商品详情
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((BS.product_description))).send_keys(
            product_description)
        # 选择分类
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((BS.classification))).click()
        # 选择二级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.classification_Secondary))).click()
        # 选择三级分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.classification_Third_grade))).click()
        # 商品总价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.total_price))).send_keys(total_price)
        # 预付款
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.subsist))).send_keys(subsist)
        # 商品库存
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((BS.stock))).send_keys(stock)
        # 限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.limit_quantity))).send_keys(
            limit_quantity)