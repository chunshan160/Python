# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm
import time

from Web.PageLocators.Web.Login import Login
from Web.Common.BasePage import BasePage


class LoginPage(BasePage):

    # 输入手机号
    def input_phone(self, phone, text=""):
        doc = text + "输入【手机号】-"
        self.input_text(Login.phone, phone, doc=doc)

    # 点击下一步
    def click_next(self, text=""):
        doc = text + "点击【下一步】按钮-"
        self.click_element(Login.next, doc=doc)

    # 点击立即注册
    def register(self, text=""):
        doc = text + "点击【立即注册】按钮-"
        self.click_element(Login.register, doc=doc)

    # 取消立即注册
    def cancel(self, text=""):
        doc = text + "点击【取消】按钮-"
        self.click_element(Login.cancel, doc=doc)

    # 输入验证码
    def input_code(self,code, text=""):
        doc = text + "输入【验证码】-"
        self.input_text(Login.input_code, code, doc=doc)

    # 获取验证码
    def obtain_code(self, text=""):
        doc = text + "获取【验证码】-"
        self.click_element(Login.obtain_code, doc=doc)

    # 已有账号
    def have_account(self, text=""):
        doc = text + "点击【已有账号】-"
        self.click_element(Login.have_account, doc=doc)

    # 输入密码
    def input_password(self,password, text=""):
        doc = text + "输入【密码】-"
        self.input_text(Login.input_password, password, doc=doc)

    # 显示密码
    def display_password(self, text=""):
        doc = text + "点击显示【密码】-"
        self.click_element(Login.display_password, doc=doc)

    # 点击登录
    def click_login(self, text=""):
        doc = text + "点击【登录】-"
        self.click_element(Login.login, doc=doc)

    # 验证码登录
    def switch_code_login(self, text=""):
        doc = text + "点击【验证码登录】按钮-"
        self.click_element(Login.code_login, doc=doc)

    # 找回密码
    def retrieve_password(self, text=""):
        doc = text + "点击【找回密码】按钮-"
        self.click_element(Login.retrieve_password, doc=doc)

    # 密码登录
    def switch_pwd_login(self, text=""):
        doc = text + "点击【密码登录】按钮-"
        self.click_element(Login.pwd_login, doc=doc)

    # 注册地址
    def address(self, text=""):
        doc = text + "点击【注册地址】按钮-"
        self.click_element(Login.address, doc=doc)

    # 选择【省】
    def province(self, text=""):
        doc = text + "选择【省】-"
        self.click_element(Login.province, doc=doc)

    # 选择【市】
    def city(self, text=""):
        doc = text + "选择【市】按钮-"
        self.click_element(Login.city, doc=doc)

    # 选择【区】
    def area(self, text=""):
        doc = text + "选择【区】按钮-"
        self.click_element(Login.area, doc=doc)

    # 点击完成
    def perfection(self, text=""):
        doc = text + "点击【完成】按钮-"
        self.click_element(Login.perfection, doc=doc)

    # 勾选协议
    def tick(self, text=""):
        doc = text + "勾选【协议】按钮-"
        self.click_element(Login.tick, doc=doc)

    # 进入首页
    def go_index(self, text=""):
        doc = text + "点击【进入首页】按钮-"
        self.click_element(Login.go_index, doc=doc)

    # 输入新密码
    def input_pwd_new(self, text=""):
        doc = text + "输入【新密码】-"
        self.click_element(Login.pwd_new, doc=doc)

    # 再次输入新密码
    def input_new_pwd_again(self, text=""):
        doc = text + "输入【新密码】-"
        self.click_element(Login.pwd_again, doc=doc)

    # 提交
    def submit(self, text=""):
        doc = text + "输入【新密码】-"
        self.click_element(Login.submit, doc=doc)

    '''
    登录业务
    '''

    # 登录
    def login(self, phone, pwd=None, code="666666", text=""):
        # 输入手机号
        time.sleep(1)
        self.input_phone(phone,text=text)
        # 点击下一步
        time.sleep(1)
        self.click_next(text=text)
        time.sleep(1)
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            time.sleep(1)
            self.switch_code_login(text=text)
            # 点击输入框
            time.sleep(1)
            self.input_code(code,text=text)
            # 默认666666  传值的话会变
            time.sleep(1)
            self.send_phone_number(code, text=text)
        # 用密码登录
        else:
            # 点击输入框 输入密码 默认qaz123
            time.sleep(1)
            self.input_password(pwd,text=text)
        # 点击登录
        time.sleep(2)
        self.click_login(text=text)

