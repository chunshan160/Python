#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 16:17
#@Author :春衫
#@File :GoodDetail_Business.py

from appium.webdriver.common.mobileby import MobileBy

#顶部商品
top_good=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("商品")')
#顶部详情
top_detail=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("详情")')
#顶部评价
top_evaluation=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("评价")')
#店铺
shop=(MobileBy.ID,"com.ecloud.hobay:id/tv_shop")
#收藏
collection=(MobileBy.ID,"com.ecloud.hobay:id/tv_collection")
#聊天
chat=(MobileBy.ID,"com.ecloud.hobay:id/tv_chat")
#加入购物车
add_car=(MobileBy.ID,"com.ecloud.hobay:id/tv_add")
#立即购买
buy_now=(MobileBy.ID,"com.ecloud.hobay:id/tv_buy_now")
#-
less=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("—")')
#购买数量
add_amount=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("0")')
#+
add=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("＋")')
#确定
confirm=(MobileBy.ID,"com.ecloud.hobay:id/btn_confirm")