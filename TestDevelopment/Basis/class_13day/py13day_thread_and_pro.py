#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/30 15:18
# @Author :春衫
# @File :py13day_thread_and_pro.py

"""
比较1000个任务
分别使用3个进程或线程来完成，哪个更快

#进程快
任务数量少于CPU数量：并行

#线程：全局解释器锁GIL的存在，并发（不可能同事执行三个任务）

#做多任务的时候，进程快，只用进程 合不合理？
不合理，进程占用的资源过大
"""

import queue
import requests
import threading
import time
from multiprocessing import Queue, Manager, Pool

# 线程的队列（只能在一个进程中使用）
q = queue.Queue()
for i in range(1000):
    q.put("http://127.0.0.1:5000")

# 可以再多个进程之间通信（可以给多个进程来用）
# q2 = Queue()

# 进程池中的队列（给进程池中的各个进程之间使用）
# q3 = Manager().Queue()
# for i in range(1000):
#     q3.put("http://127.0.0.1:5000")


# def work(q):
#     while q.qsize() > 0:
#         url = q.get()
#         requests.get(url=url)


# def main():
#     st=time.time()
#     t1=threading.Thread(target=work)
#     t2=threading.Thread(target=work)
#     t3=threading.Thread(target=work)
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     et=time.time()
#     print("耗时：{}".format(et-st))

i = 0


def work(q):
    while q.qsize() > 0:
        url = q.get()
        requests.get(url=url)
        global i
        i += 1
    print("该进程运行了%s次" % i)


if __name__ == '__main__':
    # main()
    # 线程的耗时时间：3.662994146347046

    q3 = Manager().Queue()
    for i in range(1000):
        q3.put("http://127.0.0.1:5000")

    # 进程池
    pool = Pool(3)
    st = time.time()
    for i in range(3):
        pool.apply_async(work, args=(q3,))

    # 关闭进程池
    pool.close()
    # 主进程等待进程池中所有的进程执行结束之后再往下执行
    pool.join()
    et = time.time()
    print("耗时：{}".format(et - st))
    # 耗时：3.077998638153076
    # 进程比线程的时间短
