#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import os
from ddt import ddt,data
from interface_auto.common.read_config import ReadConfig
from interface_auto.common.read_excel import ReadExcel
from interface_auto.common.my_log import MyLog
from interface_auto.common.http_request import HttpRequest
from interface_auto.common.project_path import data_dir
from interface_auto.common.get_data import GetData
import warnings

#拼接测试数据的路径
data_path = os.path.join(data_dir,'data.xlsx')
#获取测试数据
test_data = ReadExcel(data_path,'recharge').get_data()

@ddt
class TestApi(unittest.TestCase):
    """
    充值接口测试
    """
    def setUp(self):
        self.base_url = ReadConfig().read_config('ENV','url')
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self,case):
        url = self.base_url + case['url']
        data = case['data']
        method = case['method']
        expected = str(case['expected'])
        if data.find('${login_phone}') != -1:
            data = data.replace('${login_phone}',getattr(GetData,'login_phone'))
        elif data.find('${recharge_phone}') != -1:
            data = data.replace('${recharge_phone}',getattr(GetData,'recharge_phone'))
        res = HttpRequest.http_request(url=url,data=eval(data),method=method,cookie=getattr(GetData,'COOKIE'))
        if res.cookies:
            setattr(GetData,'COOKIE',res.cookies)
        try:
            self.assertEqual(expected,res.json()['code'])
            self.result = '通过'
        except Exception as e:
            MyLog().info('执行用例出错：{0}'.format(e))
            self.result = '不通过'
            raise e
        finally:
            MyLog().debug('获取到的结果是：{}'.format(res.json()))
            ReadExcel(data_path,'recharge').write_data(case['case_id']+1,self.result)

if __name__ == '__main__':
    unittest.main()