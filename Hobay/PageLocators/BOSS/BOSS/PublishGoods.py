#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/31 15:03
# @Author :春衫
# @File :PublishGood.py

from selenium.webdriver.common.by import By


# 公共
class Pubilc:
    # 发布商品
    publish_goods = (By.XPATH, '//span[contains(text(),"发布商品")]')
    # # 第一分类
    # first_category = (By.XPATH, '//li[contains(text(),"实物商品")]')
    # # 第二分类
    # second_categpry = (By.XPATH, '//li[text()="大家电2"]')
    # # 第三分类
    # third_categpry = (By.XPATH, '//li[text()="电视"]')
    # 下一步
    next = (By.XPATH, '//span[text()="下一步，填写商品信息"]//parent::button')
    # 上传图片的脚本
    path = ('D:\Pycharm_workspace\web_test\image.exe')
    # 立即上架
    submit = (By.XPATH, '//span[contains(text(),"立即发布")]//parent::button')
    # 放入仓库
    storage = (By.XPATH, '//span[contains(text(),"放入仓库")]//parent::button')
    #成功提示信息
    success_msg = (By.XPATH, '//p[@class="el-message__content"]')


# 实物商品
class Real_Goods:
    # 第一分类
    first_category = (By.XPATH, '//li[contains(text(),"实物商品")]')
    # 第二分类
    second_categpry = (By.XPATH, '//li[text()="大家电2"]')
    # 第三分类
    third_categpry = (By.XPATH, '//li[text()="电视"]')
    # 商品名称
    product_title = (By.XPATH, '//*[contains(text(),"商品名称")]//following-sibling::div//div//input')
    # 品相
    quality = (By.XPATH, '//*[contains(text(),"品相")]//following-sibling::div//div[@class="el-select"]')
    # 品相- 全新
    quality_new = (By.XPATH, '//span[contains(text(),"全新")]//parent::li')
    #点击是否进入焕焕商超
    supermarket = (By.XPATH,'//label[contains(text(),"是否进入焕焕商超")]//following-sibling::div/div')
    #是
    supermarket_yes = (By.XPATH,'//span[text()="是"]//parent::li')
    #商超列表
    supermarket_list = (By.XPATH,'//div[@class="el-col el-col-12"]/div[@class="el-select"]')
    #开放全不商超
    supermarket_name = (By.XPATH,'//span[text()="开放全不商超"]//parent::li')
    # 限购数量
    limit_quantity = (By.XPATH, '//p[contains(text(),"限制每人购买数量")]//preceding-sibling::div//input')
    # 点击运费
    fare = (By.XPATH, '//label[contains(text(),"运费")]//parent::div//div//div[@class="el-select"]')
    # 点击运费-包邮
    fare_manner = (By.XPATH, '//span[contains(text(),"包邮")]//parent::li')
    # 上传主图
    product_image = (By.XPATH, '//label[contains(text(),"图片")]//following-sibling::div/div[@class="avatar-uploader"]')
    # 商品描述图片
    product_detail = (
        By.XPATH, '//label[contains(text(),"商品描述")]//following-sibling::div/div[@class="avatar-uploader"]')
    # 商品详情内容
    product_description = (By.XPATH, '//textarea')
    # 下一步
    next = (By.XPATH, '//span[contains(text(),"下一步")]')
    # 规格_1_2
    property_1 = (By.XPATH, '//input[@placeholder="输入属性名，如颜色"]')
    property_2 = (By.XPATH, '//input[@placeholder="输入属性值，如红色"]')
    # 规格图片
    specification_image = (By.XPATH, '//div[@class="img"]')
    # 进货价
    purchase_price = (By.XPATH, '//input[@placeholder="请输入进货价格"]')
    # 销售价
    sell_price = (By.XPATH, '//input[@placeholder="请输入销售价格"]')
    # 库存
    stock = (By.XPATH, '//input[@placeholder="请输入商品库存"]')


# 本地生活
class Local_Life:
    # 第一分类
    first_category = (By.XPATH, '//li[contains(text(),"本地生活")]')
    # 第二分类
    second_categpry = (By.XPATH, '//li[text()="酒水"]')
    # 第三分类
    third_categpry = (By.XPATH, '//li[text()="红酒"]')
    # 商品名称
    product_title = (By.XPATH, '//*[contains(text(),"商品名称")]//following-sibling::div//div//input')
    # 点击卡券种类
    coupon = (By.XPATH, '//input[@placeholder="请选择"]')
    # 卡券类型-代金券
    coupon_classification = (By.XPATH, '//span[contains(text(),"代金券")]//parent::li')
    # 价格
    total_price = (By.XPATH, '//label[contains(text(),"价格")]/following-sibling::div/div/input')
    # 库存
    stock = (By.XPATH, '//label[contains(text(),"库存")]/following-sibling::div/div/input')
    # 限购数量
    limit_quantity = (By.XPATH, '//p[contains(text(),"限制")]//preceding-sibling::div//input')
    # 上传主图
    product_image = (By.XPATH, '//label[contains(text(),"图片")]//following-sibling::div/div[@class="avatar-uploader"]')
    # 商品描述图片
    product_detail = (
        By.XPATH, '//label[contains(text(),"商品描述")]/parent::div/div/div[@class="avatar-uploader"]')
    # 商品详情内容
    product_description = (By.XPATH, '//textarea')


# 商企服务
class Business_Services:
    # 第一分类
    first_category = (By.XPATH, '//li[contains(text(),"商企服务")]')
    # 第二分类
    second_categpry = (By.XPATH, '//li[text()="设计"]')
    # 第三分类
    third_categpry = (By.XPATH, '//li[text()="广告设计"]')
    # 商品名称
    product_title = (By.XPATH, '//*[contains(text(),"商品名称")]//following-sibling::div//div//input')
    # 总价
    total_price = (By.XPATH, '//label[contains(text(),"商品总价")]/following-sibling::div/div/input')
    # 预付款
    subsist = (By.XPATH, '//label[contains(text(),"预付款")]/following-sibling::div/div/input')
    # 库存
    stock = (By.XPATH, '//label[contains(text(),"库存")]/following-sibling::div/div/input')
    # 限购数量
    limit_quantity = (By.XPATH, '//p[contains(text(),"限制")]//preceding-sibling::div//input')
    # 上传主图
    product_image = (By.XPATH, '//label[contains(text(),"图片")]//following-sibling::div/div[@class="avatar-uploader"]')
    # 商品描述图片
    product_detail = (
        By.XPATH, '//label[contains(text(),"商品描述")]/parent::div/div/div[@class="avatar-uploader"]')
    # 商品详情内容
    product_description = (By.XPATH, '//textarea')
