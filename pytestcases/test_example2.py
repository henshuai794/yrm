# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 20:51
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：运行方式
"""
import pytest

def test_xxx():
    """
    这个也是测试用例，是属于测试模块的测试用例
    :return:
    """
    print(2)

if __name__ == "__main__":
    pytest.main(['./test_example3.py','-s','-n','2'])