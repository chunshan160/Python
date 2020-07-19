#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/31 17:14
# @Author :春衫
# @File :Login.py

from selenium.webdriver.common.by import By


class LoginPage:
    # 输入手机号
    # name = (By.XPATH, '//input[@placeholder="请输入账号"]//parent::div')
    name = (By.XPATH, '//input[@placeholder="请输入账号"]')
    # 密码
    pwd = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录
    login_but = (By.XPATH, '//button[@class="el-button el-button--primary"]')
