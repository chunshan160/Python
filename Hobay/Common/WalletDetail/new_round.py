#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/12 15:52
# @Author :春衫
# @File :new_round.py

# 四舍五入
def new_round(_float, _len):
    """
    Parameters
    ----------
    _float: float
    _len: int, 指定四舍五入需要保留的小数点后几位数为_len

    Returns
    -------
    type ==> float, 返回四舍五入后的值
    """
    if isinstance(_float, float):
        if str(_float)[::-1].find('.') <= _len:
            return (_float)
        if str(_float)[-1] == '5':
            return (round(float(str(_float)[:-1] + '6'), _len))
        else:
            return (round(_float, _len))
    else:
        return (round(_float, _len))

if __name__ == '__main__':
    a=new_round(9.9,2)
