#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:01
#@Author :春衫
#@File :EntityGood_Page.py

from selenium.webdriver.common.by import By

'''
发布商品-实物商品
'''

# 商品主图
product_image = (By.XPATH, '//input[@class="uploadFile"]//..')

upload_image=(By.XPATH,'//input[@class="uploadFile"]')
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
# 立即上架
submit = (By.XPATH, '//div[@class="submit-sell"]')
# 放入仓库
storage = (By.XPATH, '//div[@class="submit-storage"]')
#错误提示
error_toast=(By.XPATH,'//div[@class="van-toast van-toast--text van-toast--middle"]//div')