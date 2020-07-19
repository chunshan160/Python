#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/8 20:32
#@Author :春衫
#@File :ceshi.py
import datetime
from selenium.webdriver.common.by import By

name = (By.XPATH, '//input[@type="number"]')
print(name[0])