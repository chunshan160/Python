#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/8 16:49
# @Author :春衫
# @File :Index_Business.py

from selenium.webdriver.common.by import By

# 城市定位
location=(By.CLASS_NAME,"city_box")
# 搜索框
search = (By.CLASS_NAME, "search_box")
# 易购车
shopping_car = (By.CLASS_NAME, "icon_box")
# 首页询问城市定位弹窗
ask_location = (By.XPATH,'//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]')

#全国
all_city=(By.CLASS_NAME,"allCity")

#弹窗
location_pop_ups=(By.ID,"com.ecloud.hobay:id/tv_title")
#确定
yes=(By.ID,"com.ecloud.hobay:id/btn_right")
#取消
no=(By.ID,"com.ecloud.hobay:id/btn_left")


input=(By.XPATH,'//input[@placeholder="输入关键字"]')



entity_good_title = (By.XPATH,'//span[text()="实物商品"]')
entity_good_more = (By.XPATH,'//span[text()="实物商品"]//following-sibling::div[@class="more"]')
entity_good = (By.XPATH,'(//div[@class="product-pic"])[1]')



coupon_good = (By.XPATH, '//span[text()="本地生活"]')
coupon_good_more = (By.XPATH, '//span[text()="本地生活"]//following-sibling::div')

services_good = (By.XPATH, '//span[text()="商企服务"]')
services_good_more = (By.XPATH, '//span[text()="商企服务"]//following-sibling::div')