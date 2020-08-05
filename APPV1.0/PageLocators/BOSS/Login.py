#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/31 17:14
# @Author :春衫
# @File :Login_Business.py




class LoginPage:
    # 输入手机号
    # name = (MobileBy.ID, '//input[@placeholder="请输入账号"]//parent::div')
    name = (MobileBy.ID, '//input[@placeholder="请输入账号"]')
    # 密码
    pwd = (MobileBy.ID, '//input[@placeholder="请输入密码"]')
    # 登录
    login_but = (MobileBy.ID, '//button[@class="el-button el-button--primary"]')
