#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 10:59
# @Author :春衫
# @File :class_10day_thread.py

import time
import threading


def func1():
    for i in range(5):
        time.sleep(1)
        print("-----正在做事情1---{}---".format(threading.current_thread()))


def func2():
    for i in range(6):
        time.sleep(1)
        print("-----正在做事情2---{}---".format(threading.current_thread()))


def main():
    # 创建一个线程去执行 事情1
    t1 = threading.Thread(target=func1, name="th_1")
    # 创建一个线程去执行 事情2
    t2 = threading.Thread(target=func2)
    start_time = time.time()

    # t1.setName("线程1")
    # print(t1.getName())
    # print(t1.name)
    # 判断是否有线程在运行
    print(t1.is_alive())
    # 开始执行线程1
    t1.start()
    print(t1.is_alive())
    # 开始执行线程2
    t2.start()
    # 让主线程等待子线程执行完了之后再继续往下执行
    # print(threading.current_thread())
    print(threading.enumerate())  # 当前运行的所有线程对象
    print(threading.active_count())  # 返回当前执行线程的数量 （主线+子线）
    t1.join()
    t2.join()

    end_time = time.time()
    print("耗时：", end_time - start_time)


if __name__ == '__main__':
    main()

    # start_time=time.time()
    # # func1()
    # # func2()
    # # end_time=time.time()
    # # print("耗时：",end_time-start_time)
