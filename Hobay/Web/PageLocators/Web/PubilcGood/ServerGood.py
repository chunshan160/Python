#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:02
#@Author :春衫
#@File :ServerGood_Page.py

from selenium.webdriver.common.by import By

'''
发布商品-商企服务
'''

# 商品主图
product_image = (By.XPATH, '//form[@class="upload-box"]')
# 商品标题
product_title = (By.XPATH, '//textarea[@placeholder="请输入标题"]')
# 商品详情
product_description = (By.XPATH, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
# 总价
total_price = (By.XPATH, '//input[@placeholder="商品总价"]')
# 预付款
subsist = (By.XPATH, '//input[@placeholder="预先支付的款项"]')
# 库存
stock = (By.XPATH, '//input[@placeholder="商品库存"]')