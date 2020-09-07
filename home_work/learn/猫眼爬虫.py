#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/8 15:34
# @Author :春衫
# @File :猫眼爬虫.py


'''
python领域
1.爬虫
    信息采集程序
    模拟浏览器向网站服务器发送一个http请求 get(）网站服务器向爬虫响应数据
2.web
    网站搭建
        http请求浏览器网站服务器
        django
            重量级的网站搭建框架它里面涵盖的网站功能基本都有框架比较大消耗的资源比较多
        flask
            轻量级的框架网站基本的功能都有需要高级的功能得自己写灵活消耗资源小做定制化
        tornado
            性能级框架支持高并发IO多路复用门槛高学习成本有点大
            视频推流网站


3.自动化测试
4.自动化运维
5．游戏
6.人工智能
7.数据分析 科学计算 munpy

'''

'''
如果你想实现此脚本
就必须借助一些第三方工具
联网工具爬虫工具返回数据
数据筛选包
re正则表达式
bs4网页选择器 pip install bs4
xpath
pyquary
将我们的数据以json的数据格式保存下来
json前端 html|
import reguests
from bs4 import BeautifulSoup
import json
'''

import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}


# 获取请求页面
def getpage(url):
    # 异常处理 保证我们的程序不会因为断网等一系列的原因导致程序崩溃
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None


# 获取电影信息
def getInfo(html):
    # 使用BeautifulSoup匹配电影的排名海报电影名主演评分
    # BeautifulSoup 必须传入两个参数你要提取的网页html解析器
    soup = BeautifulSoup(html, "lxml")
    # 找到网页中所有dd标签10个
    items = soup.select('dd')
    for item in items:
        index = item.find('i', class_='board-index').get_text()
        name = item.find('p', class_='name').get_text()
        start = item.find('p', class_='star').get_text().strip()[3:]
        time = item.find('p', class_='releasetime').get_text()[5:]
        score = item.find('p', class_='score').get_text()

        # 生成器
        yield {
            '排名': index,
            '电影名称': name,
            '主演': start,
            '上映时间': time,
            '评分': score
        }


# 写入文件
def writeData(file):
    # 文件处理
    with open('../za/maoyan.txt', 'a', encoding='utf-8') as f:
        # 在python中一个对象无法写入文件中 所以我们要把字典对象转成json数据
        # Ascii码
        f.write(json.dumps(file, ensure_ascii=False) + '\n')


# 程序入口
if __name__ == "__main__":
    for num in [i * 10 for i in range(11)]:
        url = 'https://maoyan.com/board/4?offset=' + str(num)
        html = getpage(url)
        for item in getInfo(html):
            print(item)
            writeData(item)
