#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/18 14:02
# @Author :春衫
# @File :class_08day_model_orm.py

from class_08day.filed import BaseFiled, BoolFiled, CharFiled, IntFiled


# 利用元类实现模型类
class FieldMetaClass(type):
    """模型类的元类"""

    def __new__(cls, name, bases, dic, *args, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, dic)
        else:
            table_name = name.lower()  # 将类名转换成小写，对应数据表的名称
            fields = {}  # 定义一个空字典，用来存放模型类字段和数据表中字段对应的关系
            for k, v in dic.items():  # 遍历所有的属性
                if isinstance(v, BaseFiled):  # 判断属性值是否为字段类型的
                    fields[k] = v

            dic["t_name"] = table_name
            dic["fields"] = fields

            return super().__new__(cls, name, bases, dic)


class BaseModel(metaclass=FieldMetaClass):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)  # 遍历出来所有关键字参数，并且对对象进行属性设置

    def save(self):
        # 保存一条数据，生成一条对应的SQL语句
        # 获取表名
        t_name = self.t_name
        # 获取字段名称
        fields = self.fields

        field_dict = {}  # 创建一个字典用来存储键值对
        # 获取对应字段的值
        for field in fields.keys():
            field_dict[field] = getattr(self, field)

        # 生成对应的SQL语句
        sql = "INSERT INTO {} VALUES{};".format(t_name, tuple(field_dict.values()))
        print(sql)

class User(BaseModel):
    """用户模型类"""
    username = CharFiled()
    pwd = CharFiled()
    age = IntFiled()
    live = BoolFiled()


class Order(BaseModel):
    """订单模型类"""
    id = IntFiled()
    money = IntFiled()


xiaoming = User(username="小明", age=18, pwd="123", live=True)

xiaoming.save()

# order1 = Order(id=111, money=222)
# print(xiaoming.username)
# print(order1.id)
