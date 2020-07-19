#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 16:49
#@Author :春衫
#@File :Index.py


from selenium.webdriver.common.by import By

class Home:
    real_goods_title = (By.XPATH,'//span[text()="实物商品"]')
    real_goods_more = (By.XPATH,'//span[text()="实物商品"]//following-sibling::div[@class="more"]')
    real_goods = (By.XPATH,'//div[contains(text(),"00连衣裙易贝商品")]//parent::div')

    local_life_title = (By.XPATH, '//span[text()="本地生活"]')
    local_life_more = (By.XPATH, '//span[text()="本地生活"]//following-sibling::div')
    local_life_goods = (By.XPATH,'//div[contains(text(),"55测试易贝代金券")]//parent::div')

    business_services_title = (By.XPATH, '//span[text()="商企服务"]')
    business_services_more = (By.XPATH, '//span[text()="商企服务"]//following-sibling::div')
    business_services_goods = (By.XPATH, '//div[contains(text(),"00测试商企易贝")]//parent::div')

    cash_goods_title = (By.XPATH, '//span[text()="现金区"]')
    cash_goods_more = (By.XPATH, '//span[text()="现金区"]//following-sibling::span')
    cash_goods_goods = (By.XPATH, '//div[contains(text(),"本地生活：出售中：审核通过，待复审")]//parent::div')