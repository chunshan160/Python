#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/20 22:29
# @Author :春衫
# @File :123.py

import requests
import json

data = {
 'a': 123,
 'b': 456
}
headers = {'Content-Type': 'application/json'} ## headers中添加上content-type这个参数，指定为json格式
response = requests.post(url='url', headers=headers, data=json.dumps(data)) ## post的时候，将data字典形式的参数用json包转换成json格式。
