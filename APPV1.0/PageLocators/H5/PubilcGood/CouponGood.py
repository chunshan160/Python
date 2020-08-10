#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:01
#@Author :春衫
#@File :coupon_good.py

from appium.webdriver.common.mobileby import MobileBy

'''
发布商品-本地生活
'''

# 商品标题
product_title = (MobileBy.ID, "com.ecloud.hobay:id/et_product_title")
# 商品详情
product_description = (MobileBy.ID, "com.ecloud.hobay:id/et_product_desc")

# 点击券类
coupon = (MobileBy.ID, "com.ecloud.hobay:id/tv_select_volume")
# 卡券类型
coupon_categpry = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("代金券")')
# 价格
total_price = (MobileBy.ID, "com.ecloud.hobay:id/et_product_price")
# 库存
stock = (MobileBy.ID, "com.ecloud.hobay:id/et_product_number")
# 限购数量
limit_quantity = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")