import requests
from interface_auto.common.my_log import MyLog


class HttpRequest:
    """封装接口请求方法"""

    @staticmethod
    def http_request(url, data, method, header=None, cookie=None):
        try:
            if method.upper() == 'GET':
                res = requests.get(url, data, headers=header, cookies=cookie)
            elif method.upper() == 'POST':
                res = requests.post(url, data, headers=header, cookies=cookie)
            elif method.upper() == 'PUT':
                res = requests.put(url, data, headers=header, cookies=cookie)
            else:
                MyLog().error('输入的请求方式有误，请检查！')
        except Exception as e:
            MyLog().error('请求报错，结果为{0}'.format(e))
            raise e
        return res

if __name__ == '__main__':
    login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    login_data = {"mobilephone":"17777700001","pwd":"123456"}
    res = HttpRequest.http_request(login_url, login_data, 'post')
    print(res.json())
    print(res.cookies)
