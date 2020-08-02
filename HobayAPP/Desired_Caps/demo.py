#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/2 15:15
# @Author :春衫
# @File :demo.py

import yaml

# 打开yaml文件
fs = open("demo.yaml")
# 2\转换成python对象
res = yaml.load(fs,Loader=yaml.FullLoader)
print(res)
