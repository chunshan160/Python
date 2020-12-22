#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/16 16:01
# @Author :春衫
# @File :RegisterSuccess.py


from selenium.webdriver.common.by import By

'''
注册账号-成功-系统提示
'''

# 注册成功
register_success_text = (By.CLASS_NAME, "success-msg")
#下载焕呗APP
download_app=(By.XPATH,'//button[text()="下载焕呗APP"]')
# 进入首页
go_to_index = (By.CLASS_NAME, "white-btn")