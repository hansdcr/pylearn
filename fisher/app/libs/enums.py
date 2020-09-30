# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 4:31 下午 
# @Author : hans.li
# @File : enums.py

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
