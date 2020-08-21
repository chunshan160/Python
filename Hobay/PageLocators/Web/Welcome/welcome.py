#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 13:33
# @Author :春衫
# @File :welcome.py

from selenium.webdriver.common.by import By

#焕呗LOGO
logo=(By.ID,"com.ecloud.hobay:id/iv_logo")
#隐私政策
desc=(By.ID,"com.ecloud.hobay:id/tv_desc")
#不同意
no=(By.ID,"com.ecloud.hobay:id/tv_no")
#同意
yes=(By.ID,"com.ecloud.hobay:id/tv_yes")
#立即体验
experience_now=(By.ID,"com.ecloud.hobay:id/btn_experience_now")