# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/20 17:38
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from keywords.AppKeys import App

app = App()
app.startappium()
app.starapp('''{
  "platformName": "Android",
  "platformVersion": "9.0",
  "deviceName": "3e5d55a",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI",
  "noReset": true,
  "unicodeKeyboard": true,
  "resetKeyboard": true,
  "automationName": "uiautomator1"
}''')

app.swipe('(532,525)','(525,2061)')
app.click("//*[@text='美团丨外卖…']/..")
app.click("//*[@text='输入商家名、品类或商圈']")
app.input("//*[@text='取消']/../android.view.View/android.view.View","药")
app.click("//*[@text='药店']")
app.sleep(5)
app.back()
app.click("//*[@text='我的']/..")
app.click("//android.widget.Button[@text='订单']")

app.quitappium()
