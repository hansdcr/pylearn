# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:58 上午 
# @Author : hans.li
# @File : __init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
