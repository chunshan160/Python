#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/3 15:49
#@Author :春衫
#@File :BuyGood_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.H5.BuyGoods import BuyGoods as BG

class BuyGoods:

    def __init__(self, driver):
        self.driver = driver

    #购买商品-易贝支付
    def BugGoods1(self):
        #点击加入易购车
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.cart))).click()
        #数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        #选择支付方式
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        #确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    #支付按键
    def PayPassword(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()


    #购买商品-易贝券支付
    def BugGoods2(self):
        #点击加入易购车
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.cart))).click()
        #数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        #点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        #选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.yibeiquan))).click()
        #确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    #购买商品-抵工资支付
    def BugGoods3(self):
        #点击加入易购车
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.cart))).click()
        #数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        #点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        #选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.digongzi))).click()
        #确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()


    #购买商品-家人购支付
    def BugGoods4(self):
        #点击加入易购车
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.cart))).click()
        #数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        #点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        #选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.jiarengou))).click()
        #确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()


    #购买商品-现金账户支付
    def BugGoods5(self):
        #点击加入易购车
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.cart))).click()
        #数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        #确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        #提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        #点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        #选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xianjinzhanghu))).click()
        #确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()