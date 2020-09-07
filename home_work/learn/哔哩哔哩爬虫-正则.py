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
    index_regx = re.compile(r'<div class="num">(.*?)</div>')
    index_list = re.findall(index_regx, web_data)
    #稿件标题
    tittle_regx = re.compile(r'"title":"(.*?)",')
    tittle_list = re.findall(tittle_regx, web_data)
    #弹幕数量
    BarrageNum_regx = re.compile(r'<i class="b-icon view"></i>(.*?)</span>')
    BarrageNum_list = re.findall(BarrageNum_regx, web_data)
    #up名字
    upname_regx = re.compile(r'"author":"(.*?)",')
    upname_list = re.findall(upname_regx, web_data)
    #综合得分
    score_regx = re.compile(r'"pts":(.*?),')
    score_list = re.findall(score_regx, web_data)

    return index_list, tittle_list, BarrageNum_list, upname_list, score_list


def save_item(index_list, tittle_list, BarrageNum_list, upname_list, score_list):
    d = {}
    for index, tittle, actor, time, score in zip(index_list, tittle_list, BarrageNum_list, upname_list, score_list):
        d['排名'] = index
        d['稿件标题'] = tittle
        d['弹幕数量'] = actor
        d['up名字'] = time
        d['综合得分'] = score
        f.write(json.dumps(d, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    f = open('../za/bilibili.txt', 'w', encoding='utf-8')
    url = 'https://www.bilibili.com/ranking'
    s = get_response(url)
    print(s)
    index_list, tittle_list, actor_list, time_list, score_list = parse_response(s)
    save_item(index_list, tittle_list, actor_list, time_list, score_list)
