#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:39
# @Author :春衫
# @File :Common.py

from appium.webdriver.common.mobileby import MobileBy

'''
公共定位
'''

# 立即上架
submit = (MobileBy.ID, "com.ecloud.hobay:id/btn_immediately_publish")
# 放入仓库
storage = (MobileBy.ID, "com.ecloud.hobay:id/btn_into_warehouse")
# 错误提示
error_toast = (MobileBy.XPATH, '//*[contains(text(),"请输入商品标题")]')
