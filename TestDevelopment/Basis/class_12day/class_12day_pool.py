#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 15:52
# @Author :春衫
# @File :class_12day_pool.py

import os
import requests
from multiprocessing import Pool, Manager

# 进程池
a = 0


def work(q):
    global a
    # 判断队列中是否有数据
    # 获取任务
    url = q.get()
    # 执行任务
    requests.get(url)
    print("work1正在执行任务-----{}".format(os.getpid()))
    a += 1


if __name__ == '__main__':
    # 进程池之间的队列
    q = Manager().Queue()

    for i in range(10):
        q.put("http://127.0.0.1:5000")

    # 创建进程池（3个进程）
    pool = Pool(5)

    for i in range(10):
        if q.qsize()>0:
            pool.apply_async(work,args=(q,))
        else:
            break

    pool.close()
    pool.join()
