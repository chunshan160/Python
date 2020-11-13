#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/24 17:07
# @Author :春衫
# @File :ceshi.py

import requests

url="http://env.hobay.com.cn/zentao/www/index.php?m=bug&f=browse&productID=47&branch=0&browseType=unclosed&param=0&orderBy=&recTotal=90&recPerPage=20&pageID=1&productid=47"

res=requests.get(url)
print(res.json())