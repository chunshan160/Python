#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/6/22 12:46
#@Author :春衫
#@File :get_js.py

import execjs


# 执行本地的js

def get_js(a,b):
    f = open("../des2.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    password=ctx.call(a, b)
    return password