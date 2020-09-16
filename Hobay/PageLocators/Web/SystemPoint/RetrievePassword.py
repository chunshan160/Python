#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/16 16:04
# @Author :春衫
# @File :RetrievePassword.py

from selenium.webdriver.common.by import By

'''
找回密码-成功-系统提示
'''

# 找回成功
title = (By.CLASS_NAME, "waiting-title")
# 立即登录
login_now = (By.CLASS_NAME, "fni-link")
