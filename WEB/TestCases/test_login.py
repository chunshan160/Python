#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:39
# @Author :春衫
# @File :test_login.py

import unittest
import pytest


@pytest.mark.usefixtures("accless_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data",LD.phone_data)#替代ddt
    def test_login_success(self,accless_web,data):
        logging.info("***球容****登陆用例:正常场景:使用正确的用户名和密码登陆*********")
        # 步骤输入用户名:XXx密码XXX点击登陆
        accless_web[1].login(data["user"],data["passwd"])
        # 断言―首页当中-能否找到退出这个元素。
        self.assertTrue(IndexPage(accless_web[0]).isExist_logout_ele())

