# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 7:52 下午 
# @Author : hans.li
# @File : main.py
from . import web


@web.route('/')
def index():
    return 'hello index'
