# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/10 21:51
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：运行入口
"""
import os
import pytest




# 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
pytest.main(['./datadriven/test_Web.py', '--alluredir', './temp'])
# 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
# os.system('allure generate ./temp -o ./report --clean')


