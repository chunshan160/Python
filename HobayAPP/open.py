#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 15:44
# @Author  : Aries
# @Site    : 
# @File    : 搜索.py
# @Software: PyCharm


# #导入模块
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time
import uiautomator2 as U2

caps = {}
caps["platformName"] = "Android"   #android的apk还是IOS的ipa
caps["platfromVersion"] = "10"    #Android系统的版本号
caps["deviceName"] = "eba33135"   #手机设备名称，通过adb devices
caps["Package"] = "com.ecloud.hobay"   #apk的包名  aapt dump badging 包路径
caps["Activity"] = "com.ecloud.hobay.function.main.HomeActivity"   #apk的launcherActivity  同上，下拉
caps["noReset"] = "True"
# caps['unicodekeyboard'] = True    # 使用unicodeKeyboard的编码方式来发送字符串
# caps['resetkeyboard'] = True   # 将键盘给隐藏起来
caps["automationName"] = "uiautomator2"
driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)   #启动服务器地址，后面跟的是手机信息


# time.sleep(3)
# # #点击跳过
# driver.find_element_by_id('com.ecloud.hobay:id/rb_me').click()
#
# # #休眠5秒等待页面加载完成
time.sleep(5)

# # #登录放这里
# driver.find_element_by_id('com.ecloud.HobayAPP:id/rb_me').click()
# time.sleep(5)
# # TouchAction(driver).tap(x=385, y=791).perform()


# loc = 'new UISelector().text("登录")'
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR.loc)))
# driver.find_element_by_android_uiautomator(loc).click()

# #等待WebView元素出现
# WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((MobileBy.CLASS_NAME,'android.widget.FrameLayout')))
# time.sleep(1)

#前提：我们可以识别到webview     需要开启app的webview debug属性
#context  #原生控件     #webview
# #先列出所有上下文
# cons = driver.contexts  #列表
# print(cons)
#
# #切换
# driver.switch_to.context(cons[-1])

#切换之后：当前的操作对象：html
#等待元素可见
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.XPATH,'//input[@placeholder="请填写手机号"]')))
# driver.find_element_by_xpath('//input[@placeholder="请填写手机号"]').click()


#搜索商品
driver.find_element_by_id("com.ecloud.HobayAPP:id/tv_search").click()
time.sleep(2)
driver.find_element_by_id("com.ecloud.HobayAPP:id/et_search").send_keys("限购")
time.sleep(2)

#调用输入法的搜索按钮（搜狗输入法）
driver.keyevent(66)
time.sleep(5)

#点击第一个商品
driver.find_elements_by_id('com.ecloud.HobayAPP:id/iv_product_pic')[1].click()


#点击立即购买
driver.find_element_by_id('com.ecloud.HobayAPP:id/tv_buy_now').click()


driver.quit()

