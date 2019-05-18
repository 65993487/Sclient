#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 10:08 PM
# @Author  : w8ay
# @File    : config.py

# 程序运行的线程数
import os
import time

THREAD_NUM = 25
DEBUG = False
# LOGGER_LEVEL = 1 if DEBUG else 2
LOGGER_LEVEL = 1

# Ip的缓存数量
NUM_CACHE_IP = 77

# 域名的缓存数量
NUM_CACHE_DOMAIN = 2

# Masscan相关
MASSCAN_RATE = 3000  # masscan 的速率
MASSCAN_DEFAULT_PORT = "21,22,23,80-90,161,389,443,445,873,1099,1433,1521,1900,2082,2083,2222,2601,2604,3128,3306," \
                       "3311,3312,3389,4440,4848,5432,5560,5900,5901,5902,6082,6379,7001-7010,7778,8080-8090,8649," \
                       "8888,9000,9200,10000,11211,27017,28017,50000,50030,50060 "
MASSCAN_FULL_SCAN = False  # 是否扫描全端口

# WEB Restful接口地址
WEB_INTERFACE = os.environ.get("WEB_INTERFACE", default="http://127.0.0.1:8000/")
WEB_INTERFACE_KEY = "hello-w12scan!"

# WEB POCS repository 提供指纹识别对应的poc仓库
WEB_REPOSITORY = "https://github.com/65993487/Scan_POC"

# 是否用 plugins目录下的插件进行扫描探，为false将不会进行探测和使用airbug项目进行攻击
IS_START_PLUGINS = True

# reids数据库
REDIS_HOST = os.environ.get("REDIS_HOST", default="127.0.0.1:6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", default="")

# 该扫描节点的名称(自定义)
NODE_NAME = "w12_node_{0}".format(os.environ.get("NODE_NAME", "Scanner_"+str(time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())))))
