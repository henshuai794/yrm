# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/13 20:10
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：使用PO设计模式设计用例
"""
import time

import pytest

from keywords.WebKeys import Web


class Test_Shop:
    """
    电商web自动化，页面对象化封装类
    """

    def setup_class(self):
        """
        完成初始化
        """
        # 创建运行的关键字库对象
        self.web = Web()
        # 打开谷歌浏览器
        self.web.openbrowser()

    def test_login_error(self):
        """
        登录：用户名密码错误的用例
        :return:
        """
        # 登录用例
        self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
        self.web.input('//*[@id="username"]', '13800138006')
        self.web.input('id=password', '11111')
        self.web.input('xpath=//*[@id="verify_code"]', '111')
        self.web.jsclick('//*[@id="loginform"]/div/div[6]/a')

    def test_login_succ(self):
        """
        登录：登录成功的用例
        :return:
        """
        self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
        self.web.input('//*[@id="username"]', '13800138006')
        self.web.input('id=password', '123456')
        self.web.getverify('//*[@id="verify_code_img"]')
        self.web.input('xpath=//*[@id="verify_code"]', '{verify}')
        time.sleep(5)
        self.web.jsclick('//*[@id="loginform"]/div/div[6]/a')
        time.sleep(1)
        self.web.gettext('//a[@class="red userinfo"]', 'nickname')
        print(self.web.assertequal('aa{nickname}bb', 'aa单身的willbb'))

    def test_order_succ(self):
        """
        我的订单用例
        必须先调用login_succ页面用例
        :return:
        """
        # 我的订单用例
        self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/User/index.html')
        self.web.click('(//a[text()="我的订单"])[1]')
        self.web.switchwin(1)
        self.web.click('(//*[contains(text(),"取消订单")])[1]')
        self.web.click('//*[@id="layui-layer100001"]/span[1]/a')
        self.web.closewin()
        self.web.switchwin(0)

    def test_userinfo_succ(self):
        """
        个人信息
        :return:
        """
        # 个人信息
        self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/User/info.html')
        self.web.click('//*[@id="preview"]')
        self.web.intoiframe('//*[@id="layui-layer-iframe1"]')
        self.web.input('//*[@id="filePicker"]/div[2]/input',
                  r'E:\software\Python\VipWebFrame06\lib\images\q-icon.png')
        self.web.outiframe()
        self.web.click('//*[@id="layui-layer1"]/span[1]/a[3]')

    def test_search_succ(self):
        """
        搜索用例
        :return:
        """
        self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/User/index.html')
        self.web.input('//*[@id="q"]', '手机')
        self.web.click('//*[@id="sourch_form"]/a')
        time.sleep(1)
        self.web.runjs('window.scrollBy(0,500)')
        self.web.runjs('document.getElementsByClassName("p-btn")[1].children[0].click()')

    def test_slide_qq(self):
        """
        qq滑块验证码破解
        :return:
        """
        # QQ验证码
        self.web.geturl('http://i.qq.com')
        self.web.intoiframe('//*[@id="login_frame"]')
        self.web.click('//*[@id="switcher_plogin"]')
        self.web.input('//*[@id="u"]', '324234423')
        self.web.input('//*[@id="p"]', 'ewrewqrds')
        self.web.click('//*[@id="login_button"]')
        self.web.intoiframe('//*[@id="tcaptcha_iframe"]')
        self.web.slideverify('//*[@id="slideBg"]', '//*[@id="slideBlock"]',
                        '{"offset-x":22,"refresh":"//*[@id=\\\"e_reload\\\"]"}')

    def test_slide_douyin(self):
        """
        抖音滑块验证码破解
        :return:
        """
        # 抖音的验证码
        self.web.geturl('https://union.bytedance.com/open/')
        self.web.click('//*[@id="root"]/div/div[2]/div[7]/div[1]')
        self.web.click('//*[@id="root"]/div/div[2]/div[8]/div/div[1]/div[2]')
        self.web.input('//*[@id="root"]/div/div[2]/div[8]/div/div[2]/div[2]/div[1]/input', '15366669999')
        self.web.click('//*[@id="root"]/div/div[2]/div[8]/div/div[2]/div[2]/div[2]/div/div')
        time.sleep(3)
        self.web.slideverify('//*[@id="captcha_container"]/div/div[2]/img[1]',
                        '//*[@id="captcha_container"]/div/div[2]/img[2]',
                        '{"zoom":1.25,"offset-x":30,"offset-y":444,"slide":"puautogui"}')

    def test_slide_jd(self):
        """
        京东滑块验证码破解
        :return:
        """
        # 京东验证码
        self.web.geturl('https://passport.jd.com/new/login.aspx')
        self.web.click('//*[@id="content"]/div[2]/div[1]/div/div[3]/a')
        self.web.input('//*[@id="loginname"]', 'wuqingfadqng')
        self.web.input('//*[@id="nloginpwd"]', 'dsafds')
        self.web.click('//*[@id="loginsubmit"]')
        self.web.slideverify('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img',
                        '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img',
                        '{"zoom":1.25,"offset-x":20,"offset-y":308,"slide":"puautogui"}')

    def close(self):
        """
        运行结束
        :return:
        """
        time.sleep(5)
        # 退出浏览器
        self.web.quit()


if __name__ == "__main__":
    pytest.main(['./PO.py','-s'])
