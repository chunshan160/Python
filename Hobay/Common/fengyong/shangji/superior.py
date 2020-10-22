#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/13 12:04
# @Author :春衫
# @File :Superior.py

from Common.fengyong.sql.personal import personal
from Common.fengyong.sql.chengshihuanshang import chengshihuanshang
from Common.fengyong.sql.ratio import ratio
from Common.user_log import UserLog

my_logger = UserLog()


class Superior:

    def superior(self, ip, regional_agent, phone):
        '''
        :param regional_agent:上级代理商/城市焕商
        :param phone:手机号
        :return:上级代理商/城市焕商模板
        '''

        a = personal(ip, phone)
        c = [a]

        b = {}
        # print(len(regional_agent))
        for i in range(0, len(regional_agent)):

            if (regional_agent)[i].__contains__('type'):
                # print("上级是代理商")
                u1 = regional_agent[i]['type']
                u2 = regional_agent[i]['id']

                if u1 == 1:
                    b["省代理商"] = u2
                elif u1 == 2:
                    b["市代理商"] = u2
                else:
                    b["区代理商"] = u2

            else:
                my_logger.info("上级是城市焕商")
                u2 = regional_agent[i]['signed_user_id']
                if (regional_agent)[i]['area_name'] != "":
                    b["区代理商"] = u2
                else:
                    b["市代理商"] = u2

        if "省代理商" not in b:
            b["省代理商"] = None
        if "市代理商" not in b:
            b["市代理商"] = None
        if "区代理商" not in b:
            b["区代理商"] = None

        c.append(b)
        return c

    def fenyong(self, ip, province_id, city_id, area_id, personal_id):

        data = ratio(ip, province_id, city_id, area_id, personal_id)

        fenyong = {}
        # # [{'user_id': 2000408, 'ratio': Decimal('0.15'), 'type': 4}, {'user_id': 1000445, 'ratio': Decimal('0.30'), 'type': 5}]
        # data = [{'user_id': 2000408, 'ratio': Decimal('0.15'), 'type': 4},
        #         {'user_id': 1000446, 'ratio': Decimal('0.60'), 'type': 5},
        #         {'user_id': 1000445, 'ratio': Decimal('0.30'), 'type': 5}]
        if data != None:
            for i in range(len(data)):
                if data[i]['type'] == 1:
                    fenyong["省分佣比例"] = data[i]['ratio']

                elif data[i]['type'] == 2:
                    fenyong["市分佣比例"] = data[i]['ratio']

                elif data[i]['type'] == 3:
                    fenyong["区分佣比例"] = data[i]['ratio']

                elif data[i]['type'] == 4:
                    fenyong["个人分佣比例"] = data[i]['ratio']
                else:
                    sss = chengshihuanshang(ip, data[i]['user_id'])
                    fenyong[sss] = data[i]['ratio']

        if province_id == None:
            fenyong["省分佣比例"] = None
        if city_id == None:
            fenyong["市分佣比例"] = None
        if area_id == None:
            fenyong["区分佣比例"] = None
        if personal_id == None:
            fenyong["个人分佣比例"] = None

        return fenyong


if __name__ == '__main__':
    from decimal import *

    a = Superior().fenyong('192.168.0.102', None, None, 1000445, 2000408)
    print(a)
