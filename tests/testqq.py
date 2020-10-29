# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/11 20:04
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：滑动验证码
"""
import time

import cv2
from selenium import webdriver
import requests
from selenium.webdriver import ActionChains


# 通过url下载图片，并保存到本地
def get_img(ele1, filepath='../lib/images/target.png'):
    """
    通过图片获取到src，然后下载图片到本地
    :param ele1: 图片元素定位器
    :param filepath: 需要保存的图片位置
    :return:
    """
    # 获取图片的url地址，也就是图片元素的src属性
    img_url = ele1.get_attribute('src')
    # 通过requests去请求url，获取到图片的二进制码
    result = requests.get(img_url).content
    # 保存二进制为本地图片
    with open(filepath, 'wb') as f:
        f.write(result)


def find_pic():
    target_rgb = cv2.imread('../lib/images/template.png')
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread('../lib/images/target.png', 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    return value[2][0]


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
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)

driver.get('https://i.qq.com/')

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="login_frame"]'))
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys('343432432')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('545645')
driver.find_element_by_xpath('//*[@id="login_button"]').click()

time.sleep(1)
# 获取到滑块
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="tcaptcha_iframe"]'))


def slide_img(driver):
    while True:
        # 获取滑块图片
        ele1 = driver.find_element_by_xpath('//*[@id="slideBlock"]')
        # 下载滑块图片
        get_img(ele1, '../lib/images/target.png')
        # 获取背景图片
        ele2 = driver.find_element_by_xpath('//*[@id="slideBg"]')
        # 下载背景图片
        get_img(ele2, '../lib/images/template.png')
        # 滑块需要滑动的距离
        x = find_pic()
        print(x)

        # 背景图在网页的大小
        w1 = ele2.size['width']
        # 获取原图的大小
        # 获取背景图片实际大小
        img = cv2.imread('../lib/images/template.png')
        w2 = img.shape[1]

        x = int(x * (w1 / w2)) - 22
        slide_by_selenium(ele1, x)

        time.sleep(2)
        ele1 = driver.find_element_by_xpath('//*[@id="slideBlock"]')
        if not ele1.is_displayed():
            return
        else:
            driver.find_element_by_xpath('//*[@id="e_reload"]').click()
            time.sleep(1)


slide_img(driver)
