#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index_Business.py

from appium.webdriver.common.mobileby import MobileBy

# 首页定位
location = (MobileBy.ID, "com.ecloud.hobay:id/tv_city")
# 搜索框
search = (MobileBy.ID, "com.ecloud.hobay:id/tv_search")
# 易购车
shopping_car = (MobileBy.ID, "com.ecloud.hobay:id/ib_shopping")
# 扫一扫
scan_code = (MobileBy.ID, "com.ecloud.hobay:id/ib_qr")
# 首页询问城市定位
# ask_location = (MobileBy.ID,"//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]")

#全国
all_city=(MobileBy.ID,"com.ecloud.hobay:id/tv_national")

#弹窗
location_pop_ups=(MobileBy.ID,"com.ecloud.hobay:id/tv_title")
#确定
yes=(MobileBy.ID,"com.ecloud.hobay:id/btn_right")
#取消
no=(MobileBy.ID,"com.ecloud.hobay:id/btn_left")