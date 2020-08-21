#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/13 12:04
# @Author :春衫
# @File :Superior.py

from Common.DoMysql.sql import SQL


class Superior:

    def superior(self, ip, regional_agent, phone):
        '''
        :param regional_agent:上级代理商/城市焕商
        :param phone:手机号
        :return:上级代理商/城市焕商模板
        '''

        # t=[{'signed_user_id': 15239, 'area_name': ''}]
        a = SQL(ip).personal(phone)
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
                print("上级是城市焕商")
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

        data = SQL(ip).ratio(province_id, city_id, area_id, personal_id)

        fenyong = {}

        if data!=None:
            # print(data)
            for i in data:

                if data[0]['type'] != 5:
                    u1 = i['ratio']
                    if i['type'] == 1:
                        fenyong["省分佣比例"] = u1

                    elif i['type'] == 2:
                        fenyong["市分佣比例"] = u1

                    elif i['type'] == 3:
                        fenyong["区分佣比例"] = u1

                    elif i['type'] == 4:
                        fenyong["个人分佣比例"] = u1
                else:
                    if len(data) == 2:
                        u2 = [data[0]['ratio'], data[1]['ratio']]
                        if data[0]['ratio'] >= data[1]['ratio']:
                            fenyong["市分佣比例"] = u2[0]
                            fenyong["区分佣比例"] = u2[1]
                        else:
                            fenyong["市分佣比例"] = u2[1]
                            fenyong["区分佣比例"] = u2[0]
                    else:
                        u3 = data[0]['ratio']
                        sss = SQL(ip).chengshihuanshang(data[0]['user_id'])
                        fenyong[sss] = u3

        if province_id == None:
            fenyong["省分佣比例"] = None
        if city_id == None:
            fenyong["市分佣比例"] = None
        if area_id == None:
            fenyong["区分佣比例"] = None
        if personal_id == None:
            fenyong["个人分佣比例"] = None

        # print("最终",fenyong)

        return fenyong


if __name__ == '__main__':
    # b=[{'type': 1, 'id': 13691}, {'type': 2, 'id': 13947}, {'type': 3, 'id': 14453}]
    # a=Superior().superior("192.168.0.107",b,17777777786)
    # print(a)
    # c = [{'type': 1, 'id': 1000646}]
    # d = Superior().superior("192.168.0.101", c, 17777777781)
    # print(d)

    qq = Superior().fenyong("192.168.0.102",None,15239, None, None)
    print(qq)
