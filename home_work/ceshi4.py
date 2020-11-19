#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/11/19 16:47
# @Author :春衫
# @File :ceshi4.py

phone = input('请输入一个字符串：')


def validate_phone(phone):

    a="False"

    if phone in ' ':
        print('手机号码不合法，字符串中不能包含空格')
    else:
        if len(phone) != 11:
            print('手机号码不合法，手机号为十一位')
        else:
            if not phone.isdigit():
                print('手机号码不合法，手机号必须全是数字')
            else:
                if phone[0] != "1":
                    print('手机号码不合法，手机号必须为数字1开头')
                else:
                    if phone.count('8') > 4 or phone.count('6') > 4:
                        print('手机号码合法，VIP客户')
                    else:
                        print('手机号码合法，不是VIP客户')
                    a="True"

    return a
fjx = validate_phone(phone)
print(fjx)
