# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 21:43
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：测试yaml文件读取
"""
import yaml


with open('../cases/cases.yml',encoding='utf-8') as f:
    result = yaml.safe_load(f)

print(result)
