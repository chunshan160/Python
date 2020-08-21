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
# 分类
classification = (By.XPATH, '//label[text()="分类"]//parent::div')
# 二级分类
second_classification = (By.XPATH, '//div[text()="酒水"]')
# 三级分类
third_classification = (By.XPATH, '//li[text()="红酒"]')
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
# 上传图片的脚本
path = ('D:\Pycharm_workspace\web_test\image.exe')
# 立即上架
submit = (By.XPATH, '//div[@class="submit-sell"]')
# 放入仓库
storage = (By.XPATH, '//div[@class="submit-storage"]')