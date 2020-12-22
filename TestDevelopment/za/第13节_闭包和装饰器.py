#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/7 14:58
# @Author :春衫
# @File :第13节_闭包和装饰器.py

# 闭包
# def func():
#     print('----func被调用-—-----------')
#
#     def count_book():
#         print('这个是计算买书方式的函数')
#
#     return count_book

# #方法一：
# func()()
#
# #方法二：
# res = func( )
# res()


# 满足三个闭包条件:
# 条件一:函数中嵌套函数
# 条件二:外层函数返回内层嵌套函数名
# 条件三:内层嵌套函数有引用外层的一个非全局变量

# 作用：实现数据的锁定 提高稳定性


# 二、装饰器
# 讲装饰器之前我们先来了解一下开放封闭原则(面向对象原则的核心)
# 开放封闭原则:软件实体应该是可扩展，而不可修改的。也就是说，对扩展是开放的，而对修改是封闭的。
# 装饰器的作用∶在不更改原功能函数内部代码，并且不改变调用方法的情况下为原函数添加新的功能。
# 装饰器的应用场景:
# 1.登录验证
# 2.函数运行时间统计
# 3.执行函数之前做准备工作
# 4.执行函教后清理功能
# 5.1、实现一个装饰器
# 在上面的过程中其实我们已经完成了一个装饰器定义并应用，只是现在的语法并不是按照整个的装饰器来写的，装饰器之要在上面的基础稍加改动一点点就可以了

# def func_a(fun):
#     print('------func_a--调用了---')
#
#     def func_w():
#         print('----先洗手-')
#         fun()
#
#     return func_w


# 开放封闭原则
# def login(func):
#     def fun():
#         username = "ceshi"
#         password = "qaz123"
#         user = input('请输入账号：')
#         pw = input('请输入密码：')
#         if username == user and pw == password:
#             func()
#         else:
#             print('账号或者密码错误')
#
#     return fun
#
#
# @login  # @login :语法糖 -->index = login(index)  把函数index传给login执行 执行完后把结果返回给index接收
# def index():
#     print("这是网站的首页")

# index.__closure__
# index()

# 装饰器原理阐述:将被装饰的函数当做一个参数传到装饰器中，并且让被装饰的函数名指向装饰器内部的函数，在
# 装饰器的内部函数中用接收到的参数再调用被装饰的函数。
# 5.2、有参数的装饰器

def add(func):
    def fun(a, b):
        print('相乘:', a * b)
        print('相除:', a / b)
        func(a, b)
        print('相减:', a - b)

    return fun


@add
def add_num(a, b):
    # 打印两个数相加
    print('相加:', a + b)


add_num(11, 22)


# 执行步骤：
# 首先，@add 指向add()返回回来的内层函数fun()
# 因为add_num()传了两个参数，但是fun()不需要参数，所以就会报错，提示不需要参数但是传了两个 所以fun()需要加上两个参数才不会报错
# 到了func()这步，func()调用函数add_num()，运行就会提示缺少参数，所以也得加上两个参数

# 5.3、通用装饰器
# 如果同一个装饰器既要装饰有参数的函数，又要装饰无参数的函数，那么我们在传参的时候就设置成不定长参数,
# 这样不管被装饰的函数有没有参数都能用。

# def add(func):
#     def fun(*args, **kwargs):#*args 元祖 **kwargs 字典
#         func(*args, **kwargs)#这里的* ** 是拆包
#
#     return fun


# 装饰器装饰类
# 使用类装饰器的时候，记得要返回被装饰的类调用的结果

# def add(func):
#     def fun(*args, **kwargs):
#         print('装饰器的功能代码:登录')
#         return func(*args, **kwargs)  # 装饰类必须要加return 装饰函数就不用
#
#     return fun
#
#
# @add  # MyClass= add(MyClass)
# class MyClass:
#     def __init__(self, name, age):
#         print(name)
#         print(age)
#
#
# m = MyClass("ceshi", "18")
# print('m的值', m)
