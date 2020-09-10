# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:54 下午 
# @Author : hans.li
# @File : gift.py
from flask_login import login_required

from . import web


@web.route('/my/gifts')
@login_required
def my_gifs():
    return 'my gifts'
