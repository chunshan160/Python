#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

import time
import ddt
import unittest
import warnings
from appium import webdriver
from Common.find_element import FindElement
from PageLocators.H5.Index import Index
from PageLocators.H5.MyIndex import MyIndex
from PageLocators.H5.MyIndex import Setting
from Business.H5.Login.Login_Business import LoginBusiness
from Business.H5.Index.Index_Business import IndexBusiness
from Business.H5.SearchGood.SearchGood_Business import SearchGoodBusiness
from Business.H5.GoodDetail.GoodDetail_Business import GoodDetailBusiness
from Business.H5.ConfirmOrder.ConfirmOrder_Business import ConfirmOrderBusiness
from Business.H5.Pay.Pay_Business import PayBusiness
from Business.H5.SystemPoint.Pay_Success import PaySuccessBusiness


@ddt.ddt
class BuyEntityGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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
        cls.fd.find_element(Index.publish_good).click()
        cls.LG = LoginBusiness(cls.driver,model="MI 8")
        cls.LG.login("17777777781")
        time.sleep(3)

    def setUp(cls):
        # 首页点击搜索
        IndexBusiness(cls.driver).click_search()
        # 输入商品名
        SearchGoodBusiness(cls.driver).search_good("APP商企服务")
        # 商品详情
        GoodDetailBusiness(cls.driver).buy_good()
        # 确认订单
        ConfirmOrderBusiness(cls.driver).confirm_order()
        time.sleep(3)

    # 购买实物商品-易贝支付
    def test_1_cbp_pay(self):
        PayBusiness(self.driver).click_cbp_pay()
        # 断言
        PaySuccessBusiness(self.driver).click_closes()
        text = PaySuccessBusiness(self.driver).get_title()
        self.assertTrue(text)
        PaySuccessBusiness(self.driver).click_return_home()

    # 购买实物商品-易贝券支付
    def test_2_voucher_pay(self):
        PayBusiness(self.driver).click_voucher_pay()
        # 断言
        PaySuccessBusiness(self.driver).click_closes()
        text = PaySuccessBusiness(self.driver).get_title()
        self.assertTrue(text)
        PaySuccessBusiness(self.driver).click_return_home()

    # 购买实物商品-抵工资支付
    def test_3_wages_pay(self):
        PayBusiness(self.driver).click_wages_pay()
        # 断言
        PaySuccessBusiness(self.driver).click_closes()
        text = PaySuccessBusiness(self.driver).get_title()
        self.assertTrue(text)
        PaySuccessBusiness(self.driver).click_return_home()

    # 购买实物商品-家人购
    def test_4_family_pay(self):
        PayBusiness(self.driver).click_family_pay()
        # 断言
        PaySuccessBusiness(self.driver).click_closes()
        text = PaySuccessBusiness(self.driver).get_title()
        self.assertTrue(text)
        PaySuccessBusiness(self.driver).click_return_home()

    # 购买实物商品-现金账户
    def test_5_cash_pay(self):
        PayBusiness(self.driver).click_cash_pay()
        # 断言
        PaySuccessBusiness(self.driver).click_closes()
        text = PaySuccessBusiness(self.driver).get_title()
        self.assertTrue(text)
        PaySuccessBusiness(self.driver).click_return_home()

    @classmethod
    def tearDownClass(cls):
        # 退出登录
        # 首页点击我的
        time.sleep(1)
        cls.fd.find_element(Index.my_index).click()
        time.sleep(1)
        cls.fd.find_element(MyIndex.setting).click()
        time.sleep(1)
        cls.fd.find_element(Setting.exit).click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
