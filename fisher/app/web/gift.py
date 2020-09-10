# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:54 下午 
# @Author : hans.li
# @File : gift.py
from flask import current_app, redirect, url_for
from flask_login import login_required, current_user

from . import web
from .. import Gift, db


@web.route('/my/gifts')
@login_required
def my_gifs():
    return 'my gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    """ 赠送图书 """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            # current_user实际代表的是User模型，是通过@login_manager.user_loader它获得的
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        print('这本书已经添加至你的赠送清单或已经存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.index', isbn=isbn))
