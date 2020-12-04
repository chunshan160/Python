#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 13:41
# @Author :春衫
# @File :class_05day_01.py

import time


def wrapper(func):
    def count_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("函数运行的时间为：{:.5f}".format(end_time - start_time))

    return count_time


with open('zy/user.txt')as f:
    users = eval(f.read())


def login_check(func):
    """
    登录验证的装饰器
    :param func:type：function
    :return:
    """

    def ado(*args, **kwargs):
        print("登录校验的装饰器")
        if not users["token"]:  # 判断token值是否为False
            print('-----登录页面-----')
            username = input('账号：')
            password = input('密码：')
            # 登录校验
            if users["user"] == username and users["pwd"] == password:
                users["token"] = True  # 修改token值
                func(*args, **kwargs)  # 调用被装饰器的函数
        else:
            func(*args, **kwargs)  # token值为True直接调用函数

    return ado


@login_check  # count_time ==> func = login_check(func)  func ==>ado
@wrapper  # func = wrapper(func)  func ==> count_time
def func():
    time.sleep(3)
    print("这是需要被装饰器的函数")


# 从下往上装饰，从上往下执行
# func()


class MyTest():
    age = 20

    def __init__(self, name):
        self.name = name

    @classmethod  # 被classmethod装饰了之后，该方法就是一个类方法  classmethod只能在类里面调用
    def cls_method(cls):  # cls 代表的是类本身
        print("add中的cls：", cls)
        print("类方法")

    @staticmethod  # 静态方法 实例和类都可以调用
    def static():  # 默认没有参数
        print("静态方法")

    @property  # 设置只读属性
    def read_attr(self):  # Getter 应返回或生成某些内容
        print("这个装饰器装饰完了之后，该方法可以像属性一样被调用")
        return "18岁"

    def self_method(self):  # self 代表实例本身
        print("sub中的self：", self)
        print("实例方法/对象方法")


t = MyTest("chunshan")  # 创建实例t
# t.cls_method()  # <class '__main__.MyTest'>  类
# t.sub()  # <__main__.MyTest object at 0x000002A975582820> 实例对象
# MyTest.sub()#报错 类不能调用实例方法

# 静态方法
# MyTest.static()
# t.static()

# t.read_attr()  # TypeError: 'NoneType' object is not callable
# t.read_attr  # 执行
print(t.read_attr)  # 默认None return啥就是啥 不可更改
# t.read_attr = 17  # AttributeError: can't set attribute

# t.name="ceshi"
# print(t.name)


# print(t.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# print(MyTest.name) # 打印类的name属性
# t.age = 18 # 给实例绑定name属性
# print(t.age) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# print(MyTest.age) # 但是类属性并未消失，用MyTest.name仍然可以访问
# del t.age # 如果删除实例的name属性
# print(t.age) # 再次调用t.age，由于实例的name属性没有找到，类的name属性就显示出来了
#
# # 类属性可以被类、实例调用
# print(MyTest.age)
# print(t.age)
#
# # 类方法可以被类、实例调用
# MyTest.cls_method()
# t.cls_method()
#
# # 实例属性不可以被类调用
# t.score = 90
# # MyTest.score  # 报错
#
# # 实例方法不可以被类调用
# MyTest.self_method()  # TypeError: add() missing 1 required positional argument: 'self'
# t.self_method()  # 实例方法可以被实例调用
