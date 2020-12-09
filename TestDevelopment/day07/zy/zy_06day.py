#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/9 13:34
# @Author :春衫
# @File :zy_06day.py

import pymysql


# 1、实现一个操作mysql的上下文管理器（可以自动断开链接）
class DB:
    # 数据库操作的上下文管理器

    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


DATABASES_CONF = dict(
    host="localhost",
    user="root",
    password="mysql",
    database="test",
    port=3306,
    charset="utf8")

with DB(DATABASES_CONF) as cur:
    cur.execute("SELECT * FROM students")
    print(cur.fetchone())


# 2、描述__slots__属性的作用，并修改读取Excel类中保存用例的类
# 2.1、限制对象属性，指定的slots的属性
# 2.2、节约内存

# 保存用例的
class Case:
    __slots__ = ["case_id", "title", "url", "data", "excepted"]

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.excepted = None


"""
3、面向对象的三大特征是什么?多态又是什么?

特征:封装、继承、多态
多态:指的是一类事物有多种形态，一个抽象类有多个子类，
不同的子类对象调用相同的方法，产生不同的执行结果,

4、私有属性怎么定义，不同的定义方式有什么区别?

单下划线、双下划线开头
单下划线开头的，对外是公开的，可以直接访问
双下划线开头的，对外不能直接访问，为了保护这个变量(对外改了一个名字) ,
在原有的属性名前面加了一个_类名
"""
