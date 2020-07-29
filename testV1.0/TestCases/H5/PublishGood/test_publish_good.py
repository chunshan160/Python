#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 17:21
#@Author :春衫
#@File :test_publish_good.py

import ddt
import time
import unittest
import pytest
from selenium import webdriver
from TestData import Common_Data as CD
from Handle.H5.za.Login_page import LoginPage
from PageLocators.H5.PubilcGood import pubilc_good as PG
from Business.H5.PublishGood.EntityGood import EntityGoodBusiness
from TestData.H5.Publish_Data import *
from Business.H5.toAuditOk import ToAuditOkBusiness


@ddt.ddt
class PublishGood(unittest.TestCase):

    def setUp(cls):
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(CD.H5_Login_url)
        cls.lg = LoginPage(cls.driver)
        cls.lg.login("17777777776", "qaz123")
        time.sleep(2)
        cls.driver.find_element(*PG.publish_good).click()
        time.sleep(5)
        cls.driver.find_element(*PG.entity_good).click()
        time.sleep(2)

    @pytest.mark.smoke
    @ddt.data(*EntityGood_data)
    def test_1_publish_entity_good(self,data):
        EntityGoodBusiness(self.driver).publish_entity_good(data["product_title"], data["product_description"], data["property_1"],
                          data["property_2"], data["purchase_price"], data["sell_price"], data["stock"],
                          data["limit_quantity"])
        EntityGoodBusiness(self.driver).submit()
        self.assertTrue(ToAuditOkBusiness(self.driver).get_text())

    # def test_2_no_image(self):
    #     text = EntityGoodBusiness(self.driver).get_error_text("请上传商品图片")
    #     self.assertTrue(text)

    def tearDown(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)

