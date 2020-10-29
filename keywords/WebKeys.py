# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/6 21:44
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：Web自动化的关键字驱动类，面向对象的封装
"""
import time

from selenium import webdriver

from common.Slide import Slide
from common.verify import Verify


class Web:
    """
    Web自动化关键字驱动类
    """

    def __init__(self):
        # 操作浏览器的对象
        self.driver = None
        # self.driver = webdriver.Chrome()
        # 关联的字典
        self.relations = {}
        # 用来表示是否找到元素
        self.ele = None

    def openbrowser(self, br='gc'):
        """
        打开浏览器的关键字
        :用法: ['openbrowser','gc']
        :param br: 指定你要打开的浏览器，默认是Chrome浏览器
                ff：Firefox浏览器，ie：IE浏览器
        :return: 是否打开成功
        """
        if br == 'gc':
            # driver是selenium webdriver模块里面WebDriver类的一个对象
            # 这个对象提供里
            self.driver = webdriver.Chrome()
        elif br == 'ie':
            # driver是selenium webdriver模块里面WebDriver类的一个对象
            # 这个对象提供里
            self.driver = webdriver.Ie()
        elif br == 'ff':
            # driver是selenium webdriver模块里面WebDriver类的一个对象
            # 这个对象提供里
            self.driver = webdriver.Firefox()
        else:
            # 在此处添加启动其他浏览器的代码
            pass

        # 设置默认隐式等待10s
        # 如果立即去找，没找到元素，那么就每隔一秒钟去找一次这个元素，
        # 直到10s之后还没找到就报错
        # 如果在期间某一次找到了，就继续往下运行
        # 触发条件是find_element
        # 可以使你的脚本运行更流畅，稳定
        self.driver.implicitly_wait(10)
        # 最大化启动
        self.driver.maximize_window()
        # self.driver.find_element_by_css_selector().screenshot()
        return True

    def __find_ele(self, locator=''):
        """
        支持八种定位方式
        :param locator: xpath=//*[@id="username"]
        :return: 放回定位到的元素
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=') + 1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(
                locator[locator.find('=') + 1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(
                locator[locator.find('=') + 1:])
        elif locator.startswith('link_text(='):
            ele = self.driver.find_element_by_link_text(
                locator[locator.find('=') + 1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(
                locator[locator.find('=') + 1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_css_selector(
                locator[locator.find('=') + 1:])
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def geturl(self, url=''):
        """
        打开网站
        :param url: 网页地址
        :return:
        """
        self.driver.get(url)
        return True

    def click(self, locator=''):
        """
        找到，并点击元素
        :param locator: 定位器
        :return: 是否点击成功
        """
        ele = self.__find_ele(locator)
        ele.click()
        return True

    def jsclick(self, locator=''):
        """
        使用js点击元素
        :param locator: 元素定位器
        :return:
        """
        ele = self.__find_ele(locator)
        self.driver.execute_script("$(arguments[0]).click()", ele)
        return True

    def input(self, locator='', value=''):
        """
        找到元素，并输入文本
        :param locator: 定位器
        :param value: 需要输入的文本
        :return: 是否输入成功
        """
        value = self.__get_relations(value)
        ele = self.__find_ele(locator)
        ele.send_keys(value)
        return True

    def switchwin(self, index='0'):
        """
        切换窗口
        :param index: 需要切换到的窗口序号
        :return:
        """
        index = int(index)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[index])
        return True

    def closewin(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
        return True

    def intoiframe(self, locator=''):
        """
        进入iframe
        :param locator: iframe定位器
        :return:
        """
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)
        return True

    def outiframe(self):
        """
        退出所有iframe
        :return:
        """
        # 切换到客厅，也就是最外层页面
        self.driver.switch_to.default_content()
        return True

    def runjs(self, js=''):
        """
        执行js
        :param js: 可执行的js语句
        :return:
        """
        self.driver.execute_script(js)
        return True

    def gettext(self, locator='', paramname=''):
        """
        获取文本，保存参数
        :param locator: 文本元素定位器
        :param paramname: 需要保存的参数名字
        :return:
        """
        ele = self.__find_ele(locator)
        self.relations[paramname] = ele.text
        return True

    def assertequal(self, actvalue='', respvalue=''):
        """
        断言相等
        :param actvalue: 实际结果
        :param respvalue: 预期结果
        :return:
        """
        actvalue = self.__get_relations(actvalue)
        respvalue = self.__get_relations(respvalue)
        int('a')
        if actvalue == respvalue:
            return True
        else:
            return False

    def __get_relations(self, s):
        """
        获取关联后的字符串
        约定，如果要使用关联的变量，形式为{paramname}
        :param s: 需要关联的字符串
        :return: 返回关联后的字符串
        """
        if s is None or s == '':
            return ''
        else:
            s = str(s)
            for key in self.relations.keys():
                s = s.replace('{' + key + '}', self.relations[key])
            return s

    def getverify(self, locator=''):
        """
        获取图文验证码
        :param locator: 验证码图片的定位器
        :return: 验证码
        """
        ele = self.__find_ele(locator)
        # 截取验证码图片
        ele.screenshot('./lib/images/verify.png')
        # 调用Verify库，获取验证码
        verify = Verify('wuqingfqng', '6e8ebd2e301f3d5331e1e230ff3f3ca5', '96001')
        verify_text = verify.PostPic(1902, im='./lib/images/verify.png')
        self.relations['verify'] = verify_text
        return True

    def slideverify(self,locator1='',locator2='',jsonp=None):
        """

        :param locator1: 背景图片定位器
        :param locator2: 滑块图片的定位器
        :return:
        """
        slide = Slide(self.driver)
        jsonp = str(jsonp)
        slide.slide_verify(locator1,locator2,jsonp=jsonp)
        return True

    def sleep(self,t='1'):
        """
        固定等待
        :param t: 需要等待的时间
        :return:
        """
        t = int(t)
        time.sleep(t)

    def quit(self):
        """
        退出浏览器
        :return: 是否退出成功
        """
        self.driver.quit()
        return True
