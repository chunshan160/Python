#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 15:52
#@Author :春衫
#@File :SearchGood_Business.py

from appium.webdriver.common.mobileby import MobileBy

#搜索框-输入
send_search=(MobileBy.ID,"com.ecloud.hobay:id/et_search")
#商品tap
good_tap=(MobileBy.ACCESSIBILITY_ID,"商品")
#店铺tap
shop_tap=(MobileBy.ACCESSIBILITY_ID,"商品")
#综合
Comprehensive=(MobileBy.ID,"com.ecloud.hobay:id/tv_sort_complex")
#全新
new=(MobileBy.ID,"com.ecloud.hobay:id/tv_sort_new")
#人气
hot=(MobileBy.ID,"com.ecloud.hobay:id/tv_sort_hot")
#价格
price=(MobileBy.ID,"com.ecloud.hobay:id/tv_sort_price")
#筛选
filter=(MobileBy.ID,"com.ecloud.hobay:id/fl_sort_filter")
#商品
good=(MobileBy.ID,"com.ecloud.hobay:id/fl_root")
#进店
go_shop=(MobileBy.ID,"com.ecloud.hobay:id/tv_go1")
#搜索-店铺-商品
shop_good=(MobileBy.ID,"com.ecloud.hobay:id/iv_p1")