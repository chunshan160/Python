#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/8 15:34
# @Author :春衫
# @File :猫眼爬虫-正则.py

import re
import requests
import json


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
    except:
        print("请求异常")
        return None
    else:
        r.encoding = 'utf-8'
        return r.text


def parse_response(web_data):
    # 排名
    index_regx = re.compile(r'<i class="board-index board-index-.*?">(.*?)</i>')
    index_list = re.findall(index_regx, web_data)

    tittle_regx = re.compile(r'data-val="{movieId:.*?}">(.*?)</a>')
    tittle_list = re.findall(tittle_regx, web_data)

    actor_regx = re.compile(r'<p class="star">[\s]*主演：(.*?)[\s]*</p>')
    actor_list = re.findall(actor_regx, web_data)

    time_regx = re.compile(r'<p class="releasetime">上映时间：(.*?)</p>')
    time_list = re.findall(time_regx, web_data)

    score_regx = re.compile(r'<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>')
    score_list = ["".join(i) for i in re.findall(score_regx, web_data)]

    return index_list, tittle_list, actor_list, time_list, score_list


def save_item(index_list, tittle_list, actor_list, time_list, score_list):
    d = {}
    for index, tittle, actor, time, score in zip(index_list, tittle_list, actor_list, time_list, score_list):
        d['排名'] = index
        d['电影名称'] = tittle
        d['主演'] = actor
        d['上映时间'] = time
        d['评分'] = score
        f.write(json.dumps(d, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    f = open('../maoyan.txt', 'w', encoding='utf-8')
    url = 'https://maoyan.com/board/4?offset={}'
    for offset in range(0, 100, 10):
        s = get_response(url.format(offset))
        index_list, tittle_list, actor_list, time_list, score_list = parse_response(s)
        save_item(index_list, tittle_list, actor_list, time_list, score_list)
