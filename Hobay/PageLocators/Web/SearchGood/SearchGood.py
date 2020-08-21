#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 15:52
#@Author :春衫
#@File :SearchGood_Business.py

from selenium.webdriver.common.by import By

#搜索框-输入
send_search=(By.ID,"com.ecloud.hobay:id/et_search")
#商品tap
good_tap=(By.ACCESSIBILITY_ID,"商品")
#店铺tap
shop_tap=(By.ACCESSIBILITY_ID,"店铺")
#综合
Comprehensive=(By.ID,"com.ecloud.hobay:id/tv_sort_complex")
#全新
new=(By.ID,"com.ecloud.hobay:id/tv_sort_new")
#人气
hot=(By.ID,"com.ecloud.hobay:id/tv_sort_hot")
#价格
price=(By.ID,"com.ecloud.hobay:id/tv_sort_price")
#筛选
filter=(By.ID,"com.ecloud.hobay:id/fl_sort_filter")
#商品
good=(By.ID,"com.ecloud.hobay:id/fl_root")
#进店
go_shop=(By.ID,"com.ecloud.hobay:id/tv_go1")
#搜索-店铺-商品
shop_good=(By.ID,"com.ecloud.hobay:id/iv_p1")