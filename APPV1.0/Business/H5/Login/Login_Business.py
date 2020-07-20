# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_Handle.py
# @Software: PyCharm

from PageLocators.H5.Login.Login import local
from Handle.H5.Login.Login_Handle import LoginHandle


class LoginBusiness:

    def __init__(self, driver, model="小米8"):
        self.driver = driver
        self.local = local[model]
        self.LH = LoginHandle(driver, self.local)

    # 登录操作
    def login(self, phone, pwd=None):
        self.phone(phone)
        self.password(pwd)

    # 输入手机号
    def phone(self, phone):
        # 点击输入框
        self.LH.click_phone_box()
        # 输入手机号
        self.LH.nine_keys_key_board(phone)
        # 点击下一步
        self.LH.click_next()

    def password(self, pwd=None, code="666666"):
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            self.LH.switch_code()
            # 点击输入框
            self.LH.click_code_box()
            # 默认666666  传值的话会变
            self.LH.nine_keys_key_board(code)
        # 用密码登录
        else:
            # 点击输入框
            self.LH.click_pwd_box()
            # 输入密码 默认qaz123
            self.LH.send_pwd()
        # 点击登录
        self.LH.click_login()


if __name__ == '__main__':
    pass
