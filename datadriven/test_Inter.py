# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/15 20:32
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：接口自动化的数据驱动执行
"""
import os
import time

import allure
import cv2
import pytest
import yaml

from keywords.interKeys import HTTP
from common.Logger import logger


# 获取yaml用例
def get_cases(path):
    with open(path, encoding='utf-8') as f:
        result = yaml.safe_load(f)
    return result


# 设置结果
def setresult(obj):
    if obj.jsonres is not None:
        allure.attach(str(obj.jsonres), '运行结果', attachment_type=allure.attachment_type.YAML)
        return

    if obj.result is not None:
        try:
            allure.attach(str(obj.result.text), '运行结果', attachment_type=allure.attachment_type.TEXT)
            return
        except Exception as e:
            allure.attach(str(obj.result), '运行结果', attachment_type=allure.attachment_type.TEXT)
        return


cases = get_cases('./lib/cases/zhihu.yml')


@allure.feature('接口测试自动化')
class Test_Inter:
    """
    数据驱动执行Http接口自动化用例
    """

    def setup_class(self):
        # 初始化关键字库的对象
        self.http = HTTP()

    @allure.step
    def run_step(self, func, params):
        """
        一个步骤
        :param func: 关键字
        :param value: 参数列表
        :return:
        """
        func(*params)

    @allure.story('知乎接口自动化')
    @pytest.mark.parametrize("caseslist", cases['知乎'])
    def test_zhihu(self, caseslist):
        """
        使用参数化执行所有用例
        :return:
        """
        print(caseslist)
        allure.dynamic.title(caseslist['title'])
        logincases = caseslist['cases']
        for onecase in logincases:
            # 反射获取到关键字
            logger.info(onecase)
            func = getattr(self.http, onecase['method'])
            params = list(onecase.values())[2:]
            try:
                with allure.step(onecase['name']):
                    self.run_step(func, params)
                    setresult(self.http)
            except Exception as e:
                # 给出失败也异常信息
                pytest.fail("用例执行失败：{}".format(e))


if __name__ == "__main__":
    os.system(r'rd ..\report /s/q')
    os.system(r'rd ..\temp /s/q')
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['-s', './test_Inter.py', '--alluredir', '../temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../temp -o ../report --clean')
