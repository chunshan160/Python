#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 16:49
#@Author :春衫
#@File :Index.py


from selenium.webdriver.common.by import By

class Home:
    real_goods = (By.XPATH,'//span[text()="实物商品"]')
    real_goods_more = (By.XPATH,'//span[text()="实物商品"]//following-sibling::div')
    local_life = (By.XPATH, '//span[text()="本地生活"]')
    local_life_more = (By.XPATH, '//span[text()="本地生活"]//following-sibling::div')
    business_services = (By.XPATH, '//span[text()="商企服务"]')
    business_services_more = (By.XPATH, '//span[text()="商企服务"]//following-sibling::div')
