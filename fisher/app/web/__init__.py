# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:59 上午 
# @Author : hans.li
# @File : __init__.py
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book, gift, auth, main
