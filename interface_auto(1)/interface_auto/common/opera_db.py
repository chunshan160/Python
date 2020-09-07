import pymysql
from interface_auto.common.read_config import ReadConfig

host = ReadConfig().read_config('DB', 'host')
port = ReadConfig().read_config('DB', 'port')
user = ReadConfig().read_config('DB', 'user')
password = ReadConfig().read_config('DB', 'password')
db_name = ReadConfig().read_config('DB', 'db_name')


class OperaDb:
    """封装数据库操作的方法"""

    def __init__(self):
        """连接数据库"""
        self.contection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          passwd=password,
                                          db=db_name,
                                          cursorclass=pymysql.cursors.DictCursor,
                                          charset='utf8')
        # 创建游标
        self.cur = self.contection.cursor()

    def get_one(self, sql):
        """获取一条数据"""
        self.cur.execute(sql)
        data = self.cur.fetchone()
        self.close()
        return data

    def get_all(self, sql):
        """获取多条数据"""
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.close()
        return data

    def close(self):
        """关闭游标对象并断开连接"""
        self.cur.close()
        self.contection.close()


if __name__ == '__main__':
    res = OperaDb().get_one('select RegName from member where MobilePhone="17777700001"')
    print(res)
    print(res['RegName'])
