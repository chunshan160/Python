#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   :2019/12/26 12:36
# @Author :春衫
# @Email  :1605936478@qq.com
# @File   :loginpage_locators.py

from selenium.webdriver.common.by import By


class common:
    # 手机号
    name = (By.XPATH, '//input[@type="number"]')
    # 下一步
    next = (By.XPATH, '//button[text()="下 一 步"]')


class LoginPage:
    click_code=(By.XPATH,'//div[text()="验证码登录"]')
    # 错误提示
    error_toast = (By.XPATH, '//div[@class="van-toast__text"]')
    # 立即注册
    registered = (By.XPATH, '//span[contains(text(),"立即注册")]//parent::button')
    # 输入验证码
    verification_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    # 密码
    pwd = (By.XPATH, '//input[@type="password"]')
    # 登录
    login_but = (By.XPATH, '//button[contains(text(),"登 录")]')
    # 首页询问城市定位
    location = (By.XPATH,
                '//button[@class="van-button van-button--default van-button--large van-dialog__confirm van-hairline--left"]')
    # 首页-我的
    my = (By.XPATH, '//i[@class="my-icon"]')


class Registered:
    # 定位
    location = (By.CLASS_NAME, '//span[text()="获取定位失败"]')
    # 省
    province = (By.XPATH, '//div[contains(text(),"广东省")]')
    # 市
    city = (By.XPATH, '//div[contains(text(),"广州市")]')
    # 区
    area = (By.XPATH, '//div[contains(text(),"白云区")]')
    # 邀请人
    invite_people = (By.XPATH, '//input[@placeholder="请填写邀请人手机号(选填)"]')
    # 勾选协议
    tick = (By.XPATH, '//div[@class="checkbox"]')
    # 完成
    perfection = (By.XPATH, '//button[contains(text(),"完 成")]')


class Retrieve_Password:
    # 忘记密码
    retrieve_password = (By.XPATH, '//div[contains(text(),"找回密码")]')
    # 输入验证码
    verification_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    # 输入新密码
    pwd_new = (By.XPATH, '//input[@placeholder="请设置您的新密码"]')
    # 再次输入新密码
    pwd_again = (By.XPATH, '//input[@placeholder="请再次确认密码"]')
    # 提交
    submit = (By.XPATH, '//div[@class="submit-btn no-btn"]')
    # 找回密码---找回成功
    msg = (By.XPATH, '//div[contains(text(),"密码找回成功")]')
