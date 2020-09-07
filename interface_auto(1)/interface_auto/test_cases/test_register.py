#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import os
from ddt import ddt,data
from interface_auto.common.read_config import ReadConfig
from interface_auto.common.read_excel import ReadExcel
from interface_auto.common.my_log import MyLog
from interface_auto.common.get_data import GetData
from interface_auto.common.http_request import HttpRequest
from interface_auto.common.project_path import data_dir
import warnings

#拼接测试数据的路径
data_path = os.path.join(data_dir,'data.xlsx')
#获取测试数据
test_data = ReadExcel(data_path,'register').get_data()

@ddt
class TestApi(unittest.TestCase):
    """注册接口测试"""

    def setUp(self):
        self.base_url = ReadConfig().read_config('ENV','url')
        self.register_phone = getattr(GetData,'register_phone')
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self):
        ReadConfig().write_data('ENV','register_phone',str(int(self.register_phone)+1))

    @data(*test_data)
    def test_api(self,case):
        url = self.base_url + case['url']
        data = case['data']
        method = case['method']
        expected = str(case['expected'])
        if data.find('register_phone') != -1:
            data = data.replace('${register_phone}',self.register_phone)
        res = HttpRequest.http_request(url=url,data=eval(data),method=method)
        try:
            self.assertEqual(expected,res.json()['code'])
            self.result = '通过'
        except Exception as e:
            MyLog().info('执行用例出错：{0}'.format(e))
            self.result = '不通过'
            raise e
        finally:
            MyLog().debug('获取到的结果是：{}'.format(res.json()))
            ReadExcel(data_path,'register').write_data(case['case_id']+1,self.result)

if __name__ == '__main__':
    unittest.main()