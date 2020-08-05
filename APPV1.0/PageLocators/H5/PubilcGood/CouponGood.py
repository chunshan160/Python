#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:01
#@Author :春衫
#@File :coupon_good.py

from appium.webdriver.common.mobileby import MobileBy

'''
发布商品-本地生活
'''

# 商品主图
product_image = (MobileBy.ID, "com.ecloud.hobay:id/iv_add_pic")
# 选择图片
check_image = (MobileBy.ID, "com.ecloud.hobay:id/cb_check")
# 点击确定
btn_ok = (MobileBy.ID, "com.ecloud.hobay:id/btn_ok")
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
# 点击券类
coupon = (MobileBy.ID, "com.ecloud.hobay:id/tv_select_volume")
# 卡券类型
coupon_categpry = (MobileBy.CLASS_NAME, "android.widget.TextView")
# 价格
total_price = (MobileBy.ID, "com.ecloud.hobay:id/et_product_price")
# 库存
stock = (MobileBy.ID, "com.ecloud.hobay:id/et_product_number")
# 限购数量
limit_quantity = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")