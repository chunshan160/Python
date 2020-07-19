#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/9 13:36
#@Author :春衫
#@File :find_element.py


from selenium import webdriver
from Common.user_log import UserLog

class FindElement(object):

    def __init__(self,driver):
        self.driver=driver
        self.logger = UserLog()

    def find_element(self,key,index=None):
        by=key[0]
        value=key[1]
        self.logger.info("定位方式:" + by + "--->定位值:" + value)
        try:
            if by == "id":
                if index==None:
                    return self.driver.find_element_by_id(value)
                else:
                    return self.driver.find_elements_by_id(value)[index]
            elif by == "class_name":
                if index == None:
                    return self.driver.find_element_by_class_name(value)
                else:
                    return self.driver.find_elements_by_class_name(value)[index]
            elif by == "accessibility_id":
                if index == None:
                    return self.driver.find_element_by_accessibility_id(value)
                else:
                    return self.driver.find_elements_by_accessibility_id(value)[index]
            elif by == "android_uiautomator":
                if index == None:
                    return self.driver.find_element_by_android_uiautomator(value)
                else:
                    return self.driver.find_elements_by_android_uiautomator(value)[index]
            elif by == "xpath":
                if index == None:
                    return self.driver.find_element_by_xpath(value)
                else:
                    return self.driver.find_elements_by_xpath(value)[index]
            else:
                print("不支持这个方法")
        except:
            print("没有找到这个元素")


if __name__ == '__main__':
    desired_caps = {}
    desired_caps["platformName"] = "Android"  # android的apk还是IOS的ipa
    # desired_caps["platfromVersion"] = "8.1"    #Android系统的版本号
    # desired_caps["deviceName"] = "872QEDUQ2224T"   #手机设备名称，通过adb devices

    desired_caps["platfromVersion"] = "10"  # Android系统的版本号
    desired_caps["deviceName"] = "eba33135"  # 手机设备名称，通过adb devices

    desired_caps["appPackage"] = "com.ecloud.hobay"  # apk的包名  aapt dump badging 包路径
    # desired_caps["appActivity"] = "com.ecloud.hobay.function.main.HomeActivity"   #apk的launcherActivity  同上，下拉
    desired_caps["appActivity"] = "com.ecloud.hobay.function.splash.SplashActivity"
    desired_caps["noReset"] = True
    # desired_caps['unicodekeyboard'] = True    # 使用unicodeKeyboard的编码方式来发送字符串
    # desired_caps['resetkeyboard'] = True   # 将键盘给隐藏起来
    # desired_caps["automationName"] = "uiautomator2"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    A=FindElement(driver).find_element(("XPATH", '//div[@class="audit-text"]')).text
    print(A)