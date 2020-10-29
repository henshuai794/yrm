# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/14 10:44
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：logging日志打印模块
"""
import logging

import yaml

with open(file="./lib/data/logger.yaml", mode='r', encoding="utf-8")as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    # print(logging_yaml)
    # 配置logging日志：主要从文件中读取handler的配置、formatter（格式化日志样式）、logger记录器的配置
    logging.basicConfig(**logging_yaml)
# 获取根记录器：配置信息从yaml文件中获取
logger = logging.getLogger()

if __name__ == "__main__":
    # 等级顺序
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning('WARNING')
    logger.error('ERROR')
    try:
        int('a')
    except Exception as e:
        logger.exception(e)