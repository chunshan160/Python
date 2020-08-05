# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm
import os
import re
import time
from Common.TouchAction import Touch

local= {"MI 8":{"输入手机号":(440,775),"下一步":(540,1030),"输入密码":(500,860),"验证码登录":(190,1255),"登录":(540,1110)}}

class LoginPage:

    def __init__(self, driver,model="MI 8"):
        self.driver = driver
        self.model=model

    # 登录操作
    def login(self, phone, pwd=None):
        self.phone(phone)
        self.password(pwd)

    def phone(self, phone):
        X_proportion = self.get_size_proportion()[0]
        Y_proportion = self.get_size_proportion()[1]
        time.sleep(2)
        # 点击输入框
        Touch(self.driver).tap(int(400 / X_proportion), int(770 / Y_proportion))
        time.sleep(2)

        # 输入手机号
        # self.nine_keys_key_board(phone, X_proportion)
        Y1 = eval(self.get_screen_size()['height'])
        for i in phone:
            if i == "1":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 1
            elif i == "2":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 2
            elif i == "3":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 3
            elif i == "4":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 4
            elif i == "5":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 5
            elif i == "6":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 6
            elif i == "7":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 7
            elif i == "8":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 8
            elif i == "9":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 9
            elif i == "0":
                Touch(self.driver).tap(int(530 / X_proportion), int(Y1 - (2248 - 2090) + 60))  # 0
        time.sleep(1)
        # 关闭软键盘
        Touch(self.driver).tap(int(1000 / X_proportion), int(Y1 - (2248 - 1480)+60))
        time.sleep(1)
        # 点击下一步
        Touch(self.driver).tap(int(522 / X_proportion), int(1019 / Y_proportion))

    def password(self, pwd=None, code="666666"):

        X_proportion = self.get_size_proportion()[0]
        Y_proportion = self.get_size_proportion()[1]

        time.sleep(1)
        Y1 = eval(self.get_screen_size()['height'])
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            Touch(self.driver).tap(int(170 / X_proportion), int(1255 / Y_proportion))
            time.sleep(1)
            # 点击输入框
            Touch(self.driver).tap(int(432 / X_proportion), int(860 / Y_proportion))
            # 默认666666  传值的话会变
            time.sleep(1)
            # self.nine_keys_key_board(code, X_proportion)

            for i in code:
                if i == "1":
                    Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 1
                elif i == "2":
                    Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 2
                elif i == "3":
                    Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1630) + 60))  # 3
                elif i == "4":
                    # Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 4
                    driver.keyevent(11)
                elif i == "5":
                    Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 5
                elif i == "6":
                    Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1780) + 60))  # 6
                elif i == "7":
                    Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 7
                elif i == "8":
                    Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 8
                elif i == "9":
                    Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1940) + 60))  # 9
                elif i == "0":
                    Touch(self.driver).tap(int(530 / X_proportion), int(Y1 - (2248 - 2090) + 60))  # 0
            time.sleep(1)
            # 关闭软键盘
            Touch(self.driver).tap(int(1000 / X_proportion), int(Y1 - (2248 - 1480) + 60))

        # 用密码登录
        else:
            # 点击输入框
            Touch(self.driver).tap(int(432 / X_proportion), int(860 / Y_proportion))
            time.sleep(1)

            # 输入密码 默认qaz123
            Touch(self.driver).tap(int(64 / X_proportion), int(1630 / Y_proportion))
            Touch(self.driver).tap(int(112 / X_proportion), int(1780 / Y_proportion))
            Touch(self.driver).tap(int(216 / X_proportion), int(1940 / Y_proportion))

            Touch(self.driver).tap(int(50 / X_proportion), int(1490 / Y_proportion))
            Touch(self.driver).tap(int(160 / X_proportion), int(1490 / Y_proportion))
            Touch(self.driver).tap(int(270 / X_proportion), int(1490 / Y_proportion))
        time.sleep(1)
        # 关闭软键盘
        Touch(self.driver).tap(int(1000 / X_proportion), int(Y1 - (2248 - 1480)+60))
        time.sleep(1)
        # 点击登录
        Touch(self.driver).tap(int(512 / X_proportion), int(1116 / Y_proportion))

    def get_size_proportion(self):
        # 获取当前手机屏幕大小：x和y表示
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        X1 = eval(self.get_screen_size()['width'])
        Y1 = eval(self.get_screen_size()['height'])

        if X == 1080 and Y == 2029:
            X3 = 1
            Y3 = 1
        else:
            if X == X1:
                X3 = float(str(X / 1080)[:4])
            else:
                X3 = float(str(X1 / 1080)[:4])

            if Y == Y1:
                # 默认尺寸
                Y3 = float(str(Y / 2029)[:4])
            else:
                Y3 = float(str(Y1 / 2029)[:4])

        return (X3, Y3)

    def get_screen_size(self):
        # 高 宽
        '获取手机屏幕大小'
        size_str = os.popen('adb shell wm size').read()
        m = re.search(r'(\d+)x(\d+)', size_str)
        return {'height': m.group(2), 'width': m.group(1)}

    def nine_keys_key_board(self, a, X_proportion):

        Y1 = eval(self.get_screen_size()['height'])
        for i in a:
            if i == "1":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1630)))  # 1
            elif i == "2":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1630)))  # 2
            elif i == "3":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1630)))  # 3
            elif i == "4":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1780)))  # 4
            elif i == "5":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1780)))  # 5
            elif i == "6":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1780)))  # 6
            elif i == "7":
                Touch(self.driver).tap(int(310 / X_proportion), int(Y1 - (2248 - 1940)))  # 7
            elif i == "8":
                Touch(self.driver).tap(int(540 / X_proportion), int(Y1 - (2248 - 1940)))  # 8
            elif i == "9":
                Touch(self.driver).tap(int(770 / X_proportion), int(Y1 - (2248 - 1940)))  # 9
            elif i == "0":
                Touch(self.driver).tap(int(530 / X_proportion), int(Y1 - (2248 - 2090)))  # 0


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
    a = LoginPage(driver).get_size_proportion(310, 1780)
    print(a)
