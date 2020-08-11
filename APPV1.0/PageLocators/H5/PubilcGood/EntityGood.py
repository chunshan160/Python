#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 13:01
# @Author :春衫
# @File :EntityGood_Page.py

from appium.webdriver.common.mobileby import MobileBy

'''
发布商品-实物商品
'''


# 商品标题
product_title = (MobileBy.ID, "com.ecloud.hobay:id/et_product_title")
# 商品描述
product_detail = (MobileBy.ID, "com.ecloud.hobay:id/tv_product_detail")
# 商品详情内容
product_description = (MobileBy.CLASS_NAME, "android.widget.EditText")
# 上传商品详情图片按钮
description_btn = (MobileBy.ID, "com.ecloud.hobay:id/btn_add_pic")
# 完成按钮
finish = (MobileBy.ID, "com.ecloud.hobay:id/btn_complete")
# 品相
quality = (MobileBy.ID, "com.ecloud.hobay:id/tv_product_phase")
# 品相-全新
quality_new = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")')
# 商品类型
product_type = (MobileBy.ID, "com.ecloud.hobay:id/tv_product_type")
# 商品类型-易贝商品
product_type_select = (MobileBy.ID, "com.ecloud.hobay:id/tv_dialog_item")
# 规格
specification = (MobileBy.ID, "com.ecloud.hobay:id/tv_specification")
# 规格_1_2
property_1 = (MobileBy.ID, "com.ecloud.hobay:id/et_first_attributes")
property_2 = (MobileBy.ID, "com.ecloud.hobay:id/et_name")
# 上传规格图片
upload_specification_image = (MobileBy.ID, "com.ecloud.hobay:id/tv_add_pic")
# 选择规格图片
check_specification_image = (MobileBy.ID, "com.ecloud.hobay:id/iv_thumb")
# 下一步
next = (MobileBy.ID, "com.ecloud.hobay:id/btn_next")
# 进货价
purchase_price = (MobileBy.ID, "com.ecloud.hobay:id/et_purchase_price")
# 销售价
sell_price = (MobileBy.ID, "com.ecloud.hobay:id/et_price")
# 库存
stock = (MobileBy.ID, "com.ecloud.hobay:id/et_number")
# 确定按钮
determine = (MobileBy.ID, "com.ecloud.hobay:id/btn_confirm")
# 运费
fare = (MobileBy.ID, "com.ecloud.hobay:id/tv_freight")
# 运费-包邮
fare_manner = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")')
# 限购数量
limit_quantity = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")
# 品牌
brand = (MobileBy.ID, "com.ecloud.hobay:id/et_brand")
# 生产日期
production_Date = (MobileBy.ID, "com.ecloud.hobay:id/tv_data")
# 生产日期-完成
production_Date_ok = (MobileBy.ID, "com.ecloud.hobay:id/btn_complete_address")
# 保质期
shelf_life = (MobileBy.ID, "com.ecloud.hobay:id/et_shelf_life")
# 产地
address = (MobileBy.ID, "com.ecloud.hobay:id/et_address")
# 制造商
manufacturer = (MobileBy.ID, "com.ecloud.hobay:id/et_manufacturer")
# 生产许可证编号
production_number = (MobileBy.ID, "com.ecloud.hobay:id/et_production_number")

