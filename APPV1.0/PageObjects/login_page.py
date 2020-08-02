#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/25 18:24
#@Author :春衫
#@File :login_page.py

from Common.basepage import BasePage

class LoginPage(BasePage):

    #登陆操作
    def login(self, username,passwd,remeber_user=True):
        #输入用户名
        #输入密码
        doc ="登陆页面_登陆功能"
        self.wait_eleVisible(loc.user_input, doc=doc)
        self.input_text(loc.user_input, username, doc=doc)
        self.input_text(loc.passwd_input, passwd, doc=doc)
        # 判断一下rember_user的值，来决定是否勾选。
        self.click_element(loc.login_button, doc=doc)

