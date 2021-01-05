#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 1:24
# @Author :春衫
# @File :Boss_setting_requests.py

from Web.Common.fengyong.tools.http_request import HttpRequest
from Web.Common import UserLog

my_logger = UserLog()


def boss_setting_requests(surroundings, phone, operational_setting):
    '''

    Parameters
    ----------
    surroundings：test/dev1/mtest
    phone：手机号
    operational_setting：[{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]

    Returns：None
    -------

    '''

    if operational_setting == "未设置":
        salesRatio = "0"
        freeSalesRatio = "0"
        tcoRatio = "0"
    else:
        salesRatio = str(operational_setting['销售'])
        freeSalesRatio = str(operational_setting['业务焕商'])
        tcoRatio = str(operational_setting['TCO'])

    # 登录
    login_url = f'http://boss.{surroundings}.hobay.com.cn/bosszuul/boss/user/login'  # 登录
    login_data = {"phone": phone, "password": "qaz123"}
    login_res = HttpRequest().http_request(login_url, "post", data=login_data)
    my_logger.debug(f"BOSS登录结果是：{login_res.json()}")

    # 设置运营比例
    agentId = login_res.json()['id']
    secondPayagentRatio_url = f'http://boss.{surroundings}.hobay.com.cn/bosszuul/order/secondPayagentRatio/addOrUpdateSecondPayagentRatio'
    secondPayagentRatio_data = {"agentId": agentId,
                                "freeSalesRatio": freeSalesRatio,
                                "salesRatio": salesRatio,
                                "tcoRatio": tcoRatio}
    secondPayagentRatio_res = HttpRequest().http_request(secondPayagentRatio_url, "post", data=secondPayagentRatio_data,
                                                         cookies=login_res.cookies)
    my_logger.debug(f"设置运营比例的结果是：{secondPayagentRatio_res.json()}")


if __name__ == '__main__':
    pass
