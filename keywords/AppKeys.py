# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/20 20:49
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：APP自动化关键字库
"""
import json
import os
import threading
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common.Logger import logger


class App:
    """
    APP关键字库
    """

    def __init__(self):
        # 全局的驱动变量
        self.driver = None
        # appium服务的端口
        self.port = '4723'
        # 报错截图，记录是否找到元素
        self.ele = None

    def conndevice(self, devicename=''):
        """
        使用adb连接设备
        :param devicename: 设备名字
        :return:
        """
        os.system('adb connect ' + devicename)

    def startappium(self, port='4723', appiumpath='E:\Appium-1.5.1'):
        """
        启动appium服务，依赖node命令
        :param port: appium 启动的端口
        :param appiumpath: appium客户端安装路径
        :return:
        """
        self.port = str(port)

        # 启动appium
        def runappium(logger):
            cmd = r'node %s\resources\app\node_modules\appium\build\lib\main.js -p %s' % (appiumpath, str(port))
            logger.info(cmd)
            os.system(cmd)

        # 使用多线程
        th = threading.Thread(target=runappium, args=(logger,))
        th.start()
        time.sleep(5)
        logger.info('appium已经启动')

    def starapp(self, conf, t='8'):
        """
        连接appium服务器，启动APP
        :param conf: APP启动的配置，为标准的json字符串
        :param t: app启动的等待时间
        :return:
        """
        # 通过json库，把json配置字符串转化为字典
        caps = json.loads(conf)
        self.driver = webdriver.Remote("http://localhost:%s/wd/hub" % self.port, caps)
        self.driver.implicitly_wait(10)
        t = int(t)
        time.sleep(t)

    def find_ele(self, locator=''):
        """
        三种通用的定位方式
        :param locator: 定位器
        :return: 定位到的元素
        """
        self.ele = None

        if locator.startswith('/'):
            # 以/开头的定位方式，是xpath
            ele = self.driver.find_element_by_xpath(locator)
        elif locator.find(':id/') >= 0:
            # 包含:id/的定位方式是id定位
            ele = self.driver.find_element_by_id(locator)
        else:
            # 其他的都使用accessibility_id定位
            ele = self.driver.find_element_by_accessibility_id(locator)

        self.ele = ele
        return ele

    def click(self, locator=''):
        """
        找到并点击元素
        :param locator: 元素定位器
        :return:
        """
        ele = self.find_ele(locator)
        ele.click()

    def input(self, locator, value):
        """
        找到元素，并且输入
        :param locator: 元素定位器
        :param value: 需要输入的元素
        :return:
        """
        ele = self.find_ele(locator)
        ele.send_keys(value)

    def swipe(self, position1='(1,1)', position2='(2,2)', t='1000'):
        """
        滑动
        :param position1: 开始位置
        :param position2: 结束位置
        :param t: 滑动的持续时间(ms)
        :return:
        """
        p1 = eval(position1)
        p2 = eval(position2)
        t = int(t)
        TouchAction(self.driver).press(x=p1[0], y=p1[1]).move_to(x=p2[0], y=p2[1]).wait(t).release().perform()

    def back(self):
        self.driver.back()

    def sleep(self,t='1'):
        t = int(t)
        time.sleep(t)

    def quitappium(self):
        time.sleep(2)
        self.driver.quit()
        time.sleep(2)
        os.system('taskkill /F /IM node.exe')
        logger.info('appium已经停止')


if __name__ == "__main__":
    caps = '''{
  "platformName": "Android",
  "platformVersion": "9.0",
  "deviceName": "3e5d55a",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI",
  "noReset": true,
  "unicodeKeyboard": true,
  "resetKeyboard": true,
  "automationName": "uiautomator1"
}'''

    # caps = caps.replace('\n', '')
    # print(caps)
    caps = json.loads(caps)
    print(caps)
