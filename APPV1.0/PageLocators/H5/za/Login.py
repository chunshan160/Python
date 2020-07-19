#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   :2019/12/26 12:36
# @Author :春衫
# @Email  :1605936478@qq.com
# @File   :loginpage_locators.py




class LoginPage:

    def pwd_login(self):
        # 手机号
        name = ("id", '//input[@type="number"]')
        # 下一步
        next = ("id", '//button[text()="下 一 步"]')
        # 错误提示
        error_toast = ("id", '//div[@class="van-toast__text"]')
        # 立即注册
        register = ("id", '//span[contains(text(),"立即注册")]//parent::button')
        # 取消
        cancel = ("id", '//span[contains(text(),"取消")]//parent::button')

    def new_register(self):
        # 输入验证码
        enter_code = ("id", '//input[@placeholder="请输入验证码"]')
        # 获取验证码
        obtain_code = ("id", '//button[contains(text(),"获取验证码")]')
        # 下一步
        next = ("id", '//button[text()="下 一 步"]')
        # 已有账号
        have_account = ("id", '//div[contains(text(),"已有账号")]')

    def password_login(self):
        # 输入密码
        enter_password = ("id", '//input[@placeholder="请输入密码"]')
        # 显示密码
        display_password = ("id", '//div[@class="slot-right-icon"]')
        # 登录
        login = ("id", '//button[contains(text(),"登 录")]')
        # 验证码登录
        code_login = ("id", '//div[text()="验证码登录"]')
        # 找回密码
        retrieve_password = ("id", '//div[contains(text(),"找回密码")]')

    def code_login(self):
        # 输入验证码
        enter_code = ("id", '//input[@placeholder="请输入验证码"]')
        # 获取验证码
        obtain_code = ("id", '//button[contains(text(),"获取验证码")]')
        # 登录
        login = ("id", '//button[contains(text(),"登 录")]')
        # 密码登录
        pwd_login = ("id", '//div[text()="密码登录"]')
        # 找回密码
        retrieve_password = ("id", '//div[contains(text(),"找回密码")]')

    def improving_info(self):
        # 地区
        address = ("id", '//div[@class="address-box"]')
        # 定位
        location = ("id", '//span[text()="获取定位失败"]')
        # 省
        province = ("id", '//div[contains(text(),"广东省")]')
        # 市
        city = ("id", '//div[contains(text(),"广州市")]')
        # 区
        area = ("id", '//div[contains(text(),"白云区")]')
        # 邀请人
        invite_people = ("id", '//input[@placeholder="请填写邀请人手机号(选填)"]')
        # 完成
        perfection = ("id", '//button[contains(text(),"完 成")]')
        # 勾选协议
        tick = ("id", '//div[@class="checkbox"]')

    def register_success_new(self):
        #进入首页
        get_index=("id",'//button[@class="white-btn"]')
        #注册成功提示
        register_success_text=("id",'//div[contains(text(),"成功加入焕呗")]')

    def Retrieve_Password(self):
        # 忘记密码
        retrieve_password = ("id", '//div[contains(text(),"找回密码")]')
        # 输入验证码
        verification_code = ("id", '//input[@placeholder="请输入验证码"]')
        # 输入新密码
        pwd_new = ("id", '//input[@placeholder="请设置您的新密码"]')
        # 再次输入新密码
        pwd_again = ("id", '//input[@placeholder="请再次确认密码"]')
        # 提交
        submit = ("id", '//div[@class="submit-btn no-btn"]')
        # 找回密码---找回成功
        msg = ("id", '//div[contains(text(),"密码找回成功")]')
