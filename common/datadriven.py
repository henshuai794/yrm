# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 21:57
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：数据驱动的功能函数
"""
import yaml


def get_yaml(path):
    """
    读取指定位置的yaml文件
    :param path: yaml文件的位置
    :return: 返回读取到的数据结构
    """
    with open(path, 'rb') as f:
        result = yaml.safe_load(f)

    return result




