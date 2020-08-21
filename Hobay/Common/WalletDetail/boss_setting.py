#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/22 12:59
# @Author :春衫
# @File :boss_setting.py
import time
from Handle.BOSS.Boss_Login_page import Boss_LoginPage
from PageLocators.BOSS.yunyin import YunYin
from selenium import webdriver
from Common.DoMysql.sql import SQL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.BOSS.SC import SC as sc

class BossSetting:

    def __init__(self,driver):
        self.driver=driver

    def boss_operational_setting(self,operational_setting,):

        time.sleep(0.5)

        if operational_setting == "未设置":
            xiaoshou = "0"
            yewuhuanshang = "0"
            TCO = "0"
        else:
            xiaoshou = str(operational_setting['销售'])
            yewuhuanshang = str(operational_setting['业务焕商'])
            TCO = str(operational_setting['TCO'])

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.yunyin))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((YunYin.fencheng))).click()
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.yewuhaunshang))).clear()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.yewuhaunshang))).send_keys(
            yewuhuanshang)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.xiaoshou))).clear()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.xiaoshou))).send_keys(xiaoshou)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.tco))).clear()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.tco))).send_keys(TCO)
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((YunYin.save))).click()

        time.sleep(1)

        #退出账号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((sc.logout))).click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((sc.queding))).click()
        time.sleep(0.5)

    def main(self,ip,payment_method,superior,operational_setting):

        if payment_method in ["易贝", "易贝券"]:

            operational_setting_province_id = superior[1]["省代理商"]
            operational_setting_province_data = operational_setting["省代理商"]

            operational_setting_city_id = superior[1]["市代理商"]
            operational_setting_city_data = operational_setting["市代理商"]

            operational_setting_area_id = superior[1]["区代理商"]
            operational_setting_area_data = operational_setting["区代理商"]

            if operational_setting_province_id != None:
                phone = SQL(ip).user_phone(operational_setting_province_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(operational_setting_province_data)

            if operational_setting_city_id != None:
                phone = SQL(ip).user_phone(operational_setting_city_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(operational_setting_city_data)

            if operational_setting_area_id != None:
                phone = SQL(ip).user_phone(operational_setting_area_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(operational_setting_area_data)
        else:

            reserve_fund_superior_province_id = superior["储备池分佣"][1]["省代理商"]
            reserve_fund_operational_setting_province_data = operational_setting["储备池分佣"]["省代理商"]

            reserve_fund_superior_city_id = superior["储备池分佣"][1]["市代理商"]
            reserve_fund_operational_setting_city_data = operational_setting["储备池分佣"]["市代理商"]

            reserve_fund_superior_area_id = superior["储备池分佣"][1]["区代理商"]
            reserve_fund_operational_setting_area_data = operational_setting["储备池分佣"]["区代理商"]

            if reserve_fund_superior_province_id != None:
                phone = SQL(ip).user_phone(reserve_fund_superior_province_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(reserve_fund_operational_setting_province_data)

            if reserve_fund_superior_city_id != None:
                phone = SQL(ip).user_phone(reserve_fund_superior_city_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(reserve_fund_operational_setting_city_data)

            if reserve_fund_superior_area_id != None:
                phone = SQL(ip).user_phone(reserve_fund_superior_area_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(reserve_fund_operational_setting_area_data)

            service_fee_superior_province_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_province_data = operational_setting["支付服务费分佣"]["省代理商"]

            service_fee_superior_city_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_city_data = operational_setting["支付服务费分佣"]["省代理商"]

            service_fee_superior_area_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_area_data = operational_setting["支付服务费分佣"]["省代理商"]

            if service_fee_superior_province_id != None:
                phone = SQL(ip).user_phone(service_fee_superior_province_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(service_fee_operational_setting_province_data)

            if service_fee_superior_city_id != None:
                phone = SQL(ip).user_phone(service_fee_superior_city_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(service_fee_operational_setting_city_data)

            if service_fee_superior_area_id != None:
                phone = SQL(ip).user_phone(service_fee_superior_area_id)
                Boss_LoginPage(self.driver).login(phone, "qaz123")
                self.boss_operational_setting(service_fee_operational_setting_area_data)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = "192.168.0.101"
    operational_setting = {'省代理商': {'销售': 0.3, '业务焕商': 0, 'TCO': 0.3}, '市代理商': '未设置', '区代理商': '未设置'}
    superior = [{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]
    # 窗口最大化
    driver.maximize_window()
    phone = SQL(ip).user_phone(superior[1]["市代理商"])
    BossSetting(driver).boss_operational_setting(operational_setting["市代理商"])
