# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/20 20:42
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9.0"
caps["deviceName"] = "3e5d55a"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["noReset"] = True
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
caps["automationName"] = "uiautomator1"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 隐式等待
driver.implicitly_wait(10)
time.sleep(8)
TouchAction(driver).press(x=562, y=380).move_to(x=553, y=1927).release().perform()

els2 = driver.find_elements_by_xpath("//*[@text='美团丨外卖…']/..")
els2[0].click()
time.sleep(6)
els3 = driver.find_elements_by_xpath("//*[@text='输入商家名、品类或商圈']")
els3[0].click()
els4 = driver.find_elements_by_xpath("//*[@text='取消']/../android.view.View/android.view.View")
els4[0].send_keys("药")
els5 = driver.find_elements_by_xpath("//*[@text='药店']")
els5[0].click()
time.sleep(5)
driver.back()
els7 = driver.find_elements_by_xpath("//*[@text='我的']/..")
els7[0].click()
els9 = driver.find_elements_by_xpath("//android.widget.Button[@text='订单']")
els9[0].click()

time.sleep(5)
driver.quit()