# -*- coding: utf-8 -*- 
# @Time : 2020/9/30 5:54 下午 
# @Author : hans.li
# @File : __init__.py.py

from flask import Blueprint


api = Blueprint('api', __name__)

from app.api.v1 import hello, token