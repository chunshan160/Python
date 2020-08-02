__author__ = '小翟'

import yaml
from appium import webdriver

class BaseDriver:


    def base_driver(self, device, automationName="appium", noReset=True):
        fs = open(r"D:\Program\Jenkins\workspace\APP_AutoTest\appium_AutoTest\Caps\Caps.yaml", encoding="utf-8")
        datas = yaml.load(fs)
        for i in datas:
            if device == i["deviceDesc"]:
                if automationName != "appium":
                    i["desired_caps"]["automationName"] = automationName
                if noReset == False:
                    i["desired_caps"]["noReset"] = False
                desired_caps = i["desired_caps"]
                driver = webdriver.Remote("http://{0}:{1}/wd/hub".format(i["server_url"], i["server_port"]), desired_caps)
                return driver

