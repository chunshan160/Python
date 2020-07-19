#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/31 14:38
# @Author :春衫
# @File :BOSS.py

import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_test.PageLocators.BOSS.PublishGoods import Real_Goods as RG
# from web_test.PageLocators.BOSS.PublishGood import Local_Life as LL
# from web_test.PageLocators.BOSS.PublishGood import Business_Services as BS
from web_test.PageLocators.BOSS.PublishGoods import Pubilc
from web_test.PageLocators.BOSS.PublishGoods import Local_Life as LL
from web_test.PageLocators.BOSS.PublishGoods import Business_Services as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# 发布商品-商品类型
class Product:

    def __init__(self, driver):
        self.driver = driver

    # 实物类
    def Real_Goods(self, product_title,
                   limit_quantity, product_description, property_1, property_2, purchase_price, sell_price,
                   stock):
        # 点击实物商品
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.first_category))).click()
        # 点击实物商品-大家电2
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.second_categpry))).click()
        # 点击实物商品-大家电2-电视
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.third_categpry))).click()
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Pubilc.next))).click()
        # 输入商品名称
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_title))).send_keys(
            product_title)
        # 点击品相
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality))).click()
        # 选择全新
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality_new))).click()
        # 输入限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.limit_quantity))).send_keys(
            limit_quantity)
        # 点击运费
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare))).click()
        # 选择包邮
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare_manner))).click()
        # 点击上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 点击上传商品描述图片
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_detail))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品描述
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_description))).send_keys(
            product_description)
        # 滚动至元素【下一步】可见
        target = self.driver.find_element(*RG.next)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.next))).click()
        # 输入规格1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_1))).send_keys(property_1)
        # 输入规格2
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_2))).send_keys(property_2)
        # 点击上传规格图片
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.specification_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入进货价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.purchase_price))).send_keys(
            purchase_price)
        # 输入销售价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.sell_price))).send_keys(sell_price)
        # 输入库存
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.stock))).send_keys(stock)

    # 实物类 商超
    def Real_Goods_SC(self, product_title,
                      limit_quantity, product_description, property_1, property_2, purchase_price, sell_price,
                      stock):
        # 点击实物商品
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.first_category))).click()
        # 点击实物商品-大家电2
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.second_categpry))).click()
        # 点击实物商品-大家电2-电视
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.third_categpry))).click()
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Pubilc.next))).click()
        # 输入商品名称
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_title))).send_keys(
            product_title)
        # 点击品相
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality))).click()
        # 选择全新
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.quality_new))).click()
        # 点击是否加入商超
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.supermarket))).click()
        # 选择是
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.supermarket_yes))).click()
        # 点击商超列表
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.supermarket_list))).click()
        time.sleep(1)
        # 点击选择商超
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.supermarket_name))).click()
        # 输入限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.limit_quantity))).send_keys(
            limit_quantity)
        # 点击运费
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare))).click()
        # 选择包邮
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.fare_manner))).click()
        # 点击上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 点击上传商品描述图片
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_detail))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品描述
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.product_description))).send_keys(
            product_description)
        # 滚动至元素【下一步】可见
        target = self.driver.find_element(*RG.next)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.next))).click()
        # 输入规格1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_1))).send_keys(property_1)
        # 输入规格2
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.property_2))).send_keys(property_2)
        # 点击上传规格图片
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.specification_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入进货价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.purchase_price))).send_keys(
            purchase_price)
        # 输入销售价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.sell_price))).send_keys(sell_price)
        # 输入库存
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RG.stock))).send_keys(stock)

    # 本地生活
    def Local_Life(self, product_title, total_price, stock, limit_quantity, product_description):
        # 点击本地生活
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.first_category))).click()
        # 点击本地生活-酒水
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.second_categpry))).click()
        # 点击本地生活-酒水-红酒
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.third_categpry))).click()
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Pubilc.next))).click()
        # 输入商品名称
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.product_title))).send_keys(
            product_title)
        # 点击卡券种类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.coupon))).click()
        # 选择代金券
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.coupon_classification))).click()
        # 输入价格
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.total_price))).send_keys(
            total_price)
        # 输入库存
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.stock))).send_keys(
            stock)
        # 输入限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.limit_quantity))).send_keys(
            limit_quantity)
        # 上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 上传详情图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.product_detail))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品详情
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LL.product_description))).send_keys(
            product_description)

    # 商企服务
    def Business_Services(self, product_title, total_price, subsist, stock, limit_quantity, product_description):
        # 点击商企服务
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.first_category))).click()
        # 点击商企服务-设计
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.second_categpry))).click()
        # 点击商企服务-设计-广告设计
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.third_categpry))).click()
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Pubilc.next))).click()
        # 输入商品名称
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.product_title))).send_keys(
            product_title)
        # 输入商品总价
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.total_price))).send_keys(
            total_price)
        # 输入预付款
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.subsist))).send_keys(
            subsist)
        # 输入库存
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.stock))).send_keys(
            stock)
        # 输入限购数量
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.limit_quantity))).send_keys(
            limit_quantity)
        # 上传主图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.product_image))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 上传详情图
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.product_detail))).click()
        os.system(Pubilc.path)
        time.sleep(2)
        # 输入商品详情
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BS.product_description))).send_keys(
            product_description)

    # 立即上架
    def submit(self, submit):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((submit))).click()

    # 放入仓库
    def storage(self, storage):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((storage))).click()
