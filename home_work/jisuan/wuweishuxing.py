#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/29 12:59
# @Author :春衫
# @File :wuweishuxing.py

#敏
def Sensitive(value):
    #initial_general_attack_coefficient 初始普攻系数
    igac=0.55
    #initial_general_attack_speed 初始攻击速度
    igas=2.5
    #general_attack_hurt
    gah=value*igac*igas*1.3
    print(gah)
Sensitive(713)


b=0.0275*713
print(b)



# import random
#
# s=0
# for i in range(1,101):
#     a=random.randint(1,100)
#     if a<58:
#         s=s+1
#
# print(s)