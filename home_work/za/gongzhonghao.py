#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/21 12:13
# @Author :春衫
# @File :gongzhonghao.py
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
desired_caps["platformName"] = "Android"  # android的apk还是IOS的ipa
desired_caps["platfromVersion"] = "10"  # Android系统的版本号
desired_caps["deviceName"] = "eba33135"  # 手机设备名称，通过adb devices
desired_caps["appPackage"] = "com.tencent.mm"  # apk的包名  aapt dump badging 包路径
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"  # apk的launcherActivity  同上，下拉
desired_caps["noReset"] = True
desired_caps["automationName"] = "UiAutomator2"
# desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}
# desired_caps['recreateChromeDriverSessions'] = 'true'
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 启动服务器地址，后面跟的是手机信息

time.sleep(5)
#点击发现
driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
#点击搜一搜
driver.find_element_by_android_uiautomator('new UiSelector().text("搜一搜")').click()
#等待搜索框出现
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.tencent.mm:id/f93")))
#点击搜索框
driver.find_element_by_id("com.tencent.mm:id/f93").click()
time.sleep(5)
#点击搜索记录
driver.find_element_by_android_uiautomator('new UiSelector().text("shanghailifeDAT")').click()
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("shanghailifeDAT 已关注 LIVE IT UP 上海人寿保险股份有限公司")').click()
time.sleep(5)
#点击进入公众号
driver.find_element_by_id("com.tencent.mm:id/azz").click()
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("微快服务")').click()
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("微服务")').click()
time.sleep(5)

#获取上下文
cons=driver.contexts
print("当前所有的上下文为：",cons)

#切换
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
#打印当前所有窗口
hs=driver.window_handles
print("当前所有的窗口为：",hs)