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
product_image = (By.CLASS_NAME, "upload-box")
# 商品标题
product_title = (By.XPATH, '//textarea[@placeholder="输入商品标题"]')
# 商品描述
product_detail = (By.XPATH, '//label[text()="商品描述"]/parent::div')
# 商品详情内容
product_description = (By.XPATH, '//textarea')
# 商品详情图片
product_description_image = (By.CLASS_NAME, 'upload-btn')
# 完成按钮
finish = (By.CLASS_NAME, 'fin-btn')
# 品相
quality = (By.XPATH, '//label[text()="品相"]/parent::div')
# 品相-全新
quality_new = (By.XPATH, '//*[contains(text(),"{}")]/span')
# 商品类型
product_type = (By.XPATH, '//label[text()="商品类型"]/parent::div')
# 商品类型-易贝商品
product_type_select = (By.XPATH, '//*[contains(text(),"{}")]/span')
# 规格
specification = (By.XPATH, '//*[contains(text(),"规格")]/parent::div')
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
determine = (By.XPATH, '//div[@class="fin-btn"]/div[contains(text(),"确定")]')
# 运费
fare = (By.XPATH, '//label[text()="运费"]/parent::div')
# 运费-包邮
fare_manner = (By.XPATH, '//*[contains(text(),"{}")]/span')
# 品牌
brand = (By.XPATH, '//label[text()="品牌"]/following-sibling::div/input')
# 生产日期
production_Date = (By.XPATH, '//label[contains(text(),"生产日期")]/following-sibling::div')
# 生产日期-完成
production_Date_ok = (By.CLASS_NAME, "sure")
# 保质期
shelf_life = (By.XPATH, '//input[@placeholder="输入天数，选填"]')
# 产地
address = (By.XPATH, '//input[@placeholder="如，中国大陆，选填"]')
# 制造商
manufacturer = (By.XPATH, '//input[@placeholder="公司名称，选填"]')
# 生产许可证编号
production_number = (By.XPATH, '//label[contains(text(),"生产许可证编号")]/following-sibling::div')
#错误提示
error_toast=(By.XPATH,'//div[@class="van-toast van-toast--text van-toast--middle"]/div')