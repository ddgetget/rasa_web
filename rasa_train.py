#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-12 16:10
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    rasa_train.py
# @Project: rasa_web
# @Package: 
# @Ref:

import rasa

# from config import my_config
# #
# os.environ['CUDA_VISIBLE_DEVICES'] = my_config.depend['rasa_run_cuda']

rasa.train(
    domain="domain.yml",

    # classifier
    # method1
    # config="config/config.LogisticRegressionClassifier.yml",
    # fixed_model_name="LogisticRegressionClassifier",

    # method2
    # config="config/config.SparseNaiveBayesClassifierr.yml",
    # fixed_model_name="SparseNaiveBayesClassifierr",

    #extractors
    # method1
    # config="config/config.DateparserEntityExtractor.yml",
    # fixed_model_name="DateparserEntityExtractor",

    # # method2
    # config="config/config.DateparserEntityExtractorRelative.yml",
    # fixed_model_name="DateparserEntityExtractorRelative",

    # # method2
    # config="config/config.FlashTextEntityExtractor.yml",
    # fixed_model_name="FlashTextEntityExtractor",


    # featurizer.dense
    # method1
    config="config/config.BytePairFeaturizer.yml",
    fixed_model_name="BytePairFeaturizer",


    training_files="data",
)
