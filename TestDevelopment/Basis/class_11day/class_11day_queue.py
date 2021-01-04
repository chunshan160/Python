#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 11:04
# @Author :春衫
# @File :class_11day_queue.py

import queue

# 三种队列
# 1、先入先出
# q = queue.Queue(3)
# # 往队列里添加数据
# q.put(1)
# q.put(11)
# q.put(12)
# q.put(13)  # 会卡主，等待数据出去
# 往队列中添加数据不等待
# q.put(22, block=False)  # 如果队列已满会报错：queue.Full

# 获取队列中的数据
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())#会一直等待
# print(q.get(block=False))#不等待，报错：_queue.Empty

# 获取队列中的任务数
# print(q.qsize())

# # 判断队列是否已满
# print(q.full())
#
# #判断队列是否为空
# print(q.empty())


# q.task_done()
# q.task_done()
# q.task_done()

#等待队列中的任务执行完毕再继续往下执行
# q.join()



# 2、后入先出
# q2 = queue.LifoQueue(3)
# # 往队列里添加数据
# q2.put(1)
# q2.put(11)
# q2.put(12)
# print(q2.get())


#3、优先级队列
q3 = queue.PriorityQueue()
# 往队列里添加数据
q3.put((2,"haha2"))
q3.put((3,"haha3"))
q3.put((1,"haha1"))
q3.put((4,"haha4"))
print(q3.get())