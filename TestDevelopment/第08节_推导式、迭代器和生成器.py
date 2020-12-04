#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/29 22:29
# @Author :春衫
# @File :第08节_推导式、迭代器和生成器.py


# urls=[]
#
# for i in range(1,101):
#     url='page{}'.format(i)
#     urls.append(url)
# print(urls)

# 列表推导式
# urls1 = ['page{}'.format(i) for i in range(1, 101)]
# print(urls1)

# 字典推导式
# dic1 = {i: i + 1 for i in range(10)}
# print(dic1)

# () 生成器表达式
tu = (i for i in range(10))
# print(tu)#<generator object <genexpr> at 0x000002036604B9E0>
# a = next(tu)


# print(a)
# print(next(tu))

# 通过yield自定生成器
# def gen_fun():
#     yield 100  # 不会立即执行函数
#     print(' hell python ')
#     yield 1000
#     yield 10000
#
#
# res = gen_fun()  # 返回一个生成器
# print(next(res))  # 100
# print(next(res))  # 100 hell python 1000


#可迭代对象 可以for循环遍历的都是可迭代对象 内部 只实现了__iter__方法
li=[1,2,3,4]
#可以用next取值的才是迭代器
#print(next(li))#TypeError: 'list' object is not an iterator

#把可迭代对象转换成迭代器
li1=iter(li)#iter()  __iter__

#迭代器 内部 实现了__iter__之外 还实现了__next__
# print(next(li1))#1

#生成器  是迭代器的一种 __iter__之外 还实现了__next__

#生成器相比迭代器 多了几种方法 send() close() throw()
# send()方法:发送数据
# close方法:关闭生成器
# throw方法:
# gen.throw(Exception, "Method throw called!")

#生成器<迭代器<可迭代对象  参考理解：子类父类 子类有自己的方法
# tu.send()#与生成器进行交互


def gen():
    for i in range(1,5):
        print('-------------------')
        se = yield i
        print('se的值：',se)

g=gen()#生成器
# print(next(g))#1
# print(g.send(100))#1 100 2
# print(next(g))#1 100 2 None 3

#第一次next运行 只运行到yield（停止/暂停） 所以打印出来的是  --1-- 和1
#第二次next运行 继续运行 所以会打印出 se的值： None  然后从头开始 打印出--1-- 和2 停止/暂停

#close:关闭生成器
# g.close()
# print(next(g))

#throw:在生成器内部主动引发一个异常 参数：异常类型 异常信息
g.throw(ValueError,'hello python')