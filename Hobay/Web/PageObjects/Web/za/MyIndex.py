# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 16:02
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : my_page.py
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.PageLocators import My

#判断【我的】页面是否存在【设置】，有的话可以判断登录成功
class MyPage:

    def __init__(self,driver):
        self.driver = driver

    def isExist_back_ele(self):
        # 等待10秒 元素有没有出现 //div[@class="back-icon"]
        # 如果[设置]存在就返回True，如果不存在，就返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((My.setup)))
            return True
        except:
            return False

