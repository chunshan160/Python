# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 14:54
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : test_login.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from Handle.H5.za.MyIndex import MyPage
from TestData import Common_Data as CD
from TestData.H5 import Login_Data as LD
from Handle.H5 import SystemPoint
from Handle.H5.za.Login_page2 import LoginPage
import ddt
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.H5 import My


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 只打开浏览器一次
        print("=======所有测试用例执行之前，setup整个测试类只执行一次==========")
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(CD.H5_Login_url)
        cls.lg = LoginPage(cls.driver)
        cls.sp = SystemPoint(cls.driver)
        cls.mp = MyPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDown整个测试类只执行一次==========")
        cls.driver.quit()

    def tearDown(self):
        # 后置
        self.driver.refresh()

    #异常用例 -手机号格式不对
    @ddt.data(*LD.PhoneError_data)
    def test_1_Login_PhoneError(cls,data):
        # 步骤 输入手机号码：XXX，点击下一步
        cls.lg.PhoneError(data["username"])
        # 断言 登录页面 提示：手机号格式不对
        cls.assertTrue(cls.sp.Login_ErrorMag(),data["check"])


    # 异常用例 -密码不正确
    @ddt.data(*LD.PasswordError_data)
    def test_2_Login_PasswordError(cls,data):
        #步骤 输入手机号码：XXX，点击下一步
        cls.lg.PasswordError(data["username"], data["password"])
        # # 断言 登录页面 提示：手机号格式不对
        cls.assertTrue(cls.sp.Login_ErrorMag(),data["check"])


    # 正常用例 -登录成功
    def test_3_Login_success(self):
        self.driver.get(CD.H5_Login_url)
        # 步骤 输入手机号码：XXX，点击下一步，输入密码：XXX。点击登录
        self.lg.login(LD.Success_data["username"],LD.Success_data["password"])
        #点击【我的】
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((My.myicon))).click()
        # 断言 在[我的]中 - 能否找到 [设置] 这个元素
        self.assertTrue(MyPage(self.driver).isExist_back_ele())

    # # 注册
    # def test_4_Registered(self):
    #     # 步骤，输入未注册过的手机号，点下一步，输入验证码，选择定位和填写邀请人，勾选协议，点完成
    #     self.lg.Registered(LD.Registered_data["username"],LD.Registered_data["code"],
    #                        LD.Registered_data["invite_people"])
    #     # # 断言 登录页面 提示：手机号格式不对
    #     #     cls.assertTrue(cls.sp.Login_ErrorMag(),data["check"])

    # # 找回密码
    # @ddt.data(*LD.RetrievePassword_data)
    # def test_5_RetrievePassword(cls, data):
    #     # 步骤，输入手机号，点击下一步，点击找回密码，输入验证码，输入密码两次，点完成
    #     cls.lg.RetrievePassword(data["username"], data["code"], data["password"])
    #     # 断言   系统提示，存在“密码找回成功字眼”
    #     cls.assertTrue(cls.sp.RetrievePassword_msg(), data["check"])

# if __name__ == '__main__':  # 如果其他的类调用的这个类的时候他就会自动忽略掉这个函数，他是为了测试自身的类用的
#         unittest.main()  # 启动程序
