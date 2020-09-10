# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:59 下午 
# @Author : hans.li
# @File : auth.py
from flask import request, url_for, redirect

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web
from flask_login import login_user


@web.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)

    return {}


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)  # 向cookie中写入票据
            next = request.args.get('next') # 获取问号后面的内容
            if not next or next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            print("账号不存在或密码错误")
    return 'login'
