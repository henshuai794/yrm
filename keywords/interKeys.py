import json, traceback, requests, jsonpath
from suds.client import Client
from common.Logger import logger


class HTTP:
    """
        自动化架构体系
        数据驱动运行入口
        Powered By Mr. William
        2020/4/3
    """

    def __init__(self):
        # 创建session管理
        self.session = requests.session()
        # 设置请求默认的头
        self.session.headers["content-type"] = 'application/x-www-form-urlencoded'
        self.session.headers[
            'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

        # 项目接口基本地址
        self.url = ""
        # 保存请求结果
        self.result = None
        # 保存json解析后的字典
        self.jsonres = None
        # 关联参数
        self.relations = {}

    def seturl(self, url):
        """
        设置项目接口基本地址
        :param url: 项目的基本地址
        :return: 成功失败
        """
        # 对传入参数的处理
        if url is None or url == '':
            url = ''

        self.url = url
        return True

    def get(self, path, params=None):
        """
        以data字典形式传键值对参数
        :param path: 接口地址
        :param params: 参数字典
        :return: 成功失败
        """

        # 对传入参数的处理
        if params is None or params == '':
            params = None

        # 对path进行处理
        if path is None or path == '':
            # 接口地址不应该为空
            logger.error("接口名字错误")
            return False
        # 实现关联
        params = self.__get__relations(params)

        # 如果传非绝对路径的地址，就拼上基础地址
        if not path.startswith("http"):
            path = self.url + "/" + path

        # 处理url连接失败的情况
        try:
            if params is None:
                self.result = self.session.get(path)
            else:
                self.result = self.session.get(path + "?" + params)
        except Exception as e:
            logger.exception(e)
            self.result = None

        try:
            # 如果返回的是json字符串，就处理为字典
            resulttext = self.result.text
            resulttext = resulttext[resulttext.find('{'):resulttext.rfind('}') + 1]
            self.jsonres = json.loads(resulttext)
        except Exception as e:
            logger.exception(e)
            self.jsonres = None

        return True

    def post(self, path, params=None):
        """
        以data字典形式传键值对参数
        :param path: 接口地址
        :param params: 参数字典
        :return: 成功失败
        """

        # 对传入参数的处理
        if params is None or params == '':
            params = None

        # 对path进行处理
        if path is None or path == '':
            # 接口地址不应该为空
            logger.error("接口名字错误")
            return False
        # 实现关联
        params = self.__get__relations(params)
        params = self.__get_data(params)

        # 如果传非绝对路径的地址，就拼上基础地址
        if not path.startswith("http"):
            path = self.url + "/" + path

        # 处理url连接失败的情况
        try:
            self.result = self.session.post(path, data=params)
        except Exception as e:
            logger.exception(e)
            self.result = None

        try:
            # 如果返回的是json字符串，就处理为字典
            resulttext = self.result.text
            resulttext = resulttext[resulttext.find('{'):resulttext.rfind('}') + 1]
            self.jsonres = json.loads(resulttext)
            logger.info(str(self.jsonres))
        except Exception as e:
            logger.exception(e)
            self.jsonres = None

        return True

    def postnodata(self, path, params=None):
        """
        以data字典形式传键值对参数
        :param path: 接口地址
        :param params: 参数字典
        :return: 成功失败
        """

        # 对传入参数的处理
        if params is None or params == '':
            params = None

        # 对path进行处理
        if path is None or path == '':
            # 接口地址不应该为空
            logger.error("接口名字错误")
            return False
        # 实现关联
        params = self.__get__relations(params)

        # 如果传非绝对路径的地址，就拼上基础地址
        if not path.startswith("http"):
            path = self.url + "/" + path

        # 处理url连接失败的情况
        try:
            self.result = self.session.post(path, data=params)
        except Exception as e:
            self.result = None

        try:
            # 如果返回的是json字符串，就处理为字典
            resulttext = self.result.text
            resulttext = resulttext[resulttext.find('{'):resulttext.rfind('}') + 1]
            self.jsonres = json.loads(resulttext)
            logger.info(self.jsonres)
        except Exception as e:
            logger.exception(e)
            self.jsonres = None

        return True

    def put(self, path, params=None):
        """
        以data字典形式传键值对参数
        :param path: 接口地址
        :param params: 参数字典
        :return: 成功失败
        """

        # 对传入参数的处理
        if params is None or params == '':
            params = None

        # 对path进行处理
        if path is None or path == '':
            # 接口地址不应该为空
            logger.error("接口名字错误")
            return False
        # 实现关联
        params = self.__get__relations(params)
        params = self.__get_data(params)

        # 如果传非绝对路径的地址，就拼上基础地址
        if not path.startswith("http"):
            path = self.url + "/" + path

        # 处理url连接失败的情况
        try:
            self.result = self.session.put(path, data=params)
        except Exception as e:
            self.result = None

        try:
            # 如果返回的是json字符串，就处理为字典
            resulttext = self.result.text
            resulttext = resulttext[resulttext.find('{'):resulttext.rfind('}') + 1]
            self.jsonres = json.loads(resulttext)
            logger.info(self.jsonres)
            print(str(self.jsonres))
        except Exception as e:
            logger.exception(e)
            self.jsonres = None

        return True

    def addheader(self, key, value=None):
        """
        往请求头里面添加一个键值对
        :param key: 头的键
        :param value: 头的值
        :return: 成功失败
        """
        value = self.__get__relations(value)
        self.session.headers[key] = value
        self.result = self.session.headers
        logger.info(self.session.headers)
        return True

    def removeheader(self, key):
        """
        从请求头删除一个键值对
        :param key: 需要删除的键
        :return: 成功失败
        """
        try:
            self.session.headers.pop(key)
        except Exception as e:
            pass

        self.result = self.session.headers
        logger.info(self.session.headers)
        return True

    def assertequals(self, key, value):
        """
        断言json结果里面某个键的值和value相等
        :param key: json的键
        :param value: 期望值
        :return: 是否相等
        """
        # 如果请求返回不是json，就直接return
        if self.jsonres is None:
            logger.error(self.jsonres)
            return False

        value = self.__get__relations(value)

        try:
            actual = str(jsonpath.jsonpath(self.jsonres, key)[0])
            self.result = actual
            if actual == str(value):
                logger.info(actual)
                return True
            else:
                logger.info(actual)
                return False
        except Exception as e:
            # 处理键不存在的情况
            logger.exception(e)
            return False

    def savejson(self, jsonkey, paramname):
        """
        从jsonres里面保存某个键的值，用来关联
        :param jsonkey: 需要保存的json的键
        :param paramname: 保存后参数的名字
        :return: 成功失败
        """
        # 去jsonres里面取值
        try:
            value = str(jsonpath.jsonpath(self.jsonres, jsonkey)[0])
        except Exception as e:
            value = None
        # 保存键值对到关联字典
        self.relations[paramname] = value

        logger.info(True, self.relations)
        return True

    def assertequaljson(self, jsonp):
        """
        断言json结果里多个键值对相等
        :param jsonp: 传入你需要比较的多个键值对的json字符串
        :return: 是否相等
        """
        # 如果请求返回不是json，就直接return
        if self.jsonres is None:
            logger.error(None)
            return False

        try:
            # 传入的参数不是json，传参错误
            jsonp = json.loads(jsonp)
        except Exception as e:
            logger.exception(e)
            return False

        try:
            # 处理键不存在的情况
            for key in jsonp.keys():
                # 只要有一个键值对不相等，就不相等
                value = str(jsonpath.jsonpath(self.jsonres, key)[0])
                if not value == str(jsonp[key]):
                    logger.error(self.jsonres)
                    return False
            # 所有键值对都相等，才返回True
            logger.info(self.jsonres)
            return True
        except Exception as e:
            logger.exception(e)
            return False

    def assertcontains(self, value):
        """
        断言返回结果的字符串包含value
        :param value: 被包含的字符串
        :return: 是否包含
        """
        try:
            # 如果返回结果为空，就报错
            result = str(self.result.text)
        except Exception as e:
            logger.exception(e)
            return False

        value = self.__get__relations(value)

        if result.__contains__(str(value)):
            logger.info(self.result.text)
            return True
        else:
            logger.error(self.result.text)
            return False

    def __get_data(self, params):
        """
        url参数转字典
        :param params: 需要转字典的参数
        :return: 转换后的字典
        """
        if params is None:
            return None

        # 定义一个字典，用来保存转换后的参数
        param = {}
        p1 = params.split('&')
        for keyvalue in p1:
            index = keyvalue.find('=')
            if index >= 0:
                key = keyvalue[0:index]
                value = keyvalue[index + 1:]
                param[key] = value
            else:
                param[keyvalue] = ''

        return param

    def __get__relations(self, params):
        """
        使用关联结果
        :param params: 需要关联的参数
        :return: 关联后的字符串
        """
        if params is None:
            return None

        for key in self.relations.keys():
            params = params.replace('{' + key + '}', str(self.relations[key]))
        return params
