__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import time

class LoginPage(BasePage):

    #元素定位
    input_phoneNumber_id = "com.xxzb.fenwoo:id/et_phone"
    next_step_id = "com.xxzb.fenwoo:id/btn_next_step"
    input_passwd_id = "com.xxzb.fenwoo:id/et_pwd"
    confirm_button_id = "com.xxzb.fenwoo:id/btn_next_step"
    invalid_phoneNumber_id = "com.xxzb.fenwoo:id/tv_message"
    phoneNumber_or_passwd_error_id = "com.xxzb.fenwoo:id/tv_login_warn"
    verify_shortMessage_toast_xpath = "//*[contains(@text, '验证码已经发送到手机')]"


    #输入手机号
    def input_phoneNumber(self, phoneNumber):
        #等待手机号输入框可见
        #输入手机号
        self.get_element(self.input_phoneNumber_id).send_keys(phoneNumber)
        #点击下一步
        self.get_element(self.next_step_id).click()


    #输入密码
    def input_passwd(self, passwd):
        #等待密码输入框可见
        #输入密码
        self.get_element(self.input_passwd_id).send_keys(passwd)
        #点击确定
        self.get_element(self.confirm_button_id).click()


    #获取无效的手机号提示信息
    def get_invalid_phoneNumber_content(self):
        #等待提示信息可见
        #获取提示信息
        invalid_phoneNumber_content = self.get_element(self.invalid_phoneNumber_id).text
        return invalid_phoneNumber_content


    #获取手机号或密码错误的提示信息
    def get_phoneNumber_or_passwd_error_content(self):
        #等待提示信息可见
        #获取提示内容
        phoneNumber_or_passwd_error_content = self.get_element(self.phoneNumber_or_passwd_error_id).get_attribute("text")
        return phoneNumber_or_passwd_error_content


    #获取验证码的提示信息
    def get_verify_shortMessage_toast_content(self):
        #等待提示信息存在
        #获取提示内容
        verify_shortMessage_toast_content = self.get_toast_content(self.verify_shortMessage_toast_xpath).text
        return verify_shortMessage_toast_content



