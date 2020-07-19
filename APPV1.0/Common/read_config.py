#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 22:24
# @Author :春衫
# @File :read_config.py

import configparser


class ReadConfig:

    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf[section][option]


if __name__ == '__main__':
    from Common.project_path import *

    res = ReadConfig().read_config(case_config_path, 'MODE', 'mode')
    print(res)
