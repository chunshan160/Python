#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/5/27 17:05
#@Author :春衫
#@File :do_regx.py

import re
from tools.get_data import GetData

class DoRegx:


    def do_regx(self,data):

        while re.search('\$\{(.*?)\}',data):

            key=re.search('\$\{(.*?)\}',data).group(0)
            value=re.search('\$\{(.*?)\}',data).group(1)
            data=data.replace(key,str(getattr(GetData,value)))

        return data

if __name__ == '__main__':
    s = '{"mobilephone": "${normal_tel}", "pwd": "123456"}'
    res=DoRegx().do_regx(s)
    print(res)