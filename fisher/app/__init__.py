# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:58 上午 
# @Author : hans.li
# @File : __init__.py
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
