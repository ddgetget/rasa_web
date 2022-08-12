#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-12 16:42
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    Task_extractors_DateparserEntityExtractor.py
# @Project: rasa_web
# @Package: 
# @Ref:
from rasa.shared.nlu.training_data.message import Message
from rasa_nlu_examples.extractors.dateparser_extractor import DateparserEntityExtractor
from rich import print

# 使用 Rich API 可以很容易的在终端输出添加各种颜色和不同风格。它可以绘制漂亮的表格，进度条，markdown，
# 突出显示语法的源代码及回溯等等，优秀的功能不胜枚举。

# FlashText算法：在文本中大规模检索或替换关键字的高效率算法

msg = Message.build("hello tomorrow, goodbye yesterday",)

extractor = DateparserEntityExtractor({})
extractor.process([msg,])  # 注意参数是列表，官网给的是错的
print(msg.as_dict_nlu())