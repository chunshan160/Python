#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/19 14:15
# @Author :春衫
# @File :第14节_类和实例.py

'''
1、一个完成的闭包需满足哪几个条件？
2、定义一个计算函数运行时间的装饰柒（计算时间使用time模块）

3、编写装饰器，为多个函数加上认证功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''


# import time
#
#
# def wrapper(func):
#     def count_time(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print("函数运行的时间为：{:.5f}".format(end_time - start_time))
#
#     return count_time
#
#
# users = {"user": "ceshi", "pwd": "123", "token": False}
#
#
# def login_check(func):
#     def ado():
#         if not users['token']:
#             print('------登录页面-—----')
#             username = input('账号:')
#             password = input('密码:')
#             # 登录校验
#             if users["user"] == username and users["pwd"] == password:
#                 users['token'] = True  # 修改token值
#                 func()  # 调用被装饰器的函数
#         else:
#             func()  # token值为True直接调用函数
#
#     return ado
#
#
# @login_check
# def index():
#     print('这个是index首页')
#
#
# @login_check
# def page2():
#     print('这个是page2')
#
#
# index()
# page2()
#
#
# @login_check  # count_time ==> func=login_check(func) func==>ado
# @wrapper  # func = wrapper(func) func==>count_time
# def func():
#     time.sleep(3)
#     print('这是是需要被装饰器的函数')
#
#
# func()


# 从下往上装饰 从上往下执行

class MyTest(object):

    def __init__(self):
        self.name="ceshi"

    @classmethod  # 被classmethod装饰了之后，该方法就是一个类方法
    def add(cls):
        print('add')
        print(cls)

    @staticmethod  # 静态方法  实例和类都可以调用
    def static():
        print('这个是静态方法')

    @property #设置只读属性
    def read_attr(self):
        print("这个装饰器装饰完后，该方法可以像属性一样被调用")
        return "18岁"

    def sub(self):  # self代表的是实例本身
        print('sub中的self:', self)


t = MyTest()
# t.read_attr #打印 这个装饰器装饰完后，该方法可以像属性一样被调用
# t.read_attr()#报错 空类型不可调用
print(t.read_attr)
# t.read_attr="19岁"#报错 只读不可更改




# print(t.name)
# t.name="lala"
# print(t.name)



# t.add()
# t.sub()
# MyTest.add()
# MyTest.sub()

#类属性可以被实例调用 类方法可以被实例调用
#类方法可以被类调用，也可以被实例调用
#类调用不了实例方法，类调用不了实例属性

