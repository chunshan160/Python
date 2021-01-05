#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 11:27
# @Author :春衫
# @File :zy_11day.py

"""
生产者消费者模式
1、用一个队列来存储商品
2、创建一个专门生产商品的线程类，当商品数量少于50时，开始生产商品，每次生产200个商品，每生产一轮暂停1秒
3、创建一个专门消费商品的线程类，当商品数量大于10时，就开始消费，循环消费，每次消费3个，当商品数量少于10的时候，暂停2秒

创建一个线程生产商品
5个线程消费商品

"""
import time
from queue import Queue
from threading import Thread

q = Queue()


# 队列里面存储商品

# 生产者和消费者模式
class Producer(Thread):
    """生产者"""

    def run(self):
        # 判断队列中的商品数是否少于50，少于50了之后就生产200个
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(200):
                    count += 1
                    goods = "---第{}个商品---".format(count)
                    q.put(goods)
                    print("生产：", goods)
                time.sleep(1)


class Consumer(Thread):
    """消费者"""

    def run(self):
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    print("消费：{}".format(q.get()))
            else:
                time.sleep(2)


p = Producer()
p.start()

# 创建五个消费者线程
for i in range(5):
    c = Consumer()
    c.start()
