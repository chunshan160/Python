#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 13:33
# @Author :春衫
# @File :welcome.py

from appium.webdriver.common.mobileby import MobileBy

#焕呗LOGO
logo=(MobileBy.ID,"com.ecloud.hobay:id/iv_logo")
#隐私政策
desc=(MobileBy.ID,"com.ecloud.hobay:id/tv_desc")
#不同意
no=(MobileBy.ID,"com.ecloud.hobay:id/tv_no")
#同意
yes=(MobileBy.ID,"com.ecloud.hobay:id/tv_yes")
#立即体验
experience_now=(MobileBy.ID,"com.ecloud.hobay:id/btn_experience_now")