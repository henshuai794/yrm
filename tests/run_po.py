# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 20:21
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：运行po设计模式用例
"""
from tests.PO import Test_Shop

shop = Test_Shop('gc')
# 登录-will
shop.login_error()
shop.login_succ()

# 搜索-tufei
shop.search_succ()

# 个人中心-will
shop.userinfo_succ()

# 订单-roy
shop.order_succ()

# 验证码的-will
shop.slide_qq()
shop.slide_jd()
shop.slide_douyin()
