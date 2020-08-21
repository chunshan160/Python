#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:43
#@Author :春衫
#@File :UploadImage.py

import time
# from pywinauto.application import Application
from Common.project_path import *
from Common.find_element import FindElement
from PageLocators.H5.PubilcGood import EntityGood as EG

class UploadImage(object):

    def __init__(self, driver):
        self.driver=driver
        self.find_element=FindElement(driver)

    def upload_main_image(self):
        # 点击上传图片
        self.find_element.find_element(EG.product_image).click()
        time.sleep(1)
        self.find_element.find_element(EG.upload_image).send_keys(image_path)
        time.sleep(1)
        os.system(upload_image)


    def upload_description_image(self):
        # 点击上传图片
        self.find_element.find_element(EG.product_description_image).click()
        time.sleep(1)
        self.find_element.find_element(EG.upload_image).send_keys(image_path)
        time.sleep(1)
        os.system(upload_image)

    def upload_specification_image(self):
        # 点击上传图片
        self.find_element.find_element(EG.specification_image).click()
        time.sleep(1)
        self.find_element.find_element(EG.upload_image).send_keys(image_path)
        time.sleep(1)
        os.system(upload_image)