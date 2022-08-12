#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-12 11:53
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    rasa_run.py
# @Project: rasa_web
# @Package: 
# @Ref:
import os

import rasa

# from config import my_config
# #
# os.environ['CUDA_VISIBLE_DEVICES'] = my_config.depend['rasa_run_cuda']

rasa.run(
    # model="models", # 默认在这个文件夹喜下找最新的，但是必须名字有日期
    # model="models/LogisticRegressionClassifier.tar.gz",  # 直接写死，定位到具体模型
    model="models/SparseNaiveBayesClassifierr.tar.gz",  # 直接写死，定位到具体模型
    endpoints="endpoints.yml",
    # credentials="credentials.yml" # 备注后相当于--enable-api
)
