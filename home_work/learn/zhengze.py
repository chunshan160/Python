#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/25 15:05
# @Author :春衫
# @File :zhengze.py

import re
from API_AUTO.tools.get_data import GetData

# 正则表达式
# 元字符
'''
. 任意单个字符
/d 任意单个数字
[0-9] 等价0-9
[a-z/A-Z] 等价所有的大小写字母
'''

# 限定符
'''
+ 匹配至少大于1次
？ 匹配0次或1次
* 匹配0次或多次  贪婪匹配
{n},{n,m} 匹配限定次数
'''

# s = 'www.baidu.com'  # 目标字符
# res = re.match('(w)(ww)', s)  # 全匹配  头部匹配
# print(res.group(0))  # group()==group(0) 分组 根据你正则表达式里的括号区分组
#group(0) www  group(1) w group(2) ww

# s='lalaqwerope'
# res=re.findall('(la)(qwer)',s)#列表  在字符串里面找 匹配的内容 存在列表里面
# #如果有分组 就是以元组的形式表现出来
# print(res)

# search函数:扫描整个字符串 并返回第一个成功的值，函数会在字符串内查找模式
# 匹配,只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None。


s='{"mobilephone": "${normal_tel}", "pwd": "123456"}'
res=re.search('\$\{(.*?)\}',s)
key=res.group(0)#${normal_tel}
value=res.group(1)#normal_tel
print(key,value)
new_s=s.replace(key,str(getattr(GetData,value)))
print(key,value)
print(new_s)