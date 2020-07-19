#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/4/14 22:55
#@Author :春衫
#@File :project_path.py

import os

'''专门来读取路径的值'''
project_path=os.path.realpath(__file__)
project_path2=os.path.split(os.path.realpath(__file__))[0]
project_path3=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)
print(project_path2)
print(project_path3)

