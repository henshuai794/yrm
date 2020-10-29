# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/11 21:04
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：京东验证码
"""
import time

import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains

from common.Slide import Slide


def slide_by_selenium(ele1, x):
    # 使用selenium的ActionChains模块实现滑动
    action = ActionChains(driver)
    # 先按住滑块，一定要加上.perform()
    action.click_and_hold(ele1).perform()
    # 鼠标滑动x距离
    action.move_by_offset(x, 0).perform()
    # 松开鼠标
    action.release().perform()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://passport.jd.com/new/login.aspx')

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('dsklfjaoi')
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('dfsfads')
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()

ele1 = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
ele2 = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
slide = Slide(driver)
slide.slide_img(ele1.get_attribute('src'),filepath='../lib/images/target.png')
slide.slide_img(ele2.get_attribute('src'),filepath='../lib/images/template.png')
slide.slide_verify('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img',
                   '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img',
                   jsonp='{"slide": "pyautogui","offset-y":306,"offset-x":0,"zoom":1.25}')

