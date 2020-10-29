# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 20:44
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：pytest运行的文件
"""


class Test_p:
    """
    这是一个测试类
    测试类是不允许有__init__方法
    """

    # 用例
    def test_ex1(self):
        """
        必须以test开头的实例函数才是测试用例
        :return:
        """
        print(1)
        assert 1==2


# def test_xxx():
#     """
#     这个也是测试用例，是属于测试模块的测试用例
#     :return:
#     """
#     print(2)



