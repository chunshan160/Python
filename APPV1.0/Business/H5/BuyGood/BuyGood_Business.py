#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 15:49
# @Author :春衫
# @File :BuyGood.py



class BuyGoods:

    def __init__(self, driver):
        self.driver = driver

    # 购买商品
    def buy_entity_good(self,payment_method):
        time.sleep(3)
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(4)
        # 数量+1
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((BG.add))).click()
        time.sleep(1)
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        time.sleep(3)
        # 提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        time.sleep(2)

        if payment_method !="易贝":
            # 点击更换支付方式
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
            time.sleep(3)

            if payment_method =="易贝券":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.yibeiquan))).click()


            elif payment_method =="抵工资":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.digongzi))).click()


            elif payment_method == "家人购":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.jiarengou))).click()


            elif payment_method == "现金":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xianjinzhanghu))).click()
        time.sleep(3)
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        time.sleep(3)
        self.pay()


