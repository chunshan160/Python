import os
import configparser
from interface_auto.common.project_path import config_dir
# 拼接配置文件的路径
config_path = os.path.join(config_dir, 'config.ini')


class ReadConfig:
    """封装读取和写入配置数据的方法"""
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path, encoding='utf-8')

    def read_config(self, option, section):
        """读取配置数据"""
        return self.conf[option][section]

    def write_data(self, option, section, value):
        """
        新增或修改配置数据
        :param option: 必须要有
        :param section: 有则修改，没有则新增
        :param value: 传入的值
        """
        self.conf.set(option, section, value)
        self.conf.write(open(config_path, 'w', encoding='utf-8'))

if __name__ == '__main__':
    data = eval(ReadConfig().read_config('ENV', 'register_phone'))
    print(data)
    # ReadConfig().write_data('DATA','year','hoss_new_20141016_bak99')
