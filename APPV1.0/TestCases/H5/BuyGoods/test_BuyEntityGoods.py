#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

import time
import ddt
import unittest
import warnings
import HTMLTestReportCN
from appium import webdriver
from Common.BasePage import BasePage
from PageLocators.H5.Index import Index
from PageLocators.H5.My_Index import My_Index
from PageLocators.H5.My_Index import Setting
from PageObjects.H5.Index.Index import IndexPage
from PageObjects.H5.SearchGood.SearchGood import SearchGoodPage
from PageObjects.H5.GoodDetail.GoodDetail_Page import GoodDetailPage
from PageObjects.H5.ConfirmOrder.ConfirmOrder_Page import ConfirmOrderPage
from PageObjects.H5.Login.Login_Page import LoginPage
from PageObjects.H5.Pay.Pay import PayPage
from PageObjects.H5.SystemPoint.Pay_Success import PaySuccessPage


@ddt.ddt
class BuyEntityGoods(unittest.TestCase):

    @classmethod
    def setUp(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {}
        desired_caps["platformName"] = "Android"  # android的apk还是IOS的ipa
        desired_caps["platfromVersion"] = "10"  # Android系统的版本号
        desired_caps["deviceName"] = "eba33135"  # 手机设备名称，通过adb devices
        desired_caps["appPackage"] = "com.ecloud.hobay"  # apk的包名  aapt dump badging 包路径
        desired_caps["appActivity"] = "com.ecloud.hobay.function.splash.SplashActivity"  # apk的launcherActivity  同上，下拉
        desired_caps["noReset"] = True
        desired_caps["unicodekeyboard"] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps["resetkeyboard"] = True  # 将键盘给隐藏起来
        desired_caps["automationName"] = "UiAutomator2"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 启动服务器地址，后面跟的是手机信息
        try:
            time.sleep(5)
            # 首页点击发布商品
            BasePage(cls.driver).get_element(Index.publish_good, doc="").click()
            cls.LG = LoginPage(cls.driver, model="小米8")
            cls.LG.login("17777777781")
            time.sleep(3)
            # 首页点击搜索
            IndexPage(cls.driver).search()
            # 输入商品名
            SearchGoodPage(cls.driver).send_search("APP实物商品")
            # 商品详情
            GoodDetailPage(cls.driver).buy_good()
            # 确认订单
            ConfirmOrderPage(cls.driver).submit_order_now()
            time.sleep(3)
        except Exception as e:
            # 截图
            BasePage(cls.driver).save_screenshot("测试购买实物商品")
            raise e  # 异常处理完后记得抛出

    # 购买实物商品-易贝支付
    def test_1_cbp_pay(self):
        try:
            PayPage(self.driver).click_cbp_pay()
            # 断言
            PaySuccessPage(self.driver).close_windows()
            text = PaySuccessPage(self.driver).title_text()
            self.assertTrue(text)
        except Exception as e:
            # 截图
            BasePage(self.driver).save_screenshot("测试易贝支付购买实物商品")
            raise e  # 异常处理完后记得抛出

    # 购买实物商品-易贝券支付
    def test_2_voucher_pay(self):
        try:
            PayPage(self.driver).click_voucher_pay()
            # 断言
            PaySuccessPage(self.driver).close_windows()
            text = PaySuccessPage(self.driver).title_text()
            self.assertTrue(text)
        except Exception as e:
            # 截图
            BasePage(self.driver).save_screenshot("测试易贝券购买实物商品")
            raise e  # 异常处理完后记得抛出

    # 购买实物商品-抵工资支付
    def test_3_wages_pay(self):
        try:
            PayPage(self.driver).click_wages_pay()
            # 断言
            PaySuccessPage(self.driver).close_windows()
            text = PaySuccessPage(self.driver).title_text()
            self.assertTrue(text)
        except Exception as e:
            # 截图
            BasePage(self.driver).save_screenshot("测试抵工资购买实物商品")
            raise e  # 异常处理完后记得抛出

    # 购买实物商品-家人购
    def test_4_family_pay(self):
        try:
            PayPage(self.driver).click_family_pay()
            # 断言
            PaySuccessPage(self.driver).close_windows()
            text = PaySuccessPage(self.driver).title_text()
            self.assertTrue(text)
        except Exception as e:
            # 截图
            BasePage(self.driver).save_screenshot("测试家人购购买实物商品")
            raise e  # 异常处理完后记得抛出

    # 购买实物商品-现金账户
    def test_5_cash_pay(self):
        try:
            PayPage(self.driver).click_cash_pay()
            # 断言
            PaySuccessPage(self.driver).close_windows()
            text = PaySuccessPage(self.driver).title_text()
            self.assertTrue(text)
        except Exception as e:
            # 截图
            BasePage(self.driver).save_screenshot("测试现金账户购买实物商品")
            raise e  # 异常处理完后记得抛出

    @classmethod
    def tearDownClass(cls):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
