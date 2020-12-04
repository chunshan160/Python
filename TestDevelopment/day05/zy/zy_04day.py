#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 10:34
# @Author :春衫
# @File :zy_04day.py


# 1、一个完整的闭包必须满足那几个条件？
#     1、条件一:函数中嵌套函数
#     2、条件二:外层函数返回内层嵌套函数名
#     3、条件三:内层嵌套函数有引用外层的一个非全局变量

# 2、定义一个计算函数运行时间的装饰器（计算时间使用time模块实现）
# import time
# def wrapper(func):
#     def count_time(*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         end_time=time.time()
#         print("函数运行的时间为：{:.5f}".format(end_time-start_time))
#     return count_time

# 3、编写装饰器，为多个函数加上认证功能（用户的账户密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
with open('user.txt')as f:
    users = eval(f.read())


def login_check(func):
    """
    登录验证的装饰器
    :param func:type：function
    :return:
    """
    def ado():
        if not users["token"]:  # 判断token值是否为False
            print('-----登录页面-----')
            username = input('账号：')
            password = input('密码：')
            # 登录校验
            if users["user"] == username and users["pwd"] == password:
                users["token"] = True  # 修改token值
                func()  # 调用被装饰器的函数
        else:
            func()  # token值为True直接调用函数
    return ado


@login_check
def index():
    print("这个是index首页")

@login_check
def page1():
    print("页面1")


if __name__ == '__main__':
    index()
    page1()