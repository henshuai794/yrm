# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 21:34
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：参数化
"""
import pytest
from common.datadriven import get_yaml
from pytestcases.my_mo import add


parmas = get_yaml('../lib/data/add.yaml')


class Test_add:
    @pytest.mark.parametrize("x,y,z,name", parmas)
    def test_add(self, x, y, z,name):
        print(name)
        assert add(x, y) == z
