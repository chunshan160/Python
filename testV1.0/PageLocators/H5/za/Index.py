#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 16:49
#@Author :春衫
#@File :Index.py

from selenium.webdriver.common.by import By


# 首页询问城市定位
ask_location = (By.XPATH,
            '//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]')
# 首页-我的
my = (By.XPATH, '//i[@class="my-icon"]')

location=(By.XPATH,'//div[@class="city_box"]')
all_city=(By.XPATH,'//div[@class="allCity"]')
search=(By.XPATH,'//div[@class="search_box"]')
input=(By.XPATH,'//input[@placeholder="输入关键字"]')



entity_good_title = (By.XPATH,'//span[text()="实物商品"]')
entity_good_more = (By.XPATH,'//span[text()="实物商品"]//following-sibling::div[@class="more"]')
entity_good = (By.XPATH,'(//div[@class="product-pic"])[1]')



coupon_good = (By.XPATH, '//span[text()="本地生活"]')
coupon_good_more = (By.XPATH, '//span[text()="本地生活"]//following-sibling::div')

services_good = (By.XPATH, '//span[text()="商企服务"]')
services_good_more = (By.XPATH, '//span[text()="商企服务"]//following-sibling::div')
