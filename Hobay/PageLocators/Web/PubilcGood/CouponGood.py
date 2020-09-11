#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:01
#@Author :春衫
#@File :coupon_good.py

from selenium.webdriver.common.by import By

'''
发布商品-本地生活
'''

# 商品主图
product_image = (By.XPATH, '//form[@class="upload-box"]')
# 商品标题
product_title = (By.XPATH, '//textarea[@placeholder="请输入标题"]')
# 商品详情
product_description = (By.XPATH, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
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