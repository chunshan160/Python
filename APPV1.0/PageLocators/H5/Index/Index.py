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


# # 首页
# my = (MobileBy.ID, "//i[@class="my-icon"]")
#
# all_city=(MobileBy.ID,"//div[@class="allCity"]")
#
# input=(MobileBy.ID,"//input[@placeholder="输入关键字"]")
#
#
#
# entity_good_title = (MobileBy.ID,"//span[text()="实物商品"]")
# entity_good_more = (MobileBy.ID,"//span[text()="实物商品"]//following-sibling::div[@class="more"]")
# entity_good = (MobileBy.ID,"(//div[@class="product-pic"])[1]")
#
#
#
# coupon_good = (MobileBy.ID, "//span[text()="本地生活"]")
# coupon_good_more = (MobileBy.ID, "//span[text()="本地生活"]//following-sibling::div")
#
# services_good = (MobileBy.ID, "//span[text()="商企服务"]")
# services_good_more = (MobileBy.ID, "//span[text()="商企服务"]//following-sibling::div")
