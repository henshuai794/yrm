# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/18 21:37
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：pip install Appium-Python-Client
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import os
import time
import pytest
import threading
from appium import webdriver


class Test_APP:

    def setup_class(self):
        # 启动appium
        def runappium():
            cmd = r'node C:\Users\qqq\AppData\Local\Programs\Appium\resources\app\node_modules\
            appium\build\lib\main.js'
            os.system(cmd)

        # 使用多线程
        th = threading.Thread(target=runappium, args=())
        th.start()
        time.sleep(5)
        print('appium已经启动')

        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.mobileqq"
        caps["appActivity"] = ".activity.SplashActivity"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["automationName"] = "uiautomator1"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    def test_login(self):
        el1 = self.driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
        el1.clear()
        el1.send_keys("1264790452")
        el2 = self.driver.find_element_by_accessibility_id("密码 安全")
        el2.clear()
        el2.send_keys("321321qqq")
        el3 = self.driver.find_element_by_accessibility_id("登 录")
        el3.click()
        time.sleep(5)

    def test_logout(self):
        el4 = self.driver.find_element_by_accessibility_id("帐户及设置")
        el4.click()
        el5 = self.driver.find_element_by_accessibility_id("设置")
        el5.click()
        el6 = self.driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
        el6.click()
        el7 = self.driver.find_element_by_accessibility_id("退出当前帐号按钮")
        el7.click()
        el8 = self.driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
        el8.click()

    def teardown_class(self):
        self.driver.quit()
        time.sleep(2)
        os.system('taskkill /F /IM node.exe')
        print('appium已经停止')


if __name__ == "__main__":
    # pytest.main(['./PO_APP.py','-s'])

    def runappium():
        cmd = r'node E:\Appium\resources\app\node_modules\appium\build\lib\main.js'
        os.system(cmd)


    th = threading.Thread(target=runappium, args=())
    th.start()
    print('appium已经启动')
    time.sleep(20)
    print('appium已经停止')
    os.system('taskkill /F /IM node.exe')
