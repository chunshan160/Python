#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 17:21
# @Author :春衫
# @File :test_publish_good.py

import time
import ddt
import unittest
import warnings
import HTMLTestReportCN
from appium import webdriver
from TestData.H5.Publish_Data import *
from PageLocators.H5.PubilcGood.PubilcGood import *
from PageLocators.H5.Index.Index import *
from PageLocators.H5.SystemPoint.SubmitReviewOK import *
from Common.find_element import FindElement
from Business.H5.Login.Login_Business import LoginBusiness
from Business.H5.PublishGood.EntityGood_Business import EntityGoodBusiness
from Business.H5.PublishGood.CouponGood_Business import CouponGoodBusiness
from Business.H5.PublishGood.ServicesGood_Business import ServicesGoodBusiness
from Business.H5.SystemPoint.SubmitReview_OK import SubmitReviewOKBusiness


@ddt.ddt
class PublishGood(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.report_dir = HTMLTestReportCN.ReportDirectory(path="./Report/")
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {}
        desired_caps["platformName"] = "Android"  # android的apk还是IOS的ipa
        desired_caps["platfromVersion"] = "10"  # Android系统的版本号
        desired_caps["deviceName"] = "eba33135"  # 手机设备名称，通过adb devices
        # desired_caps["platfromVersion"] = "7.0"  # Android系统的版本号
        # desired_caps["deviceName"] = "621CECQ928KFW"  # 手机设备名称，通过adb devices
        desired_caps["appPackage"] = "com.ecloud.hobay"  # apk的包名  aapt dump badging 包路径
        desired_caps["appActivity"] = "com.ecloud.hobay.function.splash.SplashActivity"  # apk的launcherActivity  同上，下拉
        desired_caps["noReset"] = True
        desired_caps["unicodekeyboard"] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps["resetkeyboard"] = True  # 将键盘给隐藏起来
        desired_caps["automationName"] = "UiAutomator2"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 启动服务器地址，后面跟的是手机信息
        cls.fd = FindElement(cls.driver)
        time.sleep(5)
        # 首页点击发布商品
        cls.fd.find_element(publish_good).click()
        cls.LG = LoginBusiness(cls.driver, model="MI 8")
        cls.LG.login("44444444444")
        time.sleep(3)
        # 首页点击发布商品
        cls.fd.find_element(publish_good).click()

    @ddt.data(*EntityGood_data)
    def test_1_publish_entity_good(self, data):
        try:
            time.sleep(1)
            # 选择发布实物商品
            self.fd.find_element(entity_good).click()
            time.sleep(1)
            EntityGoodBusiness(self.driver).publish_entity_good(data["product_title"], data["product_description"],
                                                                data["property_1"],
                                                                data["property_2"], data["purchase_price"],
                                                                data["sell_price"], data["stock"],
                                                                data["limit_quantity"])
            EntityGoodBusiness(self.driver).submit()
            # 断言
            text = SubmitReviewOKBusiness(self.driver).get_text()
            self.assertTrue(text)
            self.fd.find_element(good_audit_btn).click()
        except Exception as e:
            # 截图
            self.report_dir.get_screenshot(self.driver)
            raise e  # 异常处理完后记得抛出

    @ddt.data(*CouponGood_data)
    def test_2_publish_coupon_good(self, data):
        time.sleep(1)
        # 选择发布本地生活商品
        self.fd.find_element(coupon_good).click()
        time.sleep(1)
        CouponGoodBusiness(self.driver).publish_coupon_good(data["product_title"], data["product_description"],
                                                            data["total_price"], data["stock"],
                                                            data["limit_quantity"])
        CouponGoodBusiness(self.driver).submit()
        # 断言
        text = SubmitReviewOKBusiness(self.driver).get_text()
        self.assertTrue(text)
        self.fd.find_element(good_audit_btn).click()

    @ddt.data(*ServerGood_data)
    def test_3_publish_server_good(self, data):
        time.sleep(1)
        # 选择发布商企服务商品
        self.fd.find_element(services_good).click()
        time.sleep(1)
        ServicesGoodBusiness(self.driver).publish_services_good(data["product_title"], data["product_description"],
                                                                data["total_price"], data["subsist"], data["stock"],
                                                                data["limit_quantity"])
        ServicesGoodBusiness(self.driver).submit()
        # 断言
        text = SubmitReviewOKBusiness(self.driver).get_text()
        self.assertTrue(text)
        self.fd.find_element(good_audit_btn).click()

    def tearDown(cls):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
