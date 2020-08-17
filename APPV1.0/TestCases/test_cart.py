#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 21:46
# @Author :春衫
# @File :test_cart.py
import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example():
    import random
    assert random.choice([True, False, False])



if __name__ == '__main__':
    pytest.main(['--reruns', '3', '--reruns-delay', '5'])