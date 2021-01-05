#!/usr/bin/envpython
# -*-coding:utf-8-*-
# @Time:2020/4/2616:43
# @Author:春衫
# @File:test_superior.py


from Web.Common import regional_agent
from Web.Common.fengyong.shangji.superior import Superior


class SuperiorTemplate:

    def superior_template(self, ip, payment_method, data, phone_1, phone_2=None):
        '''

        :param payment_method: 支付方式
        :param data: data
        :param sheet_name: 表单
        :param case_id: 用例id
        :param phone_1: 手机号 易贝 易贝券
        :param phone_2: 手机号 其余支付方式 需要考虑卖家/家人/企业
        :return: 写回Excel的上级城市焕商/代理商id模板
        '''

        if payment_method in ["易贝", "易贝券"]:
            buyer_phone = eval(data)['buyer_phone']
            buyer_regional_agent = regional_agent(ip, buyer_phone)  # 查询买家上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            b = buyer_superior


        elif payment_method in ["抵工资", "家人购"]:
            buyer_phone = eval(data)['buyer_phone']
            disanfang_phone = eval(data)['disanfang_phone']
            buyer_regional_agent = regional_agent(ip, buyer_phone)  # 查询买家上级
            disanfang_regional_agent = regional_agent(ip, disanfang_phone)  # 查询企业/家人上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            disanfang_superior = Superior().superior(ip, disanfang_regional_agent, phone_2)
            b = {"储备池分佣": buyer_superior, "支付服务费分佣": disanfang_superior}


        else:  # 现金
            buyer_phone = eval(data)['buyer_phone']
            seller_phone = eval(data)['seller_phone']
            buyer_regional_agent = regional_agent(ip, buyer_phone)  # 查询买家上级
            seller_regional_agent = regional_agent(ip, seller_phone)  # 查询卖家上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            seller_superior = Superior().superior(ip, seller_regional_agent, phone_2)
            b = {"储备池分佣": buyer_superior, "支付服务费分佣": seller_superior}

        return b

    def fenyong_template(self, ip, payment_method, province1_id, city1_id, area1_id, personal1_id,
                         province2_id=None, city2_id=None, area2_id=None, personal2_id=None):
        '''

        :param ip:数据库的地址
        :param payment_method:支付方式
        :param sheet_name:表单名
        :param case_id:用例id
        :param province1_id:买家上级省代理商
        :param city1_id:买家上级市代理商
        :param area1_id:买家上级区代理商
        :param personal1_id:买家上级个人焕商
        :param province2_id:卖家上级省代理商
        :param city2_id:卖家上级市代理商
        :param area2_id:卖家上级区代理商
        :param personal2_id:卖家上级个人焕商
        :return: 写回Excel的上级城市焕商/代理商分佣比例模板
        '''

        if payment_method in ["易贝", "易贝券"]:
            buyer_fenyong = Superior().fenyong(ip, province1_id, city1_id, area1_id, personal1_id)
            if buyer_fenyong == None:
                buyer_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}
            b = buyer_fenyong

        elif payment_method in ["抵工资", "家人购", "现金"]:
            buyer_fenyong = Superior().fenyong(ip, province1_id, city1_id, area1_id, personal1_id)

            if buyer_fenyong == None:
                buyer_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            disanfang_fenyong = Superior().fenyong(ip, province2_id, city2_id, area2_id, personal2_id)
            if disanfang_fenyong == None:
                disanfang_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            b = {"储备池分佣": buyer_fenyong, "支付服务费分佣": disanfang_fenyong}

        return b

    def superior_template_main(self, ip, payment_method, data, buyer_phone):
        if payment_method in ["易贝", "易贝券"]:
            superior = SuperiorTemplate().superior_template(ip, payment_method, data,
                                                            buyer_phone)

        elif payment_method in ["抵工资", "家人购"]:
            disanfang_phone = eval(data)['disanfang_phone']
            superior = SuperiorTemplate().superior_template(ip, payment_method, data,
                                                            buyer_phone, disanfang_phone)

        else:
            seller_phone = eval(data)['seller_phone']
            superior = SuperiorTemplate().superior_template(ip, payment_method, data,
                                                            buyer_phone, seller_phone)

        return superior

    def fenyong_template_main(self, ip, payment_method, superior):

        # 获取上级分佣比例
        if payment_method in ["易贝", "易贝券"]:
            buyer_province_id = superior[1]['省代理商']
            buyer_city_id = superior[1]['市代理商']
            buyer_area_id = superior[1]['区代理商']
            buyer_personal_id = superior[0]['个人焕商']
            proportion = SuperiorTemplate().fenyong_template(ip, payment_method, buyer_province_id,
                                                             buyer_city_id, buyer_area_id, buyer_personal_id)

        elif payment_method in ["抵工资", "家人购", "现金"]:
            buyer_province_id = superior['储备池分佣'][1]['省代理商']
            buyer_city_id = superior['储备池分佣'][1]['市代理商']
            buyer_area_id = superior['储备池分佣'][1]['区代理商']
            buyer_personal_id = superior['储备池分佣'][0]['个人焕商']

            disanfang_province_id = superior['支付服务费分佣'][1]['省代理商']
            disanfang_city_id = superior['支付服务费分佣'][1]['市代理商']
            disanfang_area_id = superior['支付服务费分佣'][1]['区代理商']
            disanfang_personal_id = superior['支付服务费分佣'][0]['个人焕商']

            proportion = SuperiorTemplate().fenyong_template(ip, payment_method, buyer_province_id,
                                                             buyer_city_id, buyer_area_id, buyer_personal_id,
                                                             disanfang_province_id, disanfang_city_id,
                                                             disanfang_area_id, disanfang_personal_id)

        return proportion


if __name__ == '__main__':
    data = '{"buyer_phone":17777777786,"seller_phone":17777777775,"disanfang_phone":13724765586,"bangding_phone":17777777778,"买家":1000173,"出钱方":1000114,"卖家":1000208,"平台":8}'
    a = SuperiorTemplate().fenyong_template("192.168.0.102", "抵工资", 1000348,1000284 ,None ,1000505 ,None ,None ,1000445 ,2000408)
    print(a)
    # qqq={'储备池分佣': [{'个人焕商': None}, {'省代理商': 13691, '市代理商': 13947, '区代理商': 14453}], '支付服务费分佣': [{'个人焕商': None}, {'市代理商': 1000168, '省代理商': None, '区代理商': 1000169}]}
    # ww = SuperiorTemplate().fenyong_template("192.168.0.102", "现金", "焕商分佣_dev1", 5, 1000348, 1000284, 1000248, 1000504,None,
    #                                          15239, None, None)
    # print(ww)
