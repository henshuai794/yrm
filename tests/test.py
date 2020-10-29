# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/6 20:08
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：Web自动化测试脚本
"""
import time

from selenium import webdriver


# 打开浏览器（chrome）
# driver是selenium webdriver模块里面WebDriver类的一个对象
# 这个对象提供里
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()

# 保护模式
# 缩放比例
driver = webdriver.Ie()
# 隐式等待
# 如果立即去找，没找到元素，那么就每隔一秒钟去找一次这个元素，
# 直到10s之后还没找到就报错
# 如果在期间某一次找到了，就继续往下运行
# 触发条件是find_element
# 可以使你的脚本运行更流畅，稳定
driver.implicitly_wait(10)

# 在打开的浏览器上面访问网站
driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")

# 登录-密码错误
# # id属性，一般是唯一的，是可以用的，但是不一定存在
# driver.find_element_by_id('username')
# # name属性，不一定是唯一的，并不建议使用
# driver.find_element_by_name('username')
# # class属性，不一定是唯一的，并不建议使用
# driver.find_element_by_class_name('text_cmu')
# # 标签名字，不一定是唯一的，并不建议使用
# driver.find_element_by_tag_name('input')
# # a标签中间的文本，也不一定是唯一的
# driver.find_element_by_link_text('1号店')
# # 一部分a标签的文本，其实就是包含，也不一定是唯一的
# driver.find_element_by_partial_link_text('号店')
# # copy selector
# driver.find_element_by_css_selector('#username')
# # copy xpath
# 找到元素
ele = driver.find_element_by_xpath('//*[@id="username"]')
# 操作元素-输入
ele.send_keys('13800138006')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('11111')
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('11')
ele = driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a')
# js点击
driver.execute_script("$(arguments[0]).click()", ele)
text = driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
print(text)

# 在打开的浏览器上面访问网站
driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
# 找到元素
ele = driver.find_element_by_xpath('//*[@id="username"]')
# 操作元素-输入
ele.send_keys('13800138006')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('11')
ele = driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a')
# js点击
driver.execute_script("$(arguments[0]).click()", ele)
# 获取登录后的昵称
time.sleep(1)
text = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[1]').text
print(text)

# 脚本执行到这里的时候，固定等待5s
time.sleep(5)
# 关闭浏览器
driver.quit()
