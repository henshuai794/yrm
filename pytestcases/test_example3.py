# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 21:05
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：运行原理
"""
import time

import pytest


class Test_ABC:

    # def setup_class(self):
    #     """
    #     类级别的初始化
    #     整个测试类运行前，会运行一次
    #     :return:
    #     """
    #     print("\n------->setup_class")
    #
    # def setup(self):
    #     """
    #     用例级别的初始化
    #     每一个用例执行前，都会执行
    #     :return:
    #     """
    #     print("\n------->setup")
    #
    # def teardown(self):
    #     print("------->teardown")
    #
    # def teardown_class(self):
    #     print("------->teardown_class")

    @pytest.fixture()
    def a_setup_teardown(self):
        print("开始a")
        yield
        print("结束a")

    def test_a(self,a_setup_teardown):
        print("\n------->test_a")
        assert False

    def test_b(self):
        print("\n------->test_b")
        assert False

    def test_c(self):
        print("\n------->test_c")
        assert False

    def test_d(self):
        print("\n------->test_d")
        assert False