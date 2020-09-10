# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 5:08 下午 
# @Author : hans.li
# @File : wish.py
from flask import current_app, redirect, url_for
from flask_login import current_user

from . import web
from .. import Gift, db, Wish


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    """ 添加心愿清单 """

    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        print('这本书已经添加至你的赠送清单或已经存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.index', isbn=isbn))