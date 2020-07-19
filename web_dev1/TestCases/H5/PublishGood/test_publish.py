#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/24 15:28
# @Author :春衫
# @File :123.py

from selenium import webdriver
from web_dev1.PageObjects.H5.Login_page import LoginPage
from web_dev1.TestData import Common_Data as CD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_dev1.PageObjects.H5 import PublishGood_page as PG
import unittest
from web_dev1.TestData.H5 import Login_Data as LD, Publish_Data as PD
import ddt
from web_dev1.PageObjects.H5.SystemPoint_page import SystemPoint
from web_dev1.PageLocators.H5.PublishGood import Pubilc
import time


@ddt.ddt
class PiblishGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        print("=======所有测试用例执行之前，setUpClass整个测试类只执行一次==========")
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(CD.H5_Login_url)
        cls.lg = LoginPage(cls.driver)
        cls.pp = PG.Product(cls.driver)
        cls.lg.login(LD.Success_data["username"], LD.Success_data["password"])
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((Pubilc.location))).click()
        # 首页点击发布商品
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.publish_goods))).click()



    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 发布实物商品，立即上架
    @ddt.data(*PD.Real_Goods_data)
    def test_1_RealGoods_submit(cls, data):
        # 点击发布实物商品
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.real_goods))).click()
        cls.pp.Real_Goods(data["product_title"], data["product_description"], data["property_1"],
                          data["property_2"], data["purchase_price"], data["sell_price"], data["stock"],
                          data["limit_quantity"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        time.sleep(1)
        # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
        cls.assertTrue(SystemPoint(cls.driver).Perfection())

    # # 发布实物商品，放入仓库
    # @ddt.data(*PD.Real_Goods_data)
    # def test_2_RealGoods_storage(cls, data):
    #     # 点击发布实物商品
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.real_goods))).click()
    #     cls.pp.Real_Goods(data["product_title"], data["product_description"], data["property_1"],
    #                       data["property_2"], data["purchase_price"], data["sell_price"], data["stock"],
    #                       data["limit_quantity"])
    #     # 放入仓库
    #     cls.pp.storage(Pubilc.storage)
    #     time.sleep(1)
    #     # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
    #     cls.assertTrue(SystemPoint(cls.driver).Perfection())

    # 发布本地生活，立即上架
    @ddt.data(*PD.Local_Life_data)
    def test_3_LocalLife_submit(cls, data):
        # 点击发布本地生活
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.local_life))).click()
        cls.pp.Local_Life(data["product_title"], data["product_description"], data["total_price"],
                          data["stock"], data["limit_quantity"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        time.sleep(1)
        # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
        cls.assertTrue(SystemPoint(cls.driver).Perfection())

    # # 发布本地生活，放入仓库
    # @ddt.data(*PD.Local_Life_data)
    # def test_4_LocalLife_storage(cls, data):
    #     # 点击发布本地生活
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.local_life))).click()
    #     cls.pp.Local_Life(data["product_title"], data["product_description"], data["total_price"],
    #                       data["stock"], data["limit_quantity"])
    #     # 放入仓库
    #     cls.pp.storage(Pubilc.storage)
    #     time.sleep(1)
    #     # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
    #     cls.assertTrue(SystemPoint(cls.driver).Perfection())

    # 发布商企服务，立即上架
    @ddt.data(*PD.Business_Services_data)
    def test_5_BusinessServices_submit(cls, data):
        # 点击发布本地生活
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.business_services))).click()
        cls.pp.Business_Services(data["product_title"], data["product_description"], data["total_price"],
                                 data["subsist"], data["stock"], data["limit_quantity"])
        # 放入仓库
        cls.pp.submit(Pubilc.submit)
        time.sleep(1)
        # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
        cls.assertTrue(SystemPoint(cls.driver).Perfection())

    # # 发布商企服务，放入仓库
    # @ddt.data(*PD.Business_Services_data)
    # def test_6_BusinessServices_storage(cls, data):
    #     # 点击发布本地生活
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.business_services))).click()
    #     cls.pp.Business_Services(data["product_title"], data["product_description"], data["total_price"],
    #                              data["subsist"], data["stock"], data["limit_quantity"])
    #     # 放入仓库
    #     cls.pp.storage(Pubilc.storage)
    #     time.sleep(1)
    #     # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
    #     cls.assertTrue(SystemPoint(cls.driver).Perfection())

    def tearDown(cls):
        cls.driver.get(CD.H5_publishGood_url)
        # 后置
        cls.driver.refresh()
