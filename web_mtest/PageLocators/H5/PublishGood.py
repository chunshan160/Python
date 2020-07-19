#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/28 13:48
# @Author :春衫
# @File :PublishGoodspage_Locators.py

from selenium.webdriver.common.by import By


# 公共
class Pubilc:
    # 城市定位
    location = (By.XPATH,
                '//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]')
    # 首页点击发布商品
    publish_goods = (By.XPATH, '//i[@class="cart-icon"]')
    # 点击发布实物商品
    real_goods = (By.XPATH, '//span[@class="btn material-btn"]')
    # 点击发布本地生活
    local_life = (By.XPATH, '//span[@class="btn business-btn"]')
    # 点击发布商企服务
    business_services = (By.XPATH, '//span[@class="btn service-btn"]')
    # 上传图片的脚本
    path = ('D:\Pycharm_workspace\web_mtest\image.exe')
    # 立即上架
    submit = (By.XPATH, '//div[@class="submit-sell"]')
    # 放入仓库
    storage = (By.XPATH, '//div[@class="submit-storage"]')


# 实物类
class Real_Goods:
    # 商品主图
    product_image = (By.XPATH, '//form[@class="upload-box"]')
    # 商品标题
    product_title = (By.XPATH, '//textarea[@placeholder="输入商品标题"]')
    # 商品描述
    product_detail = (By.XPATH, '//label[text()="商品描述"]//parent::div')
    # 商品详情内容
    product_description = (By.XPATH, '//textarea')
    # 商品详情图片
    product_description_image = (By.CLASS_NAME, 'upload-btn')
    # 完成按钮
    finish = (By.CLASS_NAME, 'fin-btn')
    # 品相
    quality = (By.XPATH, '//label[text()="品相"]//parent::div')
    # 品相-全新
    quality_new = (By.XPATH, '//*[contains(text(),"全新")]//span')
    # 分类
    category = (By.XPATH, '//label[text()="分类"]//parent::div')
    # 二级分类
    second_categpry = (By.XPATH, '//div[text()="大家电2"]')
    # 三级分类
    third_categpry = (By.XPATH, '//li[text()="电视"]')
    # 商品类型
    product_type = (By.XPATH, '//label[text()="商品类型"]//parent::div')
    # 商品类型-易贝商品
    product_type_select = (By.XPATH, '//*[contains(text(),"易贝商品")]//span')
    # 规格
    specification = (By.XPATH, '//*[contains(text(),"规格")]//parent::div')
    # 规格_1_2
    property_1 = (By.ID, 'id_0')
    property_2 = (By.ID, 'id_0_0')
    # 规格图片
    specification_image = (By.XPATH, '//*[contains(text(),"上传图片")]')
    # 下一步
    next = (By.XPATH, '//*[contains(text(),"下一步")]')
    # 进货价
    purchase_price = (By.ID, 'skuTb_id_0')
    # 销售价
    sell_price = (By.ID, 'skuTb_id_1')
    # 库存
    stock = (By.ID, 'skuTb_id_2')
    # 确定按钮
    determine = (By.XPATH, '//div[@class="fin-btn"]//div[contains(text(),"确定")]')
    # 运费
    fare = (By.XPATH, '//label[text()="运费"]//parent::div')
    # 运费-包邮
    fare_manner = (By.XPATH, '//*[contains(text(),"包邮")]//span')
    # 限购数量
    limit_quantity = (By.XPATH, '//input[@placeholder="默认不限"]')


class Local_Life:
    # 商品主图
    product_image = (By.XPATH, '//form[@class="upload-box"]')
    # 商品标题
    product_title = (By.XPATH, '//textarea[@placeholder="请输入标题"]')
    # 商品详情
    product_description = (By.XPATH, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
    # 分类
    classification = (By.XPATH, '//label[text()="分类"]//parent::div')
    # 二级分类
    classification_Secondary = (By.XPATH, '//div[text()="酒水"]')
    # 三级分类
    classification_Third_grade = (By.XPATH, '//li[text()="红酒"]')
    # 点击券类
    coupon = (By.XPATH, '//label[text()="券类"]//parent::div')
    # 卡券类型
    coupon_classification = (By.XPATH, '//li[text()="代金券"]')
    # 确认按钮
    determine = (By.XPATH, '//div[contains(text(),"确认")]')
    # 总价
    total_price = (By.XPATH, '//input[@placeholder="商品总价"]')
    # 库存
    stock = (By.XPATH, '//input[@placeholder="商品库存"]')
    # 限购数量
    limit_quantity = (By.XPATH, '//input[@placeholder="默认不限"]')


class Business_Services:
    # 商品主图
    product_image = (By.XPATH, '//form[@class="upload-box"]')
    # 商品标题
    product_title = (By.XPATH, '//textarea[@placeholder="请输入标题"]')
    # 商品详情
    product_description = (By.XPATH, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
    # 分类
    classification = (By.XPATH, '//label[text()="分类"]//parent::div')
    # 二级分类
    classification_Secondary = (By.XPATH, '//div[text()="设计"]')
    # 三级分类
    classification_Third_grade = (By.XPATH, '//li[text()="广告设计"]')
    # 总价
    total_price = (By.XPATH, '//input[@placeholder="商品总价"]')
    # 预付款
    subsist = (By.XPATH, '//input[@placeholder="预先支付的款项"]')
    # 库存
    stock = (By.XPATH, '//input[@placeholder="商品库存"]')
    # 限购数量
    limit_quantity = (By.XPATH, '//input[@placeholder="默认不限"]')
