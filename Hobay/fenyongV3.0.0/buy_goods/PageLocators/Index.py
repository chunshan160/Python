#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 16:49
#@Author :春衫
#@File :Index.py


from selenium.webdriver.common.by import By

class Home:

    location=(By.XPATH,'//div[@class="city_box"]')
    all_city=(By.XPATH,'//div[@class="allCity"]')
    search=(By.XPATH,'//div[@class="search_box"]')
    input=(By.XPATH,'//input[@placeholder="输入关键字"]')

    real_goods_title = (By.XPATH,'//span[text()="实物商品"]')
    real_goods_more = (By.XPATH,'//span[text()="实物商品"]//following-sibling::div[@class="more"]')
    real_goods = (By.XPATH,'(//div[@class="product-pic"])[1]')



    local_life = (By.XPATH, '//span[text()="本地生活"]')
    local_life_more = (By.XPATH, '//span[text()="本地生活"]//following-sibling::div')

    business_services = (By.XPATH, '//span[text()="商企服务"]')
    business_services_more = (By.XPATH, '//span[text()="商企服务"]//following-sibling::div')
