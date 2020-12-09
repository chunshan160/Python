#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/6 12:41
# @Author :春衫
# @File :第11节_常用内置函数.py

# 2.2、python中的内置函数
# 内置函数: https://docs.python.org/zh-cn/3.7/library/functions.html
# 常用的内置函数
# map函数:会根据提供的函数对指定序列做映射。
# filter函数:函数用于过滤序列。
# zip函数:函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组

# 内置函数
# filter:过滤函数 第一参数是函数 第二参数是可迭代对象
# def fun(n):
#     return n<10
# li = [1,1,2,122,331,11,22,33,4,6,7,2,88,31]
# res = filter(fun, li)
# print(list(res))
#
# li2=iter(li)
# li3=(i for i in range(5))

# print(isinstance(li,Iterable))
# print(isinstance(li2,Iterable))
# print(isinstance(li2,Iterable))

# map：将可迭代对象中的数据迭代出来，一个一个传到函数中去调用，将返回结果放到新的对象中
# res2=map(fun,li)
# print(list(res2))

# 假如return的条件是 n<10 那么filter就会返回满足条件的结构 map返回True False
# 假如return的条件是 n*10 那么filter就不过滤，返回原本的list  map则是返回运算后的结果

# zip 打包
# res3 = zip([1, 2, 3], [3, 4, 5])
# print(list(res3))  # [(1, 3), (2, 4), (3, 5)] 元组省内存
# 如果打包列表元素数量不一致，多的就会抛弃

# dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
# print(list(dict1.items()))

# 匿名函数 lambda
# def function(a, b):
#     return a + b


# 匿名函数适用场景  简单的函数定义（只有一个表达式） 参数：返回值
# res=lambda a, b: a + b
# res2=(lambda a, b: a + b)(11,22)
# print(res(11, 22))
# print(res2)

# li = [1, 2, 122, 331, 11, 22, 33, 4, 6, 7, 2, 88, 31]
# res2 = filter(lambda x: x < 10, li)
# print(list(res2))

# li2 = [(lambda x: x % 5 == 0)(i) for i in range(10)]
# print(li2)

# 三目运算符
# a=100
# print(100) if a >100 else print(22)


# 四、偏函数

# 问题一:什么是偏函数?
# 在Python的内置模块functoo1s提供了很多有用的功能，其中一个就是偏函数（partial ).

# 问题二:偏函数有什么用?
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# 偏函数应用案列
# #在我们之前学到的内置函数中filter中，调用的时候需要传入两个参数，第一个是函数，第二个是我们需要过滤的可迭代类型的数据，

# 我们可以通过传入不同的过滤条件去过滤出来我们需要的数据。
li1 = [1, 1, 2, 122, 331, 11, 22, 33, 4, 6, 7, 2, 88, 31]
filter(lambda x: x > 3, li1)
filter(lambda x: x > 10, li1)

# 要获取数据中大于5的数据
li1 = [1, 2, 3, 11, 22, 33]
li2 = [2, 3, 4, 22, 33]
li3 = [3, 4, 5, 33, 44, 55]
# ... 一直加

# 之前的写法
filter(lambda x: x > 5, li1)
filter(lambda x: x > 5, li2)
filter(lambda x: x > 5, li3)


# ... 一直加

# 那么这个时候我们是不是每次都要传入同样的参数，是不是比较麻烦，有没有更简单的方法
# 这个时候我们可以选择自定义一个函数，在函数中调用filter这个函数，在这个时候将过滤条件的参数提前传进去
# 那么接下来我们按这个要求进行过滤的时候就可以之间调用自定义的filter2函数了。
def filter2(iter):
    return filter(lambda x: x > 5, iter)


res=filter2(li1)
res2=filter2(li2)
print(list(res))
# 这样的话我们在调用过滤函数实现过滤操作的时候更加简单方便
# 那么上面定义filter2的这种，减少调用参数的方式，就可以用到我们刚刚提到的偏函数来做了

# 通过偏函数创建一个新函数，提前传入原函数所需要的参数，让我们在调用的时候更加简单。
filter3 = partial(filter, lambda x: x > 5)
print(list(filter3(li1)))

# 练习题:rosted默认是升序排序，通过偏函数，创建一个默认是降序排序的函数
