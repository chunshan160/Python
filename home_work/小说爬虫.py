#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/8 15:34
# @Author :春衫
# @File :猫眼爬虫.py


import re
import requests
from bs4 import BeautifulSoup

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

爬虫的运行流程:
模拟浏览器向服务器[网站后台提供数据能接收http请求]发送http请求(get()，post())
服务器接收到请求后向爬虫返回数据
代码思路:
1.使用代码去打开书籍详情页，并且返回详情页的所有数据
2.请求成功拿到详情页数据之后，去做数据筛选
3.把筛选好的数据放在文件中 文件操作


筛选数据
    1.提取所有小说章节名称
    2.提取所有小说章节中的a标签中的链接，对主域名做字符串拼接
    3.利用requests对拼接好的域名做请求
    4.拿到内容页数据后做数据筛选
'''


def get_response(url):
    try:
        response = requests.get(url)
    except:
        print("请求异常")
        return None
    else:
        response.encoding = 'utf-8'
        return response.text


def getbook(url, file_path, mode=True):
    # 响应文本
    response =get_response(url)
    # 网页选择器实例化
    soup = BeautifulSoup(response, 'lxml')
    #书名
    book_name=soup.find('h1').text
    print(book_name)
    # 全部章节
    data_list = soup.find('ul')

    # 具体章节
    for book in data_list.find_all('a'):
        # 获取章节跳转URL
        book_url = url + book["href"]
        # 获取章节文本
        data_book = get_response(book_url)
        # 网页选择器实例化
        soup = BeautifulSoup(data_book, 'lxml')
        # 章节名
        chapter_name = soup.find('h1').get_text()
        print(chapter_name,"爬取完成")
        # 章节内容
        data = soup.find('div', {'id': 'htmlContent'}).text

        # 文件操作
        # 全部章节写入一个文件内
        if mode == True:
            with open(file_path+book_name+'.txt', 'a+', encoding='utf-8') as f:
                f.write(chapter_name + '\n' + '\n' + data + '\n' + '\n')
        # 每个章节单独写入一个文件内
        else:
            file_name = re.sub('[\/:*?"<>|]', '-', book.text)  # 去掉非法字符
            with open(file_path+file_name+'.txt', 'w', encoding='utf-8') as f:
                f.write(data)


if __name__ == '__main__':
    url = 'http://www.biquw.com/book/5336/'
    file_path = 'E:\\新建文件夹\\凡人修仙传仙界篇\\'
    getbook(url, file_path, mode=True)
