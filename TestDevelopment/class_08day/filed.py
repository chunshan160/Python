#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/18 14:12
# @Author :春衫
# @File :filed.py

# 字段的父类
class BaseFiled(object):
    pass


class CharFiled(BaseFiled):

    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError("字符串长度在{}以内".format(self.max_lenght))
        else:
            raise TypeError("need a str")

    def __delete__(self, instance):
        self.value = None


class IntFiled(BaseFiled):

    # def __init__(self, max_lenght=20):
    #     self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("need a int")

    def __delete__(self, instance):
        self.value = None


class BoolFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise ValueError

    def __delete__(self, instance):
        self.value = None
