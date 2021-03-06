#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:39
# @Author :春衫
# @File :PubilcGoodCommon.py

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

'''
公共定位
'''

# 商品主图
product_image = (MobileBy.ID, "com.ecloud.hobay:id/iv_add_pic")
# 选择图片
check_image = (MobileBy.ID, "com.ecloud.hobay:id/cb_check")
# 点击确定
btn_ok = (MobileBy.ID, "com.ecloud.hobay:id/btn_ok")
# 立即上架
submit = (MobileBy.ID, "com.ecloud.hobay:id/btn_immediately_publish")

# 分类
category = (MobileBy.ID, "com.ecloud.hobay:id/tv_select_type")
# 二级分类
second_category = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")')
# 三级分类
third_category = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")')

# 限购选项
Purchase_limit = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")
# 控制按钮-不限购
Purchase_limit_no = (MobileBy.ID, "com.ecloud.hobay:id/cb_no")
# 控制按钮-限购
Purchase_limit_yes = (MobileBy.ID, "com.ecloud.hobay:id/cb_yes")
# 控制按钮-不限天数
Purchase_limit_no_day = (MobileBy.ID, "com.ecloud.hobay:id/cb_no_day")
# 控制按钮-限天数
Purchase_limit_yes_day = (MobileBy.ID, "com.ecloud.hobay:id/cb_yes_day")

# 限购件数
limit_quantity = (MobileBy.ID, "com.ecloud.hobay:id/et_buy_num")
# 限购周期
limit_time = (MobileBy.ID, "com.ecloud.hobay:id/et_day_num")

# 放入仓库
storage = (MobileBy.ID, "com.ecloud.hobay:id/btn_into_warehouse")
# 错误提示
error_toast = (MobileBy.XPATH, '//*[contains(text(),"请输入商品标题")]')
