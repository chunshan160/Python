#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   :2019/12/27 16:55
# @Author :春衫
# @Email  :1605936478@qq.com
# @File   :systempoint_page.py


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_dev1.PageLocators.BOSS.PublishGoods import Pubilc


# 系统提示页面，主要是为了断言用
class SystemPoint:

    def __init__(self, driver):
        self.driver = driver

    # 为了判断登录成功，去看发布商品，有没有【下一步】这个元素
    def Perfection(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((Pubilc.next)))
            return True
        except:
            return False

    # 获取系统提示信息 ----登录区域
    def Success_Msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Pubilc.success_msg)))
        return self.driver.find_element(*Pubilc.success_msg).text
