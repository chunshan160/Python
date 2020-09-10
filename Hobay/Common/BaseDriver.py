#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 22:55
# @Author :春衫
# @File :BaseDriver.py

import yaml
from appium import webdriver
from Common.project_path import caps_dir


class BaseDriver:

    def base_driver(self, device, automationName="appium", noReset=True,unicodekeyboard=True,resetkeyboard=True):
        fs = open(caps_dir, encoding="utf-8")
        datas = yaml.load(fs,Loader=yaml.FullLoader)
        for i in datas:
            if device == i["deviceDesc"]:
                if automationName != "appium":
                    i["desired_caps"]["automationName"] = automationName
                if noReset == False:
                    i["desired_caps"]["noReset"] = False
                if unicodekeyboard == False:
                    i["desired_caps"]["unicodekeyboard"] = False
                if resetkeyboard == False:
                    i["desired_caps"]["resetkeyboard"] = False
                desired_caps = i["desired_caps"]
                driver = webdriver.Remote("http://{0}:{1}/wd/hub".format(i["server_url"], i["server_port"]),
                                          desired_caps)
                return driver

if __name__ == '__main__':
    pass