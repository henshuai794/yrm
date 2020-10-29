# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/6 22:07
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：调用面向对象实现自动化运行
"""
import time

from keywords.WebKeys import Web

web = Web()
web.openbrowser('gc')

# 登录用例
web.geturl('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
web.input('//*[@id="username"]', '13800138006')
web.input('id=password', '11111')
web.input('xpath=//*[@id="verify_code"]', '111')
web.jsclick('//*[@id="loginform"]/div/div[6]/a')

web.geturl('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
web.input('//*[@id="username"]', '13800138006')
web.input('id=password', '123456')
web.getverify('//*[@id="verify_code_img"]')
web.input('xpath=//*[@id="verify_code"]', '{verify}')
time.sleep(5)
web.jsclick('//*[@id="loginform"]/div/div[6]/a')
time.sleep(1)
web.gettext('//a[@class="red userinfo"]', 'nickname')
print(web.assertequal('aa{nickname}bb', 'aa单身的willbb'))

# 我的订单用例
web.click('(//a[text()="我的订单"])[1]')
web.switchwin(1)
web.click('(//*[contains(text(),"取消订单")])[1]')
web.click('//*[@id="layui-layer100001"]/span[1]/a')
web.closewin()
web.switchwin(0)

# 个人信息
web.geturl('http://testingedu.com.cn:8000/index.php/Home/User/info.html')
web.click('//*[@id="preview"]')
web.intoiframe('//*[@id="layui-layer-iframe1"]')
web.input('//*[@id="filePicker"]/div[2]/input',
          r'E:\software\Python\VipWebFrame06\lib\images\q-icon.png')
web.outiframe()
web.click('//*[@id="layui-layer1"]/span[1]/a[3]')

# 搜索
web.input('//*[@id="q"]', '手机')
web.click('//*[@id="sourch_form"]/a')
time.sleep(1)
web.runjs('window.scrollBy(0,500)')
web.runjs('document.getElementsByClassName("p-btn")[1].children[0].click()')


# QQ验证码
web.geturl('http://i.qq.com')
web.intoiframe('//*[@id="login_frame"]')
web.click('//*[@id="switcher_plogin"]')
web.input('//*[@id="u"]','324234423')
web.input('//*[@id="p"]','ewrewqrds')
web.click('//*[@id="login_button"]')
web.intoiframe('//*[@id="tcaptcha_iframe"]')
web.slideverify('//*[@id="slideBg"]','//*[@id="slideBlock"]',
                '{"offset-x":22,"refresh":"//*[@id=\\\"e_reload\\\"]"}')

# 抖音的验证码
web.geturl('https://union.bytedance.com/open/')
web.click('//*[@id="root"]/div/div[2]/div[7]/div[1]')
web.click('//*[@id="root"]/div/div[2]/div[8]/div/div[1]/div[2]')
web.input('//*[@id="root"]/div/div[2]/div[8]/div/div[2]/div[2]/div[1]/input','15366669999')
web.click('//*[@id="root"]/div/div[2]/div[8]/div/div[2]/div[2]/div[2]/div/div')
time.sleep(3)
web.slideverify('//*[@id="captcha_container"]/div/div[2]/img[1]',
                '//*[@id="captcha_container"]/div/div[2]/img[2]',
                '{"zoom":1.25,"offset-x":30,"offset-y":444,"slide":"puautogui"}')

# 京东验证码
web.geturl('https://passport.jd.com/new/login.aspx')
web.click('//*[@id="content"]/div[2]/div[1]/div/div[3]/a')
web.input('//*[@id="loginname"]','wuqingfadqng')
web.input('//*[@id="nloginpwd"]','dsafds')
web.click('//*[@id="loginsubmit"]')
web.slideverify('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img',
                '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img',
                '{"zoom":1.25,"offset-x":20,"offset-y":308,"slide":"puautogui"}')


time.sleep(5)
# 退出浏览器
web.quit()


