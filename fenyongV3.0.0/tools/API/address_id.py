#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:34
# @Author :春衫
# @File :address_id.py

from tools.http_request import HttpRequest


def get_address_id(surroundings, cookies):

    address_url = f'http://m.{surroundings}.hobay.com.cn/api/user/graphql/flat'
    address_data = {
        "query": "query currentUser{\n        currentUser{\n          receiveAddress(page:1,pageSize:100){\n            numPerPage\n            pageNum\n            totalCount\n            totalPage\n            recordList{\n              id\n              name\n              provinceName\n              cityName\n              areaName\n              detailAddress\n              phone\n              default\n            }\n          }\n        }\n      }"}
    address_headers = {"login": ""}
    address_res = HttpRequest().http_request(address_url, 'post', json=address_data,
                                             cookies=cookies,
                                             headers=address_headers)
    return address_res
