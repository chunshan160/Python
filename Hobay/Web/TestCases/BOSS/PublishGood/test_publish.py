#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/24 15:28
# @Author :春衫
# @File :123.py

from selenium import webdriver
from Handle.BOSS import LoginPage, PublishGoods_page as PG
from Web.TestData.BOSS import Login_Data as LD
from Handle.BOSS.SystemPoint_page import SystemPoint
from Web.PageLocators.BOSS.PublishGoods import Pubilc
from Web.TestData.BOSS import Publish_Data as PD
import unittest
from Web.TestData.Web import Common_Data as CD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ddt


@ddt.ddt
class PiblishGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        print("=======所有测试用例执行之前，setUpClass整个测试类只执行一次==========")
        cls.driver = webdriver.Chrome()
        # 窗口最大化
        cls.driver.maximize_window()
        cls.driver.get(CD.Boss_login_url)
        cls.lg = LoginPage(cls.driver)
        cls.pp = PG.PublishGood(cls.driver)
        cls.sp = SystemPoint(cls.driver)
        cls.lg.login(LD.Login_data["username"], LD.Login_data["password"])
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.publish_goods))).click()

    def tearDown(cls):
        # 后置
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 发布实物商品，立即上架
    @ddt.data(*PD.EntityGood_data)
    def test_1_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.EntityGood(data["product_title"], data["limit_quantity"], data["product_description"],
                          data["property_1"], data["property_2"], data["purchase_price"], data["sell_price"],
                          data["stock"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        # 断言 在【发布商品】中，存在[提交审核成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), '提交审核成功')

    # 发布实物商品，放入仓库
    @ddt.data(*PD.EntityGood_data)
    def test_2_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.EntityGood(data["product_title"], data["limit_quantity"], data["product_description"],
                          data["property_1"], data["property_2"], data["purchase_price"], data["sell_price"],
                          data["stock"])
        # 放入仓库
        cls.pp.storage(Pubilc.storage)
        # 断言 在【发布商品】中，存在[放入仓库成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "放入仓库成功")

    # 发布本地生活，立即发布
    @ddt.data(*PD.Local_Life_data)
    def test_3_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.Local_Life(data["product_title"], data["total_price"], data["stock"],
                          data["limit_quantity"], data["product_description"])
        # 立即发布
        cls.pp.submit(Pubilc.submit)
        # 断言 在【发布商品】中，存在[提交审核成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "提交审核成功")

    # 发布本地生活，放入仓库
    @ddt.data(*PD.Local_Life_data)
    def test_4_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.Local_Life(data["product_title"], data["total_price"], data["stock"],
                          data["limit_quantity"], data["product_description"])
        # 放入仓库
        cls.pp.storage(Pubilc.storage)
        # 断言 在【发布商品】中，存在[放入仓库成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "放入仓库成功")

    # 发布商企服务，立即发布
    @ddt.data(*PD.Business_Services_data)
    def test_5_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.Business_Services(data["product_title"], data["total_price"], data["subsist"], data["stock"],
                                 data["limit_quantity"], data["product_description"])
        # 立即发布
        cls.pp.submit(Pubilc.submit)
        # 断言 在【发布商品】中，存在[提交审核成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "提交审核成功")

    # 发布商企服务，放入仓库
    @ddt.data(*PD.Business_Services_data)
    def test_6_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.Business_Services(data["product_title"], data["total_price"], data["subsist"], data["stock"],
                                 data["limit_quantity"], data["product_description"])
        # 放入仓库
        cls.pp.storage(Pubilc.storage)
        # 断言 在【发布商品】中，存在[提交审核成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "放入仓库成功")
