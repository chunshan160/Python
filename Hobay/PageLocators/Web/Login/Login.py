#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py

from selenium.webdriver.common.by import By

# 手机号
name = (By.XPATH, '//input[@type="number"]')
# 下一步
next = (By.XPATH, '//button[text()="下 一 步"]')
# 错误提示
error_toast = (By.XPATH, '//div[@class="van-toast__text"]')
# 立即注册
register = (By.XPATH, '//span[contains(text(),"立即注册")]//parent::button')
# 取消
cancel = (By.XPATH, '//span[contains(text(),"取消")]//parent::button')

# 输入验证码
input_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
# 获取验证码
obtain_code = (By.XPATH, '//button[contains(text(),"获取验证码")]')
# 已有账号
have_account = (By.XPATH, '//div[contains(text(),"已有账号")]')

# 输入密码
input_password = (By.XPATH, '//input[@placeholder="请输入密码"]')
# 显示密码
display_password = (By.XPATH, '//div[@class="slot-right-icon"]')
# 登录
login = (By.XPATH, '//button[contains(text(),"登 录")]')
# 验证码登录
code_login = (By.XPATH, '//div[text()="验证码登录"]')
# 找回密码
retrieve_password = (By.XPATH, '//div[contains(text(),"找回密码")]')
# 密码登录
pwd_login = (By.XPATH, '//div[text()="密码登录"]')

# 地区
address = (By.XPATH, '//div[@class="address-box"]')
# 定位
location = (By.CLASS_NAME, '//span[text()="获取定位失败"]')
# 省
province = (By.XPATH, '//div[contains(text(),"广东省")]')
# 市
city = (By.XPATH, '//div[contains(text(),"广州市")]')
# 区
area = (By.XPATH, '//div[contains(text(),"白云区")]')
# # 邀请人
# invite_people = (By.XPATH, '//input[@placeholder="请填写邀请人手机号(选填)"]')
# 完成
perfection = (By.XPATH, '//button[contains(text(),"完 成")]')
# 勾选协议
tick = (By.XPATH, '//div[@class="checkbox"]')

# 进入首页
get_index = (By.XPATH, '//button[@class="white-btn"]')
# 注册成功提示
register_success_text = (By.XPATH, '//div[contains(text(),"成功加入焕呗")]')

# 输入新密码
pwd_new = (By.XPATH, '//input[@placeholder="请设置您的新密码"]')
# 再次输入新密码
pwd_again = (By.XPATH, '//input[@placeholder="请再次确认密码"]')
# 提交
submit = (By.XPATH, '//div[@class="submit-btn no-btn"]')
# 找回密码---找回成功
msg = (By.XPATH, '//div[contains(text(),"密码找回成功")]')
