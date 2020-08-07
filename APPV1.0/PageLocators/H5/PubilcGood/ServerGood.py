#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:02
# @Author :春衫
# @File :ServerGood_Page.py

from appium.webdriver.common.mobileby import MobileBy

"""
发布商品-商企服务
"""


# 商品标题
product_title = (MobileBy.ID, "com.ecloud.hobay:id/et_product_title")
# 商品详情
product_description = (MobileBy.ID, "com.ecloud.hobay:id/et_product_desc")
# 分类
category = (MobileBy.ID, "com.ecloud.hobay:id/tv_select_type")
# 二级分类
second_categpry = (MobileBy.ID, "com.ecloud.hobay:id/tv_list_name")
# 三级分类
third_categpry = (MobileBy.ID, "com.ecloud.hobay:id/tv_show_name")
# 总价
total_price = (MobileBy.ID, "com.ecloud.hobay:id/et_product_all_price")
# 预付款
subsist = (MobileBy.ID, "com.ecloud.hobay:id/et_product_price")
# 库存
stock = (MobileBy.ID, "com.ecloud.hobay:id/et_product_number")
# 限购数量
limit_quantity = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")

