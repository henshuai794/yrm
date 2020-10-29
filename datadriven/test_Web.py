# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/15 20:32
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：Web自动化的数据驱动执行
"""
import os
import allure
import cv2
import pytest
import yaml

from keywords.WebKeys import Web


# 获取yaml用例
def get_cases(path):
    with open(path, encoding='utf-8') as f:
        result = yaml.safe_load(f)
    return result


def get_error_img(obj, zoom=1.25):
    """
    错误截图
    :param zoom:
    :return:
    """
    if obj.ele is None:
        return obj.driver.get_screenshot_as_png()
    else:
        # 标注元素位置
        obj.driver.get_screenshot_as_file("../lib/images/tmp.png")
        # 使用cv2画图
        img = cv2.imread("../lib/images/tmp.png")
        # 先获取位置
        location = obj.ele.location
        # 再获取元素的大小
        size = obj.ele.size
        # 再计算缩放
        x = int(location['x'] * zoom)
        y = int(location['y'] * zoom)
        # 去画一个矩形
        cv2.rectangle(img, (x, y), (x + int(size['width'] * zoom), y + int(size['height'] * zoom)), (0, 0, 255), 5)
        # 把画好的图保存
        cv2.imwrite("../lib/images/tmp.png", img)
        # 再读出二进制返回
        with open('./lib/images/tmp.png', 'rb') as f:
            file = f.read()
        return file


cases = get_cases('./lib/cases/cases.yml')


@allure.feature('Web自动化')
class Test_Web:
    """
    数据驱动执行Web自动化用例
    """

    def setup_class(self):
        # 初始化关键字库的对象
        self.web = Web()

    @allure.step
    def run_step(self, func, params):
        """
        一个步骤
        :param func: 关键字
        :param value: 参数列表
        :return:
        """
        func(*params)

    @allure.story('登录')
    @pytest.mark.parametrize("caseslist", cases['loginError'])
    def test_login(self, caseslist):
        """
        使用参数化执行所有用例
        :return:
        """
        print(caseslist)
        allure.dynamic.title(caseslist['title'])
        logincases = caseslist['cases']
        for onecase in logincases:
            # 反射获取到关键字
            func = getattr(self.web, onecase['method'])
            params = list(onecase.values())[2:]
            try:
                with allure.step(onecase['name']):
                    self.run_step(func, params)
            except Exception as e:
                # 在此添加截图，需要是二进制图片
                allure.attach(get_error_img(self.web), '失败截图', allure.attachment_type.PNG)
                # 给出失败也异常信息
                pytest.fail("用例执行失败：{}".format(e))

            # 在此添加截图，需要是二进制图片
            allure.attach(get_error_img(self.web), '结果截图', allure.attachment_type.PNG)

    @allure.story('滑动验证码破解')
    @pytest.mark.parametrize("caseslist", cases['testQQVerify'])
    def test_qq_verify(self, caseslist):
        """
        使用参数化执行所有用例
        :return:
        """
        print(caseslist['title'])
        allure.dynamic.title(caseslist['title'])
        logincases = caseslist['cases']
        for onecase in logincases:
            # 反射获取到关键字
            func = getattr(self.web, onecase['method'])
            params = list(onecase.values())[2:]
            try:
                with allure.step(onecase['name']):
                    self.run_step(func, params)
            except Exception as e:
                # 在此添加截图，需要是二进制图片
                allure.attach(get_error_img(self.web), '失败截图', allure.attachment_type.PNG)
                # 给出失败也异常信息
                pytest.fail("用例执行失败：{}".format(e))

    def teardown_class(self):
        self.web.sleep(3)
        self.web.quit()


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['./test_Web.py', '--alluredir', '../temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../temp -o ../report --clean')
