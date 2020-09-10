# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:58 上午 
# @Author : hans.li
# @File : __init__.py
from flask import Flask
from app.models.base import db
from app.models import *
from flask_login.login_manager import LoginManager


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 注册login登陆管理插件
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)
