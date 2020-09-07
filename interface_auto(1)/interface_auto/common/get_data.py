from interface_auto.common.read_config import ReadConfig


class GetData:
    """该模块用来存放初始化数据（反射使用）"""

    # 登录成功的cookie
    COOKIE = None
    # 注册使用手机号
    register_phone = ReadConfig().read_config('ENV', 'register_phone')
    # 登录使用手机号
    login_phone = ReadConfig().read_config('ENV', 'login_phone')
    # 充值使用手机号
    recharge_phone = ReadConfig().read_config('ENV', 'recharge_phone')

