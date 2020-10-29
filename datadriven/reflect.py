# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/15 20:45
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：反射
"""

class MyTest:

    def do1(self,a):
        print("这是函数1")

    def do2(self):
        print("这是函数2")

    def do3(self):
        print("这是函数3")


if __name__ == '__main__':
    t = MyTest()
    def get_func(obj,f):
        func = getattr(obj,f)
        return func

    l = [
        ['a'],
        [],
        [],
        []
    ]

    for i in range(4):
        m = input("请输入你要执行的函数")
        func = get_func(t,m)
        func(*l[i])

    # a = input()
    # # 捕获异常
    # try:
    #     a = int(a)
    # except Exception as e:
    #     a = 0
    #
    # print(a)
