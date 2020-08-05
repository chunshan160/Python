#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:00
#@Author :春衫
#@File :PubilcGood.py

from appium.webdriver.common.mobileby import MobileBy

'''
发布商品
'''

# 点击发布实物商品
entity_good = (MobileBy.ID, "com.ecloud.hobay:id/iv_publish_product")
# 点击发布本地生活
coupon_good = (MobileBy.ID, "com.ecloud.hobay:id/iv_publish_card")
# 点击发布商企服务
services_good = (MobileBy.ID, "com.ecloud.hobay:id/iv_publish_service")