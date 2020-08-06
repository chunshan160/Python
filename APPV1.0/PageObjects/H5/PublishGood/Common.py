#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:37
# @Author :春衫
# @File :Common.py

import time
from PageLocators.H5.PubilcGood import Common
from Common.BasePage import BasePage

class PublishGoodCommon(BasePage):

    # 立即上架
    def submit(self):
        time.sleep(0.5)
        self.click_element(Common.submit)

    # 放入仓库
    def storage(self):
        time.sleep(0.5)
        self.click_element(Common.storage)