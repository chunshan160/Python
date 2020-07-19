#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/6 17:19
# @Author :春衫
# @File :test_publish_sc.py

from selenium import webdriver
from Handle.BOSS import LoginPage, PublishGoods_page as PG
from Handle.ERP import LoginPage as lp
from TestData.BOSS import Login_Data as LD
from TestData.ERP import Login
from TestData.BOSS import Publish_SC_Data as PD
from Handle.BOSS.SystemPoint_page import SystemPoint
from Handle.BOSS import ShangChao
from Handle.ERP import Check
from PageLocators.BOSS.PublishGoods import Pubilc
import unittest
from TestData import Common_Data as CD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ddt
from Handle.ERP import Check as ck


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
        cls.lp = lp(cls.driver)
        cls.pp = PG.PublishGood(cls.driver)
        cls.sp = SystemPoint(cls.driver)
        cls.ShangChao = ShangChao(cls.driver)
        cls.ck = ck(cls.driver)
        cls.Ck = Check(cls.driver)
        cls.lg.login(LD.Login_data["username"], LD.Login_data["password"])
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.publish_goods))).click()

    def tearDown(cls):
        # 后置
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 需要仓主审核的商超，发布全新商超商品，立即上架
    @ddt.data(*PD.EntityGood_1_data)
    def test_1_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.EntityGood_SC(data["product_title"], data["limit_quantity"], data["product_description"],
                             data["property_1"], data["property_2"], data["purchase_price"], data["sell_price"],
                             data["stock"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        # 断言 在【发布商品】中，存在[提交审核成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), '提交审核成功')

    # 需要仓主审核的商超，发布全新商超商品，放入仓库
    @ddt.data(*PD.EntityGood_2_data)
    def test_2_EntityGood_submit(cls, data):
        # 点击发布实物商品
        cls.pp.EntityGood_SC(data["product_title"], data["limit_quantity"], data["product_description"],
                             data["property_1"], data["property_2"], data["purchase_price"], data["sell_price"],
                             data["stock"])
        # 放入仓库
        cls.pp.storage(Pubilc.storage)
        # 断言 在【发布商品】中，存在[放入仓库成功] 这个元素   对比一样就ok，不一样就报错
        cls.assertTrue(cls.sp.Success_Msg(), "放入仓库成功")

    # # 整理审核状态
    # @ddt.data(*GoodCheck.Search_Phone_data)
    # def test_3_EntityGood(cls, data):
    #     # 退出账号
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((sc.logout))).click()
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((sc.queding))).click()
    #     cls.lg.login(LD.Boss_Login_data["username"], LD.Boss_Login_data["password"])
    #     # Boss仓主商品入仓审核
    #     cls.ShangChao.sc()
    #     # ERP登录
        cls.driver.get(CD.ERP_login_url)
        cls.lp.login(Login.ERP_Login_data["username"], Login.ERP_Login_data["password"])
    #     # 商品中心----商品审核
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.goods_center))).click()
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.good_check))).click()
    #     # 点击卖家手机搜索框，输入卖家手机
    #     cls.ck.Search_Pnone(data["phone"])
    #     # 点击查询
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.search))).click()
    #     time.sleep(1)
    #     # 审核商品
    #     # WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_chutd))).click()
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_chutt))).click()
    #     cls.Ck.Check_Pass()
    #     time.sleep(1)
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_djj))).click()
    #     cls.Ck.Check_Refuse(data["refuse_reason"])
    #     time.sleep(1)
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_ctd))).click()
    #     cls.Ck.Check_Pass()
    #     time.sleep(1)
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_ctt))).click()
    #     cls.Ck.Check_Pass()
    #     time.sleep(1)
    #     WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((CK.check_cwj))).click()
    #     cls.Ck.Check_Refuse(data["refuse_reason"])
    #     #回到成员boss后台继续调整
    #     cls.driver.get(CD.Boss_login_url)
    #     cls.lg.login(LD.Login_data["username"], LD.Login_data["password"])
    #     #
