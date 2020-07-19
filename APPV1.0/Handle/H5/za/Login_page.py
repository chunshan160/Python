# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm

import time
from Common.TouchAction import Touch

local= {"小米8":{"输入手机号":(440,775),"下一步":(540,1030),"输入密码":(500,860),"验证码登录":(190,1255),"输入验证码":(500,860),"登录":(540,1110)}}

class LoginPage:

    def __init__(self, driver,model="小米8"):
        self.driver = driver
        self.model=model
        self.local=local[self.model]

    # 登录操作
    def login(self, phone, pwd=None):
        self.phone(phone)
        self.password(pwd)

    def phone(self, phone):
        time.sleep(2)
        # 点击输入框
        Touch(self.driver).tap(self.local["输入手机号"][0], self.local["输入手机号"][1])
        time.sleep(2)
        # 输入手机号
        self.nine_keys_key_board(phone)
        time.sleep(1)
        # 点击下一步
        Touch(self.driver).tap(self.local["下一步"][0], self.local["下一步"][1])

    def password(self, pwd=None, code="666666"):

        time.sleep(1)
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            Touch(self.driver).tap(self.local["验证码登录"][0], self.local["验证码登录"][1])
            time.sleep(1)
            # 点击输入框
            Touch(self.driver).tap(self.local["输入验证码"][0], self.local["输入验证码"][1])
            # 默认666666  传值的话会变
            time.sleep(1)
            self.nine_keys_key_board(code)
            time.sleep(1)
        # 用密码登录
        else:
            # 点击输入框
            Touch(self.driver).tap(self.local["输入密码"][0], self.local["输入密码"][1])
            time.sleep(1)
            # 输入密码 默认qaz123
            self.driver.keyevent(45)
            self.driver.keyevent(29)
            self.driver.keyevent(54)
            self.driver.keyevent(8)
            self.driver.keyevent(9)
            self.driver.keyevent(10)
        time.sleep(1)
        time.sleep(1)
        # 点击登录
        Touch(self.driver).tap(self.local["登录"][0], self.local["登录"][1])

    def nine_keys_key_board(self, a):

        for i in a:
            if i == "1":
                self.driver.keyevent(8)
            elif i == "2":
                self.driver.keyevent(9)
            elif i == "3":
                self.driver.keyevent(10)
            elif i == "4":
                self.driver.keyevent(11)
            elif i == "5":
                self.driver.keyevent(12)
            elif i == "6":
                self.driver.keyevent(13)
            elif i == "7":
                self.driver.keyevent(14)
            elif i == "8":
                self.driver.keyevent(15)
            elif i == "9":
                self.driver.keyevent(16)
            elif i == "0":
                self.driver.keyevent(7)


if __name__ == '__main__':
    from appium import webdriver

    desired_caps = {}
    desired_caps["platformName"] = "Android"  # android的apk还是IOS的ipa
    # desired_caps["platfromVersion"] = "10"  # Android系统的版本号
    # desired_caps["deviceName"] = "eba33135"  # 手机设备名称，通过adb devices

    desired_caps["platfromVersion"] = "7.0"  # Android系统的版本号
    desired_caps["deviceName"] = "621CECQ928KFW"  # 手机设备名称，通过adb devices
    desired_caps["appPackage"] = "com.ecloud.hobay"  # apk的包名  aapt dump badging 包路径
    desired_caps["appActivity"] = "com.ecloud.hobay.function.splash.SplashActivity"  # apk的launcherActivity  同上，下拉
    desired_caps["noReset"] = True
    # desired_caps['unicodekeyboard'] = True    # 使用unicodeKeyboard的编码方式来发送字符串
    # desired_caps['resetkeyboard'] = True   # 将键盘给隐藏起来
    desired_caps["automationName"] = "UiAutomator2"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 启动服务器地址，后面跟的是手机信息
    # a = LoginPage(driver).get_size_proportion(310, 1780)
    # print(a)
